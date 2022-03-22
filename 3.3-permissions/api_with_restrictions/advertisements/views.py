from .filters import AdvertisementFilter
from .permissions import IsAdminOrIsSelf, AddToFavorite
from .models import Advertisement, AdvertisementStatusChoices,  Favorite
from .serializers import AdvertisementSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status

class AdvertisementViewSet(ModelViewSet):

    queryset =  Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = (DjangoFilterBackend,)    
    filterset_class= AdvertisementFilter
    filterset_fields = ['creator', 'created_at',]

    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyOrAdmin]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "delete"] :
            return [IsAdminOrIsSelf()]
        elif self.action == 'add_to_favorites':     
            return [AddToFavorite()] 
        else:
            return [IsAuthenticated()]

    @action(methods=['GET'], detail=False)
    def favorites(self, request):
        favorite = Favorite.objects.filter(user_id=request.user.id)    
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data) 

    @action(methods=['POST'], detail=True, permission_classes=[AddToFavorite])
    def add_to_favorites(self,request, pk=None):
        advertisement = self.get_object()
        advertisement.user.add(request.user.id)
        advertisement.save()
        Favorite.objects.get_or_create(advertisement=advertisement,
                                       user_id=request.user.id) 
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_queryset(self):
        owner_advertisement = Advertisement.objects.filter(Q(creator=self.request.user.id))
        users_advertisement  = Advertisement.objects.filter(~Q(creator=self.request.user.id), ~Q(status=AdvertisementStatusChoices.DRAFT)) 
        return owner_advertisement | users_advertisement 
