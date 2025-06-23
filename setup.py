
from setuptools import setup, find_packages

setup(
    name='kurwica',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'kurwica = kurwica.cli.main:main',
        ],
    },
    install_requires=[
        # Add dependencies here
    ],
    author='OpenHands',
    author_email='openhands@all-hands.dev',
    description='A tool for automating ZFS pool maintenance on Debian systems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dk7458/kurwica',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
