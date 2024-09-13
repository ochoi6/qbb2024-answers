#!/usr/bin/env python3

#Question 3. (tally-fixed.py) Starting with tally.py, identify and fix the three bugs in this code. The output of this program should match the output of cut -f 1 | uniq -c e.g.

#Load sys into the environment 
import sys 

#Setting file as the second thing to consider in the command line to open it when running the loop
my_file = open( sys.argv[1] )

#For loop 
chr = ""
count = 0

for my_line in my_file:
    if "#" in my_line:
        continue
    fields = my_line.split("\t")
    if chr == "":
        chr = fields[0]
    if fields[0] != chr:
        print( count, chr )
        chr = fields[0]
        count = 1
        continue
    count = count + 1
print( count, chr )
my_file.close()






