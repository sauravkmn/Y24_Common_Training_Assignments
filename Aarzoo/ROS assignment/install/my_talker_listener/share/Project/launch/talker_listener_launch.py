import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the talker node
        Node(
            package='my_talker_listener',  # Name of your package
            executable='talker',            # The talker node executable
            name='talker_node',             # The node's name
            output='screen',                # Print output to the screen
        ),

        # Launch the listener node
        Node(
            package='my_talker_listener',  # Name of your package
            executable='listener',         # The listener node executable
            name='listener_node',          # The node's name
            output='screen',               # Print output to the screen
        ),
    ])
