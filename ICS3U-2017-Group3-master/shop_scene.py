# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
# this is the shop scene 
from scene import *
import config
import dialogs

global space_ship
#global counter
#counter = 0 
#space_ship = SpriteNode('./images/alien.png')

#global score
class ShopScene(Scene):
    def setup(self):
        #global score
        # this method is called, when user moves to this scene
        
        self.ship_purchased = False
        self.counter = 0
        # add background color
        
                                     
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        #self.score_position = Vector2()
        self.back_position = Vector2()
        self.ship_display_position = Vector2()
        self.last_position = Vector2()
        self.next_position = Vector2()
        self.buy_position = Vector2()
        
        #self.score = score
        
        #self.score_position = Vector2()
        
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./images/shop_backround.jpeg',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
        
        ship_position = self.size / 2                                                       
        self.ship = SpriteNode(config.ship_type,
                                    parent = self, 
                                    position = ship_position,
                                    scale = 0.9)                            
                                     
        self.back_position.x = 85 
        self.back_position.y = self.size_of_screen_y - 80
        self.back = SpriteNode('./images/left.PNG',
                                    parent = self,
                                    position = self.back_position,
                                    size = (150,150))
        '''
        self.ship_display_position.x = 540 
        self.ship_display_position.y = self.size_of_screen_y - 400
        self.ship_display = SpriteNode(space_ship,
                                    parent = self,
                                    position = self.ship_display_position,
                                    size = (150,150))
        '''
        
        
        self.last_position.x = 250 
        self.last_position.y = self.size_of_screen_y - 400
        self.last = SpriteNode('./images/left.PNG',
                                    parent = self,
                                    position = self.last_position,
                                    size = (150,150))
        self.next_position.x = 800 
        self.next_position.y = self.size_of_screen_y - 400
        self.next = SpriteNode('./images/right.PNG',
                                    parent = self,
                                    position = self.next_position,
                                    size = (150,150))
        self.buy_position.x = 500
        self.buy_position.y = self.size_of_screen_y - 700
        self.buy = SpriteNode('./images/buy.PNG',
                                    parent = self,
                                    position = self.buy_position,
                                    size = (600,600))
        
        
        #self.score_label.text = 'Score: ' + str(self.score)
    def update(self):
        #self.counter
        #global space_ship
        # this method is called, hopefully, 60 times a second
        #if self.counter == 0:
            #space_ship = SpriteNode('./images/alien.png')
            #self.ship = (space_ship)
            #self.ship.position = self.size / 2
            #self.add_child(self.ship)
        #if self.counter == 1:
            #space_ship = SpriteNode('spc:PlayerShip3Blue')
            #self.ship = (space_ship)
            #self.ship.position = self.size / 2
            #self.add_child(self.ship)  
                                         
        pass
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        #global counter
        #global space_ship
        
        # th method is called, when user releases a finger from the screen
        
        # how a button works exampule 
        if self.back.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
            
        if self.next.frame.contains_point(touch.location):
            self.counter = self.counter + 1
            if self.counter == 2:
                self.counter = 0
            self.ship_purchased = True
            self.choose_ship()
        
        if self.buy.frame.contains_point(touch.location):
            dialogs.alert(title = "free",
                                message = "HaHa we tricked you since we are nice its on us",
                                hide_cancel_button = False)
        
        if self.last.frame.contains_point(touch.location):
            self.counter = self.counter -1
            if self.counter == -1:
                self.counter = 0
            self.ship_purchased = False
            self.choose_ship()
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
        
    def choose_ship(self):
        if self.ship_purchased == True and self.counter == 1:  
           self.ship.remove_from_parent()  
           config.ship_type = './images/user_ship_2.PNG'          
           ship_position = self.size / 2            
           self.ship = SpriteNode(config.ship_type,
                                    parent = self, 
                                    position = ship_position,
                                    scale = 0.5,
                                    size = (500,500))
           self.ship_purchased == False                                          
        elif self.ship_purchased == False and self.counter == 1:      
           config.ship_type = './images/user_ship_2.PNG'
           self.ship_purchased = True
           ship_position = self.size / 2                 
           self.ship = SpriteNode(config.ship_type,
                                    parent = self, 
                                    position = ship_position,
                                    scale = 0.5,
                                    size = (500,500))  
           self.ship_purchased == False                                     
        if self.ship_purchased == True and self.counter == 0:  
           self.ship.remove_from_parent()  
           config.ship_type = 'images/usership1.png'
           ship_position = self.size / 2                
           self.ship = SpriteNode(config.ship_type,
                                    parent = self, 
                                    position = ship_position,
                                    scale = 0.3)                                                                                                        
        elif self.ship_purchased == False and self.counter == 0:           
           config.ship_type = 'images/usership1.png' 
           self.ship_purchased = True           
           ship_position = self.size / 2                   
           self.ship = SpriteNode(config.ship_type,
                                    parent = self, 
                                    position = ship_position,
                                    scale = 0.9)  


