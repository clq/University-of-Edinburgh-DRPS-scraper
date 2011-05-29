import urllib
import re
class datafromurl:
   def __init__ (self, url): 
        self.f = urllib.urlopen(url)
        self.url = url
   def run(self):
        while 1:
            line = self.f.readline()
            if not line:
                break
            if '<h1 id="sitspagetitle" class="sitspagetitle"' in line:
                a = coursescraping(line)
                self.gradlevel = a.gradlevel()
                self.coursename = a.coursename()
                self.coursecode = a.coursecode()
            elif '> : Course Catalogue : ' in line:
                a = scraping(line)
                self.schoolcode = a.schoolcode()
                self.schoolname = a.schoolname()
            elif 'College of ' in line:
                a = collegescraping(line)
                self.collegename = a.collegename()
            elif 'width="35%">SCQF' in line:
                a = scraping(line)
                self.SCQF = a.SCQF()
                self.normyear = a.normyear()
                line = self.f.readline()
                line = self.f.readline()
                a = scraping(line)
                self.credits = a.credits()
            elif '"15%">Course website' in line:
                line = self.f.readline()
                line = self.f.readline()
                a = scraping(line)
                self.coursepage = a.coursepage()
            elif 'width ="15%">Course description</td>' in line:
                line = self.f.readline()
                a = scraping(line)
                total = a.description()
                line = self.f.readline()
                while (('</td' not in line) and ('</tr' not in line)):
                    total = total + " " + line
                    line = self.f.readline()
                total = total + " " + line
                line = self.f.readline()
                total = re.sub('<br />', "", total)
                total = re.sub('</td>', "", total)     
                total = re.sub('</tr>', "", total)    
                total = re.sub('\n', "  ", total)                
                self.description = total
            elif 'an="6">Delivery period' in line:
                if (('Semester 2' in line) or ('semester 2' in line) or ('Sem 2' in line) or ('sem 2' in line)):
                    self.semester = '2'
                elif (('Semester 1' in line) or ('semester 1' in line) or ('Sem 1' in line) or ('sem 1' in line)):
                    self.semester = '1'
                elif 'Full Year' in line:
                    self.semester = '3'
                else:
                    self.semester = '0'


            elif 'List of TELS:' in line:
                line = self.f.readline()
                a = timetablescrape(line)
                self.timetable = a.times()

                

        
class coursescraping:
    def __init__ (self, linein):
        self.raw = linein
        self.use = self.raw[:self.raw.index("</h1>")]
        self.use = self.use[69:]
    def gradlevel (self):
        if "Undergraduate" in self.use:
            return "UG"
        elif "Postgraduate" in self.use:
            return "PG"
        else:
            return "NA"
    def coursename (self):
        name = self.use
        name = re.sub(".* Course: ", "", name)
        name = re.sub("\(.*\)", "", name)
        name = re.sub(" $", "", name)
        return name
    def coursecode (self):
        code = self.use
        code = re.sub(".*\(", "", code)
        code = re.sub("\)", "", code)
        return code
        
class scraping:
    def __init__ (self, linein):
        self.use = linein
    def schoolcode (self):
        code = self.use
        code = re.sub('.*<a href="cx_s_su', "SU", code)
        code = re.sub('.htm">.*', "", code)
        code = re.sub('\n', "", code)
        return code
    def schoolname (self):
        name = self.use
        name = re.sub('.*School of ', "", name)
        name = re.sub('.*Business School', "Business School", name)
        name = re.sub('.*College of Medicine and Veterinary Medicine', "College of Medicine and Veterinary Medicine", name)
        name = re.sub('</a> :.*', "", name)
        name = re.sub('\)</a>.*', "", name)
        name = re.sub('\n', "", name).strip()
        return name
    def SCQF (self):
        level = self.use
        level = re.sub('.*">SCQF Level ', "", level)
        level = re.sub(' \(Year.*', "", level).strip()
        level = re.sub('[^0-9]', "", level)
        return level
    def normyear (self):
        if (('n/a' in self.use) or ('Postgraduate' in self.use)):
            return 0
        else:
            year = self.use
            year = re.sub('.*\(Year ', "", year)
            year = re.sub(' \(Year.*', "", year).strip()
            year = re.sub('[^0-9]', "", year)
            return year
    def credits (self):
        credits = self.use
        credits = re.sub('.*dth="35%">', "", credits)
        credits = re.sub('[^0-9]', "", credits).strip()
        return credits    
    def coursepage (self):
        if "None" in self.use:
            return "NA"
        else:
            url = self.use
            url = re.sub('.*href="', "", url)
            url = re.sub('" "target=.*', "", url).strip()
            return url
    def description (self):
        description = self.use
        description = re.sub('.*th ="85%" colspan="99">', "", description)
        total = description
        return description
        
        
        
        
class collegescraping:
    def __init__ (self, linein):
        self.use = linein
    def collegename (self):
        name = self.use
        name = re.sub('.*College of ', "", name)
        name = re.sub('</td>.*', "", name)
        name = re.sub('\n', "", name)
        return name

class timetablescrape:
    def __init__ (self, linein):
        self.use = linein
        self.entry = []
    def times (self):
        data = self.use
        data = re.sub('^<tr><td class="data1nobg" nowrap="nowrap">', '</td></tr><tr><td class="data1nobg" nowrap="nowrap">', data)
        data = re.sub('</br>', "", data)
        data = re.sub('<b>or</b>', " OR", data)
        print data
        while "nowrap" in data:
            data = re.sub('^</td></tr><tr><td class="data1nobg" nowrap="nowrap">', "", data)
            location = data[:data.index("<")]
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            type = data[:data.index("<")]
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            description = data[:data.index("<")]
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            weeks = data[:data.index("<")]
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            mon = data[:data.index("<")].strip()
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            tue = data[:data.index("<")].strip()
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            wed = data[:data.index("<")].strip()
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            thu = data[:data.index("<")].strip()
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            fri = data[:data.index("<")].strip()
            data = data[data.index("<"):]
            data = re.sub('^</td><td>', "", data)
            tempentry = [location, type, description, weeks, mon, tue, wed, thu, fri]
            self.entry.append(tempentry)
        return self.entry
