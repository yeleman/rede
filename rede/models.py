#!/usr/bin/env python
# encoding=utf-8

INPUT_TEXT = 'text'
INPUT_POSITIVE_INTEGER = 'posint'
INPUT_SIGNED_INTEGER = 'int'
INPUT_NEGATIVE_INTEGER = 'negint'
INPUT_DATE = 'date'


class FormSet(object):

    def __init__(self, title=None, id=None):
        self.title = title
        self.forms = []
        self.attrs = {}

    def addAttribute(self, name, value):
        self.attrs[name] = value

    def addForm(self, form):
        self.forms.append(form)


class Form(object):

    def __init__(self, title=None, id=None):
        self.title = title
        self.items = []
        self.attrs = {}

    def addAttribute(self, name, value):
        self.attrs[name] = value

    def addItem(self, item):
        self.items.append(item)


class GenericItem(object):
    def __init__(self):
        self.attrs = {}

    def addAttribute(self, name, value):
        self.attrs[name] = value

    def displayName(self):
        if hasattr(self, 'label'):
            if self.label:
                return self.label
        if hasattr(self, 'title'):
            if self.title:
                return self.title
        return self.__class__


class Separator(GenericItem):

    def __init__(self, title=None, id=None):
        self.title = title
        self.id = id


class Item(GenericItem):

    def __init__(self, id=None):

        self.id = id
        self.label = u""
        self.input = None
        self.attrs = {}

    def addAttribute(self, name, value):
        self.attrs[name] = value


class Input(object):

    def __init__(self, type=INPUT_TEXT, value=None):

        self.type = type
        self.value = value
