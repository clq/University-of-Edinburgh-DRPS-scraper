 ######  ######  ######   #####  
 #     # #     # #     # #     # 
 #     # #     # #     # #       
 #     # ######  ######   #####  
 #     # #   #   #             # 
 #     # #    #  #       #     # 
 ######  #     # #        #####  


1. ABOUT:
DRPS Scraper is a program that scrapes the University of Edinburgh Degree Program Regulations and outputs a text file with information about, and a the timetables for all the courses. The program has a configuration-file in which the user can specify what information about the course they want. The program does not scrape courses that are not delivered.

The runtime of the program depends primarily on the speed of the internet-connection. On a quick connection it finishes within 20 minutes, but this may vary significantly on slower connections.

2. USAGE:

The program currently consists of four files, main.py, scrapeclasses.py, urlhandler.py and config.txt. config.txt in the configuration-file, for more information on configuration see config.txt.
The program output is output.txt. Make sure that you have write-access to the folder in which you run the program.
Run the program by running main.py ("python main.py" from the command-line)


3. AVAILABLE INFORMATION

The options should be contained on the first line of config.txt separated by spaces. All information will be outputted on a single line, followed by one line for each of the days with timetable-entries. See config.txt for sample outputs. For details of the parameters and what they output, see config.txt.

The program can output Graduate level, Course name, Course code, School code, School name, College name, SCQF-level, Normal year taken, Credits, Course-website, Description, DRPS-URL, Semester normally taken in.

The program also outputs the course timetable. Currently this is non-optional.


4. TIMETABLE

The timetable is outputted on the lines after the course-information. Each weekday will have a line of its own, starting with the day of the week, followed by the information for every event that happens on that day, separated by ";". The format of the timetable is the following:
Day "location" "Event" "Description" weeks starttime endtime; "location2" "Event2" etc...

Actual output from a course with activities on Tuesday and Thursday may look like this. Note that there are two events on Tuesday and three events on Thursday:
Tue "King's Buildings" "Tutorial" "Examples class" 2-11 1000 1050; "King's Buildings" "Tutorial" "" 2-11 1500 1550;
Thu "King's Buildings" "Lecture" "" 1-11 1210 1300; "King's Buildings" "Lecture" "" 1-11 1500 1550; "King's Buildings" "Tutorial" "" 2-11 1610 1700;


5. KNOWN BUGS/ERRORS/INACCURACIES/PITFALLS

* Some courses have timetable-entries with options (along the lines of '"time a" or "time b"') At the moment these are outputted as separate individual events for that day.


6. TODO
* Make timetable-data optional
* Scrape more information (Co-requirements, pre-requisites, etc)
* Figure out a way to handle OR-timetable entries
* Clean up code/condense it into one or two files
* Add option to scrape only given schools

7. CREDITS
By Christian Leonard Quale (clq@clq.no) Don't hesitate to contact me with any comments, corrections, rants about good coding practises etc.
This is my first Software'ish-project ever, so consider this my official apology for the state of the code.


8. VERSION HISTORY

Version 0.2.12 - 28-05-2011
    * First Release 

    
9. LICENSE
Feel free to use the code however you want to. If you, God knows why, want to use my code in a mostly unaltered form for anything, please consider giving me some kind of credit. Otherwise you will feel bad.
