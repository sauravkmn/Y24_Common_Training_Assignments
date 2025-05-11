#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from launcher_package.talkernode import TalkerNode
from launcher_package.listenernode import ListenerNode     
class LauncherNode(Node):
    def __init__(self):
        super().__init__('launcher')
        self.get_logger().info("Launcher Node is starting...")
        
    def start_nodes(self):
        # Create both Talker and Publisher Nodes
        talker_node = TalkerNode()
        publisher_node = ListenerNode()
        
        # Start the nodes with MultiThreadedExecutor
        executor = MultiThreadedExecutor()
        executor.add_node(TalkerNode)
        executor.add_node(ListenerNode)
        
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