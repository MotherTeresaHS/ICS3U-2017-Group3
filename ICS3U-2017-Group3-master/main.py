# Created by: luca,khoa
# with the help of Mr.Coxall's space alien code
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

# these are the links to the backround photes we found
#https://goo.gl/images/ztLTKy
#https://goo.gl/images/mp6MXd
#https://goo.gl/images/asdDvg
#https://goo.gl/images/Gvz2Sb



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


