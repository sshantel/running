import re
import math

def km_to_mi(km):
    miles = km / 1.609
    return miles 

def time_to_seconds(run_time):
    components = run_time.split(":")
    hours = int(components[0])
    minutes = int(components[1])
    seconds = int(components[2])
    total_s = seconds + (minutes*60) + (hours*3600)
    return total_s

def clean_distance_to_mi(dist):
    clean = re.sub('[^0-9]', '', dist)
    clean = km_to_mi(int(clean))
    return clean

def min_float_to_pace(mins): 
    remainder = mins - (mins//1)
    return remainder*60 

def km_to_mi_per_min():
    run1 = "00:47:44"
    run2 = "00:56:28"

    run1dist = "10k"
    run2dist = "10K" 

    run1dist = clean_distance_to_mi(run1dist) 
    run2dist = clean_distance_to_mi(run2dist)

    run1_s = time_to_seconds(run1)  
    run2_s = time_to_seconds(run2)

    sec_per_mi = run1_s / run1dist 
    print(sec_per_mi)
    min_per_mi = sec_per_mi /60.0
    print(min_per_mi)
    min_per_mi_sliced = str(min_per_mi)
    minutes = min_per_mi_sliced.split('.')[0]

    seconds=(min_float_to_pace(min_per_mi))
    km_to_mi(10) 

    return(f'your average pace was {minutes}:{seconds} a mile')

print(km_to_mi_per_min())


