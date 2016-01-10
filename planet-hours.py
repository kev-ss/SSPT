#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import ephem
import time
import string
from ephem import cities

#Getting current date
date = datetime.now()

#   Getting coordinates (WORK HERE TO MAKE THE NAME BE DECLARED BY USER)
#   TO DO: capitalize input DONE, set cityname as raw_input DONE
cityinput = raw_input("Please select a city: ")     #city declared by user
cityname = string.capwords(cityinput)                #city capitalized for searching in the DB
city = ephem.city(cityname)
lat = city.lat
lon = city.lon

# Use lat and lon to create ephem observer instance and update with given values (Correct, do not touch)
my_location = ephem.Observer()
my_location.lat = lat
my_location.lon = lon
my_location.date = date

# Get sunrise of the current day (HUGE MISTAKE HERE SOMEWHERE)
sunrisep = my_location.previous_rising(ephem.Sun())
sunsetp = my_location.previous_setting(ephem.Sun())
sunrisen = my_location.next_rising(ephem.Sun())
sunsetn = my_location.next_setting(ephem.Sun())

#Getting the weekday (Correct, returns an interger though, 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday)
weekday = datetime.today().weekday()

#Converting rising and setting to strings to split them into dates
a1 = str(sunrisep)
a2 = str(sunsetp)
a3 = str(sunrisen)
a4 = str(sunsetn)

#Splitting into dates and times
b1 = a1.split(' ')
b2 = a2.split(' ')
b3 = a3.split(' ')
b4 = a4.split(' ')

#Splitting into Hr, Min, S
c1 = b1[1].split(':')
c2 = b2[1].split(':')
c3 = b3[1].split(':')
c4 = b4[1].split(':')

#Main coding area
if (b1[0] == b2[0]):
   #Disregard b1, because that was yesterday
   #Compute night length
   Hrdif = int(c2[0]) - int(c3[0])
   Mindif = int(c2[1]) - int(c3[1])
   Sdif = int(c2[2]) - int(c3[2])
   #Makes time length always positive
   if (Hrdif < 0):
      Hrdif = int(c3[0]) - int(c2[0])
      Mindif = int(c3[1]) - int(c2[1])
      Sdif = int(c3[2]) - int(c2[2])
      if (Mindif < 0):
         Hrdif = Hrdif - 1
         Mindif = int(c3[1]) - int(c2[1]) + 60
      if (Sdif < 0):
         Mindif = Mindif - 1
         Sdif = int(c3[2]) - int(c2[2]) + 60
   if (Mindif < 0):
      Hrdif = Hrdif - 1
      Mindif = int(c3[1]) - int(c2[1]) + 60
      if (Sdif < 0):
         Mindif = Mindif - 1
         Sdif = int(c3[2]) - int(c2[2]) + 60
   if (Sdif < 0):
      Mindif = Mindif - 1
      Sdif = int(c3[2]) - int(c2[2]) + 60
   #Finding hour length by converting to seconds then dividing by 12
   Hrs = Hrdif * 60 * 60
   Mins = Mindif * 60
   Secs = Sdif
   totalS = Hrs + Mins + Secs
   HrlenS = totalS / 12
   SecN = HrlenS % 60
   HrlenS = (HrlenS - SecN) / 60
   MinN = HrlenS % 60
   HrN = (HrlenS - MinN) / 60
   #Length of a Night Hour
   NightHours = [HrN, MinN, SecN]
   #Checking weekday (VERY IMPORTANT DO NOT REMOVE)
   dateString = str(date)
   dateList = dateString.split(' ')
   if (dateList[0] == b1[0]):
      weekadd = -1
   else:
      weekadd = 0
   #Making weekday
   tempweekday = weekday + weekadd
   #Making list of hours
   Night = list()
   x = 0
   while(True):
      Hr = int(c2[0]) + x*NightHours[0]
      Min = int(c2[1]) + x*NightHours[1]
      Sec = int(c2[2]) + x*NightHours[2]
      if (Sec > 59):
         Sec = Sec - 60
         Min = Min + 1
      if (Min > 59):
         Min = Min - 60
         Hr = Hr + 1
      if (Hr > 23):
         Hr = Hr - 24
      Temp = str(Hr) + ':' + str(Min) + ':' + str(Sec)
      Night.append(Temp)
      x = x + 1
      print Hr, Min, Sec, x
      time.sleep(1)
      if (Hr == b3[0]):
         break
print Night
