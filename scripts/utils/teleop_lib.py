import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy,Image, CameraInfo
from signal import signal, SIGINT
from std_msgs.msg import Bool

class Teleop():

    def __init__(self):

        self.lin = 0
        self.ang = 0
        self.start = False
        self.restart = False
        self.cmd_vel = Twist()
        self.__MAX_LIN = 0
        self.__MAX_ANG = 0
        self.cmd_vel_pub = None
        self.restart_pub = None
        self.pub_visual = False
        self.rate = 30

    def set_max(self, max_lin=1, max_ang=1):
        """
            Defines the max values for linear and angular velocities.
        """

        self.__MAX_LIN = max_lin
        self.__MAX_ANG = max_ang


    def callback_joy(self, msg):
        """
            Receives the raw message from publisher
        """

        # Setting velocities
        self.lin = msg.axes[1] * self.__MAX_LIN
        self.ang = msg.axes[2] * self.__MAX_ANG
        self.start = msg.buttons[0]
        self.restart = msg.buttons[1]

        if msg.buttons[3]:
            self.pub_visual = not self.pub_visual
            self.send_pub_visual()

        if self.restart:
            self.send_restart()

    def reset(self):
        """
            Reset all values to initial condition.
        """

        self.lin = 0
        self.lin = 0
        self.cmd_vel = Twist()
        self.start = False

    def send_cmd(self):
        """
            Publishes the velocity command.
        """

        self.cmd_vel.linear.x = self.lin
        self.cmd_vel.angular.z = self.ang

        if not self.start:
            self.cmd_vel = Twist()

        self.cmd_vel_pub.publish(self.cmd_vel)

        print(f"***\nLin: {self.cmd_vel.linear.x}\
                \nAng: {self.cmd_vel.angular.z}\
                \nSend vel: {self.start}\
                \nRestart: {self.restart}\n")

    def send_restart(self):

        if self.restart:
            restart = Bool()
            restart.data = True
            self.restart_pub.publish(restart)
            self.restart = False

    def send_pub_visual(self):

        self.start = False
        self.send_cmd()
        pub_visual = Bool()
        pub_visual.data = self.pub_visual
        self.pub_visual_pub.publish(pub_visual)

    #@staticmethod
    def exiting(self, signal_received, frame):
        """
            Handle any cleanup here
        """
        print('SIGINT or CTRL-C detected. Exiting gracefully')
        exit(0)

    def run(self):
        """
            Runs the node.
        """

        # Starting ros node
        rospy.init_node("joy_node", anonymous=True)

        # Publishers
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.restart_pub = rospy.Publisher('restart', Bool, queue_size=10)
        self.pub_visual_pub = rospy.Publisher('pub_visual', Bool, queue_size=10)

        # Subscribers
        rospy.Subscriber('joy', Joy, self.callback_joy)

        # Control parameters
        self.rate = rospy.Rate(self.rate)
        time.sleep(2)

        # Start loop
        while not rospy.is_shutdown():
            if not self.pub_visual:
                self.send_cmd()

            self.rate.sleep()

        signal(SIGINT, self.exiting)