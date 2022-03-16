from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly
from .models import Advertisement, AdvertisementStatusChoices,  Favorite
from .serializers import AdvertisementSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404


class AdvertisementViewSet(ModelViewSet):

    queryset =  Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = (DjangoFilterBackend,)    
    filterset_class= AdvertisementFilter
    filterset_fields = ['creator', 'created_at',]

    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated, IsAdminUser|IsOwnerOrReadOnly]


    @action(methods=['GET'], detail=False)
    def favorites(self, request):
        favorite = Favorite.objects.filter(user_id=request.user.id)    
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data) 


    def get_queryset(self):
        owner_advertisement = Advertisement.objects.filter(Q(creator=self.request.user.id))
        users_advertisement  = Advertisement.objects.filter(~Q(creator=self.request.user.id), ~Q(status=AdvertisementStatusChoices.DRAFT)) 
        return owner_advertisement | users_advertisement 
