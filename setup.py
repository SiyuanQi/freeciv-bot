from setuptools import setup

setup(name='freecivbot',
      version='0.1',
      description='Freeciv bot allowing for research on AI for complex strategy games',
      url='http://github.com/chris1869/freeciv-bot',
      author='Chris1869',
      author_email='TBD',
      license='GLP3.0',
      package_dir={'':'src'},
      packages=['freecivbot'],
#      extras_require={"DOCK_IMG" : []},
#      entry_points = {
#        'console_scripts': ['create_img=freecivbot.build_server:build_docker_img [DOCK_IMG]'],
#      },
      install_requires=['docker'],
      zip_safe=False)

from freecivbot import build_server

build_server.build_docker_img()
