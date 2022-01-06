import csv
import math
import matplotlib.pyplot as plt 
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',  # 设置字体类型
    # "font.size": 80,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)
def getRawData(datapath):
    rawData=[]
    with open(datapath+'/Accelerometer.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            nowRawData={}
            nowRawData["time"]=int(float(row["seconds_elapsed"])*100)/100
            nowRawData["a"]=math.sqrt(float(row["x"])**2+float(row["y"])**2+float(row["z"])**2)
            rawData.append(nowRawData)
    return rawData

def printRawData(rawData,stTime,endTime):
    timeAxis=[]
    accAxis=[]
    for eachData in rawData:
        if eachData["time"]<stTime:
            continue
        elif eachData["time"]>endTime:
            break
        else:
            timeAxis.append(eachData["time"])
            accAxis.append(eachData["a"])
    plt.plot(timeAxis,accAxis)


rjyData=getRawData("rjy_step")
ljmData=getRawData("ljm_step")
printRawData(rjyData,45,47)
printRawData(ljmData,45,47)
plt.show()
