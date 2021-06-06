#!/usr/bin/python
import argparse
import sys
import os 



# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-robot", "--robot", required=True, help="name of the robot")

args = vars(ap.parse_args())

robot = args['robot']

base_path = "$HOME/catkin_ws/src"

os.system('roslaunch hticros rviz_launcher.launch model:="{}/hticros/urdf/{}.urdf"'.format(base_path,robot))
