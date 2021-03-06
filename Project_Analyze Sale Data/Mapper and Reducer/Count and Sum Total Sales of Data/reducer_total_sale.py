#!/usr/bin/python

import sys

salesTotal = 0
count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# Only calculate and count total sales in the data 

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    salesTotal += float(thisSale)
    count += 1

print "Total sales value", "\t", salesTotal
print "Total number of sales", "\t", count
