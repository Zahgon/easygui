"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|

"""
import os
import sys
import traceback
runningPython27 = False
runningPython34 = False
if 34013424 <= sys.hexversion <= 50331888:
    runningPython27 = True
if 50594032 <= sys.hexversion <= 67109104:
    runningPython34 = True
if not runningPython27 and (not runningPython34):
    raise Exception('You must run on Python 2.7+ or Python 3.4+')
try:
    import tkinter as tk
    from tkinter import *
    import tkinter.filedialog as tk_FileDialog
    import tkinter.font as tk_Font
except ImportError:
    try:
        import Tkinter as tk
        from Tkinter import *
        import tkFileDialog as tk_FileDialog
        import tkFont as tk_Font
    except ImportError:
        raise ImportError('Unable to find tkinter package.')
if tk.TkVersion < 8.0:
    raise ImportError('You must use python-tk (tkinter) version 8.0 or higher')
try:
    from PIL import Image as PILImage
    from PIL import ImageTk as PILImageTk
except:
    pass
if runningPython27:
    basestring = basestring
if runningPython34:
    basestring = str

def exception_format():
    """
    Convert exception info into a string suitable for display.
    """
    pass

def uniquify_list_of_strings(input_list):
    """
    Ensure that every string within input_list is unique.
    :param list input_list: List of strings
    :return: New list with unique names as needed.
    """
    pass
import re

def parse_hotkey(text):
    """
    Extract a desired hotkey from the text.  The format to enclose
    the hotkey in square braces
    as in Button_[1] which would assign the keyboard key 1 to that button.
      The one will be included in the
    button text.  To hide they key, use double square braces as in:  Ex[[qq]]
    it  , which would assign
    the q key to the Exit button. Special keys such as <Enter> may also be
    used:  Move [<left>]  for a full
    list of special keys, see this reference: http://infohoglobal_state.nmt.edu/tcc/help/
    pubs/tkinter/web/key-names.html
    :param text:
    :return: list containing cleaned text, hotkey, and hotkey position within
    cleaned text.
    """
    pass

def load_tk_image(filename, tk_master=None):
    """
    Load in an image file and return as a tk Image.

    Loads an image.  If the PIL library is available use it.  otherwise use the tk method.

    NOTE: tk_master is required if there are more than one Tk() instances, which there are very often.
      REF: http://stackoverflow.com/a/23229091/2184122

    :param filename: image filename to load
    :param tk_master: root object (Tk())
    :return: tk Image object
    """
    pass

def getFileDialogTitle(msg, title):
    """
    Create nicely-formatted string based on arguments msg and title
    :param msg: the msg to be displayed
    :param title: the window title
    :return: None
    """
    pass
if __name__ == '__main__':
    print('Hello from utils')

def mouse_click_handlers(callback):
    pass
