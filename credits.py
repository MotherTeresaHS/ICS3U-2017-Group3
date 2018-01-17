# this is credits scene 
#made by luca
from scene import *
import ui
import config

class Credits (Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.back_position = Vector2()
        self.credits_position = Vector2()
        self.programers_position = Vector2()
        self.luca1_position = Vector2()
        self.khoa1_position = Vector2()
        self.graphic_disgners_position = Vector2()
        self.luca2_position = Vector2()
        self.khoa2_position = Vector2()
        self.music_position = Vector2()
        self.john_patraboy_position = Vector2()
        
                                     
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
        self.background = SpriteNode('./images/credits_backround.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        
        self.credits_position.x = 550
        self.credits_position.y = self.size_of_screen_y - 100
        self.credits_label = LabelNode(text = 'Credits',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.credits_position)
        
        self.programers_position.x = 150
        self.programers_position.y = self.size_of_screen_y - 280
        self.progamers_label = LabelNode(text = 'Programers',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.programers_position)
        self.luca1_position.x = 120
        self.luca1_position.y = self.size_of_screen_y - 340
        self.luca1_label = LabelNode(text = '-luca',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.luca1_position)
        self.khoa1_position.x = 120
        self.khoa1_position.y = self.size_of_screen_y - 420
        self.khoa1_label = LabelNode(text = '-khoa',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.khoa1_position)
        
        
        
        self.luca2_position.x = 780
        self.luca2_position.y = self.size_of_screen_y - 340
        self.luca2_label = LabelNode(text = '-khoa',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.luca2_position)
        self.khoa2_position.x = 780
        self.khoa2_position.y = self.size_of_screen_y - 420
        self.khoa2_label = LabelNode(text = '-luca',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.khoa2_position)
        
        self.graphic_disgners_position.x = 800
        self.graphic_disgners_position.y = self.size_of_screen_y - 280
        self.art_label = LabelNode(text = 'Graphic Disginers',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.graphic_disgners_position)
        
        self.back_position.x = 85 
        self.back_position.y = self.size_of_screen_y - 80
        self.back = SpriteNode('./images/left.PNG',
                                    parent = self,
                                    position = self.back_position,
                                    size = (150,150))
        
        self.music_position.x = 500
        self.music_position.y = self.size_of_screen_y - 500
        self.music_label = LabelNode(text = 'Music developer',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.music_position)
        
        self.john_patraboy_position.x = 480
        self.john_patraboy_position.y = self.size_of_screen_y - 560
        self.creator_label = LabelNode(text = '-John Patraboy',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.john_patraboy_position)
        
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
