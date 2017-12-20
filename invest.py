import sys
from collections import OrderedDict
range = input().split(", ")
starting_date = range[0]
ending_date = range[1]
line = input()
dates = OrderedDict()
while True:
    try:
        line = input()
        data = line.split(",")
        datemon = data[0]
        if datemon > starting_date and datemon < ending_date:
            datemo = datemon[0:7]
            if datemo not in dates:
                dates[datemo] = {}
            if data[1]in dates[datemo]:
                dates[datemo][data[1]] = int(dates[datemo][data[1]]) + int(data[2])
                
            else:
                dates[datemo].update({data[1] : data[2]})
    except EOFError:
        keys = sorted(dates.keys(), reverse = True)
        for key in keys:
            if len(dates[key]) > 1:
                #inner_keys = sorted(dates[key].keys())
                str = "".join("{!s},{!r},".format(key,val) for (key,val) in sorted(dates[key].items()))
                str = str.replace("'","")
                str = str.rstrip(",")
                print (key+","+str)
                #text = ""
                #for inner_key in inner_keys:
                #    text = text + inner_key + ((dates[key][inner_key]))
                #print (text)
            else:
                str = "".join("{!s},{!r}".format(key,val) for (key,val) in dates[key].items())
                str = str.replace("'","")
                print (key+","+str)
                #print ( key + ", "+str(dates[key].keys()))
        #print (dates)
        break
    

