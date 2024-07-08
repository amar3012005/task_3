cmake_minimum_required(VERSION 3.5)
project(task_3)

set(CMAKE_CXX_STANDARD 14)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(image_transport REQUIRED)

add_executable(detect_aruco src/detect_aruco.cpp)
ament_target_dependencies(detect_aruco rclcpp cv_bridge sensor_msgs image_transport)
install(TARGETS
  detect_aruco
  DESTINATION lib/${PROJECT_NAME})

ament_package()

