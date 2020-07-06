import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

def callback(msg):
    print msg.ranges[360]
    move.linear.x = 0.1
    if msg.ranges[360] < 2:
	move.linear.x = 0
    pub.publish(move)

rospy.init_node('check')
sub = rospy.Subbscriber('/kobuki/laser/scan')
pub = rospy.Publisher('/cmd_vel',Twist)
move = Twist()

rospy.spin()
