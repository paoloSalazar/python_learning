"""
   player.py
   ---------

   This module contains the Player class that represents game characters.
"""

__author__ = "psv"

class Player:
    """
    The player class represents the characters in the game.
    :ivar healt: the current healt of the characters. Starts at 100.
                 Once it reaches 0, we're dead
    """
    def __init__(self, name, weapon):
        """
        Create a new Player.

        :param name: The name of the Player.
        :param weapon: The weapon that this player users to fight with
        """
        self.name = name
        self.weapon = weapon
        self.health = 100

    def take_hit(self, damage):
        """
        This method getys called when the player takes a hit from the opponent's weapon
        :para damage: The damage dealt. This will be substracted from :attr:`health`.
        :return: The new value of :attr:`health`.
        """
        self.health -= damage
        return self.health

    