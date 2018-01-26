# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
# this is the main menu scene 
from scene import *
from main_game import *
from shop_scene import *
from settings import *
from credits import *
from tutorial import *
import config
import ui
from game_over_scene import *

class MainMenu (Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color     
                                     
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        if config.music_is_on == True:
           config.music.play()
        elif config.music_is_on == False:
           config.music.pause()

        play_position = Vector2()
        tutorial_position = Vector2()
        title_position = Vector2()
        shop_position = Vector2()
        credits_position = Vector2()
        settings_position = Vector2()
        
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/MB.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
        
        play_position.x = self.screen_center_x-140
        play_position.y = self.screen_center_y-150
        self.play_button = SpriteNode('./images/StartButton.PNG',
                                    parent = self,
                                    position = play_position,
                                    size = (600,500))
                                    
        tutorial_position.x = self.screen_center_x+170
        tutorial_position.y = self.screen_center_y-150
        self.tutorial_button = SpriteNode('./images/Tutorial.PNG',
                                    parent = self,
                                    position = tutorial_position,
                                    size = (600,500))
        
        title_position.x = self.screen_center_x
        title_position.y = self.size_of_screen_y - 100
        self.title = SpriteNode('./images/Title.png',
                                    parent = self,
                                    position = title_position,
                                    size = self.size)
        
        shop_position.x = self.screen_center_x-440
        shop_position.y = self.size_of_screen_y - 230
        self.shop_button = SpriteNode('./images/shop1.PNG',
                                    parent = self,
                                    position = shop_position,
                                    size = (140,140))
        credits_position.x = self.screen_center_x-440
        credits_position.y = self.size_of_screen_y - 400
        self.credits = SpriteNode('./images/credits.PNG',
                                    parent = self,
                                    position = credits_position,
                                    size = (140,140))
        settings_position.x = self.screen_center_x-440
        settings_position.y = self.size_of_screen_y - 570
        self.settings = SpriteNode('./images/settings.PNG',
                                    parent = self,
                                    position = settings_position,
                                    size = (140,140))
    def update(self):
        # this method is called, hopefully, 60 times a second
        if config.game_over == True:
            self.present_modal_scene(GameOverScene())
            config.game_over = False
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # how a button works exampule 
        if self.play_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        if self.shop_button.frame.contains_point(touch.location):
            self.present_modal_scene(ShopScene())
        if self.settings.frame.contains_point(touch.location):
            self.present_modal_scene(Settings())
        if self.credits.frame.contains_point(touch.location):
            self.present_modal_scene(Credits())
        if self.tutorial_button.frame.contains_point(touch.location):
            self.present_modal_scene(Tutorial())
        
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

