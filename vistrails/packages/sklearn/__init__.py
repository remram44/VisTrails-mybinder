from vistrails.core.requirements import require_python_module

from .identifiers import *


def package_requirements():
    require_python_module('sklearn', {
                          'pip': 'scikit-learn',
                          'linux-debian': 'python-sklearn',
                          'linux-ubuntu': 'python-sklearn'})
