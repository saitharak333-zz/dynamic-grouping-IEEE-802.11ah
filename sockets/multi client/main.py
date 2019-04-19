# Number of Stations
N = int(input("No of Nodes connected to the server: "))
# Data Rate
datarate = float(input("Enter the data rate in Mbps: "))
# Packet Size
size = int(input("Enter the packet size in bytes: "))
# Packet Arrival Rate
pktrate = int(input("Enter packet arrival rate: "))
# Beacon Interval
beaconinterval = int(input("Enter Beacon Interval in us: "))

# Initialisation
# No of groups
nogrp = int(input("No of groups to be present: "))
# Group duration
grpdur = []
for i in range(nogrp):
    grpdur.append(beaconinterval/nogrp)
# No of packets recieved from each station
pktrec = [0 for i in range(N)]
# Grouping of Stations into groups
grpsta = [[] for i in range(nogrp)]
for i in range(N):
    grpsta[i % nogrp].append(i)
# No of raw slots in each group
rawslot = int(input("Enter intial no of raw slots: "))
# No of RAW Slots for each group
slotspergrp = [rawslot for i in range(nogrp)]

# Only for the first time
# Itereating through all the groups and setting stations prer slot and slot time

for i in range(nogrp):
    # Stations present in each slot
    slotsta = [[] for j in range(slotspergrp[i])]
    for j in range(len(grpsta[i])):
        slotsta[j % slotspergrp[i]].append(grpsta[i][j])
    # Time duration of each raw slot
    slottime = [(grpdur[i]/slotspergrp[i]) for j in range(slotspergrp[i])]
    # Iterating in each RAW slot
    for j in slotspergrp[i]:






import threading
def calc_square(number):
    print('Square:' , number * number)
def calc_quad(number):
    print('Quad:' , number * number * number * number)

if __name__ == "__main__":
    number = 7
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=(number,))
# Will execute both in parallel
    thread1.start()
    thread2.start()
# Joins threads back to the parent process, which is this program
    thread1.join()
    thread2.join()
# This program reduces the time of execution by running tasks in parallel
