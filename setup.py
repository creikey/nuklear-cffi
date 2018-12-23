"""
Setup script for 'pynk' library.
"""

from setuptools import setup

setup(name='pynk',
      version='0.4',
      description='Python integration of the \'nuklear\' C library.',
      url='http://github.com/nathanrw/nuklear-cffi',
      author='Nathan Woodward',
      author_email='nathanrichardwoodward@gmail.com',
      license='Public domain',
      packages=['pynk'],
      setup_requires=["cffi>=1.0.0"],
      cffi_modules=["pynk/build.py:maker"],
      install_requires=["cffi>=1.0.0"],
      zip_safe=False)
