from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError 
from advertisements.models import Advertisement, AdvertisementStatusChoices, Favorite

class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )


    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        self.validate_status(AdvertisementStatusChoices.OPEN)
        return super().create(validated_data)

    
    def validate_status(self, value):
        count = Advertisement.objects.filter(creator=self.context["request"].user,
                                            status=AdvertisementStatusChoices.OPEN).count()
        print('count==', count)
        if value == AdvertisementStatusChoices.OPEN and count >= 10:
            raise serializers.ValidationError("You can't have more then 10 opened advertisement")
        return value



class FavoriteSerializer(serializers.ModelSerializer):

    advertisements = AdvertisementSerializer(source='advertisement')

    class Meta:
        model = Favorite
        fields = ('advertisements',)
