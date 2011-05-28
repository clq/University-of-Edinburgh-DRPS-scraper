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
        output = open('output.txt', 'a')
        monb = False
        tueb = False
        wedb = False
        thub = False
        frib = False
        mon = "Mon"
        tue = "Tue"
        wed = "Wed"
        thu = "Thu"
        fri = "Fri"
        o = datafromurl(self.url)
        out = o.run()
        localtimetable = o.timetable
        config = open('config.txt', 'r')
        line2 = config.readline()
        while 1:
            line2 = re.sub('^ ', "", line2)
            if ' ' in line2:
                line = line2[:line2.index(" ")]
                print line
                line2 = line2[line2.index(" "):]
            else:
                line = line2
            if "GRADLEVEL" in line:
                print >> output, o.gradlevel,
            if "COURSENAME" in line:
                print >> output, '"' + o.coursename + '"',  
            if "COURSECODE" in line:
                print >> output, o.coursecode,
            if "SCHOOLCODE" in line:
                print >> output, o.schoolcode,  
            if "SCHOOLNAME" in line:
                print >> output, '"' + o.schoolname + '"',
            if "COLLEGENAME" in line:
                print >> output, '"' + o.collegename + '"',
            if "SCQFLEVEL" in line:
                print >> output, o.SCQF,  
            if "NORMALYEAR" in line:
                print >> output, o.normyear,
            if "CREDITS" in line:
                print >> output, o.credits,
            if "COURSEPAGE" in line:
                print >> output, o.coursepage,  
            if "DESCRIPTION" in line:
                print >> output, '"' + o.description + '"',
            if "DRPSURL" in line:
                print >> output, o.url,  
            if "SEMESTER" in line:
                print >> output, o.semester,
            if ' ' not in line2:
                break
        for f in localtimetable:
            if f[4]:
                string = f[4]
                monb = True
                mon = mon + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " "
                string = re.sub('^OR ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                mon = mon + temp
                string = string[string.index("-"):]
                string = re.sub('^- ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                mon = mon + " " + temp + ";"
                while 'OR' in string:
                    string = re.sub('^OR ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]  
                    mon = mon + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " " + temp        
                    string = string[string.index("-"):]
                    string = re.sub('^- ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]
                    mon = mon + " " + temp + ";"                       
            if f[5]:
                string = f[5]
                tueb = True
                tue = tue + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " "
                string = re.sub('^OR ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                tue = tue + temp
                string = string[string.index("-"):]
                string = re.sub('^- ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                tue = tue + " " + temp + ";"
                while 'OR' in string:
                    string = re.sub('^OR ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]  
                    tue = tue + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " " + temp 
                    string = string[string.index("-"):]
                    string = re.sub('^- ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]
                    tue = tue + " " + temp + ";"        
            if f[6]:
                string = f[6]
                wedb = True
                wed = wed + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " "
                string = re.sub('^OR ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                wed = wed + temp
                string = string[string.index("-"):]
                string = re.sub('^- ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                wed = wed + " " + temp + ";"
                while 'OR' in string:
                    string = re.sub('^OR ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]  
                    wed = wed + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " " + temp
                    string = string[string.index("-"):]
                    string = re.sub('^- ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]
                    wed = wed + " " + temp + ";"         
            if f[7]:
                string = f[7]
                thub = True
                thu = thu + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " "
                string = re.sub('^OR ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                thu = thu + temp
                string = string[string.index("-"):]
                string = re.sub('^- ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                thu = thu + " " + temp + ";"
                while 'OR' in string:
                    string = re.sub('^OR ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]  
                    thu = thu + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " " + temp
                    string = string[string.index("-"):]
                    string = re.sub('^- ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]
                    thu = thu + " " + temp + ";"          
            if f[8]:
                string = str(f[8])
                frib = True
                fri = fri + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " "
                string = re.sub('^OR ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                fri = fri + temp
                string = string[string.index("-"):]
                string = re.sub('^- ', "", string)
                temp = string[:string.index(":")]
                string = string[string.index(":"):]
                string = re.sub('^:', "", string)
                temp = temp + string[:2]
                fri = fri + " " + temp + ";"
                while 'OR' in string:
                    string = re.sub('^OR ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]  
                    fri = fri + " " + '"' + f[0] + '"' + " " + '"' + f[1] + '"' + " " + '"' + f[2] + '"' + " " + f[3] + " " + temp
                    string = string[string.index("-"):]
                    string = re.sub('^- ', "", string)
                    temp = string[:string.index(":")]
                    string = string[string.index(":"):]
                    string = re.sub('^:', "", string)
                    temp = temp + string[:2]
                    fri = fri + " " + temp + ";"     
        print >> output, ""
        if monb == True:
            print >> output, mon
        if tueb == True:
            print >> output, tue
        if wedb == True:
            print >> output, wed
        if thub == True:
            print >> output, thu
        if frib == True:
            print >> output, fri
        print >> output, ""
                    #       if (mon == True):
            