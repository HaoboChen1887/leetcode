from setuptools import setup

setup(
    name='filegen',
    version='1.0',
    packages=['filegen'],
    include_package_data=True,
    install_requires=[
        'click==7.0',
    ],
    entry_points={
        'console_scripts': [
            'filegen = filegen.__main__:main'
        ]
    },
)
