#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32

class SubscriberPyNode:

  def __init__(self):
      # Initialise a subscriber
      rospy.Subscriber("/great_topic", UInt32, self.subscriberCallback, queue_size=1)

  # Implement the subscriber callback
  def subscriberCallback(self, msg):
      # Extract the data from the message
      this_data = msg.data
      # Display the data
      rospy.loginfo("[SUBSCRIBER PY  NODE] received message with data = " + str(this_data))


if __name__ == '__main__':
    # Initialise the node
    rospy.init_node("plain_py_node")
    # Display the namespace of the node handle
    rospy.loginfo("PLAIN PY NODE] namespace of node = " + rospy.get_namespace())
    # Spin as a single-threaded node
    SubscriberPyNode()
    rospy.spin()
