# task_3
# ArUco Marker Detection with TurtleBot3 in Gazebo
## This project demonstrates ArUco marker detection using OpenCV and simulates the detection with TurtleBot3 in Gazebo.
## Note: Setup has no camera caliberation so as a result i had to assume default matrix as 
                                                                                            [1000, 0, 640],
                                                                                            [0, 1000, 360],
                                                                                            [0,   0,   1]]

## Install opencv
  sudo apt-get update
  sudo apt-get install python3-opencv
## MAKING THE PACKAGE:
  ros2 pkg create --build-type ament_python aruco_detection_pkg
### Once all the files are made successfully the respective locations
  colcon build
  source install/setup.bash
### Executing aruco detection from video.mp4
    ros2 launch task_3 detect_aruco.py
### Executing aruco detection in gazebo
    ros2 launch task_3 detect_aruco_in_gazebo.launch.py
  

  
  
