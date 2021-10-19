lines = ''
memoryLine = ''
cpuLine = ''
cpuUsePercentage = ''
topFile = ''
memoryIdle = ''
memoryUsed = ''
memoryTotal = ''

topFile = open('top.txt', 'r')
lines = topFile.readline()

while lines:
  lines = topFile.readline()
  #print(lines)
  #print('--------------')

  if lines.find('mem') > 1 and lines.find('cach') > 1:    
      memoryLine = lines      
  
  if lines.find(':') > 1 and lines.find('us') > 1 and lines.find('sis') > 1 and lines.find('ni') > 1and lines.find('oc') > 1and lines.find('ag') > 1:    
      cpuLine = lines

memoryTotal = memoryLine[memoryLine.index(':')+1:memoryLine.index('total')] 
memoryTotal = float(memoryTotal.replace(',','.'))

memoryIdle = memoryLine[memoryLine.index('total')+6:memoryLine.index('livre')] 
memoryIdle = float(memoryIdle.replace(',','.'))

memoryUsed = memoryLine[memoryLine.index('livre')+6:memoryLine.index('usados')] 
memoryUsed = float(memoryUsed.replace(',','.'))

quotient = memoryUsed/memoryTotal
memoryUsePercentage = round(quotient * 100, 2)

cpuUsePercentage = cpuLine[cpuLine.index('ni')+4:cpuLine.index('oc')-1] 
cpuUsePercentage = 100 - float(cpuUsePercentage.replace(',','.')) 

lines = ''
dfFile = ''
mainHd = ''
lines = ''

dfFile = open('df.txt', 'r')
lines = dfFile.readline()

while lines:
  lines = dfFile.readline()

  if lines.find('nvme0n1p2') > 1:    
    mainHd += lines

mainHdUsage = mainHd[mainHd.index('%')-3:mainHd.index('%')] 
mainHdUsage = float(mainHdUsage.replace(',','.'))
mainHdUsage

import time;
ts = time.time()
readable = time.ctime(ts)
readable

hdwData = [[str(memoryUsePercentage), str(cpuUsePercentage), str(mainHdUsage), str(readable), str(ts)]]
hdwData

import csv
fields = ['memoryUsePercentage', 'cpuUsePercentage', 'mainHdUsage', 'utcDateHour', 'utcDateHourInt'] 
fileExists = True
f=''
try:
    f = open("hdwData.csv")
    # Do something with the file
except IOError:
    fileExists = False

if fileExists:
  with open('hdwData.csv','a') as f:
      write = csv.writer(f)      
      write.writerows(hdwData)
else:
  with open('hdwData.csv','w') as f:
      write = csv.writer(f)      
      write.writerow(fields)
      write.writerows(hdwData)