# Created by: luca
# Created on: Jan 2018
# Created for: ICS3U

# This scene shows the game over scene and also user's score and highscore


from scene import *
from main_menu_scene import *
from main_game import *
import ui
import config



class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode('./images/game_backround.png',
                                     position = self.size / 2, 
                                     
                                     parent = self, 
                                     size = self.size)
        
        
        
        
        
        game_over_position = self.size
        game_over_position.x = self.size_of_screen_x -500
        game_over_position.y = game_over_position.y - 300
        
        
        self.game_over = SpriteNode('./images/GameOver.png',
                                       parent = self,
                                       position = game_over_position)
        
        
        back_button_position = self.size
        back_button_position.x = self.size_of_screen_x / 2
        back_button_position.y = back_button_position.y * 0.33
        
        
        self.back_button = SpriteNode('./images/BackToMenu.png',
                                       parent = self,
                                       position = back_button_position)
    
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
        
        # go to previouse scene when this butten is touched (and released)
        if self.back_button.frame.contains_point(touch.location):
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
    
