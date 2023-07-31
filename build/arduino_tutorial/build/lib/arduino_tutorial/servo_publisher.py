import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial
import time

class ServoPublisher(Node):
    def __init__(self):
        super().__init__('servo_publisher')
        self.pos = 0

        self.publisher_ = self.create_publisher(String, '/servo_control', 10)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.declare_parameter('arduino_port', '/dev/ttyACM0')
        self.declare_parameter("baud_rate", 9600)
        
        arduino_port = self.get_parameter('arduino_port').value
        baud_rate = self.get_parameter('baud_rate').value
        
        self.ser = serial.Serial(arduino_port, baud_rate)
        time.sleep(3) #아두이노 연결 대기
        self.get_logger().info('아두이노 연결!!')
    
    def timer_callback(self):
        msg = String()
        self.pos += 10
        if self.pos > 180:
            self.pos = 0
        msg.data = str(self.pos)
        self.publisher_.publish(msg)
        
        self.get_logger().info('publish: {0}'.format(msg.data))
def main(args=None):
    rclpy.init(args=args)
    
    servo_publisher = ServoPublisher()
    
    rclpy.spin(servo_publisher)
    
    servo_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()