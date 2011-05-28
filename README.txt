 ######  ######  ######   #####  
 #     # #     # #     # #     # 
 #     # #     # #     # #       
 #     # ######  ######   #####  
 #     # #   #   #             # 
 #     # #    #  #       #     # 
 ######  #     # #        #####  


1. ABOUT:
DRPS Scraper is a program that scrapes the University of Edinburgh Degree Program Regulations and outputs a textfile with information about and a the timetables of all the courses. The program has a configuration-file in which the user can specify what information about the course they want.

2. USAGE:

TO BE UPDATED
The program outputs output.txt, and reads the configuration-file from config.txt. The program is run by running main.py.

3. AVAILABLE INFORMATION

The options should be contained on the first line of config.txt seperated by spaces. All information will be outputted on a single line, followed by one line for each of the days with timetable-entries. See config.txt for sample outputs. For details of the parametres and what they output, see config.txt.

The program can output Graduate level, Course name, Course code, School code, School name, College name, SCQF-level, Normal year taken, Credits, Course-website, Description, DRPS-URL, Semester normally taken in.

The program also outputs the course timetable. Currently this is non-optional.

4. TIMETABLE

The timetable is outputted on the lines after the course-information. Each weekday will have a line of its own, starting with the day of the week, followed by the information for every event that happens on that day, seperated by ";". The format of the timetable is the following:
Day "location" "Event" "Description" weeks starttime endtime; "location2" "Event2" etc...

Actual output from a course with activities on Tuesday and Thursday may look like this. Note that there are two events on Tuesday and three events on Thursday:
Tue "King's Buildings" "Tutorial" "Examples class" 2-11 1000 1050; "King's Buildings" "Tutorial" "" 2-11 1500 1550;
Thu "King's Buildings" "Lecture" "" 1-11 1210 1300; "King's Buildings" "Lecture" "" 1-11 1500 1550; "King's Buildings" "Tutorial" "" 2-11 1610 1700;

5. KNOWN BUGS/ERRORS/INACCURACIES/PITFALLS

* Some courses have timetable-entries with options (along the lines of "time a" or "time b") At the moment these are outputted as seperate individual events for that day.



