#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval

week_dic = {}
week_cnt_dic = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    if thisKey not in week_dic:
        week_dic[thisKey] = thisSale
        week_cnt_dic[thisKey] = 1
    else:
        week_dic[thisKey] += thisSale
        week_cnt_dic[thisKey] += 1

for key, value in week_dic.iteritems():
    print key, "\t", value / week_cnt_dic[key]