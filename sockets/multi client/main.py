import random
import time
import threading

# Threading function call for each station
def mac(lock, station_id, slottime):
    begin = time.time()  # time when thread got started
    global pktrec       #  Packets recieved for each station
    global channel      #  Channel is set as global
    CWmin = 15          #  Min window size
    CWmax = 1024        #  Max window size
    while True:
        if time.time() - begin > slottime:
            break
        count = 0         # a variable to keep track of retrylimit and use in selecting backoff value
        while True:
            if time.time() - begin > slottime:
                break
            # Selecting a random backoff counter value
            count += 1
            backOff = int(random.randint(0,min((pow(2,count)-1) * CWmin, CWmax)))
            while backOff > 0:
                if time.time() - begin > slottime:
                    break
                # Waste is for sigma is taken as 50us
                waste = [0 for i in range(1000)]

                if channel == 0:
                    backOff = backOff - 1
            else:
                while channel == 1:
                    if time.time() - begin > slottime:
                        break
                    waste = [0 for i in range(1000)]
                if time.time() - begin > slottime:
                    break
                lock.acquire()
                if channel == 0:
                    channel = 1
                else:
                    while channel:
                        waste = [0 for i in range(1000)]
                    else:
                        channel = 1
                lock.release()
                if time.time() - begin > slottime:
                    channel = 0
                    break
                time.sleep(250 * (10**(-6)))    #  Time for sending the packet
                if time.time() - begin > slottime:
                    channel = 0
                    break
                pktrec[station_id] += 1
                channel = 0

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
beaconinterval = float(beaconinterval * (10 ** (-6)))
# Channel
channel = 0
# 0 means channel idle
# 1 means channel busy

# Initialisation
# No of groups
nogrp = int(input("No of groups to be present: "))
# Group duration
grpdur = []
for i in range(nogrp):
    grpdur.append(float(beaconinterval/nogrp))
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
lock = threading.Lock()     #  Used for locking the channel

start = time.time()
for i in range(nogrp):
    # Stations present in each slot
    slotsta = [[] for j in range(slotspergrp[i])]
    for j in range(len(grpsta[i])):
        slotsta[j % slotspergrp[i]].append(grpsta[i][j])
    # Time duration of each raw slot
    slottime = [float(grpdur[i]/slotspergrp[i]) for j in range(slotspergrp[i])]
    # Iterating in each RAW slot
    for j in range(slotspergrp[i]):
        for k in slotsta[j]:
            stationthreads = threading.Thread(target = mac, name = str(i), args=(lock, k, slottime[j],))
            stationthreads.start()
        else:
            stationthreads.join()

print(pktrec)
print(time.time() - start)
