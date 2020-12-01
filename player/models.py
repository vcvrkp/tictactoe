from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent",on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="invitations_recieved",on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " {0} sent {1} an Invitation".format(self.from_user, self.to_user)
