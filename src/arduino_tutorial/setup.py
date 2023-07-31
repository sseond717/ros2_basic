from setuptools import setup

import os
import glob

package_name = 'arduino_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob.glob(os.path.join('param', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiro04',
    maintainer_email='sseond717@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'led_subscriber = arduino_tutorial.led_subscriber:main',
            'dist_publisher = arduino_tutorial.dist_publisher:main',
            'dist_subscriber = arduino_tutorial.dist_subscriber:main',
            'servo_subscriber = arduino_tutorial.servo_subscriber:main',
            'servo_publisher = arduino_tutorial.servo_publisher:main'
        ],
    },
)
