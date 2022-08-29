# Network Scanner 1.0.0

## What is this script?

This is a simple network scanner created with Python. This code is heavily based on the udemy course "Learn Python & Ethical Hacking From Scratch" from the tutors "Zaid Sabih" and "z Security" (https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/)

[![Travis branch](https://img.shields.io/cran/l/devtools.svg)](https://github.com/its0v3r/Network-Scanner/blob/master/LICENSE)
[![Travis branch](https://img.shields.io/badge/made%20with-%3C3-red.svg)](https://github.com/its0v3r/Network-Scanner)

## Commented code

There is one .py file with the code fully commented (for educational purposes) and another .py file that contains only the code with necessary comments (if you don't see both files, it's because it is in progress).

## How to use the script?

- To scan the network, the user bacically needs to provide an valid IPv4 address and the CIDR value (Example: 192.168.0.1/24). This can be done by using the argument -t --target;
- If the user don't pass the -t --target argument, the script will ask for the user to input the pending information;
- This script needs to run as sudo or root, otherwise the user will get an error;
- This code is meant to work with Python3.

Example 1 - Specifing the IPv4 and the CIDR:

```
sudo ./network_scanner.py -t 192.168.0.1/24
```
