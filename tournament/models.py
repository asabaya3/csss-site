from django.db import models

class Tournament(models.Model):
    SWISS = 'SW'
    SINGLE_ELIM = '1X'
    DOUBLE_ELIM = '2X'
    STYLE_CHOICES = (
        (SWISS, 'Swiss'),
        (SINGLE_ELIM, 'Single Elimination'),
        (DOUBLE_ELIM, 'Double Elimination'),
    )        

    name = models.CharField()
    password = models.CharField()
    organizer = models.ForeignKey(Organizer)
    num_of_rounds = models.PositiveIntegerField(default = 1)
    current_round = models.PositiveIntegerField(default = 0)
    session = models.PositiveIntegerField(default = 1)
    style = models.CharField(choices = STYLE_CHOICES,
                             default = SWISS)
    is_open = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
class Player(models.Model):
    tournament = models.ForeignKey(Tournament)
    name = models.CharField()
    password = models.CharField()
    email = models.EmailField()
    in_game_contact = models.CharField()
    session_points = models.IntegerField(default = 0)
    lifetime_points = models.IntegerField(default = 0)
    in_session = models.BooleanField(default = True)

    def __str__(self):
        return self.name + ' in ' + self.tournament.name

class Game(models.Model):
    tournament = models.ForeignKey(Tournament)
    session = models.PositiveIntegerField()
    round = models.PositiveIntegerField()
    player1 = models.ForeignKey(Player)
    player2 = models.ForeignKey(Player)

    def __str__(self):
        return self.player1.name + ' vs ' + self.player2.name

class Result(models.Model):
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Player)
    score = models.CharField()
    notes = models.CharField()

    def __str__(self):
        return self.winner + ' ' + self.score