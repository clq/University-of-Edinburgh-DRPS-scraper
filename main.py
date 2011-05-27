import urllib
import re
from urlhandler import *
from scrapeclasses import *
#http://www.star.euclid.ed.ac.uk/ipp/cx_sb_easc.htm
class subjectpage:
    def __init__ (self, url):
        self.page = urllib.urlopen(url)
    def fromsubjectpage (self):
        url2 = "null"
        while 1:
            pline = self.page.readline()
            if not pline:
                break
            if '<td><a href' in pline:
                    tempurl = re.sub('<td><a href="', "", pline)
                    tempurl = re.sub('">.*', "", tempurl).strip()
                    url = "https://www.star.euclid.ed.ac.uk/ipp/" + tempurl
                    pline = self.page.readline()
                    if (("Not" not in pline) and ('italic' not in pline) and (url != url2)):
                        finder = fromurl(url)
                        ha = finder.run()
                        url2 = url
                        print ""
                        print ""

class schoolpage:
    def __init__ (self, url):
        self.page = urllib.urlopen(url)
    def fromschoolpage (self):
        while 1:
            pline = self.page.readline()
            if not pline:
                break
            if '<a href="cx_sb' in pline:
                tempurl = re.sub('<li><a href="', "", pline)
                tempurl = re.sub('">.*', "", tempurl).strip()
                url = "https://www.star.euclid.ed.ac.uk/ipp/" + tempurl
                scrapesubjects = subjectpage(url)
                hm = scrapesubjects.fromsubjectpage()
                
class mainpage:
    def __init__ (self, url):
        self.page = urllib.urlopen(url)
    def frommainpage (self):
        while 1:
            pline = self.page.readline()
            if not pline:
                break
            if '<a href="cx_s' in pline:
                tempurl = re.sub('<li><a href="', "", pline)
                tempurl = re.sub('">.*', "", tempurl).strip()
                url = "https://www.star.euclid.ed.ac.uk/ipp/" + tempurl
                scrapeschool = schoolpage(url)
                hm = scrapeschool.fromschoolpage()
                
print "Testing"
program = mainpage("http://www.star.euclid.ed.ac.uk/ipp/cx_schindex.htm")
hm = program.frommainpage()

