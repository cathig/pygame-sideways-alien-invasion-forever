# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:46:47 2020

@author: Cathig
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set is rec attribute.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <=0:
            return True

    def update(self):
        """Move the alien down or up."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y