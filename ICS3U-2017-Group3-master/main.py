# Created by: luca,khoa
# with the help of Mr.Coxall’s space alien code
# Created on: Jan 2018
# Created for: ICS3U
# This program is the first file in a multi-scene game template
#    This template is meant to be used with the Xcode template,
#    to make apps for the App Store.
#
# Originally from: Ole Zorn, from the Xcode template
# for use with https://github.com/omz/PythonistaAppTemplate
# Also from the Pythonista community forum.
#
# This file creates the UIView that will be used by Xcode,
#  then creates the scene inside it. once everything is ready
#  to go, the scene transitions immediately to the first scene.
# It is assumed you bring along all your assets, 
#   and not use any of the mornal ones built into Pythonista.
#y
# To exit the app in Pythonista, pull down with 2 fingers.

# these are the links to the backroumd photes we found
#https://goo.gl/images/NW6itq
#https://goo.gl/images/3Sk2PF
#https://goo.gl/images/kmQgDY
#https://www.google.ca/search?hl=en-CA&q=space+background&tbm=isch&tbs=simg:CAQSmQEJRBQQ3L5Il2YajQELEKjU2AQaBggVCAAIAQwLELCMpwgaYgpgCAMSKOkVlAuVC5ML6hXMAdYBmAuXC_1gWpDfhKJUg2iieN6w34SGjN9go5SgaMHOwR2j7QJ-vU0RnKwKAJD5X_1Ddyr1oO5OL0KeFFJDFWSODCUio6h-I12AWt33kBsCAEDAsQjq7-CBoKCggIARIElO4fmQw&sa=X&ved=0ahUKEwj6l4T5493YAhVB6YMKHf7yCaIQwg4IIygA&biw=1920&bih=925#imgrc=30uKDJcL-7Y4-M



from scene import *
import ui

from splash_scene import *
from company_splash_screen import *

#  ..use when deploying app for Xcode and the App Store
main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = SplashScene()
main_view.present(hide_title_bar = True, animated = False)


