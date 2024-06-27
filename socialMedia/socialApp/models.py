from django.db import models
from account.models import User


# Create your models here.

class friendRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_request_sent", blank=True, null=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_request_recieved", blank=True,
                                null=True)
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"from {self.author} by {self.to_user} status {self.status}"

    class Meta:
        unique_together = ('author', 'to_user')
