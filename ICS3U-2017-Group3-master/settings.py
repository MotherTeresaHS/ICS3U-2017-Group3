# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
# this is the settings scene 
from scene import *
import ui
import config

class Settings (Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.back_position = Vector2()
        self.off_position = Vector2()
        self.on_position = Vector2()
        
                # This plays or does not play music 
        # based on whether the music or no music button was pressed (in settings scene)  
        if config.music_is_on == True:
           config.music.number_of_loops = -1
           config.music.play()
        elif config.music_is_on == False:
           config.music.pause()

        
                                     
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/star_background.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        self.off_position.x = self.screen_center_x-250
        self.off_position.y = self.size_of_screen_y - 430
        self.off = SpriteNode('./images/soundoff.png',
                                    parent = self,
                                    position = self.off_position,
                                    size = (350,350))
        self.on_position.x = self.screen_center_x+250  
        self.on_position.y = self.size_of_screen_y - 430
        self.on = SpriteNode('./images/soundon.PNG',
                                    parent = self,
                                    position = self.on_position,
                                    size = (350,350))
        
        self.back_position.x = self.screen_center_x-440 
        self.back_position.y = self.size_of_screen_y - 80
        self.back = SpriteNode('./images/left.PNG',
                                    parent = self,
                                    position = self.back_position,
                                    size = (150,150))
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # how a button works exampule 
        if self.back.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        if self.on.frame.contains_point(touch.location):
           config.music.play()
           config.music_is_on = True
           
        if self.off.frame.contains_point(touch.location):           
           config.music.pause()
           config.music_is_on = False

    
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
    
#run(main_me(), PORTRAIT)
