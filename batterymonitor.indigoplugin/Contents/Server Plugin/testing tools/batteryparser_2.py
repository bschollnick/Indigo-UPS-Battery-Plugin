#!/usr/bin/python
import subprocess

#data = subprocess.check_output	 ( ['pmset', '-g', 'batt']) 		# python 2.7x
#print data

proc = subprocess.Popen ( ['pmset', '-g', 'batt'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
out, err = proc.communicate ()
print "out: \n",out

out = out.split ("\n")
power_status = out[0].split ("'")[1]
data = out[1].split ("\t")
ups_model = data[0]
data = data[1].split (";")
percentage = data[0][0:-1]#data[1][0:percent_locale]
charging = data[1].endswith ("charging")
if not charging:
#percent_locale = data[0][0:-1]#data[0].find ("%")
	time	= data[2][0:data[2].find(":")+3].strip()
	min		= data[2][0:time.find(":")+1]
	sec		= data[2][time.find(":")+2:-10]
else:
	time = 0
	min  = 0
	sec  = 0

print time,"  ", min, "  ", sec
print power_status
print data
print ups_model
print percentage
print charging
print time

#

# Currently drawing from 'AC Power'
# -Back-UPS LS 500 FW:16.b3 .D USB FW:b3 	100%; charging
# Work UPS

#Currently drawing from 'AC Power'
# -Smart-UPS 1500 RM FW:617.3.D USB FW:1.5	83%; charging


#nerv:testing tools Benjamin$ pmset -g batt
"""Now drawing from 'UPS Power'
 -UPS CP1000AVRLCD (id=16711680)	100%; discharging; 0:22 remaining present: true"""

#nerv:testing tools Benjamin$ pmset -g batt
"""Now drawing from 'AC Power'
 -UPS CP1000AVRLCD (id=16711680)	100%; charging present: true"""
>>> test = out.decode().split("\n")
# test[0] = power source
>>> source=test[0][test[0].find("'")+1:-1]
>>> source
'AC Power'

# test[1] = status
status = test[1].split(";")
if len(status) == 2:
    # on AC power
    power, status = status
    power_id = power[2:power.find("(")-1]
    percentage = power[-4:-1]
elif len(status) == 3:
    power, power_usage, status = status
    power_id = power[2:power.find("(")-1]
    percentage = power[-4:-1]
    time_left = status.strip().split(" ")[0].split(":")
    hour_left = int(time_left[0])
    min_left = int(time_left[1])
