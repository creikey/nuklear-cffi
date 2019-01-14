nuklear-cffi
============

.. image:: https://travis-ci.org/nathanrw/nuklear-cffi.svg?branch=master

A semi-automatic Python binding for the nuklear C library.

The core of this is a python program that parses the nuklear.h header for
declarations and passes this to the 'cffi' Python binding generator.

Declarations are extracted using a C preprocessor followed by some simple ad
hoc text transformations.  The 'pcpp' preprocessor is used.  This is a C
preprocessor written in Python, so the preprocessing step doesn't actually
require a C compiler to be installed.

However, the process of generating the Python binding requires a C
compiler.

Some code for interfacing nuklear with pygame is provided under `pynk.nkpygame`.

Usage
-----

See `demo.py`.  The gist of it is to call the nuklear API via the `ffi` and
`lib` objects imported from `pynk` - this is provided by the `cffi` library.
Some code for interfacing with pygame is provided.

Installation
------------

The package on pypi should work: https://pypi.python.org/pypi/pynk

Otherwise

``python setup.py install``

in the git repository should do it.

Dependencies
------------

- cffi, a Python library.

For the pygame integration code, `pygame` is necessary, but it's not a
requirement for installation or to use the binding.

How to do a release
-------------------

The following script will increment the version, commit the change and push 
a tag. The Travis build will then deploy a new version.

``python ./bin/version.py (--major|--minor|--patch)``
