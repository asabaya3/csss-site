from django.shortcuts import render
from django.views import generic

from .models import Tournament, Player, Game, Result

'''
Views TODO:
    Tournament Controls:
        Start Next Round:
            generate pairings using tournament style
            create Games in db
        See/Deal with Result Conflicts
        Start/End Sessions
            player lifetime points are updated when session ends
            
    User Controls:
        Register to tournament
        Sign up for next session
        Report results