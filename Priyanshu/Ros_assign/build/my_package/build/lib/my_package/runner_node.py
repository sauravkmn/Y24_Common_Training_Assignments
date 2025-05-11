from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Declare the launch argument for the message
    message_arg = DeclareLaunchArgument(
        'message',
        default_value='Hello, ROS2 World!',
        description='Message to be published'
    )

    # Create the publisher node with the message parameter
    publisher_node = Node(
        package='my_package',
        executable='publisher_node',
        name='publisher_node',
        parameters=[{
            'message': LaunchConfiguration('message')
        }]
    )

    # Create the subscriber node
    subscriber_node = Node(
        package='my_package',
        executable='subscriber_node',
        name='subscriber_node'
    )

    # Return the launch description with all components
    return LaunchDescription([
        message_arg,
        publisher_node,
        subscriber_node
    ])