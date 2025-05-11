from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'my_pubsub_new'

setup(
    name='my_pubsub_new',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/my_pubsub_new']),
        ('share/my_pubsub_new', ['package.xml']),
        ('share/my_pubsub_new/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='devdas',
    maintainer_email='devdas@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_pubsub_new.talker:main',
            'listener = my_pubsub_new.listener:main',
        ],
    },
)

