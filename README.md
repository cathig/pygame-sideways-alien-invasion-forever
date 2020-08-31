# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:54:34 2020

@author: Cathig
"""
# Sideways Alien Invasion
Welcome to Sideways Alien Invasion -- the game that never ends!

In this exercise from _Python Crash Course_ 2nd Ed (Chapter 13 p. 272), I practiced modifying the main tutorial game -- a traditional vertical Alien Invasion -- into a horizontal game.

Game components include a moveable rocket that shoots bullets at alien spaceships.

The rocket is constrained to the left side of the screen, remaining within the window frame.

The bullets start from the tip of the rocket ship and proceed across the screen. Once off screen, the program destroys each bullet.

The alien spaceships move up and down the screen and advance towards the rocket every time a ship reaches the edge of the screen.

When a bullet collides with an alien spaceship, the program removes the bullet and spaceship.

If the player destroys all the alien spaceships, the program removes any remaining bullets and launches a new fleet of alien spaceships.

And it never ends.

Unless you close it.


![sample Sideways Shooter screen](/images/sampleScreen.png)

## How to Use
1. Run alien_invasion.py.

   A game window opens with a rocket center left and an alien fleet advancing from the right.

2. __Move the rocket:__ press your keyboard's up and down arrow keys.

3. __Shoot bullets:__ press the spacebar.

   __Note:__ Only 3 bullets can exist at once. Once a bullet collides with an alien spaceship or leaves the other side of the screen, you can shoot more bullets.

4. Close the game window with the Close (X) button or press 'q'.