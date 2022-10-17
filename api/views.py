from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import logging

from api.models import Game
from api.models import User
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

def index(request):
    latest_game_list = Game.objects.order_by('-pub_date')[:5]
    """ template = loader.get_template(/index.html') """
    context = {
        'latest_game_list': latest_game_list,
    }
    return render(request, 'api/templates/index.html')

def createUser(request, body):
    """ user = User.objects.create_user(username=body.username,
                                 email=request.body.email,
                                 password=request.body.email) """

def get_all_games(request):
    return HttpResponse("You're looking at games %s.")

def get_all_users(request):
    users = User.objects.all()
    logger.info('------test log',users)
    return render(request, 'api/templates/users.html', {'users': users})

def game(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)

def players(request, game_id):
    response = "You're looking at the players of game %s."
    return HttpResponse(response % game_id)

def actions(request, game_id):
    return HttpResponse("You're looking at the actions of game %s." % game_id)