from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game,GamesQuerySet
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .forms import Invitation

# Create your views here.
@login_required
def home(request):
    # g_f_p = Game.objects.filter(first_player=request.user,status='F')
    # g_s_p = Game.objects.filter(second_player=request.user,status='S')
    # all_games = list(g_f_p) + list(g_s_p)
    my_games = Game.objects.games_for_user(request.user)
    active = my_games.active()
    old_games = my_games.difference(active)
    invitations = request.user.invitations_recieved.all()
    dcontext = {}
    dcontext['games'] = active
    dcontext['old_games'] = old_games
    dcontext['invitations'] = invitations
    return render(request=request, template_name="player/home.html",
                  context=dcontext)

@login_required
def new_invitation(request):
    if request.method == "POST":
        #TODO Handle the request of form submission.
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request,"player/new_invitation_form.html",{"form":form})

@login_required
def accept_invitation(request,id):
    invitation = get_object_or_404(Invitation,pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player = invitation.to_user,
                second_player = invitation.from_user,
            )
        invitation.delete()
        return redirect(game)
    else:
        return render(request,"player/accept_invitation_form.html",{"invitation":invitation})