"""

.. moduleauthor:: easygui developers and Stephen Raymond Ferg
.. default-domain:: py
.. highlight:: python

Version |release|
"""
from easygui.boxes.utils import mouse_click_handlers
try:
    from . import global_state
except:
    import global_state
try:
    import tkinter as tk
except:
    import Tkinter as tk

def multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=tuple(), values=tuple(), callback=None, run=True):
    """
    Same interface as multenterbox.  But in multpassword box,
    the last of the fields is assumed to be a password, and
    is masked with asterisks.

    :param str msg: the msg to be displayed.
    :param str title: the window title
    :param list fields: a list of fieldnames.
    :param list values: a list of field values
    :return: String

    **Example**

    Here is some example code, that shows how values returned from
    multpasswordbox can be checked for validity before they are accepted::

        msg = "Enter logon information"
        title = "Demo of multpasswordbox"
        fieldNames = ["Server ID", "User ID", "Password"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multpasswordbox(msg,title, fieldNames)

        # make sure that none of the fields was left blank
        while 1:
            if fieldValues is None: break
            errmsg = ""
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg = errmsg + ('"%s" is a required field.\\n\\n' %
                     fieldNames[i])
                if errmsg == "": break # no problems found
            fieldValues = multpasswordbox(errmsg, title,
              fieldNames, fieldValues)

        print("Reply was: %s" % str(fieldValues))

    """
    pass

def multenterbox(msg='Fill in values for the fields.', title=' ', fields=[], values=[], callback=None, run=True):
    """
    Show screen with multiple data entry fields.

    If there are fewer values than names, the list of values is padded with
    empty strings until the number of values is the same as the number
    of names.

    If there are more values than names, the list of values
    is truncated so that there are as many values as names.

    Returns a list of the values of the fields,
    or None if the user cancels the operation.

    Here is some example code, that shows how values returned from
    multenterbox can be checked for validity before they are accepted::

        msg = "Enter your personal information"
        title = "Credit Card Application"
        fieldNames = ["Name","Street Address","City","State","ZipCode"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multenterbox(msg,title, fieldNames)

        # make sure that none of the fields was left blank
        while 1:
            if fieldValues is None: break
            errmsg = ""
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg += ('"%s" is a required field.\\n\\n' % fieldNames[i])
            if errmsg == "":
                break # no problems found
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)

        print("Reply was: %s" % str(fieldValues))

    :param str msg: the msg to be displayed.
    :param str title: the window title
    :param list fields: a list of fieldnames.
    :param list values: a list of field values
    :return: String
    """
    pass

class MultiBox(object):
    """ Show multiple data entry fields

    This object does a number of things:

    - chooses a GUI framework (wx, qt)
    - checks the data sent to the GUI
    - performs the logic (button ok should close the window?)
    - defines what methods the user can invoke and
      what properties he can change.
    - calls the ui in defined ways, so other gui
      frameworks can be used without breaking anything to the user
    """

    def __init__(self, msg, title, fields, values, mask_last, callback):
        """ Create box object

        Parameters
        ----------
        msg : string
            text displayed in the message area (instructions...)
        title : str
            the window title
        fields: list
            names of fields
        values: list
            initial values
        callback: function
            if set, this function will be called when OK is pressed
        run: bool
            if True, a box object will be created and returned, but not run

        Returns
        -------
        self
            The MultiBox object
        """
        self.callback = callback
        self.fields, self.values = self.check_fields(fields, values)
        self.ui = GUItk(msg, title, self.fields, self.values, mask_last, self.callback_ui)

    def run(self):
        """ Start the ui """
        pass

    def stop(self):
        """ Stop the ui """
        pass

    def callback_ui(self, ui, command, values):
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

    def check_fields(self, fields, values):
        pass

class GUItk(object):
    """ This object contains the tk root object.
        It draws the window, waits for events and communicates them
        to MultiBox, together with the entered values.

        The position in wich it is drawn comes from a global variable.

        It also accepts commands from Multibox to change its message.
    """

    def __init__(self, msg, title, fields, values, mask_last, callback):
        self.callback = callback
        self.boxRoot = tk.Tk()
        self.create_root(title)
        self.set_pos(global_state.window_position)
        self.create_msg_widget(msg)
        self.create_entryWidgets(fields, values, mask_last)
        self.create_buttons()
        self.entryWidgets[0].focus_force()

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

    def set_pos(self, pos):
        pass

    def get_pos(self):
        pass

    def get_values(self):
        pass

    def create_root(self, title):
        pass

    def create_msg_widget(self, msg):
        pass

    def create_entryWidgets(self, fields, values, mask_last):
        pass

    def create_buttons(self):
        pass

    def create_ok_button(self):
        pass

    def create_cancel_button(self):
        pass

    def bindArrows(self, widget):
        pass

    def tabRight(self, event):
        pass

    def tabLeft(self, event):
        pass

def demo1():
    pass

class Demo2:

    def __init__(self):
        msg = 'Without flicker. Enter your personal information'
        title = 'Credit Card Application'
        fieldNames = ['Name', 'Street Address', 'City', 'State', 'ZipCode']
        fieldValues = []
        fieldValues = multenterbox(msg, title, fieldNames, fieldValues, callback=self.check_for_blank_fields)
        print('Reply was: {}'.format(fieldValues))

    def check_for_blank_fields(self, box):
        pass
if __name__ == '__main__':
    demo1()
    Demo2()
