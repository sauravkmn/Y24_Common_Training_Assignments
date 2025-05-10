from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_assignment',
            executable='talker',
            name='talker',
            parameters=[{'custom_message': 'Hello from launch file!'}],
            output='screen'
        ),
        Node(
            package='ros2_assignment',
            executable='listener',
            name='listener',
            output='screen'
        )
    ])
