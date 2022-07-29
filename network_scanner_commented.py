#!/usr/bin/env python
#
# PYTHON NETWORK SCANNER
#
# Author: Matheus Heidemann
#
# Description: this is a simple network scanner created with Python. To scan the network, the user bacically needs to provide an valid IPv4 address 
# and the CIDR value (Example: 192.168.0.1/24). This code is heavily based on the udemy course "Learn Python & Ethical Hacking From Scratch" from 
# the tutors "Zaid Sabih" and "z Security" (https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/).
#
# 28 July 2022
#
# Version: 1.0.0
#
# License: MIT License
#
#
#
# Imports
import argparse
import re
import scapy.all as scapy


# MISC
valid_ipv4_cidr_addr = "^([0-9]{1,3}\.){3}[0-9]{1,3}($|/(([1-9]|[12][0-9]|3[0-2]))$)"


# FUNCTIONS
# Function to get the arguments
def getArguments():
    parser = argparse.ArgumentParser(description="PYTHON NETWORK SCANNER - Script to check for Network Devices connected in the same network")
    parser.add_argument("-t", "--target", help="Target IP address and the range (Example.: 192.168.0.1/24)")
    args = parser.parse_args()

    while True:
        if not args.target or not re.match(valid_ipv4_cidr_addr, args.target):
            args.target = input("Target IP address and range > ")
        if re.match(valid_ipv4_cidr_addr, args.target):
            break
        else:
            print("Invalid IPv4/CIDR. Please, input an valid one (0.0.0.0/24)")
    return args


# Function to perform an scan on the target IP address
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # IP source
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # ARP destination
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        print("- - - - - - - - - - - ")
    return client_list


# Function to print the results
def print_result(client_list):
    print("IP\t\t\tMAC Address")
    print("--------------------------------------")
    for client in client_list:
        print(client['ip'] + "\t\t" + client['mac'])


# PROGRAM
args = getArguments()
scan_result = scan(args.target)

if len(scan_result) != 0:
    print_result(scan_result)
else:
    print("We couldn't find any hosts with the provided IP address (" + args.target + ")")
