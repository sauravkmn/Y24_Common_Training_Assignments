# Assignments_Y24
Common Training Assignments of Y24 JTMs

ROS 2 Talker-Listener Project

This project is a basic ROS 2 (Robot Operating System 2) setup that demonstrates message publishing and subscribing using custom nodes. It consists of:

- A **Talker Node** that publishes messages to a topic.
- A **Listener Node** that subscribes to the topic and prints the messages.
- A **Launch File** that launches both nodes together.

Here's a screenshot of the running ROS@ Workspace:-
![
    
](<Screenshot from 2025-04-17 11-10-31-2.png>)

Here's a screenshot of the rqt graph of ROS2 Workspace
![
    
](<Screenshot from 2025-04-17 11-09-37.png>)

Basic  structure behind building and running of the Workspace:
An environment was set up on an Ubuntu desktop where a directory was created on the Desktop to house a ROS 2 workspace. Inside this workspace, a package was created containing three Python nodes: talker_node, publisher_node, and launcher_node. Each of these nodes was implemented in a separate Python file, where their individual functionalities were defined. The talker_node was designed to publish messages to a topic named /Input_msg, while the publisher_node subscribed to that topic and printed the received messages to the terminal. All three nodes were made executable by adding appropriate entries in the setup.py file, enabling them to be run directly using ROS 2 command-line tools. After writing the code, the workspace was built using colcon build, and then sourced to apply the new package and node definitions. The launcher_node was responsible for simultaneously launching both the talker_node and publisher_node, streamlining the testing process. When the system was visualized using rqt_graph, it clearly showed the talker_node publishing to the /Input_msg topic and the publisher_node subscribing to it, confirming the successful communication between the two. This setup provides a basic yet complete demonstration of ROS 2’s publish-subscribe model and launch system.



