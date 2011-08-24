#!/usr/bin/env python
# encoding=utf-8

from xml.dom import minidom

from models import *


class InvalidRemoteFormDocument(Exception):
    pass


class RemoteFormParser(object):

    def __init__(self):

        self._formset = None

    def parse(self, content):

        mdom = minidom.parseString(content)

        # retrieve <formset>
        # if dont exist, document is invalid.
        try:
            formsetElem = mdom.getElementsByTagName('formset')[0]
        except IndexError:
            raise InvalidRemoteFormDocument(u"No <formset> root element found")

        # build FormSet
        self._formset = FormSet(formsetElem.getAttribute('title'), \
                                formsetElem.getAttribute('id'))
        self.formset.addAttribute('onload', formsetElem.getAttribute('onload'))
        self.formset.addAttribute('onvalidate',
                                  formsetElem.getAttribute('onvalidate'))

        # loop on <form> inside FormSet
        for formElem in formsetElem.getElementsByTagName('form'):
            # build Form
            form = Form(formElem.getAttribute('title'), \
                        formElem.getAttribute('id'))

            for elem in formElem.childNodes:
                # we only interested by section, separator & item at this time
                if not elem.nodeName in ('section', 'item', 'separator'):
                    continue

                # section
                if elem.nodeName == 'section':
                    section = Section(elem.getAttribute('title'), \
                                      elem.getAttribute('id'))
                    form.addItem(section)
                    continue

                # separator
                if elem.nodeName == 'separator':
                    separator = Separator(elem.getAttribute('id'))
                    form.addItem(separator)
                    continue

                # item
                if elem.nodeName == 'item':
                    item = Item(elem.getAttribute('id'))
                    item.label = elem.getElementsByTagName('label')[0]\
                                                          .firstChild.nodeValue
                    inputElem = elem.getElementsByTagName('input')[0]
                    item.type = inputElem.getAttribute('type')
                    for attrn, attrv in inputElem.attributes.items():
                        if attrn in ('type'):
                            continue
                        item.addAttribute(attrn, attrv)
                    form.addItem(item)
                    continue

            # add created form to FormSet
            self._formset.addForm(form)

        # document without form is invalid
        if self.formset.forms.__len__() == 0:
            raise InvalidRemoteFormDocument(u"No <form> found in form set")

    @property
    def formset(self):
        return self._formset
