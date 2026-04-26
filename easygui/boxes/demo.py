"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

"""
import os
import sys
try:
    from . import utils as ut
    from .button_box import buttonbox
    from .text_box import textbox
    from .diropen_box import diropenbox
    from .fileopen_box import fileopenbox
    from .filesave_box import filesavebox
    from .multi_fillable_box import multenterbox
    from .multi_fillable_box import multpasswordbox
    from .derived_boxes import ynbox
    from .derived_boxes import ccbox
    from .derived_boxes import boolbox
    from .derived_boxes import indexbox
    from .derived_boxes import msgbox
    from .derived_boxes import integerbox
    from .derived_boxes import enterbox
    from .derived_boxes import exceptionbox
    from .derived_boxes import codebox
    from .derived_boxes import passwordbox
    from .choice_box import choicebox
    from .choice_box import multchoicebox
    from . import about
    from .about import eg_version
    from .about import abouteasygui
except (SystemError, ValueError, ImportError):
    print('Please run demo.py from outside the package')
    exit()
package_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class Demos(object):
    """ Collection of demos

        A choice is comprised of two pieces of data:
        - a description, which is a string. The descriptions will be shown
          in the choicebox, and one will be returned by it.
        - a function to execute when the description is selected
    """

    def __init__(self):
        self.demos = [('msgbox', demo_msgbox), ('ynbox', demo_ynbox), ('ccbox', demo_ccbox), ('boolbox', demo_boolbox), ('buttonbox', demo_buttonbox), ('buttonbox that displays an image', demo_buttonbox_with_image), ('buttonbox - select an image', demo_buttonbox_with_choice), ('indexbox', demo_indexbox), ('choicebox', demo_choicebox), ('multchoicebox', demo_multichoicebox), ('textbox', demo_textbox), ('codebox', demo_codebox), ('enterbox', demo_enterbox), ('integerbox', demo_integerbox), ('passwordbox', demo_passwordbox), ('multenterbox', demo_multenterbox), ('multpasswordbox', demo_multpasswordbox), ('enterbox that displays an image', demo_enterbox_image), ('filesavebox', demo_filesavebox), ('fileopenbox', demo_fileopenbox), ('diropenbox', demo_diropenbox), ('exceptionbox', demo_exceptionbox), ('About EasyGui', demo_about), ('Help', demo_help)]

    def list_descriptions(self):
        pass

    def get_demo(self, index):
        pass

    def get_description(self, index):
        pass

    def __len__(self):
        return len(self.demos)

def easygui_demo():
    """
    Run the EasyGui demo.
    """
    pass

def demo_msgbox():
    pass

def demo_buttonbox():
    pass

def demo_buttonbox_with_image():
    pass

def demo_buttonbox_with_choice():
    pass

def demo_ccbox():
    pass

def demo_multichoicebox():
    pass

def demo_ynbox():
    pass

def demo_choicebox():
    pass

def demo_integerbox():
    pass

def demo_about():
    pass

def demo_enterbox():
    pass

def demo_multpasswordbox():
    pass

def demo_textbox():
    pass

def demo_codebox():
    pass

def demo_boolbox():
    pass

def demo_enterbox_image():
    pass

def demo_passwordbox():
    pass

def demo_help():
    pass

def demo_filesavebox():
    pass

def demo_diropenbox():
    pass

def demo_exceptionbox():
    pass

def demo_indexbox():
    pass

def demo_multenterbox():
    pass

def demo_fileopenbox():
    pass
