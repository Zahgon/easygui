"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|

"""
import os
try:
    from . import utils as ut
except (SystemError, ValueError, ImportError):
    import utils as ut
try:
    import tkinter as tk
    import tkinter.font as tk_Font
except:
    import Tkinter as tk
    import tkFont as tk_Font

def fileboxSetup(default, filetypes):
    pass

class FileTypeObject:

    def __init__(self, filemask):
        if len(filemask) == 0:
            raise AssertionError('Filetype argument is empty.')
        self.masks = list()
        if isinstance(filemask, ut.basestring):
            self.initializeFromString(filemask)
        elif isinstance(filemask, list):
            if len(filemask) < 2:
                raise AssertionError('Invalid filemask.\n' + 'List contains less than 2 members: "{}"'.format(filemask))
            else:
                self.name = filemask[-1]
                self.masks = list(filemask[:-1])
        else:
            raise AssertionError('Invalid filemask: "{}"'.format(filemask))

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def add(self, other):
        pass

    def toTuple(self):
        pass

    def isAll(self):
        pass

    def initializeFromString(self, filemask):
        pass

    def getName(self):
        pass
