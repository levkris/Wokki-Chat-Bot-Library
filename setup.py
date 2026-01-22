from setuptools import setup, find_packages

setup(
    name='wokkichat',
    version='1.0.0',
    description='Python SDK to make bots for Wokki Chat',
    author='Bjarnos (& wokki20)',
    packages=find_packages(include=['wokkichat', 'wokkichat.*']),
    install_requires=[
        'python-socketio[client]',
        'aiohttp'
    ],
    python_requires='>=3.6',
    classifiers=[
        # https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta', # TODO 5 - Production/Stable
        'Natural Language :: English',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: AsyncIO',
        'Operating System :: OS Independent',
        'Typing :: Typed',
    ],
)
