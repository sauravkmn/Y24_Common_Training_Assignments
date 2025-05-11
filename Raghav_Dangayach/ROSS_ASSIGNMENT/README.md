## ROS2_WS

This is a ROS 2 workspace containing a simple publisher/subscriber setup with a launcher node.

## Packages

### launcher_package
Contains:

- `talkernode`: Publishes messages to a topic.
- `listenernode`: Subscribes and prints messages.
- `launchernode`: Launches both nodes together using a multi-threaded executor.

## Building

```bash
colcon build --symlink-install
source install/setup.bash

Important Screenshots

![
    
](<Screenshot from 2025-04-20 08-41-39.png>)
###RQT Graph 

![
    
](<Screenshot from 2025-04-20 08-42-35.png>)
###Working of ROS2 Workspace

![
    
](<Screenshot from 2025-04-20 08-45-34.png>)
###Various ROS2 functionalities

Basic Procedure

To build a ROS 2 workspace, we first created a directory named `ROS2_WS` with a `src` folder inside it using standard Linux commands. Inside `src`, we generated a new ROS 2 Python package called `launcher_package` using `ros2 pkg create`. We then opened the project in VS Code and created three node files: `talkernode.py`, `listenernode.py`, and `launchernode.py`. The `TalkerNode` publishes messages, the `ListenerNode` subscribes to them, and the `LauncherNode` launches both using a `MultiThreadedExecutor`. We wrote a `setup.py` to define entry points for each node and modified the `package.xml` to include necessary dependencies like `rclpy` and `std_msgs`. After that, we built the workspace using `colcon build`, sourced the environment, and tested each node using `ros2 run`. Once verified, we initialized a Git repository, committed the code, connected it to GitHub, pushed the changes, and added a README for documentation.