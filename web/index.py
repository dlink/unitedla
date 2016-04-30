#!/usr/bin/env python

from vweb.html import *
from vweb.htmlpage import HtmlPage

class Index(HtmlPage):

    def __init__(self, name='United LA Home Improvement'):
        HtmlPage.__init__(self, name)
        self.style_sheets = ['css/main.css']
        self.javascript_src.append('js/main.js')
        self.page = None
        
    def process(self):
        HtmlPage.process(self)
        if 'menu_choice' in self.form:
            self.page = self.form['menu_choice'].value

    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()
    
    def getHeader(self):
        return open('header.html','r').read()

    def getBody(self):
        return open('body.html','r').read() \
            % (self.getMenu(), self.getLeftSide())

    def getMenu(self):
        return open('menu.html', 'r').read()

    def getLeftSide(self):
        page = self.page

        if self.page:
            file = 'leftside-%s.html' % self.page
        else:
            file = 'leftside-home.html'

        return open(file, 'r').read()

    def getFooter(self):
        return ''

if __name__ == '__main__':
    Index().go()

