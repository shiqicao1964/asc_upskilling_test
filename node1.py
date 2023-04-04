#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32
class PublisherPyNode:

  def __init__(self):
      # Initialise a publisher
      self.m_publisher = rospy.Publisher("/great_topic", UInt32, queue_size=10, latch=False)
      # Initialise a counter
      self.counter = 1
      # Initialise a timer
      timer_delta_t_in_seconds = 0.5
      rospy.Timer(rospy.Duration(timer_delta_t_in_seconds), self.timerCallback)

  # Implement the timer callback
  def timerCallback(self, event):
      self.counter += 1
      # Publish a message
      self.m_publisher.publish(self.counter)
    
if __name__ == '__main__':
    # Initialise the node
    rospy.init_node("plain_py_node") 
    # Display the namespace of the node handle
    rospy.loginfo("PLAIN PY NODE] namespace of node = " + rospy.get_namespace())
    publisher_py_node = PublisherPyNode()
    # Spin as a single-threaded node
    rospy.spin()
