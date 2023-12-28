#programmed by TaehuaGang

#warning: You need to install the matplotlib module. To do so, open your terminal or command prompt and run the following command: 
#pip install matplotlib

with open('accinfo.csv','r') as file:
    contents=file.readlines()
with open('자동차등록대수현황_시도별_20230601224359.csv','r') as file:
    carcontents=file.readlines()
with open('도로포장률_시도_시_군_구__20230601224900.csv','r') as file:
    roadlengthcontents=file.readlines()
with open('부산광역시_교통신호제어기 현황_20221102.csv','r') as file:
    trafficlightcontents=file.readlines()
stars=contents
onlybusan=list()
for i in stars:
    busan=i.find('부산')
    if (busan!=-1):
        onlybusan.append(i)

splitbusan=list()
for i in onlybusan:
    a=i.split(',')
    del a[4]
    del a[4]
    del a[4]
    del a[4]
    del a[0]
    splitbusan.append(a)
onlynum=list()
for i in onlybusan:
    a=i.split(',')
    del a[4]
    del a[4]
    del a[4]
    del a[4]
    del a[0]
    del a[0]
    del a[0]
    onlynum.append(a)
onlylocation=list()
for i in onlybusan:
    a=i.split(',')
    del a[4]
    del a[4]
    del a[4]
    del a[4]
    del a[0]
    del a[2]
    del a[1]
    onlylocation.append(a)
locations=list()
for i in range(0,16):
    locations=locations+onlylocation[i*12]
    

accidents=list()
n=0
for i in range(16):    
    total=0
    a=(onlynum[n]+onlynum[n+1]+onlynum[n+2]+onlynum[n+3]+onlynum[n+4]+onlynum[n+5]
       +onlynum[n+6]+onlynum[n+7]+onlynum[n+8]+onlynum[n+9]+onlynum[n+10]+onlynum[n+11])
    for i in a:
        total+=int(i)
    b=total
    n+=12
    accidents.append(b)

filteringcar=list()
for i in carcontents:
    filteringcar.append(i.split('\n'))
cardic=[]
for i in filteringcar:
    a=i[0].split(',')
    second=a[1]
    cardic.append(int(second))
cars=cardic    
roadlength=list()
roadlengthcontents.pop(0)
roadlengthcontents.pop(0)

filteringload=list()
for i in roadlengthcontents:
    filteringload.append(i.split('\n'))
for i in filteringload:
    a=i[0].split(',')
    second=a[1]
    roadlength.append(int(second))
trafficlightcontents.pop(0)
lights=[]
for i in trafficlightcontents:
    a=i.split(',')
    lights.append(a)

for i in lights:
    del i[0]
    del i[0]
    del i[0]
    del i[1]
    del i[1]
alllights=[]
for i in lights:
    alllights=alllights+i
trafficlights=[(alllights.count('중구')),(alllights.count('서구')),(alllights.count('동구')),(alllights.count('영도구'))
               ,(alllights.count('부산진구')),(alllights.count('동래구')),(alllights.count('남구')),(alllights.count('북구'))
               ,(alllights.count('해운대구')),(alllights.count('사하구')),(alllights.count('금정구')),(alllights.count('강서구'))
               ,(alllights.count('연제구')),(alllights.count('수영구')),(alllights.count('사상구')),(alllights.count('기장군'))]
Trafficlight=list()
print(locations)
print(accidents)
print(cars)
print(roadlength)
print(trafficlights)
class storage():
    def __init__(self,location,accnum,cars,roadlength,trafficlight):
        self.location=location
        self.accnum=accnum
        self.cars=cars
        self.roadlength=roadlength
        self.trafficlight=trafficlight
    def Road_length_per_traffic_light(self):
        return self.roadlength/self.trafficlight
    def accidentnumber_per_cars(self):
        return self.accnum/self.cars
    def __str__(self):
        information=("위치:{}, 사고 횟수:{}번, 자동차등록대수:{}대,전체개통도:{}km,교통신호제어기 계:{}개".format(self.location,self.accnum,self.cars, self.roadlength,self.trafficlight))
        return information
    def stableone(self):
        return((self.accnum/self.cars))*((self.roadlength/self.trafficlight))
test=list()
for i in range(0,16):
    a=storage(locations[i],accidents[i],cars[i],roadlength[i],trafficlights[i])
    test.append(a)
sector1=test[0]
sector2=test[1]
sector3= test[2]
sector4= test[3]
sector5= test[4]
sector6= test[5]
sector7=test[6]
sector8=test[7]
sector9= test[8]
sector10= test[9]
sector11= test[10]
sector12=test[11]
sector13= test[12]
sector14= test[13]
sector15= test[14]
sector16=test[15]
sectorlist=(sector1,sector2,sector3,sector4,sector5,sector6,sector7,sector8,sector9,sector10,sector11,sector12,sector13,sector14,sector15,sector16)
Road_length_per_traffic_lightlist=[]
accidentnumber_per_carslist=[]
stableonelist=[]
for i in sectorlist:
    Road_length_per_traffic_lightlist.append(i.Road_length_per_traffic_light())
for i in sectorlist:
    accidentnumber_per_carslist.append(i.accidentnumber_per_cars())
for i in sectorlist:
    stableonelist.append(i.stableone())  
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path ="batang.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.figure(figsize=(12,5))
plt.bar(locations,Road_length_per_traffic_lightlist)
plt.show()


plt.figure(figsize=(12,5))
plt.bar(locations,accidentnumber_per_carslist)
plt.show()

plt.figure(figsize=(12,5))
plt.bar(locations,stableonelist)
plt.show()