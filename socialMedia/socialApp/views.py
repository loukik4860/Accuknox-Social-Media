from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    UpdateAPIView, CreateAPIView
from .models import friendRequest
from .serializers import friendRequestSerializer
from .renderes import renderClass
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle


# create friends request
class friendRequestListCreateView(CreateAPIView):
    queryset = friendRequest.objects.all()
    serializer_class = friendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    renderer_classes = [renderClass]


# show all friends request from all users
class friendListView(ListAPIView):
    queryset = friendRequest.objects.all()
    serializer_class = friendRequestSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]


# shows pending friends request from logged-In User
class UserFriendPendingList(ListAPIView):
    serializer_class = friendRequestSerializer
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]

    def get_queryset(self):
        user = self.request.user.id
        print("current user ", user)
        friends = friendRequest.objects.filter(author=user, status='pending')
        print(friends)
        return friends


# shows accepted friends request from logged-In User
class UserFriendAcceptedList(ListAPIView):
    serializer_class = friendRequestSerializer
    permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]

    def get_queryset(self):
        user = self.request.user.id
        print("current user ", user)
        friends = friendRequest.objects.filter(author=user, status='accepted')
        print(friends)
        return friends


class FriendRequestAcceptView(UpdateAPIView):
    queryset = friendRequest.objects.all()
    serializer_class = friendRequestSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == "accepted":
            return Response({'status': 'friend Request has already been accepted'}, status=status.HTTP_400_BAD_REQUEST)
        print("instance", instance)
        print("instance.to_user", instance.to_user)
        print("instance.user", instance.author)
        instance.status = "accepted"
        instance.save()
        return Response({'status': 'Friend Request Accepted'}, status=status.HTTP_205_RESET_CONTENT)


class FriendRequestRejectView(UpdateAPIView):
    queryset = friendRequest.objects.all()
    serializer_class = friendRequestSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == "accepted":
            return Response({'status': 'Friend request has been accepted'}, status=status.HTTP_400_BAD_REQUEST)
        if instance.status == "pending":
            instance.status = "rejected"
            instance.save()
        return Response({'status': 'Friend Request Rejected'}, status=status.HTTP_205_RESET_CONTENT)


# Retrieve update and delete friends request
class FriendRequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = friendRequest.objects.all()
    serializer_class = friendRequestSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [renderClass]
