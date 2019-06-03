# setup.py

from setuptools import setup, find_packages
import sys

if not sys.version_info[0] == 3:
    sys.exit('Sorry, python2 is not supported')

project_name = 'HoneyBot'
long_description = '''
HoneyBot is an IRC bot written in python3,
and distributed under MIT license.

Current features include:
- OOP architecture
- keyword parameters
- password security with config file [disabled for now]
- plugins like calc, self trivia, quotes, and many more
'''

setup(
    name = project_name,
    version = '5.0.0',
    description = 'HoneyBot is a python-based IRC bot. (python3)',
    long_description = long_description,
    url = 'https://github.com/Abdur-rahmaanJ/honeybot',
    download_url = 'https://github.com/Abdur-rahmaanJ/honeybot/tags',
    author = 'Abdur-Rahmaan Janhangeer',
    author_email = 'arj.python@gmail.com',
    license = 'MIT',
    include_package_data = True,

    packages = ['monopoly_assets', 'poker_assets'],
    package_dir = {
        'monopoly_assets' : 'honeybot/plugins/monopoly_assets',
        'poker_assets' : 'honeybot/plugins/poker_assets'
    },
    
    python_requires='>=3.0',
    classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Topic :: Utilities',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.7'
      ]
)
