#!/usr/bin/env python

ip_addr = raw_input("Please enter IP address: ")
my_list = ip_addr.split(".")
my_list[-1]= "0"
".".join(my_list)
print my_list
octet1 = my_list[0]
octet2 = my_list[1]
octet3 = my_list[2]
octet4 = my_list[3]
o1 = int(octet1)
o2 = int(octet2)
o3 = int(octet3)
o4 = int(octet4)
o1 = bin(o1)
o2 = bin(o2)
o3 = bin(o3)
o4 = bin(o4)


print '{} {} {} {}'.format(o1, o2, o3, o4) 
