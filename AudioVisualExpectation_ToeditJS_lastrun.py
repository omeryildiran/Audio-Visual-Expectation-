#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 08, 2021, at 18:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'AudioVisualExpectation_ToeditJS'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\omeru\\Documents\\FND\\My Repos\\Audio Visual Expectation\\AudioVisualExpectation_ToeditJS_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "NeutralTrial"
NeutralTrialClock = core.Clock()
target_4 = visual.ImageStim(
    win=win,
    name='target_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
distractor_4 = visual.ImageStim(
    win=win,
    name='distractor_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
maskLeft_4 = visual.ImageStim(
    win=win,
    name='maskLeft_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
maskRight_4 = visual.ImageStim(
    win=win,
    name='maskRight_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fixation_4 = visual.ShapeStim(
    win=win, name='fixation_4', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
targetPos=[0.4,-0.4]
targetDur=list([1, 2, 3, 4, 5])
currentDur=np.random.choice(targetDur)
accuracy=[]
durMask=4


# Initialize components for Routine "ResponseNeutral"
ResponseNeutralClock = core.Clock()
response_4 = keyboard.Keyboard()
#feedback=""
fixation_response_4 = visual.ShapeStim(
    win=win, name='fixation_response_4', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "FeedbackNeutral"
FeedbackNeutralClock = core.Clock()
feedBackScreen_4 = visual.TextStim(win=win, name='feedBackScreen_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
#trialNumLoop100=0
#numStaricase=30
#trialCongruency=""
#congDur=[]
#incongDur=[]

# Initialize components for Routine "end_of_exp"
end_of_expClock = core.Clock()
Instrcution100_5 = visual.TextStim(win=win, name='Instrcution100_5',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
basla_butonu_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
LoopNeutral = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('c_neutral.xlsx'),
    seed=None, name='LoopNeutral')
thisExp.addLoop(LoopNeutral)  # add the loop to the experiment
thisLoopNeutral = LoopNeutral.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopNeutral.rgb)
if thisLoopNeutral != None:
    for paramName in thisLoopNeutral:
        exec('{} = thisLoopNeutral[paramName]'.format(paramName))

for thisLoopNeutral in LoopNeutral:
    currentLoop = LoopNeutral
    # abbreviate parameter names if possible (e.g. rgb = thisLoopNeutral.rgb)
    if thisLoopNeutral != None:
        for paramName in thisLoopNeutral:
            exec('{} = thisLoopNeutral[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "NeutralTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_4.setPos((targetPos[1], 0))
    target_4.setImage(targetFile)
    distractor_4.setPos((-targetPos[1],0))
    distractor_4.setImage(maskFile)
    maskLeft_4.setPos((-0.4, 0))
    maskLeft_4.setImage(maskFile)
    maskRight_4.setPos((0.4, 0))
    maskRight_4.setImage(maskFile)
    shuffle(targetPos)
    
    # keep track of which components have finished
    NeutralTrialComponents = [target_4, distractor_4, maskLeft_4, maskRight_4, fixation_4]
    for thisComponent in NeutralTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    NeutralTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "NeutralTrial"-------
    while continueRoutine:
        # get current time
        t = NeutralTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=NeutralTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_4* updates
        if target_4.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            target_4.frameNStart = frameN  # exact frame index
            target_4.tStart = t  # local t and not account for scr refresh
            target_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_4, 'tStartRefresh')  # time at next scr refresh
            target_4.setAutoDraw(True)
        if target_4.status == STARTED:
            if frameN >= (target_4.frameNStart + currentDur):
                # keep track of stop time/frame for later
                target_4.tStop = t  # not accounting for scr refresh
                target_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_4, 'tStopRefresh')  # time at next scr refresh
                target_4.setAutoDraw(False)
        
        # *distractor_4* updates
        if distractor_4.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            distractor_4.frameNStart = frameN  # exact frame index
            distractor_4.tStart = t  # local t and not account for scr refresh
            distractor_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor_4, 'tStartRefresh')  # time at next scr refresh
            distractor_4.setAutoDraw(True)
        if distractor_4.status == STARTED:
            if frameN >= (distractor_4.frameNStart + currentDur):
                # keep track of stop time/frame for later
                distractor_4.tStop = t  # not accounting for scr refresh
                distractor_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor_4, 'tStopRefresh')  # time at next scr refresh
                distractor_4.setAutoDraw(False)
        
        # *maskLeft_4* updates
        if maskLeft_4.status == NOT_STARTED and frameN >= (expInfo['frameRate']*0.2)+currentDur:
            # keep track of start time/frame for later
            maskLeft_4.frameNStart = frameN  # exact frame index
            maskLeft_4.tStart = t  # local t and not account for scr refresh
            maskLeft_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft_4, 'tStartRefresh')  # time at next scr refresh
            maskLeft_4.setAutoDraw(True)
        if maskLeft_4.status == STARTED:
            if frameN >= (maskLeft_4.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskLeft_4.tStop = t  # not accounting for scr refresh
                maskLeft_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft_4, 'tStopRefresh')  # time at next scr refresh
                maskLeft_4.setAutoDraw(False)
        
        # *maskRight_4* updates
        if maskRight_4.status == NOT_STARTED and frameN >= (expInfo['frameRate']*0.2)+currentDur:
            # keep track of start time/frame for later
            maskRight_4.frameNStart = frameN  # exact frame index
            maskRight_4.tStart = t  # local t and not account for scr refresh
            maskRight_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight_4, 'tStartRefresh')  # time at next scr refresh
            maskRight_4.setAutoDraw(True)
        if maskRight_4.status == STARTED:
            if frameN >= (maskRight_4.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskRight_4.tStop = t  # not accounting for scr refresh
                maskRight_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskRight_4, 'tStopRefresh')  # time at next scr refresh
                maskRight_4.setAutoDraw(False)
        
        # *fixation_4* updates
        if fixation_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_4.frameNStart = frameN  # exact frame index
            fixation_4.tStart = t  # local t and not account for scr refresh
            fixation_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_4, 'tStartRefresh')  # time at next scr refresh
            fixation_4.setAutoDraw(True)
        if fixation_4.status == STARTED:
            if frameN >= (fixation_4.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001):
                # keep track of stop time/frame for later
                fixation_4.tStop = t  # not accounting for scr refresh
                fixation_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_4, 'tStopRefresh')  # time at next scr refresh
                fixation_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NeutralTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "NeutralTrial"-------
    for thisComponent in NeutralTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LoopNeutral.addData('target_4.started', target_4.tStartRefresh)
    LoopNeutral.addData('target_4.stopped', target_4.tStopRefresh)
    LoopNeutral.addData('maskLeft_4.started', maskLeft_4.tStartRefresh)
    LoopNeutral.addData('maskLeft_4.stopped', maskLeft_4.tStopRefresh)
    # the Routine "NeutralTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ResponseNeutral"-------
    continueRoutine = True
    # update component parameters for each repeat
    response_4.keys = []
    response_4.rt = []
    _response_4_allKeys = []
    # keep track of which components have finished
    ResponseNeutralComponents = [response_4, fixation_response_4]
    for thisComponent in ResponseNeutralComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ResponseNeutralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ResponseNeutral"-------
    while continueRoutine:
        # get current time
        t = ResponseNeutralClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ResponseNeutralClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response_4* updates
        waitOnFlip = False
        if response_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_4.frameNStart = frameN  # exact frame index
            response_4.tStart = t  # local t and not account for scr refresh
            response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_4, 'tStartRefresh')  # time at next scr refresh
            response_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_4.status == STARTED and not waitOnFlip:
            theseKeys = response_4.getKeys(keyList=['left', 'right'], waitRelease=False)
            _response_4_allKeys.extend(theseKeys)
            if len(_response_4_allKeys):
                response_4.keys = _response_4_allKeys[-1].name  # just the last key pressed
                response_4.rt = _response_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation_response_4* updates
        if fixation_response_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_response_4.frameNStart = frameN  # exact frame index
            fixation_response_4.tStart = t  # local t and not account for scr refresh
            fixation_response_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_response_4, 'tStartRefresh')  # time at next scr refresh
            fixation_response_4.setAutoDraw(True)
        if fixation_response_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_response_4.tStartRefresh + 2+currentDur+durMask+0.0001-frameTolerance:
                # keep track of stop time/frame for later
                fixation_response_4.tStop = t  # not accounting for scr refresh
                fixation_response_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_response_4, 'tStopRefresh')  # time at next scr refresh
                fixation_response_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseNeutralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ResponseNeutral"-------
    for thisComponent in ResponseNeutralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if targetPos[1]>0:
        if response_3.keys=='right':
            feedback="Doğru"
            accuracy.append(1)
            LoopNeutral.addData('Accuracy', 1)
        elif response_3.keys=='left':
            feedback="Yanlış"
            accuracy.append(0)
            LoopNeutral.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response_3.keys=='left':
            feedback="Doğru"
            accuracy.append(1)
            LoopNeutral.addData('Accuracy', 1)
        elif response_3.keys=='right':
            feedback="Yanlış"
            accuracy.append(0)
            LoopNeutral.addData('Accuracy', 0)
            
               
    # the Routine "ResponseNeutral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FeedbackNeutral"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedBackScreen_4.setText(feedback)
    LoopNeutral.addData('TargetDuration', currentDur*frameDur)
    
    #def staircase():
       # global accuracy
        #global currentDur
    if accuracy[-1]==0:
        currentDur=currentDur+1
    elif currentDur>1 and len(accuracy)>=2:
        if accuracy[-1]==1 and accuracy[-2]==1:
            currentDur=currentDur-1
    else: 
        currentDur=currentDur
    #return currentDur
    
    
    #if trialNumLoop100%numStaricase<30:
    #currentDur=staircase()
    if cueFile[7:11] in targetFile[7:11]:
        trialCongruency="congruent"
        congDur.append(target.tStopRefresh-target.tStartRefresh)
        incongDur.append(None)
        LoopNeutral.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        LoopNeutral.addData('congruentTrialDuration', congDur[trialNumLoop100])
    
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(None)
        LoopNeutral.addData('congruentTrialDuration', congDur[trialNumLoop100])
        LoopNeutral.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
                
    
    LoopNeutral.addData('isCongruent', trialCongruency)
    trialNumLoop100=trialNumLoop100+1
    
    # keep track of which components have finished
    FeedbackNeutralComponents = [feedBackScreen_4]
    for thisComponent in FeedbackNeutralComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackNeutralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FeedbackNeutral"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackNeutralClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackNeutralClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedBackScreen_4* updates
        if feedBackScreen_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedBackScreen_4.frameNStart = frameN  # exact frame index
            feedBackScreen_4.tStart = t  # local t and not account for scr refresh
            feedBackScreen_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedBackScreen_4, 'tStartRefresh')  # time at next scr refresh
            feedBackScreen_4.setAutoDraw(True)
        if feedBackScreen_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedBackScreen_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedBackScreen_4.tStop = t  # not accounting for scr refresh
                feedBackScreen_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedBackScreen_4, 'tStopRefresh')  # time at next scr refresh
                feedBackScreen_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackNeutralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FeedbackNeutral"-------
    for thisComponent in FeedbackNeutralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'LoopNeutral'


