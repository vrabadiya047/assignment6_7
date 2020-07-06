import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

rospy.init_node('take')

# publishers and data to publish
empty = Empty()
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)


# takeoff 
takeoff.publish(empty)

