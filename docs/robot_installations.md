# Robots Installations

The Following Commands for each robot helps a user for a basic setup of different robots in RVIZ, Gazebo. These repo have virtual information for robot constructions in the urdf file. Not all contain the moveit configuration packages, so one needs to use moveit setup for bringing motion planning into the picture.

## Elfin:
```
$ sudo apt-get install ros-melodic-soem ros-melodic-gazebo-ros-control ros-melodic-ros-control ros-melodic-ros-controllers
$ sudo apt-get update
$ sudo apt-get install ros-melodic-moveit
$ cd ~/catkin_ws/src
$ git clone -b melodic-devel https://github.com/hans-robot/elfin_robot.git
$ cd ..
$ catkin_make
$ source devel/setup.bash
```

## UR5
If you are using 18.04 then DISTRO is Melodic, if it is 16.04 then type Kinetic 
```
cd $HOME/catkin_ws/src
git clone -b $ROS_DISTRO-devel https://github.com/ros-industrial/universal_robot.git
cd $HOME/catkin_ws
rosdep update
rosdep install --rosdistro $ROS_DISTRO --ignore-src --from-paths src
catkin_make
source $HOME/catkin_ws/devel/setup.bash
```

## Staubli 560
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/ros-industrial/staubli_experimental.git
$ git clone https://github.com/ros-industrial/staubli.git
$ cd ..
$ catkin_make
$ source devel/setup.bash
```

## Kuka KR6
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/ros-industrial/kuka_experimental.git
$ cd ..
$ catkin_make
$ source devel/setup.bash
```





