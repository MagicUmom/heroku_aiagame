from django.db import models

# Create your models here.

class game_detail(models.Model):
    game_id = models.PositiveIntegerField()
    game_round = models.PositiveIntegerField()
    user_id = models.CharField(max_length=20)
    balance = models.PositiveIntegerField()
    bet_red = models.PositiveIntegerField()
    bet_white = models.PositiveIntegerField()

class game_overview(models.Model):
    game_id = models.PositiveIntegerField()
    game_round = models.PositiveIntegerField()
    total_red = models.PositiveIntegerField()
    total_white = models.PositiveIntegerField()

class game_controll(models.Model):
    game_id = models.PositiveIntegerField()
    game_round = models.PositiveIntegerField()
    game_status = models.PositiveIntegerField()  ## 0: over 1: activate 2:locking