# -*- coding: utf-8 -*-
from pymongo import Connection
import sys, os
import urllib
import xml.parsers.expat
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import simplejson as json
from lxml import etree


def parseFiles():
	n = 0
	js = json.load(open('ach.json', 'r'))
	for o in js:		
		arr = []
		for r in o.values():
			if r is not None: arr.append(r)
			else: arr.append(u'')
#		print arr
		s = u'\t'.join(arr)
		print s.encode('utf8')

if __name__ == '__main__':
	parseFiles()
			



