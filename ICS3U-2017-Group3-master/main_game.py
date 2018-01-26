# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
#main game scene

from scene import *
import ui
from numpy import random
import sound
import time
import config

global shoot
shoot = False

global lives
dead = False
global space_ship
#space_ship = SpriteNode ('./images/usership1.png',size = (180,180))


laser_counter = 0

class GameScene(Scene):
    def setup(self):
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        if config.music_is_on == True:
           config.music.play()
        elif config.music_is_on == False:
           config.music.pause()
           
        self.score_position = Vector2()
        self.wave_position = Vector2()
        self.lives_position = Vector2()
        self.menu_position = Vector2()
        self.shild1_position = Vector2()
        self.shild2_position = Vector2()
        self.shild3_position = Vector2()
        
        self.lasers = []
        self.aliens = []
        self.alien_attack_rate = 1  
        self.alien_attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.wave = 1 
        self.lives = 3
        self.dead = False
        self.back_position = Vector2()
        
        #add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/game_backround.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        #spc:PlayerShip3Blue
        self.back_position.x = self.screen_center_x-440 
        self.back_position.y = self.size_of_screen_y - 80
        self.back = SpriteNode('./images/left.PNG',
                               parent = self,
                               position = self.back_position,
                               size = (150,150))
                               
        ship_position = self.size / 2                          
        self.ship = SpriteNode(config.ship_type,
                               parent = self,
                               position = ship_position,
                               size = (150,150))
        #self.ship.position = 
        #self.ship_size = (100,100)
        #self.add_child(self.ship)
        
        self.wave_position.x = self.screen_center_x+420 
        self.wave_position.y = self.size_of_screen_y - 700
        self.wave_label = LabelNode(text = 'wave: 1',
                                    font=('Helvetica', 40),
                                    parent = self,
                                    position = self.wave_position)
        
        self.score_position.x = self.screen_center_x+420 
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
        '''
        self.lives_position.x = 100
        self.lives_position.y = self.size_of_screen_y - 700
        self.lives_label = LabelNode(text = 'Score: 3',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.lives_position)
        '''
        self.shild1_position.x = self.screen_center_x-300 
        self.shild1_position.y = self.size_of_screen_y - 700
        self.shild1 = SpriteNode('./images/shield.PNG',
                                 parent = self,
                                 position = self.shild1_position,
                                 size = (150,150))
        self.add_child(self.shild1)
        
        self.shild2_position.x = self.screen_center_x-380
        self.shild2_position.y = self.size_of_screen_y - 700
        self.shild2 = SpriteNode('./images/shield.PNG',
                                 parent = self,
                                 position = self.shild2_position,
                                 size = (150,150))
        self.add_child(self.shild2)
        
        self.shild3_position.x = self.screen_center_x-460 
        self.shild3_position.y = self.size_of_screen_y - 700
        self.shild3 = SpriteNode('./images/shield.PNG',
                                 parent = self,
                                 position = self.shild3_position,
                                 size = (150,150))
        self.add_child(self.shild3)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        global score
        global lives
        global shoot
        global dead
        #lasers = SpriteNode('spc:LaserBlue9', position=self.ship.position, z_position=-1, parent=self)
        '''
        if shoot == True:
            #lasers.run_action(Action.sequence(Action.move_by(0, 1000), Action.remove()))
            self.create_new_lasers()
        else:
            shoot = False
        '''
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
        
        # check every update to see if a missile has touched a alien
        
        if len(self.aliens) > 0 and len(self.lasers) > 0:
            
            for alien in self.aliens:
                for laser in self.lasers:
                    if alien.frame.contains_rect(laser.frame):
                        laser.remove_from_parent()
                        self.lasers.remove(laser)
                        if self.dead == True:
                            self.score = self.score
                        alien.remove_from_parent()
                        #self.aliens.remove(alien)
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
                if alien_hit.frame.intersects(self.ship.frame):
                    #print('a hit')
                    
                    alien_hit.remove_from_parent()
                    self.aliens.remove(alien_hit)
                    self.lives = self.lives - 1
                    # since game over, move to next scene
                    if self.lives == 0:
                        shoot = False
                        self.ship.remove_from_parent()
                        self.dead = True
                        dead = True
                        laser.remove_from_parent()
                        config.game_over = True
                        self.dismiss_modal_scene()
                        '''
                        self.gameover = SpriteNode('./images/GameOver.png',
                                          parent = self,
                                          position = Vector2(self.screen_center_x, 
                                                             self.screen_center_y),
                                          alpha = 1.0,
                                          scale = self.scale_size)
                        
                        self.menu_position.x = 500 
                        self.menu_position.y = self.size_of_screen_y - 600
                        self.back = SpriteNode('./images/BackToMenu.png',
                                    parent = self,
                                    position = self.menu_position,
                                    scale = self.scale_size)
                       '''
                    if self.lives == -1:
                           self.lives = 0
        else:
            pass
            #print(len(self.aliens))
        # this is the wave funtion 
        if shoot == True:
            #lasers.run_action(Action.sequence(Action.move_by(0, 1000), Action.remove()))
            self.create_new_lasers()
        else:
            shoot = False
            
        if self.score % 20 ==  0 :
            self.score = self.score + 1
            self.wave = self.wave + 1
            self.alien_attack_rate = self.alien_attack_rate + 1
        
        # update every frame the current score
        self.score_label.text = 'Score: ' + str(self.score)
        self.wave_label.text = 'Wave: ' + str(self.wave)
        #self.lives_label.text = 'lives:' + str(self.lives)
        if self.lives == 2:
            self.shild3.remove_from_parent()
        if self.lives == 1:
            #self.live3.remove_from_parent()
            self.shild2.remove_from_parent()
        if self.lives == 0:
            #self.live3.remove_from_parent()
            #self.live2.remove_from_parent()
            self.shild1.remove_from_parent()
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
        self.create_new_lasers()
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        global shoot
        shoot = True
        x, y = touch.location
        pos = self.ship.position
        pos.x = x
        pos.y = y
        self.ship.position = pos
        
    
    def create_new_lasers(self):
        # when the user touches the space ship
        '''
        laser = SpriteNode('spc:LaserBlue9', position=self.ship.position, z_position=-1, parent=self)
        if shoot == True:
            laser.run_action(Action.sequence(Action.move_by(0, 1000), Action.remove()))
        '''
            
        
        
        lasers_start_position = Vector2()
        lasers_start_position.x = self.ship.position.x
        lasers_start_position.y = self.ship.position.y
           
        lasers_end_position = Vector2()
        lasers_end_position.x = lasers_start_position.x
        lasers_end_position.y = self.size_of_screen_y + 20
            
        self.lasers.append(SpriteNode('spc:LaserBlue9',
                         position = lasers_start_position,
                         parent = self))
        laserMoveAction = Action.move_by(0, 1000, 2)
        self.lasers[len(self.lasers)-1].run_action(laserMoveAction)
        # make missile move forward
        #self.lasers.run_action(Action.sequence(Action.move_by(0, 1000), Action.remove()))
        
    def touch_ended(self, touch):
        if self.back.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        
        
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
       # global dead
        #if dead == True:
            #self.alien_attack_speed = 0
          #  self.alien_attack_rate = 0
            #print("hello")
        alien_start_position = Vector2()
        alien_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        alien_start_position.y = self.size_of_screen_y + 200
        
        alien_end_position = Vector2()
        alien_end_position.x = random.randint(100, 
                                        self.size_of_screen_x - 100)
        alien_end_position.y = -100
        
        self.aliens.append(SpriteNode('./images/alien_ship.PNG',
                             position = alien_start_position,
                             parent = self,
                             size = (150,150)))
        
        # make missile move forward
        alienMoveAction = Action.move_to(alien_end_position.x, 
                                         alien_end_position.y, 
                                         self.alien_attack_speed,
                                         TIMING_SINODIAL)
        self.aliens[len(self.aliens)-1].run_action(alienMoveAction)
        
#run(GameScene(), PORTRAIT)
