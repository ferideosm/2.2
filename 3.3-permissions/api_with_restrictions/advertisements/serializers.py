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
        return super().create(validated_data)

    def validate(self, data):
        count = Advertisement.objects.filter(creator=self.context["request"].user,
                                            status=AdvertisementStatusChoices.OPEN).count()
        if count > 10:
            raise ValidationError({'error': 'You have more then 10 advertisement'})

        return data

class FavoriteSerializer(serializers.ModelSerializer):

    advertisements = AdvertisementSerializer(source='advertisement')

    class Meta:
        model = Favorite
        fields = ('advertisements',)
