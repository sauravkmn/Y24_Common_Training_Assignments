from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_pubsub_new',
            executable='talker',
            output='screen'
        ),
        Node(
            package='my_pubsub_new',
            executable='listener',
            output='screen'
        )
    ])

