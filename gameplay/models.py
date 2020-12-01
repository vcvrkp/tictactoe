from __future__ import unicode_literals
# from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


BOARD_SIZE = 3

GAME_STATUS_CHOICES = (
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player to Win'),
    ('L', 'Second Player to Win'),
    ('D', 'Draw')
)


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):

        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(Q(status='F') | Q(status='S'))


# Create your models here.
# @python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)
    objects = GamesQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('gameplay_detail',args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

    def board(self):
        """Returns a 2 Dimensional list of Move Objects"""
        board = [[None for x in range(BOARD_SIZE)]for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.x][move.y] = move
        return board

    def is_users_move(self, user):
        return (user == self.first_player and self.status == 'F') or (user == self.second_player and self.status == 'S')

    def new_move(self):
        """Returns new move object with player, game, and count present"""
        if self.status not in 'FS':
            raise ValueError("Cannot make move on finished game.")
        return Move(
            game=self,
            by_first_player = self.status == 'F'
        )

class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(BOARD_SIZE-1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(BOARD_SIZE-1)]
    )
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField(editable=False,default=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE,editable=False)
