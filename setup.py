from setuptools import setup

setup(
    name='spacyapi',
    version='0.3',
    description='REST API for spaCy',
    author='Johannes Gontrum',
    author_email='gontrum@me.com',
    include_package_data=True,
    license='MIT license',
    entry_points={
          'console_scripts': [
              'start = spacyapi.scripts.start:run',
              'start_debug = spacyapi.scripts.start:run_debug'
          ]
      }
)
