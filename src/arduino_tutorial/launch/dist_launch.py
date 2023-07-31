import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    prarm_dir = LaunchConfiguration(
    'param_dir',
    default=os.path.join(
    get_package_share_directory('arduino_tutorial'),'param','arduino_config.yaml'))

    return LaunchDescription(
        [
            DeclareLaunchArgument('param_dir',default_value=prarm_dir),
            Node(
                package='arduino_tutorial',
                executable='dist_publisher',
                name='dist_publisher',
                parameters=[prarm_dir],
                output='screen'),
            
            Node(
                package='arduino_tutorial',
                executable='dist_subscriber',
                name='dist_subscriber',
                parameters=[prarm_dir],
                output='screen')
        
        ]
    )