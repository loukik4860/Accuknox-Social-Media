from rest_framework import serializers
from .models import friendRequest
from account.models import User
from account.serializers import userProfileSerializer


# Serializer for friend request
class friendRequestSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    Author = userProfileSerializer(source='author', read_only=True)
    to_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    ToUser = userProfileSerializer(source="to_user", read_only=True)

    class Meta:
        model = friendRequest
        fields = ['id', 'status', 'author', 'Author', 'to_user', 'ToUser', 'created_at']
