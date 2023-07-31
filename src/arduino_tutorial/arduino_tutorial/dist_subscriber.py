import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

import serial
import time

class DistSubscriber(Node):
    def __init__(self):
            super().__init__('dist_subscriber')
            self.subscriber_ = self.create_subscription(String, '/dist_data',self.dist_callback, 10)

            self.declare_parameter('arduino_port', '/dev/ttyUSB0')
            self.declare_parameter("baud_rate", 11520)

            arduino_port = self.get_parameter('arduino_port').value
            baud_rate = self.get_parameter('baud_rate').value
            
            self.ser = serial.Serial(arduino_port, baud_rate)
            time.sleep(3)
            self.get_logger().info('아두이노 연결!!')
            
    def dist_callback(self, msg):
        data = msg.data
        self.get_logger().info('sub Distance: {0}cm'.format(data))

def main(args=None):
    rclpy.init(args=args)
    
    dist_subscriber = DistSubscriber()
    
    rclpy.spin(dist_subscriber)
    
    dist_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()