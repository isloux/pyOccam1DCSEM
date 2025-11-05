#!/usr/bin/env python

from distutils.core import setup
from distutils.command.build import build
import os
import sys
import shutil
import subprocess
from pyoccam1dcsem import __version__

class CMakeBuild(build):
    def run(self):
        build_dir = os.path.abspath(self.build_temp)
        project_dir = os.path.abspath('.')

        # Create the build directory
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        # Prepare CMake command
        pyoccam_dir = os.path.join(project_dir, 'pyoccam1dcsem')
        cmake_command = f"cmake -DMKL_DIR=$MKLROOT/lib/cmake/mkl {pyoccam_dir}"

        # Run CMake
        subprocess.call(cmake_command, shell=True, cwd=build_dir)

        # Run make
        subprocess.call(['make'], cwd=build_dir)

        # Create build/lib directory
        if not os.path.exists(self.build_lib):
            os.makedirs(self.build_lib)

        # Copy the library to the package
        if sys.platform == "linux" or sys.platform == "linux2":
            lib_name = 'liboccam1dcsem.so'
        elif sys.platform == "darwin":
            lib_name = 'liboccam1dcsem.dylib'
        else:
            raise Exception("Unsupported platform")

        lib_path = os.path.join(build_dir, lib_name)
        target_dir = os.path.join(self.build_lib, 'pyoccam1dcsem')

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        shutil.copy(lib_path, target_dir)

setup(
    name='pyOccam1DCSEM',
    version=__version__,
    packages=['pyoccam1dcsem'],
    author='Christophe Ramananjaona',
    author_email='isloux AT yahoo.co.uk',
    url='https://github.com/isloux/pyOccam1DCSEM',
    license='GNU General Public License v3',
    long_description=open('README.txt').read(),
    classifiers=["Programming Language :: Python",
        "Programming Language :: Fortran"],
    cmdclass={'build': CMakeBuild}
)
