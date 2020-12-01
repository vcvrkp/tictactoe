from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invitation(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name="invitations_sent",
        on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name="invitations_recieved",
        verbose_name="User to invite ",
        help_text="Please select the user you wish to play a game with. ",
        on_delete=models.CASCADE)
    message = models.CharField(
        max_length=300,
        verbose_name="Optional Message.",
        help_text="It's always nice to add a friendly message!")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " {0} sent {1} an Invitation".format(self.from_user, self.to_user)
