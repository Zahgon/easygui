try:
    from . import utils as ut
    from . import global_state
    from .base_boxes import bindArrows
except (SystemError, ValueError, ImportError):
    import utils as ut
    import global_state
    from base_boxes import bindArrows
try:
    import tkinter as tk
    import tkinter.font as tk_Font
except:
    import Tkinter as tk
    import tkFont as tk_Font
boxRoot = None
entryWidget = None
__enterboxText = ''
__enterboxDefaultText = ''
cancelButton = None
okButton = None

def __fillablebox(msg, title='', default='', mask=None, image=None, root=None):
    """
    Show a box in which a user can enter some text.
    You may optionally specify some default text, which will appear in the
    enterbox when it is displayed.
    Returns the text that the user entered, or None if they cancel the operation.
    """
    pass

def __enterboxQuit():
    pass

def __enterboxCancel(event):
    pass

def __enterboxGetText(event):
    pass

def __enterboxRestore(event):
    pass
