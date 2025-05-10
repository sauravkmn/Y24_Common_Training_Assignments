import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sreeja/Assignments_Y24/sreeja_241041/ros/ros_new/install/py_pubsub'
