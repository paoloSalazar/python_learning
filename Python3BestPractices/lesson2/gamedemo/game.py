"""
   game.py
   -------

   This module contains the Game class that implements the actual game mechanics as well as 
   __main__ construct to make the game runnable.
"""

__author__ = "psv"

from date import datetime

class Game:
    """
    The game class implements the game mechanics for this demo. To undestand the way
    the game works, read the documentation for the :meth:`run` method:
    """

    def __init__(self, player1, player2):
        """
        Create a new game with two players.

        :param player1: First Player
        :param player2: Second Player
        """
        self.p1 = player1
        self.p2 = player2

    def run(self):
        """
        This method implements the game mechanics. The game loops until one of the players
        runs out of health. Every turn, one of the players is randomly chosen to attack. We
        call the :meth:`gamedemo.weapon.Weapon.attack` method on that player's weapon.
        The damage dealt by this attack is applied to the player by calling
        :meth:`gamedemo.player.Player.take_hit`.

        """
        print(self.p1)