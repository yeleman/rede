#!/usr/bin/env python
# encoding=utf-8

from RFParser import RemoteFormParser


def main():
    filename = '../docs/spec/examples/simpleform.xml'
    f = open(filename)
    content = u"\n".join(f.readlines())
    f.close()

    parser = RemoteFormParser()
    parser.parse(content)
    print(u"Formset: %s" % parser.formset.title)
    print(u"Forms: %d" % parser.formset.forms.__len__())
    for item in parser.formset.forms[0].items:
        print(u"Item: %s" % item.displayName())

if __name__ == '__main__':
    main()
