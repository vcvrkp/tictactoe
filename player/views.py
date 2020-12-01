from django.shortcuts import render
from gameplay.models import Game,GamesQuerySet
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    # g_f_p = Game.objects.filter(first_player=request.user,status='F')
    # g_s_p = Game.objects.filter(second_player=request.user,status='S')
    # all_games = list(g_f_p) + list(g_s_p)
    my_games = Game.objects.games_for_user(request.user)
    active = my_games.active()
    dcontext = {}
    dcontext['games'] = active
    return render(request=request, template_name="player/home.html",
                  context=dcontext)
