
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.declare_parameter('custom_message', 'Hello AUV!')
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        #msg.data = 'Hello AUV!: %d' % self.i
        #self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.i += 1

        msg.data = self.get_parameter('custom_message').get_parameter_value().string_value

        self.get_logger().info(f'Publishing: {msg.data} {self.i}')
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

'''

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.i = 0

    def publish_input_loop(self):
        try:
            while rclpy.ok():
                msg_input = input("Enter a message to publish: ")
                msg = String()
                msg.data = f"{msg_input} Hello World: {self.i}"
                self.publisher_.publish(msg)
                self.get_logger().info(f'Publishing: "{msg.data}"')
                self.i += 1
        except KeyboardInterrupt:
            pass


def main(args=None):
    rclpy.init(args=args)
    publisher = MinimalPublisher()
    publisher.publish_input_loop()
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
'''