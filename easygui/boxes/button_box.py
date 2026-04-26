"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|
"""
import os
import re
try:
    from . import global_state
    from . import utils as ut
    from .text_box import textbox
except (SystemError, ValueError, ImportError):
    import global_state
    import utils as ut
    from text_box import textbox
try:
    import tkinter as tk
    import tkinter.font as tk_Font
except (SystemError, ValueError, ImportError):
    import Tkinter as tk
    import tkFont as tk_Font

def demo_buttonbox_1():
    pass

def demo_buttonbox_2():
    pass

def is_sequence(arg):
    pass

def is_string(arg):
    pass

def buttonbox(msg='', title=' ', choices=('Button[1]', 'Button[2]', 'Button[3]'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True):
    """
    Display a message, a title, an image, and a set of buttons.
    The buttons are defined by the members of the choices argument.

    :param str msg: the msg to be displayed
    :param str title: the window title
    :param list choices: a list or tuple of the choices to be displayed
    :param str image: (Only here for backward compatibility)
    :param str images: Filename of image or iterable or iteratable of iterable to display
    :param str default_choice: The choice you want highlighted when the gui appears
    :return: the text of the button that the user selected



    """
    pass

class ButtonBox(object):
    """ Display various types of button boxes

    This object separates user from ui, defines which methods can
    the user invoke and which properties can he change.

    It also calls the ui in defined ways, so if other gui
    library can be used (wx, qt) without breaking anything for the user.
    """

    def __init__(self, msg, title, choices, images, default_choice, cancel_choice, callback):
        """ Create box object

        Parameters
        ----------
        msg : string
            text displayed in the message area (instructions...)
        title : str
            the window title
        choices : iterable of strings
            build a button for each string in choices
        images : iterable of filenames, or an iterable of iterables of filenames
            displays each image
        default_choice : string
            one of the strings in choices to be the default selection
        cancel_choice : string
            if X or <esc> is pressed, it appears as if this button was pressed.
        callback: function
            if set, this function will be called when any button is pressed.

        Returns
        -------
        object
            The box object
        """
        self.callback = callback
        self.ui = GUItk(msg, title, choices, images, default_choice, cancel_choice, self.callback_ui)

    def run(self):
        """ Start the ui """
        pass

    def stop(self):
        """ Stop the ui """
        pass

    def callback_ui(self, ui, command):
        """ This method is executed when buttons or x is pressed in the ui.
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

    @property
    def choice(self):
        """ Name of button selected """
        pass

    @property
    def choice_rc(self):
        """ The row/column of the selected button (as a tuple) """
        pass

    def to_string(self, something):
        pass

class GUItk(object):
    """ This is the object that contains the tk root object"""

    def __init__(self, msg, title, choices, images, default_choice, cancel_choice, callback):
        """ Create ui object

        Parameters
        ----------
        msg : string
            text displayed in the message area (instructions...)
        title : str
            the window title
        choices : iterable of strings
            build a button for each string in choices
        images : iterable of filenames, or an iterable of iterables of filenames
            displays each image
        default_choice : string
            one of the strings in choices to be the default selection
        cancel_choice : string
            if X or <esc> is pressed, it appears as if this button was pressed.
        callback: function
            if set, this function will be called when any button is pressed.


        Returns
        -------
        object
            The ui object
        """
        self._title = title
        self._msg = msg
        self._choices = choices
        self._default_choice = default_choice
        self._cancel_choice = cancel_choice
        self.callback = callback
        self._choice_text = None
        self._choice_rc = None
        self._images = list()
        self.boxRoot = tk.Tk()
        self.boxFont = tk_Font.nametofont('TkFixedFont')
        self.width_in_chars = global_state.fixw_font_line_length
        self.configure_root(title)
        self.create_msg_widget(msg)
        self.create_images_frame()
        self.create_images(images)
        self.create_buttons_frame()
        self.create_buttons(choices, default_choice)

    @property
    def choice(self):
        pass

    @property
    def choice_rc(self):
        pass

    def run(self):
        pass

    def stop(self):
        pass

    def set_msg(self, msg):
        pass

    def set_msg_height(self):
        pass

    def set_pos(self, pos):
        pass

    def get_pos(self):
        pass

    def x_pressed(self):
        pass

    def cancel_pressed(self, event):
        pass

    def button_pressed(self, button_text, button_rc):
        pass

    def hotkey_pressed(self, event=None):
        """
        Handle an event that is generated by a person interacting with a button.  It may be a button press
        or a key press.

        TODO: Enhancement: Allow hotkey to be specified in filename of image as a shortcut too!!!
        """
        pass

    def calc_character_width(self):
        pass

    def configure_root(self, title):
        pass

    def create_msg_widget(self, msg):
        pass

    def create_images_frame(self):
        pass

    def create_images(self, filenames):
        """
        Create one or more images in the dialog.
        :param filenames:
        May be a filename (which will generate a single image), a list of filenames (which will generate
        a row of images), or a list of list of filename (which will create a 2D array of buttons.
        :return:
        """
        pass

    def create_buttons_frame(self):
        pass

    def create_buttons(self, choices, default_choice):
        pass
if __name__ == '__main__':
    demo_buttonbox_1()
    demo_buttonbox_2()
