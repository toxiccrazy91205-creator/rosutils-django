from setuptools import find_packages, setup

package_name = 'greeter_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev_parmar',
    maintainer_email='dev_parmar@todo.todo',
    description='A simple ROS 2 greeting project.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = greeter_pkg.talker_node:main',
            'listener = greeter_pkg.listener_node:main',
        ],
    },
)
