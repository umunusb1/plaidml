from __future__ import print_function

import os
import os.path
import shutil
from setuptools import setup

def main():
  os.chdir(os.path.dirname(__file__) or '.')
  
  if 'bzl_target_cpu' == 'x64_windows':
    os.system('attrib -R .\* /S')
  
  shutil.rmtree('build', ignore_errors=True)
  shutil.rmtree(os.path.join('pkg', 'bzl_package_name.egg-info'), ignore_errors=True)
  
  setup(
    name='bzl_package_name',
    version='bzl_version',
    package_dir={'':'pkg'},
    package_data={
        '': ['*.so', '*.dll', '*.json'],
    }
  )
  
  if 'bzl_target_cpu' == 'x64_windows':
    os.system('attrib -R pkg\bzl_package_name.egg-info\*')
  
  shutil.rmtree('build', ignore_errors=True)
  shutil.rmtree(os.path.join('pkg', 'bzl_package_name.egg-info'), ignore_errors=True)


if __name__ == '__main__':
  main()