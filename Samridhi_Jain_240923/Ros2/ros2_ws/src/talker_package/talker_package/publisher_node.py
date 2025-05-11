#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.subscription = self.create_subscription(
            String,
            'input_msg',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, 'output_msg', 10)

    def listener_callback(self, msg):
        new_msg = String()
        new_msg.data = f"Modified: {msg.data}"
        self.publisher_.publish(new_msg)
        self.get_logger().info(f"Publisher published: '{new_msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()