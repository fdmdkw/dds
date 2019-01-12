from distutils.core import setup, Extension

setup(name='ddsTable',
      py_modules=['ddsTable.py'],
      ext_modules=[
        Extension('ddsTable',
                  ['ddsTable_wrap.cxx'],
                  include_dirs = [],
                  define_macros = [],

                  undef_macros = [],
                  library_dirs = [],
                  libraries = ['ddsTable']
                  )
        ]
)
'''
create libddsTable.so
'''