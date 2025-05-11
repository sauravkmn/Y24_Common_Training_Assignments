from setuptools import find_packages, setup

package_name = 'launcher_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    zip_safe=True,
    maintainer='raghav097891',
    maintainer_email='raghav097891@todo.todo',
    description='ROS2 launcher package with talker and listener nodes',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talkernode=launcher_package.talkernode:main",
            "listenernode=launcher_package.listenernode:main",
            "launchernode=launcher_package.launchernode:main"
        ],
    },
)

