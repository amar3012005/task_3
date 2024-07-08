# task_3
# ArUco Marker Detection with TurtleBot3 in Gazebo
## This project demonstrates ArUco marker detection using OpenCV and simulates the detection with TurtleBot3 in Gazebo.
## Note: Setup has no camera caliberation so as a result i had to assume default matrix as 
                                                                                            [1000, 0, 640],
                                                                                            [0, 1000, 360],
                                                                                            [0,   0,   1]]

## Install opencv
## MAKING THE PACKAGE:
  ros2 pkg create --build-type ament_python aruco_detection_pkg
  
  
