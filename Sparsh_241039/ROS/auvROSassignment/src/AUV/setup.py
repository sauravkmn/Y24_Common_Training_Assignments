from setuptools import find_packages, setup

package_name = 'AUV'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/pubsublaunch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='spark',
    maintainer_email='spark@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = AUV.publisher:main',
            'subscriber = AUV.subscriber:main',
        ],
    },
)
