from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('ros_package')

    # Ruta absoluta al URDF
    urdf_file = os.path.join(pkg_share, 'urdf', 'pepper.urdf')
    
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # Ruta al archivo rviz guardado
    #rviz_config = os.path.join(pkg_share, 'rviz', 'pepper.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name = "rviz2",
            #arguments=['-d', rviz_config],   # 👈 ahora lee TU archivo
            output='screen'
        )
    ])