from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'message',
            default_value='Hello from launch!',
            description='The message to publish'
        ),
        Node(
            package= 'AUV',
            executable='publisher',
            name = 'sim',
            output = 'screen',
            parameters=[{'message': LaunchConfiguration('message')}]
        ),
        Node(
            package= 'AUV',
            executable='subscriber',
            name = 'sim',
            output = 'screen'
        ),
    ])