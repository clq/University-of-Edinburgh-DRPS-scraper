
INFORMATION AVAILABLE:

The options should be contained on the first line of config.txt seperated by spaces. All information will be outputted on a single line, followed by one line for each of the days with timetable-entries. See config.txt for sample outputs. The parametres available are:

GRADLEVEL - Returns 'UG' if a course is registered as an Undergraduate course, 'PG' if a course is registered as Postgraduate, and 'NA' if a graduate level isn't defined.

COURSENAME - Returns the name of the course surrounded by quotation marks ("). Note that duplicate coursenames are quite common.

COURSECODE - The unique code that identifies every course.

SCHOOLCODE - The unique code identifying the school offering the course surrounded by quotation marks ("). See "School-codes" for a list of which code belongs to which school.

SCHOOLNAME - Name of the school offering the subject. Probably less robust than using the school-code.

COLLEGENAME - Theoretically the name of the College surrounded by quotation marks ("). Rather inconsistent as some lecturers seem to add additional information here. Identification of college is probably better done using school-codes and mapping them to colleges. (see "School code") 

SCQFLEVEL - SCQF level of the course (7 through 11)

NORMALYEAR - The year during which a course is normally taken. Returns 0 if a year isn't defined.

CREDITS - Course-credits

COURSEPAGE - Course website returned as a URL. Returns NA if no course-website is defined.

DESCRIPTION - The course-description surrounded by quotation-marks ("). Note that the formatting of the course description is completely up to the lecturers, may include lists and other elements. The formatting may therefore be all over the place. Any line-breaks are replaced by a double-space, and the description is outputted on a single line.

DRPSURL - The URL to the DRPS-page of the course.

SEMESTER .semester (Semester, "1" means first semester, "2" means second semester, "3" means full year, and "0" means undefined