# ------Prepare to start Routine "end_of_exp"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu_5.keys = []
basla_butonu_5.rt = []
_basla_butonu_5_allKeys = []
# keep track of which components have finished
end_of_expComponents = [Instrcution100_5, basla_butonu_5]
for thisComponent in end_of_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_of_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_of_exp"-------
while continueRoutine:
    # get current time
    t = end_of_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_of_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrcution100_5* updates
    if Instrcution100_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrcution100_5.frameNStart = frameN  # exact frame index
        Instrcution100_5.tStart = t  # local t and not account for scr refresh
        Instrcution100_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrcution100_5, 'tStartRefresh')  # time at next scr refresh
        Instrcution100_5.setAutoDraw(True)
    if Instrcution100_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instrcution100_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Instrcution100_5.tStop = t  # not accounting for scr refresh
            Instrcution100_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instrcution100_5, 'tStopRefresh')  # time at next scr refresh
            Instrcution100_5.setAutoDraw(False)
    
    # *basla_butonu_5* updates
    if basla_butonu_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu_5.frameNStart = frameN  # exact frame index
        basla_butonu_5.tStart = t  # local t and not account for scr refresh
        basla_butonu_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu_5, 'tStartRefresh')  # time at next scr refresh
        basla_butonu_5.status = STARTED
        # keyboard checking is just starting
        basla_butonu_5.clock.reset()  # now t=0
        basla_butonu_5.clearEvents(eventType='keyboard')
    if basla_butonu_5.status == STARTED:
        theseKeys = basla_butonu_5.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_5_allKeys.extend(theseKeys)
        if len(_basla_butonu_5_allKeys):
            basla_butonu_5.keys = _basla_butonu_5_allKeys[-1].name  # just the last key pressed
            basla_butonu_5.rt = _basla_butonu_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_of_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_of_exp"-------
for thisComponent in end_of_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu_5.keys in ['', [], None]:  # No response was made
    basla_butonu_5.keys = None
thisExp.addData('basla_butonu_5.keys',basla_butonu_5.keys)
if basla_butonu_5.keys != None:  # we had a response
    thisExp.addData('basla_butonu_5.rt', basla_butonu_5.rt)
thisExp.nextEntry()
# the Routine "end_of_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
