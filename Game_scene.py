#main game 

from scene import *
import ui
from numpy import random
import sound
import time

global shoot
shoot = False



class GameScene(Scene):
    def setup(self):
        
        self.background = SpriteNode('./images/MB.JPG')
        self.ship = SpriteNode('spc:PlayerShip1Orange')
        self.ship.position = self.size / 2
        self.add_child(self.ship)
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        
        self.spaceship = []
        self.laser = []
        self.aliens = []
        self.alien_attack_rate = 1  
        self.alien_attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.dead = False
        
        #add background color
        #background_position = Vector2(self.screen_center_x, 
                                      #self.screen_center_y)
        #self.background = SpriteNode('./assets/sprites/star_background.png',
                                     #position = background_position, 
                                     #parent = self, 
                                     #size = self.size)
                                     
        
        
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
        
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        
        global shoot
        laser = SpriteNode('spc:LaserBlue9', position=self.ship.position, z_position=-1, parent=self)
        if shoot == True:
            laser.run_action(Action.sequence(Action.move_by(0, 1000), Action.remove()))
            
        else:
            shoot = False
        # every update, randomly check if a new alien should be created
        alien_create_chance = random.randint(1, 120)
        if alien_create_chance <= self.alien_attack_rate:
            self.add_alien()
            
        
        
        
        # check every update if an alien is off screen
        #print(len(self.aliens))
        for alien in self.aliens:
            if alien.position.y < -50:
                alien.remove_from_parent()
                self.aliens.remove(alien)
                # only subtract points if you are still alive
                if self.dead == False:
                    self.score = self.score - 2
        
        # check every update to see if a missile has touched a space alien
        if len(self.aliens) > 0 and len(self.laser) > 0:
            #print('missile check')
            for alien in self.aliens:
                for laser in self.laser:
                    if alien.frame.contains_rect(laser.frame):
                        laser.remove_from_parent()
                        self.laser.remove(laser)
                        alien.remove_from_parent()
                        self.aliens.remove(alien)
                        self.score = self.score + 1
                        # since you destroyed one, make more show up
                        #self.alien_attack_rate = self.alien_attack_rate + 1
        else:
            pass
            #print(len(self.aliens))
        
        # check every update to see alien touches spaceship
        if len(self.aliens) > 0:
            #print('checking')
            for alien_hit in self.aliens:
                #print('alien ->' + str(alien_hit.frame))
                #print('ship  ->' + str(self.spaceship.frame))
                if alien_hit.frame.intersects(self.spaceship.frame):
                    #print('a hit')
                    self.spaceship.remove_from_parent()
                    alien_hit.remove_from_parent()
                    self.aliens.remove(alien_hit)
                    # since game over, move to next scene
                    self.dead = True
                    self.menu_button = SpriteNode('./images(/menu_button.png',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, 
                                                         self.screen_center_y),
                                      alpha = 1.0,
                                      scale = self.scale_size)
        else:
            pass
            #print(len(self.aliens))
        
        # update every frame the current score
        self.score_label.text = 'Score: ' + str(self.score)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left or right button is down
        sound.play_effect('arcade:Laser_1')
        x, y = touch.location
        pos = self.ship.position
        pos.x = x
        pos.y = y
        move_action = Action.move_to(x, y,)
        #self.ship.position = pos
        self.ship.run_action(move_action)
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        global shoot
        shoot = True
        x, y = touch.location
        pos = self.ship.position
        pos.x = x
        pos.y = y
        self.ship.position = pos
    
    def touch_ended(self, touch):
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    
        
    def add_alien(self):
        # add a new alien to come down
        
        alien_start_position = Vector2()
        alien_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        alien_start_position.y = self.size_of_screen_y + 100
        
        alien_end_position = Vector2()
        alien_end_position.x = random.randint(100, 
                                        self.size_of_screen_x - 100)
        alien_end_position.y = -100
        
        self.aliens.append(SpriteNode('./images/alien.png',
                             position = alien_start_position,
                             parent = self))
        
        # make missile move forward
        alienMoveAction = Action.move_to(alien_end_position.x, 
                                         alien_end_position.y, 
                                         self.alien_attack_speed,
                                         TIMING_SINODIAL)
        self.aliens[len(self.aliens)-1].run_action(alienMoveAction)
run(GameScene(), PORTRAIT)
