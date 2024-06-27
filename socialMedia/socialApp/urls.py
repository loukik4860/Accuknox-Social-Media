from django.urls import path, include
from .views import friendRequestListCreateView, FriendRequestDetailView, friendListView, UserFriendPendingList, \
    UserFriendAcceptedList, FriendRequestAcceptView, FriendRequestRejectView

urlpatterns = [
    path('all_friend_request/', friendListView.as_view(), name="all_friend_list"),
    path('friend_request/', friendRequestListCreateView.as_view(), name='friend_request'),
    # path('friend-requests/<int:pk>/', FriendRequestDetailView.as_view(), name='friend-request-detail'),
    # accept the friend request through friend request id
    path('friend_requests/<int:pk>/accept/', FriendRequestAcceptView.as_view(), name='friend-request-accept'),
    # Reject the friend request through friend request id
    path('friend_requests/<int:pk>/reject/', FriendRequestRejectView.as_view(), name='friend-request-accept'),
    # list of friend request pending
    path('user_friend_pending_list/<int:pk>/', UserFriendPendingList.as_view(), name="user_friend_pending_list"),
    # list of friend request accepted
    path('user_friend_accepted_list/<int:pk>/', UserFriendAcceptedList.as_view(), name="user_friend_accepted_list"),
]
