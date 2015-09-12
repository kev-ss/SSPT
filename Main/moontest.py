#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import ephem

now = datetime.now()

#Past Moon phases
d5 = ephem.previous_new_moon(now)
d6 = ephem.previous_first_quarter_moon(now)
d7 = ephem.previous_full_moon(now)
d8 = ephem.previous_last_quarter_moon(now)
print
print (d5), "	| Previous new Moon"
print (d6), "	| Previous quarter Moon"
print (d7), "	| Previous full Moon"
print (d8), "	| Previous last quarter Moon"
print

#Next Moon phases
d1 = ephem.next_full_moon(now)
d2 = ephem.next_new_moon(now)
d3 = ephem.next_first_quarter_moon(now)
d4 = ephem.next_last_quarter_moon(now)
print (d2), "	| Next new Moon"
print (d3), "	| Next quarter Moon"
print (d1), "	| Next full Moon"
print (d4), "	| Next last quarter Moon"
print

m=ephem.Moon(now)
print "Moon is actually:", (ephem.constellation(m))

quit()
