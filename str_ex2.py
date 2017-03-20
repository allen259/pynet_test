#!/usr/bin/python
ip_addr = raw_input("Enter IP address:")
ip_addr = ip_addr.split(".")

print '{:12} {:12} {:12} {:12}'.format(ip_addr[0], ip_addr[1], ip_addr[2], ip_addr[3])    
