import urllib
import re
from urlhandler import *
from scrapeclasses import *

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
        schoolnumber = 0
        while 1:
            pline = self.page.readline()
            if not pline:
                break
            if '<a href="cx_s' in pline:
                schoolnumber += 1
                print "School ", schoolnumber, " of 23"
                tempurl = re.sub('<li><a href="', "", pline)
                tempurl = re.sub('">.*', "", tempurl).strip()
                url = "https://www.star.euclid.ed.ac.uk/ipp/" + tempurl
                scrapeschool = schoolpage(url)
                hm = scrapeschool.fromschoolpage()


output = open('output.txt', 'w')                
#Main program
program = mainpage("http://www.star.euclid.ed.ac.uk/ipp/cx_schindex.htm")
hm = program.frommainpage()

#To test individual schools
#program = schoolpage("http://www.star.euclid.ed.ac.uk/ipp/cx_s_su780.htm")
#hm = program.fromschoolpage()

#To test individual subject-areas
#scrapesubjects = subjectpage("http://www.star.euclid.ed.ac.uk/ipp/cx_sb_accn.htm")
#hm = scrapesubjects.fromsubjectpage()

#To test individual courses
#program = fromurl("http://www.star.euclid.ed.ac.uk/ipp/cxbust10023.htm")
#running = program.run()