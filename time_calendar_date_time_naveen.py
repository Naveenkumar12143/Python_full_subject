__author__ = "Naveen kumar"
import calendar

# print(calendar.calendar(1999))
# print(calendar.calendar(1997))
# print(calendar.calendar(1947))

# from calendar import calendar
# print(calendar(2014))
# print(calendar(2022))

# print(calendar.calendar(2030,w=3,l=1,c=5))

''' w is the width of each week w=2 mean Mo (or) W=3 means Mon (or) W=6 means Monday
# (Width=2 is always preferable)
# I is the number of lines for each week.(I=2 is always preferable)
# where c is space b/w each month.'''

#################################################################################
# print(calendar.isleap(2004))
# print(calendar.isleap(2033))
# print(calendar.isleap(1998))
# Returns True if year is a leap year; otherwise, False.

# ################################################################################
# print(calendar.leapdays(1980, 2022)) #2022 is not considered because of range
# Returns the total number of leap days in the years within range(y1,y2)

# print(calendar.month(2018,11))
# syntax:   calendar.month(year,month,w=2,l=1)
# print(calendar.month(2018,11))

##########################################################################################

# calendar.setfirstweekday(6)
# print(calendar.calendar(2022))
# print(calendar.month(2022,5,w=3))
# '''Sets the first day of each week to weekday code weekday.
# # Weekday codes are 0 (Monday) to 6 (Sunday).'''

############ time module ######################
import time
from time import sleep
# print(time.time())  # gives time frame

# print(time.asctime())

'''time.ctime([secs]) is Like asctime(localtime(secs)) and without arguments is like asctime( )'''

# print(time.ctime())

# a = time.localtime()
# print(a,"\n",type(a))

# print(a.tm_year)
# print(a.tm_yday)
# print(a.tm_mon)
# print(a.tm_mday)
# print(a.tm_zone)
# print(a.tm_gmtoff)
# print(a.tm_wday)
# print(a.tm_isdst)
# print(a.tm_hour)
# print(a.tm_min)
# print(a.tm_sec)

'''The method sleep() suspends execution for the given number of seconds. 
The argument may be a floating point number to indicate a more precise sleep time.'''

# print("naveen your time starts now at %s" % time.ctime())
# time.sleep(10)
# print("naveen your time ends now at %s" % time.ctime())

def amma():
    sleep(2)
    print("pushpavathi")

mylist = [10,50,80]

def me (mylist):
    """ this change a passed list into this function"""
    print("values inside the function before change:",mylist)
    mylist = [5,6,4,2]
    mylist.append("moon")
    print("values inside the function after change",mylist)
    sleep(3.5)
    return mylist


# overal_start_time = time.time()  # starting time
# tc1_start_time= time.time()  # 1st test case  starting time
# amma()
# print(time.time()-tc1_start_time)
# tc2_start_time= time.time()  # 2nd test case  starting time
# me(mylist)
# print(time.time()-tc2_start_time)
# print(time.time()-overal_start_time)

"""############ datetime module ######################"""
from datetime import datetime

def cuennr_time():
    n = datetime.now()
    print(n)
    print(n.date())


# cuennr_time() # current date and time


# n = datetime.now()
# year = n.strftime("%y")
# print("year:",year)

# month = n.strftime("%m")
# print("month:",month)

# day = n.strftime("%d")
# print("day:",day)

# time = n.strftime("%H:%M:%S")
# print("time:", time)

# date_time = n.strftime("%y/%m/%d, %H:%M:%S")
# print("date and time:",date_time)