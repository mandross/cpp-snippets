#!/usr/bin/env python

import os
import glob as gl
import lxml.etree as etree
import argparse as ap

def Main():
    path = ParseArguments().path
    FormatXmlsInPath(path)

def ParseArguments():
    parser = ap.ArgumentParser(description = 'Indents the xml in given path')
    parser.add_argument('path', help = 'path to files to be processed')
    return parser.parse_args()

def Indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for e in elem:
            Indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + "    "
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def FormatXmlsInPath(pathname):
    for xml_fname in gl.glob(pathname + '*.xml'):
        xml = etree.parse(xml_fname)
        Indent(xml.getroot())
        xml.write(xml_fname,  encoding="utf-8", pretty_print=True, xml_declaration=True)

if __name__ == '__main__':
    Main()
