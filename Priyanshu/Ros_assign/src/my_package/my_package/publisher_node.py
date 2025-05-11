#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'message_topic', 10)
        self.timer_period = 1.0  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        # Declare the message parameter with a default value
        self.declare_parameter('message', 'Default message')
        
        self.get_logger().info('Publisher node initialized')

    def timer_callback(self):
        msg = String()
        # Get the message from the parameter
        msg.data = self.get_parameter('message').get_parameter_value().string_value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    
    try:
        rclpy.spin(publisher_node)
    except KeyboardInterrupt:
        pass
    finally:
        publisher_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()