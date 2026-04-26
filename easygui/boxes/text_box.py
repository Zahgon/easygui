"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|
"""
import sys
from easygui.boxes.utils import mouse_click_handlers
try:
    from . import global_state
except (SystemError, ValueError, ImportError):
    import global_state
try:
    import tkinter as tk
    import tkinter.font as tk_Font
except:
    import Tkinter as tk
    import tkFont as tk_Font

def demo_textbox():
    pass

def demo_1():
    pass

class Demo2(object):
    """ Program that challenges the user to write 5 a's """

    def __init__(self):
        """ Set and run the program """
        title = 'Demo of textbox: Classic box with callback'
        gnexp = "This is a demo of the textbox with a callback, it doesn't flicker!.\n\n"
        msg = "INSERT A TEXT WITH FIVE OR MORE A's"
        text_snippet = 'Insert your text here'
        self.finished = False
        textbox(gnexp + msg, title, text_snippet, False, callback=self.check_answer, run=True)

    def check_answer(self, box):
        """ Callback from TextBox

        Parameters
        -----------
        box: object
            object containing parameters and methods to communicate with the ui

        Returns
        -------
        nothing:
            its return is through the box object
        """
        pass

class Demo3(object):
    """ Program that challenges the user to find a typo """

    def __init__(self):
        """ Set and run the program """
        self.finished = False
        title = 'Demo of textbox: Object with callback'
        msg = 'This is a demo of the textbox set as an object with a callback, you can configure it and when you are finished, you run it.\n\nThere is a typo in it. Find and correct it.'
        text_snippet = 'Hello'
        box = textbox(msg, title, text_snippet, False, callback=self.check_answer, run=False)
        box.text = 'It was the west of times, and it was the worst of times. The  rich ate cake, and the poor had cake recommended to them, but wished only for enough cash to buy bread.The time was ripe for revolution! '
        box.run()

    def check_answer(self, box):
        """ Callback from TextBox

        Parameters
        ----------
        box: object
            object containing parameters and methods to communicate with the ui

        Returns
        -------
        nothing:
            its return is through the box object
        """
        pass

def textbox(msg='', title=' ', text='', codebox=False, callback=None, run=True):
    """Displays a dialog box with a large, multi-line text box, and returns
    the entered text as a string. The message text is displayed in a
    proportional font and wraps.

    Parameters
    ----------
    msg : string
        text displayed in the message area (instructions...)
    title : str
        the window title
    text: str, list or tuple
        text displayed in textAreas (editable)
    codebox: bool
        if True, don't wrap and width is set to 80 chars
    callback: function
        if set, this function will be called when OK is pressed
    run: bool
        if True, a box object will be created and returned, but not run

    Returns
    -------
    None
        If cancel is pressed
    str
        If OK is pressed returns the contents of textArea

    """
    pass

class TextBox(object):
    """ Display a message and a text to edit

    This object separates user from ui, defines which methods can
    the user invoke and which properties can he change.

    It also calls the ui in defined ways, so if other gui
    library can be used (wx, qt) without breaking anything for the user.
    """

    def __init__(self, msg, title, text, codebox, callback=lambda *args, **kwargs: True):
        """ Create box object

        Parameters
        ----------
        msg : string
            text displayed in the message area (instructions...)
        title : str
            the window title
        text: str, list or tuple
            text displayed in textAres (editable)
        codebox: bool
            if True, don't wrap and width is set to 80 chars
        callback: function
            if set, this function will be called when OK is pressed

        Returns
        -------
        object
            The box object
        """
        self.callback = callback
        self.ui = GUItk(msg, title, text, codebox, self.callback_ui)
        self.text = text

    def run(self):
        """ Start the ui """
        pass

    def stop(self):
        """ Stop the ui """
        pass

    def callback_ui(self, ui, command, text):
        """ This method is executed when ok, cancel, or x is pressed in the ui.
        """
        pass

    @property
    def text(self):
        """Text in text Area"""
        pass

    @text.setter
    def text(self, text):
        pass

    @text.deleter
    def text(self):
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

    def to_string(self, something):
        pass

class GUItk(object):
    """ This is the object that contains the tk root object"""

    def __init__(self, msg, title, text, codebox, callback):
        """ Create ui object

        Parameters
        ----------
        msg : string
            text displayed in the message area (instructions...)
        title : str
            the window title
        text: str, list or tuple
            text displayed in textAres (editable)
        codebox: bool
            if True, don't wrap, and width is set to 80 chars
        callback: function
            if set, this function will be called when OK is pressed

        Returns
        -------
        object
            The ui object
        """
        self.callback = callback
        self.boxRoot = tk.Tk()
        wrap_text = not codebox
        if wrap_text:
            self.boxFont = tk_Font.nametofont('TkTextFont')
            self.width_in_chars = global_state.prop_font_line_length
        else:
            self.boxFont = tk_Font.nametofont('TkFixedFont')
            self.width_in_chars = global_state.fixw_font_line_length
        self.configure_root(title)
        self.create_msg_widget(msg)
        self.create_text_area(wrap_text)
        self.create_buttons_frame()
        self.create_cancel_button()
        self.create_ok_button()

    def run(self):
        pass

    def stop(self):
        pass

    def set_msg(self, msg):
        pass

    def set_msg_height(self, numlines):
        pass

    def get_num_lines(self, widget):
        pass

    def set_text(self, text):
        pass

    def set_pos(self, pos):
        pass

    def get_pos(self):
        pass

    def get_text(self):
        pass

    def x_pressed(self):
        pass

    def cancel_pressed(self, event):
        pass

    def ok_button_pressed(self, event):
        pass

    def calc_character_width(self):
        pass

    def configure_root(self, title):
        pass

    def create_msg_widget(self, msg):
        pass

    def create_text_area(self, wrap_text):
        """
        Put a textArea in the top frame
        Put and configure scrollbars
        """
        pass

    def create_buttons_frame(self):
        pass

    def create_cancel_button(self):
        pass

    def create_ok_button(self):
        pass
if __name__ == '__main__':
    demo_textbox()
