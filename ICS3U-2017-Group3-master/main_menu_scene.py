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

        self.play_position = Vector2()
        self.tutorial_position = Vector2()
        self.title_position = Vector2()
        self.shop_position = Vector2()
        self.credits_position = Vector2()
        self.settings_position = Vector2()
        
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/MB.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
        self.play_position.x = 370
        self.play_position.y = self.size_of_screen_y - 550
        self.play_button = SpriteNode('./images/StartButton.png',
                                    parent = self,
                                    position = self.play_position,
                                    size = (600,500))
                                    
        self.tutorial_position.x = 630
        self.tutorial_position.y = self.size_of_screen_y - 550
        self.tutorial_button = SpriteNode('./images/Tutorial.png',
                                    parent = self,
                                    position = self.tutorial_position,
                                    size = (530,500))
        
        self.title_position.x = self.size.x
        print(self.size.x)
        self.title_position.y = self.size_of_screen_y - 100
        self.title = SpriteNode('./images/Title.png',
                                    parent = self,
                                    position = self.title_position,
                                    size = self.size)
        
        self.shop_position.x = 70
        self.shop_position.y = self.size_of_screen_y - 230
        self.shop_button = SpriteNode('./images/shop1.PNG',
                                    parent = self,
                                    position = self.shop_position,
                                    size = (140,140))
        self.credits_position.x = 70
        self.credits_position.y = self.size_of_screen_y - 400
        self.credits = SpriteNode('./images/credits.PNG',
                                    parent = self,
                                    position = self.credits_position,
                                    size = (140,140))
        self.settings_position.x = 70
        self.settings_position.y = self.size_of_screen_y - 570
        self.settings = SpriteNode('./images/settings.PNG',
                                    parent = self,
                                    position = self.settings_position,
                                    size = (140,140))
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
#run(main_menu(), PORTRAIT)
