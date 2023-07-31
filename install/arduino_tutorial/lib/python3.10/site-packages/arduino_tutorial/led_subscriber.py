import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial
import time

class Ledsubsciver(Node):

    def __init__(self):
        super().__init__('led_subscriber')
        self.subscriber_=self.create_subscription(String, '/led_control', self.led_callback, 10)
        