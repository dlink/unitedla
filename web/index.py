#!/usr/bin/env python

from vweb.html import *
from vweb.htmlpage import HtmlPage

class Index(HtmlPage):

    def __init__(self, name='United LA Home Improvement'):
        HtmlPage.__init__(self, name)
        self.style_sheets = ['css/main.css']

    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()
    
    def getHeader(self):
        return open('header.html','r').read()

    def getBody(self):
        return open('body.html','r').read()

    def getFooter(self):
        return ''

if __name__ == '__main__':
    Index().go()

