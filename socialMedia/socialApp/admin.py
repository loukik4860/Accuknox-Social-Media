from django.contrib import admin
from .models import friendRequest


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'to_user', 'status', 'created_at', 'updated_at')
    search_fields = ('author__username', 'to_user__username', 'status')
    list_filter = ('status', 'created_at', 'updated_at')


admin.site.register(friendRequest, FriendRequestAdmin)
