from __future__ import print_function
'\n\n.. moduleauthor:: easygui developers and Stephen Raymond Ferg\n.. default-domain:: py\n.. highlight:: python\n\nVersion |release|\n'
import os
try:
    from . import utils as ut
    from . import fileboxsetup as fbs
except (SystemError, ValueError, ImportError):
    import utils as ut
    import fileboxsetup as fbs
tk = ut.tk

def fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False):
    """
    Displays an "open file" dialog box and returns the selected file as a string.

    The "default" argument specifies a filepath that (normally)
    contains one or more wildcards.

    fileopenbox() will display only files that match the default filepath.
    If omitted, defaults to "\\*" (all files in the current directory).

    WINDOWS EXAMPLE::

        ...default="c:/myjunk/*.py"

    will open in directory c:\\myjunk\\ and show all Python files.

    WINDOWS EXAMPLE::

        ...default="c:/myjunk/test*.py"

    will open in directory c:\\myjunk\\ and show all Python files
    whose names begin with "test".


    Note that on Windows, fileopenbox automatically changes the path
    separator to the Windows path separator (backslash).

    **About the "filetypes" argument**

    If specified, it should contain a list of items,
    where each item is either:

    - a string containing a filemask          # e.g. "\\*.txt"
    - a list of strings, where all of the strings except the last one
      are filemasks (each beginning with "\\*.",
      such as "\\*.txt" for text files, "\\*.py" for Python files, etc.).
      and the last string contains a filetype description

    EXAMPLE::

        filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]  ]

    .. note:: If the filetypes list does not contain ("All files","*"), it will be added.

    If the filetypes list does not contain a filemask that includes
    the extension of the "default" argument, it will be added.
    For example, if default="\\*abc.py"
    and no filetypes argument was specified, then
    "\\*.py" will automatically be added to the filetypes argument.

    :param str msg: the msg to be displayed.
    :param str title: the window title
    :param str default: filepath with wildcards
    :param object filetypes: filemasks that a user can choose, e.g. "\\*.txt"
    :param bool multiple: If true, more than one file can be selected
    :return: the name of a file, or None if user chose to cancel
    """
    pass
if __name__ == '__main__':
    print('Hello from file open box')
    ret_val = fileopenbox('Please select a file', 'My File Open dialog')
    print('Return value is:{}'.format(ret_val))
