#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import strftime
from datetime import datetime
import ephem

now = datetime.now()
d1 = ephem.next_full_moon(now)
d2 = ephem.next_new_moon(now)
d3 = ephem.next_first_quarter_moon(now)
d4 = ephem.next_last_quarter_moon(now)
print (d2), "	| Next new Moon"
print (d3), "	| Next quarter Moon"
print (d1), "	| Next full Moon"
print (d4), "	| Next last quarter Moon"

m=ephem.Moon(now)
epoch=(strftime("%Y"))
print "Moon is actually:", (ephem.constellation(m))

quit()
