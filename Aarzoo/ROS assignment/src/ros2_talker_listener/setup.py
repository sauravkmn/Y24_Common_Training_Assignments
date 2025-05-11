from setuptools import setup

package_name = 'ros2_talker_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/talker_listener_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='Simple ROS 2 pub-sub example',
    license='MIT',
    entry_points={
        'console_scripts': [
            'talker = ros2_talker_listener.talker:main',
            'listener = ros2_talker_listener.listener:main',
        ],
    },
)
