cmake_minimum_required(VERSION 2.8.3)
project(collect_omni_data)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
)
include_directories(include ${catkin_INCLUDE_DIRS})
