from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    '_zmod',
    ['_zmod.pyx'],
    extra_compile_args=['-O3', '-fno-exceptions', '-fno-rtti'],
    extra_link_args=['-Wl,-s', '-Wl,--strip-all'],
    define_macros=[('NDEBUG', '1')],
)

setup(
    ext_modules=cythonize(
        [ext],
        compiler_directives={
            'language_level': '3',
            'boundscheck': False,
            'wraparound': False,
            'nonecheck': False,
            'embedsignature': False,
            'cdivision': True,
            'initializedcheck': False,
            'always_allow_keywords': False,
        }
    ),
    script_args=['build_ext', '--inplace']
)
