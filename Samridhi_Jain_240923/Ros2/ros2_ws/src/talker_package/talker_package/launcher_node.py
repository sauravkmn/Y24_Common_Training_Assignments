#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from talker_package.talker_node import TalkerNode
from talker_package.publisher_node import PublisherNode

class LauncherNode(Node):
    def __init__(self):
        super().__init__('launcher')
        self.get_logger().info("Launcher Node is starting...")
        
    def start_nodes(self):
        # Create both Talker and Publisher Nodes
        talker_node = TalkerNode()
        publisher_node = PublisherNode()
        
        # Start the nodes with MultiThreadedExecutor
        executor = MultiThreadedExecutor()
        executor.add_node(talker_node)
        executor.add_node(publisher_node)
        
        try:
            executor.spin()
        except KeyboardInterrupt:
            pass
        finally:
            talker_node.destroy_node()
            publisher_node.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    launcher_node = LauncherNode()
    launcher_node.start_nodes()
    rclpy.shutdown()

# Add this to ensure the node runs only if it's called directly
if __name__ == '__main__':
    main()
