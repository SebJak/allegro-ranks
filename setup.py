from setuptools import setup

setup(name='allegro-ranks',
      version='0.1',
      description='Ranks of allegro data',
      url='http://github.com/sebjak/allegro-ranks',
      author='Sebastian Jakowski',
      packages=['allegro-ranks'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)