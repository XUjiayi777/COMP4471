from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

extensions = [
    Extension(
        "im2col_cython", ["im2col_cython.pyx"], include_dirs=[numpy.get_include()]
    ),
]

setup(ext_modules=cythonize(extensions, compiler_directives={'language_level' : "2"}),)
