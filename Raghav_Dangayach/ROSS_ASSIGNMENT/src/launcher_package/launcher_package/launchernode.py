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
        # Create both Talker and Listener Nodes
        talker_node = TalkerNode()
        listener_node = ListenerNode()
        
        # Initialize MultiThreadedExecutor
        executor = MultiThreadedExecutor()
        
        # Add nodes to executor
        executor.add_node(talker_node)
        executor.add_node(listener_node)
        
        try:
            executor.spin()  # Spin the executor to handle callbacks
        except KeyboardInterrupt:
            self.get_logger().info("Shutting down the nodes...")
        finally:
            # Make sure nodes are destroyed when finished
            talker_node.destroy_node()
            listener_node.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    launcher_node = LauncherNode()
    launcher_node.start_nodes()  # Start the nodes
    rclpy.shutdown()

if __name__ == '__main__':
    main()
