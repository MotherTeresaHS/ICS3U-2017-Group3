# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
# this is the tutorial scene 
from scene import *
import ui
import config

class Tutorial (Scene):
    def setup(self):
        
        
        self.back_position = Vector2()
       
        
                                     
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        if config.music_is_on == True:
           config.music.play()
        elif config.music_is_on == False:
           config.music.pause()                
        
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/Tutorial_1.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        
        
        
        self.back_position.x = self.screen_center_x-425  
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
