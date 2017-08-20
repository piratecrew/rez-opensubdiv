# -*- coding: utf-8 -*-

name = 'opensubdiv'

version = '3.1.1'

authors = ['fredrik.brannbacka']

requires = [
    "glew-2",
    "ptex-2",
    "zlib"
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
