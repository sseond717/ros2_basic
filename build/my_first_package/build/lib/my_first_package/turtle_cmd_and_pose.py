import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose

class CmdAndPose(Node):

    def __init__(self):
        super().__init__('turtle_cmd_pose')
        self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)

    def Callback_pose(self, msg):
        print(msg)

def main(args=Node):
    rp.init(args=args)

    turtle_cmd_pose_node = CmdAndPose()
    rp.spin(turtle_cmd_pose_node)

    turtle_cmd_pose_node.destroy_node()
    rp.shutdown()

if __name__ == "__main__":
    main()
