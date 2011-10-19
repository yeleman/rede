#!/usr/bin/env python
# encoding=utf-8

INPUT_TEXT = 'text'
INPUT_POSITIVE_INTEGER = 'posint'
INPUT_SIGNED_INTEGER = 'int'
INPUT_NEGATIVE_INTEGER = 'negint'
INPUT_DATE = 'date'


class BaseElement(object):
    ''' base class used to represent all elements '''

    def __init__(self, id=None):
        # assign random id if not supplied
        if not id:
            id = self.random_id()
        self.id = id
        self.attrs = {}

    @classmethod
    def random_id(cls):
        return 24

    def addAttr(self, name, value):
        self.attrs[name] = value

    def delAttr(self, name):
        del self.attrs[name]

    def displayName(self):
        base = None
        if hasattr(self, 'title'):
            base = getattr(self, 'title')
        if hasattr(self, 'label'):
            base = getattr(self, 'label')
        if hasattr(self, 'text'):
            base = getattr(self, 'text')
        if not base:
            base = self.__class__.title()
        return u"%(base)s/%(id)s" % {'base': base, 'id': self.id}


class FormSet(BaseElement):
    ''' root object. represents a collection of forms '''

    def __init__(self, id=None, title==u''):
        super(FormSet, self).__init__(id)
        self.title = title
        self.forms = []

    def addForm(self, form):
        self.forms.append(form)


class Form(BaseElement):
    ''' represent a form with its validation associated.

        Usually represented on a single page '''

    def __init__(self, id=None, title=u''):
        super(Form, self).__init__(id)
        self.title = title
        self.items = []

    def addItem(self, item):
        self.items.append(item)

class Table(BaseElement):
    ''' Table can only hold rows '''

    def __init__(self, id=None):
        super(Table, self).__init__(id)
        self.rows = []

    def addRow(self, row):
        self.rows.append(row)


class Row(BaseElement):
    ''' Row can only contain cells '''

    def __init__(self, id=None):
        super(Row, self).__init__(id)
        self.cells = []

    def addCell(self, cell):
        self.cells.append(cell)


class Cell(BaseElement):
    ''' Cell can only contain one Item '''

    def __init__(self, id=None):
        super(Cell, self).__init__(id)
        self.items = []

    def addItem(self, item):
        self.items.append(item)


class Separator(BaseElement):
    ''' An empty container '''

    def __init__(self, id=None):
        super(Separator, self).__init__(id)


class Item(BaseElement):
    ''' Item is either Input, Separator or Label '''
    pass


class Input(BaseElement):
    ''' Input holds the data and type '''

    def __init__(self, id, type=INPUT_TEXT, value=None):
        super(Input, self).__init__(id)
        self.type = type
        self.value = value

class Label(Item):

    def __init__(self, id):
        super(Label, self).__init__(id)
        self.text = u''
