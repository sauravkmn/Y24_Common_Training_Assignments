from setuptools import find_packages, setup

package_name = 'talker'

setup(
            name=package_name,
            version='0.0.0',
            packages=find_packages (exclude=['test']),
            data files=[
                ('share/ament_index/resource_index/packages',
                ['resource/' + package_name] ),
                ('share/' + package_name, ['package.xml' ] ),

            install_requires=['setuptools'],
            zip_safe=True,
            maintainer='ashishu23',
            maintainer_email='ashishu23@iitk.ac.in',
            description='TODO: Package description',
            license='TODO: License declaration',
            tests_require=['pytest'],
            entry_points={
                'console_scripts': [
                    'talker = py_talker. talker:main',

                        
        ],
    },
)