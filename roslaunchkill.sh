#!/bin/bash

# Find the PID of the roslaunch process for myroslaunch.launch
roslaunch_pid=$(ps aux | grep mylaunchfile.launch | awk '{print $2}')

# Check if the process is found
if [[ -z "$roslaunch_pid" ]]; then
  echo "ROS launch for myroslaunch.launch not found."
  exit 1
fi

# Send SIGINT for graceful termination
kill $(ps aux | grep mylaunchfile.launch | awk '{print $2}')

echo "ROS launch for myroslaunch.launch killed."