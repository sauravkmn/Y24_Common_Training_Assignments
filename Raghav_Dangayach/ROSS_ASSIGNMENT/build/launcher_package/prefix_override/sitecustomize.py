import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/raghav097891/Desktop/ROS2_WS/install/launcher_package'
