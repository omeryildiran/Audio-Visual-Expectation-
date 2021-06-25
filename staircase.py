
import random

targetDur=list([0.008, 0.016])
currentDur=random.choice(targetDur)

accuracy=[0,0,0,1,1,1]

def staircase():
	global accuracy
	global currentDur
	if accuracy[-1]==0:
		currentDur=currentDur+0.008
	elif accuracy[-1]==1 and accuracy[-2]==1:
		currentDur=currentDur-0.008
	else:	
		currentDur=currentDur
	return currentDur

for i in range(30):
	currentDur=staircase()





Loop100.addData('TargetDuration', currentDur)




def staircase():
    global accuracy
    global currentDur
    if accuracy[-1]==0:
        currentDur=currentDur+0.016
    elif currentDur>0.016 and len(accuracy)>=2:
        if accuracy[-1]==1 and accuracy[-2]==1:
            currentDur=currentDur-0.016
    else: 
        currentDur=currentDur
    return currentDur


Loop100.addData('TargetDuration', currentDur)
cueName=""

def staircase():
    global accuracy
    global currentDur
    if accuracy[-1]==0:
        currentDur=currentDur+0.016
    elif currentDur>0.016 and len(accuracy)>=2:
        if accuracy[-1]==1 and accuracy[-2]==1:
            currentDur=currentDur-0.016
    else: 
        currentDur=currentDur
    return currentDur


if trialNumLoop100%numStaricase<30:
    currentDur=staircase()
    if cueFile[7:11] in targetFile[7:11]:
        trialCongruency="congruent"
        congDur.append(target.tStopRefresh-target.tStartRefresh)
        incongDur.append(0)
        Loop100.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        Loop100.addData('congruentTrialDuration', congDur[trialNumLoop100])
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(0)
        Loop100.addData('congruentTrialDuration', congDur[trialNumLoop100])
        Loop100.addData('incongruentTrialDuration', incongDur[trialNumLoop100])

trialNumLoop100=trialNumLoop100+1




