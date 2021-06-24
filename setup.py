from distutils.core import setup

import py2exe

setup(
  name="ROX Auto Click",
  zip_safe=False,
  console=["app.py"]
)