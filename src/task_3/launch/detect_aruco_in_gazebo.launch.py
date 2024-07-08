import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='task_3',
            executable='detect_aruco_in_gazebo.py',
            name='detect_aruco_in_gazebo',
            output='screen',
        ),
        ncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'), '/   turtlebot3_world.launch.py']
            ),
            launch_arguments={'world': world_file}.items()
        ),
    ])

