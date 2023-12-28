#programmed by TaehuaGang

sampleList = ['It','is','rather','for','us','to','be','here','dedicated','to',
'the','great','task','remaining','before','us','that','from','these','honored',
'dead','we','take','increased','devotion','to','that','cause','for','which',
'they','gave','the','last','full','measure','of','devotion','that','we',
'here','highly','resolve','that','these','dead','shall','not','have','died',
'in','vain','that','this','nation','under','God','shall','have','a',
'new','birth','of','freedom','and','that','government','of','the','people',
'by','the','people', 'for','the','people','shall','not','perish','from',
'the','earth']

gapList=[]
maxGap=[]

for i in range (0, len(sampleList)-1):
    gap=len(sampleList[i+1])-len(sampleList[i])
    if gap<0:
        gap=-gap
    gapList.append(str(i))
    gapList.append(str(i+1))
    gapList.append(sampleList[i])
    gapList.append(sampleList[i+1])
    gapList.append(gap)
    maxGap.append(gap)

findMaxGap = max(maxGap)
answer = gapList.index(findMaxGap)

print('위의 데이터를 이용할 때',str(int(gapList[answer-4])+1)+'번째에 있는',str(gapList[answer-2])+'와',str(int(gapList[answer-3])+1)+'번째에 있는',str(gapList[answer-1])+'의','단어의 길이 차가 제일 크다.', '그 차이는', str(gapList[answer])+'이다.')
