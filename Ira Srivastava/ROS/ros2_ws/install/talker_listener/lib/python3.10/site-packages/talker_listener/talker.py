#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.declare_parameter('message', 'Hello ROS2')
        self.msg = self.get_parameter('message').value
        self.get_logger().info(f"Publishing: {self.msg}")

    def timer_callback(self):
        msg = String()
        msg.data = self.msg
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
