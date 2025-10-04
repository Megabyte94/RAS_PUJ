import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/megabyte94/Desktop/RAS/taller1/taller2_ras/install/ros_package'
