from fcm_django.admin import User
from rest_framework import serializers

from entries.models import Entry


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('id', 'image', 'title', 'description', 'nasa_id')


class UserSerializer(serializers.ModelSerializer):
    entries = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'entries')