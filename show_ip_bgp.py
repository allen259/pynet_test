#!/usr/bin/env python

f = open("show_ip_bgp.txt")
output = f.read()

fields1, field2 = output.split("Weight Path")
field2 = fields2.strip()
for i in line field2.split("\n"):
   new_fields = field2.split()   
   print new_fields 
   if feilds:
      prefix = fields[1] 
      as_path = fields[5:-1]
      as_path = "".join(as_path)
      print "{} {}
