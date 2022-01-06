import csv
from collections import Counter
with open('SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)  
file_data.pop(0)

totweight = 0.0
weightlst = []

weight = 0.0
for i in file_data:
    weight = float(i[2])
    weightlst.append(weight)
    totweight = totweight + weight

l = len(file_data)
weightlst.sort()
mean = totweight/l
print(str(mean) + " is the mean value of all the weights")

# mean done now median will be calculated
median = 0
if len(weightlst) % 2:
    median1 = float(weightlst[l//2])
    median2 = float(weightlst[l//2 - 1])
    median = (median1/median2)/2
else:
    median = weightlst[l//2]
    
print(str(median) + " is the median")

data = Counter(weightlst)
modeData={
    "75-85": 0,
    "85-95": 0,
    "95-105": 0,
    "105-115": 0,
    "115-125": 0,
    "125-135": 0,
    "135-145": 0,
    "145-155": 0,
    "155-165": 0,
    "165-175": 0,
}
for w, occurance in data.items():
    if 75 < float(w) < 85:
        modeData["75-85"] += occurance
    elif 85 < float(w) < 95:
        modeData["85-95"] += occurance
    elif 95 < float(w) < 105:
        modeData["95-105"] += occurance
    elif 105 < float(w) < 115:
        modeData["105-115"] += occurance
    elif 115 < float(w) < 125:
        modeData["115-125"] += occurance
    elif 125 < float(w) < 135:
        modeData["125-135"] += occurance
    elif 135 < float(w) < 145:
        modeData["135-145"] += occurance
    elif 145 < float(w) < 155:
        modeData["145-155"] += occurance
    elif 155 < float(w) < 165:
        modeData["155-165"] += occurance
    elif 165 < float(w) < 175:
        modeData["165-175"] += occurance


modeRange, modeOccurence = 0, 0
for range, occurence in modeData.items():
    if occurence > modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        
        
        
mode = float((modeRange[0] + modeRange[1])/2)
print( str(mode)+ " is the mode")