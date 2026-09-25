from setuptools import find_packages, setup

package_name = 'aeris_core'

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
    maintainer='hp_user',
    maintainer_email='hp_user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'heartbeat = aeris_core.heartbeat:main',
        'mission_publisher = aeris_core.mission_publisher:main',
        'monitor = aeris_core.monitor:main',
    ],
},
)
