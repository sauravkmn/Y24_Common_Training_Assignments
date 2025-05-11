#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
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
        self.get_logger().info(f"Listener published: '{new_msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()