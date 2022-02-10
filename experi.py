from datetime import datetime,timedelta
from random import randrange

class locationNode:
    x: float
    y: float

    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

class timeLocationNode:
    locTime: datetime
    locNode: locationNode

    def __init__(self,locTime:datetime,x:float,y:float):
        self.locTime = locTime
        self.locNode = locationNode(x,y)

    def __str__(self):
        return f'{self.locTime:%Y-%m-%d %H:%M} ({self.locNode.x},{self.locNode.y})'

class resultList:
    vLoc:locationNode
    cLoc:locationNode
    cSeries:list()
    color:str
    foundOutliers:list()
    unfoundOutliers:list()
    foundGridCircles:list()
    unfoundGridCircles:list()

class trialResult:    
    startTime:datetime
    startwindowwidth:int
    startwindowheight:int
    endTime:datetime
    endwindowwidth:int
    endwindowheight:int
    trial:str
    searcher:str
    resultList:list()

    def __init__(self,startTime:datetime,startwindowwidth:int,startwindowheight:int,endTime:datetime,endwindowwidth:int,endwindowheight:int,trial:str,searcher:str):
        self.startTime = startTime
        self.startwindowwidth = startwindowwidth
        self.startwindowheight = startwindowheight
        self.endTime = endTime
        self.endwindowwidth = endwindowwidth
        self.endwindowheight = endwindowheight
        self.trial = trial
        self.searcher = searcher
        

point_1 = locationNode(10,100)
print(point_1)
print(f'X={point_1.x}, Y={point_1.y}')

timePoint = timeLocationNode(datetime(2022,2,9,18,30,59),100,10)
print(timePoint)
print(f'{timePoint.locTime:%Y-%m-%d %H:%M:%S} = {timePoint.locTime:%c} = {timePoint.locTime:%x}')

timePointList = []
rightNow = datetime.now()
for points in range(1,101):
    point = locationNode(randrange(100),randrange(100))
    time  = rightNow + timedelta(minutes=points)
    timePointList.append(timeLocationNode(time,point.x,point.y))

for timePoint in timePointList:
    print(timePoint)

#result1 = trialResult(datetime(2022,2,9,18,30,59),100,100,datetime(2022,2,9,18,59,59),200,200,'First Trial','Bob')