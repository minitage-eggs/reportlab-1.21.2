import os
def cd(options,buildout):
    os.chdir(options['compile-directory'])
    os.chdir('reportlab')

