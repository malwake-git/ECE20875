#!/usr/bin/python3
year=2021
# Your code should be below this line
if ((year % 4) == 0):
   if ((year % 100) == 0):
       if ((year % 400) == 0):
           print("{}".format(True))
       else:
           print("{}".format(False))
   else:
       print("{}".format(True))
else:
   print("{}".format(False))


