import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial
import time

class ServoSubscriber(Node):
    def __init__(self):
        super().__init__('servo_subscriber')
        self.subscriber_ = self.create_subscription(String, '/servo_control', self.servo_callback, 10)

        self.declare_parameter('arduino_port', '/dev/ttyACM0')
        self.declare_parameter("baud_rate", 9600)

        arduino_port = self.get_parameter('arduino_port').value
        baud_rate = self.get_parameter('baud_rate').value
        
        self.ser = serial.Serial(arduino_port, baud_rate)
        time.sleep(3)
        self.get_logger().info('아두이노 연결!!')

    def servo_callback(self, msg):
        cmd = msg.data
        self.get_logger().info("receive massage: {0}".format(cmd))
        if int(cmd) > 180:
            self.get_logger().info("180보다 작은 숫자를 입력해 주세요")
            
        elif int(cmd) < 0:
                self.get_logger().info("0보다 큰 숫자를 입력해 주세요")
        else:
            self.get_logger().info("{0}도로 이동합니다".format(cmd))
            pos = cmd.encode()
            self.ser.write(pos)

def main(args=None):
    rclpy.init(args=args)
    servo_subscriber = ServoSubscriber()
    rclpy.spin(servo_subscriber)
    servo_subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()