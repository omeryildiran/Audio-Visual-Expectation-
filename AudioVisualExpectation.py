#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 13, 2021, at 02:44
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
expName = 'AudioVisualExpectation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\omeru\\Documents\\FND\\6.dönem\\312 R\\Design\\AudioVisualExp\\AudioVisualExpectation.py',
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

# Initialize components for Routine "Validity100Trial"
Validity100TrialClock = core.Clock()
targetPos=[0.4,-0.4]

target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
distractor = visual.ImageStim(
    win=win,
    name='distractor', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
maskLeft = visual.ImageStim(
    win=win,
    name='maskLeft', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
maskRight = visual.ImageStim(
    win=win,
    name='maskRight', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Cue = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='Cue')
Cue.setVolume(1.0)

# Initialize components for Routine "Response"
ResponseClock = core.Clock()
response = keyboard.Keyboard()
feedback=""

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedBackScreen = visual.TextStim(win=win, name='feedBackScreen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Loop100 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('congruent.xlsx'),
    seed=None, name='Loop100')
thisExp.addLoop(Loop100)  # add the loop to the experiment
thisLoop100 = Loop100.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop100.rgb)
if thisLoop100 != None:
    for paramName in thisLoop100:
        exec('{} = thisLoop100[paramName]'.format(paramName))

for thisLoop100 in Loop100:
    currentLoop = Loop100
    # abbreviate parameter names if possible (e.g. rgb = thisLoop100.rgb)
    if thisLoop100 != None:
        for paramName in thisLoop100:
            exec('{} = thisLoop100[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Validity100Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(targetPos)
    
    target.setPos((targetPos[1], 0))
    target.setImage(targetFile)
    distractor.setPos((-targetPos[1],0))
    distractor.setImage(maskFile)
    maskLeft.setPos((-0.4, 0))
    maskLeft.setImage(maskFile)
    maskRight.setPos((0.4, 0))
    maskRight.setImage(maskFile)
    Cue.setSound(cueFile, secs=2.0, hamming=True)
    Cue.setVolume(1.0, log=False)
    # keep track of which components have finished
    Validity100TrialComponents = [target, distractor, maskLeft, maskRight, Cue]
    for thisComponent in Validity100TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Validity100TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Validity100Trial"-------
    while continueRoutine:
        # get current time
        t = Validity100TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Validity100TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *distractor* updates
        if distractor.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            distractor.frameNStart = frameN  # exact frame index
            distractor.tStart = t  # local t and not account for scr refresh
            distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor, 'tStartRefresh')  # time at next scr refresh
            distractor.setAutoDraw(True)
        if distractor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > distractor.tStartRefresh + $targetDur-frameTolerance:
                # keep track of stop time/frame for later
                distractor.tStop = t  # not accounting for scr refresh
                distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor, 'tStopRefresh')  # time at next scr refresh
                distractor.setAutoDraw(False)
        
        # *maskLeft* updates
        if maskLeft.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            maskLeft.frameNStart = frameN  # exact frame index
            maskLeft.tStart = t  # local t and not account for scr refresh
            maskLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft, 'tStartRefresh')  # time at next scr refresh
            maskLeft.setAutoDraw(True)
        if maskLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maskLeft.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                maskLeft.tStop = t  # not accounting for scr refresh
                maskLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft, 'tStopRefresh')  # time at next scr refresh
                maskLeft.setAutoDraw(False)
        
        # *maskRight* updates
        if maskRight.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            maskRight.frameNStart = frameN  # exact frame index
            maskRight.tStart = t  # local t and not account for scr refresh
            maskRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight, 'tStartRefresh')  # time at next scr refresh
            maskRight.setAutoDraw(True)
        if maskRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maskRight.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                maskRight.tStop = t  # not accounting for scr refresh
                maskRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskRight, 'tStopRefresh')  # time at next scr refresh
                maskRight.setAutoDraw(False)
        # start/stop Cue
        if Cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cue.frameNStart = frameN  # exact frame index
            Cue.tStart = t  # local t and not account for scr refresh
            Cue.tStartRefresh = tThisFlipGlobal  # on global time
            Cue.play(when=win)  # sync with win flip
        if Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cue.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Cue.tStop = t  # not accounting for scr refresh
                Cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue, 'tStopRefresh')  # time at next scr refresh
                Cue.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Validity100TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Validity100Trial"-------
    for thisComponent in Validity100TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop100.addData('maskRight.started', maskRight.tStartRefresh)
    Loop100.addData('maskRight.stopped', maskRight.tStopRefresh)
    Cue.stop()  # ensure sound has stopped at end of routine
    Loop100.addData('Cue.started', Cue.tStartRefresh)
    Loop100.addData('Cue.stopped', Cue.tStopRefresh)
    # the Routine "Validity100Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    ResponseComponents = [response]
    for thisComponent in ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response"-------
    while continueRoutine:
        # get current time
        t = ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['left', 'right'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response"-------
    for thisComponent in ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    Loop100.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        Loop100.addData('response.rt', response.rt)
    if targetPos[1]>0:
        if response.keys=='right':
            feedback="Doğru"
            Loop100.addData('Accuracy', 1)
        elif response.keys=='left':
            feedback="Yanlış"
            Loop100.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response.keys=='left':
            feedback="Doğru"
            Loop100.addData('Accuracy', 1)
        elif response.keys=='right':
            feedback="Yanlış"
            Loop100.addData('Accuracy', 0)
            
               
    # the Routine "Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedBackScreen.setText(feedback)
    # keep track of which components have finished
    FeedbackComponents = [feedBackScreen]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedBackScreen* updates
        if feedBackScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedBackScreen.frameNStart = frameN  # exact frame index
            feedBackScreen.tStart = t  # local t and not account for scr refresh
            feedBackScreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedBackScreen, 'tStartRefresh')  # time at next scr refresh
            feedBackScreen.setAutoDraw(True)
        if feedBackScreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedBackScreen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedBackScreen.tStop = t  # not accounting for scr refresh
                feedBackScreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedBackScreen, 'tStopRefresh')  # time at next scr refresh
                feedBackScreen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'Loop100'


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
