#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dronekit import connect, VehicleMode
import time
import collections
import sys

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
print(connection_string)

if not connection_string:
    print("Usage: python parameters.py --connect port (eg. /dev/ttyUSB0 or /dev/ttyACM0)")
    sys.exit (1)

# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True, baud=57600, heartbeat_timeout=120)

# Parameters
print("\nPrint all parameters (iterate `vehicle.parameters`):")

# Sorts the list of parameters before printing
od = collections.OrderedDict(sorted(vehicle.parameters.items()))
for key, value in od.items():
	print(" Key:%s Value:%s" % (key,value))

#Close vehicle object before exiting script
print("\nClose vehicle object")
vehicle.close()

print("Completed")
