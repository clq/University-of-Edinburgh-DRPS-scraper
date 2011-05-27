import urllib
import re
from scrapeclasses import *

       # print o.coursename + o.url
        # print " "
        # print "URL:"
        # print o.url
        # print " "
        # print "Timetable:"
        # self.timetable.append(o.timetable)
        # for f in self.timetable:
            # print f
        # return o.collegename

class fromurl:
    def __init__ (self, url):
        self.url = url
        timestart = ["Location", "Type", "Description", "Weeks", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.timetable = [timestart]
    def run (self):
        o = datafromurl(self.url)
        out = o.run()
        config = open('config.txt', 'r')
        while 1:
            line = config.readline()
            if not line:
                break
            if "GRADLEVEL" in line:
                print o.gradlevel,
            if "COURSENAME" in line:
                print '"' + o.coursename + '"',  
            if "COURSECODE" in line:
                print o.coursecode,
            if "SCHOOLCODE" in line:
                print o.schoolcode,  
            if "SCHOOLNAME" in line:
                print '"' + o.schoolname + '"',
            if "COLLEGENAME" in line:
                print '"' + o.collegename + '"',
            if "SCQFLEVEL" in line:
                print o.SCQF,  
            if "NORMALYEAR" in line:
                print o.normyear,
            if "CREDITS" in line:
                print o.credits,
            if "COURSEPAGE" in line:
                print o.coursepage,  
            if "DESCRIPTION" in line:
                print '"' + o.description + '"',
            if "DRPSURL" in line:
                print o.url,  
            if "SEMESTER" in line:
                print o.semester,
            
       