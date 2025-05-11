from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'message',
            default_value='Hello from launch!',
            description='Message to publish'
        ),
        Node(
            package='py_pub_sub',
            executable='talker',
            name='talker',
            parameters=[{'message': LaunchConfiguration('message')}]
        ),
        Node(
            package='py_pub_sub',
            executable='listener',
            name='listener'
        )
    ])

