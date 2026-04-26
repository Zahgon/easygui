import string
import sys
from easygui.boxes.utils import mouse_click_handlers
if sys.version_info < (3, 3):
    from collections import Sequence
else:
    from collections.abc import Sequence
try:
    from . import global_state
    from .base_boxes import bindArrows
except (SystemError, ValueError, ImportError):
    import global_state
    from base_boxes import bindArrows
try:
    import tkinter as tk
    import tkinter.font as tk_Font
except:
    import Tkinter as tk
    import tkFont as tk_Font

def choicebox(msg='Pick an item', title='', choices=None, preselect=0, callback=None, run=True):
    """
    The ``choicebox()`` provides a list of choices in a list box to choose
    from. The choices are specified in a sequence (a tuple or a list).

        import easygui
        msg ="What is your favorite flavor?"
        title = "Ice Cream Survey"
        choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
        choice = easygui.choicebox(msg, title, choices)  # choice is a string

    :param str msg: the msg to be displayed
    :param str title: the window title
    :param list choices: a list or tuple of the choices to be displayed
    :param preselect: Which item, if any are preselected when dialog appears
    :return: A string of the selected choice or None if cancelled
    """
    pass

def multchoicebox(msg='Pick an item', title='', choices=None, preselect=0, callback=None, run=True):
    """
    The ``multchoicebox()`` function provides a way for a user to select
    from a list of choices. The interface looks just like the ``choicebox()``
    function's dialog box, but the user may select zero, one, or multiple choices.

    The choices are specified in a sequence (a tuple or a list).

        import easygui
        msg ="What is your favorite flavor?"
        title = "Ice Cream Survey"
        choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
        choice = easygui.multchoicebox(msg, title, choices)


    :param str msg: the msg to be displayed
    :param str title: the window title
    :param list choices: a list or tuple of the choices to be displayed
    :param preselect: Which item, if any are preselected when dialog appears
    :return: A list of strings of the selected choices or None if cancelled.
    """
    pass

def make_list_or_none(obj, cast_type=None):
    pass

class ChoiceBox(object):

    def __init__(self, msg, title, choices, preselect, multiple_select, callback):
        self.callback = callback
        if choices is None:
            choices = ('Choice 1', 'Choice 2')
        self.choices = self.to_list_of_str(choices)
        preselect_list = make_list_or_none(preselect, cast_type=int)
        if not multiple_select and len(preselect_list) > 1:
            raise ValueError('Multiple selections not allowed, yet preselect has multiple values:{}'.format(preselect_list))
        self.ui = GUItk(msg, title, self.choices, preselect_list, multiple_select, self.callback_ui)

    def run(self):
        """ Start the ui """
        pass

    def stop(self):
        """ Stop the ui """
        pass

    def callback_ui(self, ui, command, choices):
        """ This method is executed when ok, cancel, or x is pressed in the ui.
        """
        pass

    @property
    def msg(self):
        """Text in msg Area"""
        pass

    @msg.setter
    def msg(self, msg):
        pass

    @msg.deleter
    def msg(self):
        pass

    def to_list_of_str(self, choices):
        pass

class GUItk(object):
    """ This object contains the tk root object.
        It draws the window, waits for events and communicates them
        to MultiBox, together with the entered values.

        The position in wich it is drawn comes from a global variable.

        It also accepts commands from Multibox to change its message.
    """

    def __init__(self, msg, title, choices, preselect, multiple_select, callback):
        self.callback = callback
        self.choices = choices
        self.width_in_chars = global_state.prop_font_line_length
        self.multiple_select = multiple_select
        self.boxRoot = tk.Tk()
        self.boxFont = tk_Font.nametofont('TkTextFont')
        self.config_root(title)
        self.set_pos(global_state.window_position)
        self.create_msg_widget(msg)
        self.create_choicearea()
        self.create_ok_button()
        self.create_cancel_button()
        self.create_special_buttons()
        self.preselect_choice(preselect)
        self.choiceboxWidget.focus_force()

    def run(self):
        pass

    def stop(self):
        pass

    def x_pressed(self):
        pass

    def cancel_pressed(self, event):
        pass

    def ok_pressed(self, event):
        pass

    def set_msg(self, msg):
        pass

    def set_msg_height(self, numlines):
        pass

    def get_num_lines(self, widget):
        pass

    def set_pos(self, pos=None):
        pass

    def get_pos(self):
        pass

    def preselect_choice(self, preselect):
        pass

    def get_choices(self):
        pass

    def calc_character_width(self):
        pass

    def config_root(self, title):
        pass

    def create_msg_widget(self, msg):
        pass

    def create_choicearea(self):
        pass

    def create_ok_button(self):
        pass

    def create_cancel_button(self):
        pass

    def create_special_buttons(self):
        pass

    def KeyboardListener(self, event):
        pass

    def choiceboxClearAll(self, event):
        pass

    def choiceboxSelectAll(self, event):
        pass
if __name__ == '__main__':
    users_choice = multchoicebox(choices=['choice1', 'choice2'])
    print("User's choice is: {}".format(users_choice))
