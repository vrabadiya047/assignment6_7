import rospy

from std_msgs.msg import Empty
rospy.init_node('sub_take')
pub_takeoff = rospy.Publisher('/drone/takeoff',Empty,queue_size=1)
var_empty = Empty()
pub_takeoff.publish(var_empty)
