#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 07, 2021, at 21:47
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
    originPath='C:\\Users\\omeru\\Documents\\FND\\My Repos\\Audio Visual Expectation\\AudioVisualExpectation_lastrun.py',
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

# Initialize components for Routine "Instruction_Deney"
Instruction_DeneyClock = core.Clock()
basla_butonu_6 = keyboard.Keyboard()
genel_instruction = visual.TextStim(win=win, name='genel_instruction',
    text='Deneyimize katıldığınız için teşekkür ederiz. Birazdan başlayacak olan deney her biri 4 aşamadan oluşan testler halindedir. Bu aşamalar %100 uyumlu (60 test), %75 uyumlu (240 test), %50 uyumlu (240 test) ve nötr (işitsel ipucunun bulunmadığı durum, 60 test) şeklinde karışık bir şekilde karşınıza çıkacaktır. Deney süresince toplam 600 teste maruz kalacaksınız. \nÖncelikle testler boyunca sizden ekranın ortasında duran sabit noktaya bakmanızı isteyeceğiz. \nBu deneyde ilk olarak 2 saniye boyunca erkek, kadın, kedi veya köpek seslerinden birini duyacaksınız. Hemen ardından çok çok kısa bir süre içinde ekranın bir tarafında düzgün bir resim diğer tarafında ise düzgün olmayan puzzle halinde parçalara ayrılıp karıştırılmış bir resim göreceksiniz. Çok kısa süren bu kısımın ardından tekrar çok çok kısa bir süre için (64 milisaniye) ekranın her iki tarafında puzzle halindeki resimleri göreceksiniz. Bu resimler az önce görmüş olduğunuz resimler ile aynı olacaktır. Ardından boş ekran gelecek ve sizden mümkün olduğunca hızlı bir şekilde ilk gördüğünüz düzgün resmin ekranın hangi tarafında olduğunu belirtmeniz istenecektir. Örneğin: düzgün olan resmi ekranın sağ tarafında gördüyseniz sağ tuşa basınız. Bir sonraki ekranda ise verdiğiniz cevabın doğruluğu ile ilgili bilgiyi göreceksiniz. Bu bilgiyi gördükten sonra hemen otomatik olarak aynı sürece devam edeceksiniz.\nTüm testler sona erdikten sonra ekranda deneyin bittiğine dair bir yazı çıkacaktır. Hazır olduğunuzda space(boşluk) tuşu ile deneme testine geçebiliriz.\n',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Validity100Trial"
Validity100TrialClock = core.Clock()
targetPos=[0.4,-0.4]
targetDur=list([1, 2, 3, 4, 5])
currentDur=np.random.choice(targetDur)
accuracy=[]
durMask=4

target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
distractor = visual.ImageStim(
    win=win,
    name='distractor', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
maskLeft = visual.ImageStim(
    win=win,
    name='maskLeft', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
maskRight = visual.ImageStim(
    win=win,
    name='maskRight', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
Cue = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='Cue')
Cue.setVolume(1.0)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)

# Initialize components for Routine "Response100"
Response100Clock = core.Clock()
response_2 = keyboard.Keyboard()
feedback=""
fixation_response_2 = visual.ShapeStim(
    win=win, name='fixation_response_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Feedback100"
Feedback100Clock = core.Clock()
feedBackScreen = visual.TextStim(win=win, name='feedBackScreen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Set experiment start values for variable component trialNumLoop100
trialNumLoop100 = 0
trialNumLoop100Container = []
# Set experiment start values for variable component numStaricase
numStaricase = 30
numStaricaseContainer = []
# Set experiment start values for variable component trialCongruency
trialCongruency = ''
trialCongruencyContainer = []
trialNumLoop100=0
numStaricase=30
trialCongruency=""
congDur=[]
incongDur=[]

# Initialize components for Routine "Instruction100"
Instruction100Clock = core.Clock()
Instrcution100 = visual.TextStim(win=win, name='Instrcution100',
    text='1.Aşama: (%100 UYUMLU) Bu aşamadaki duyacağınız tüm sesler ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
basla_butonu = keyboard.Keyboard()

# Initialize components for Routine "Validity100Trial"
Validity100TrialClock = core.Clock()
targetPos=[0.4,-0.4]
targetDur=list([1, 2, 3, 4, 5])
currentDur=np.random.choice(targetDur)
accuracy=[]
durMask=4

target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
distractor = visual.ImageStim(
    win=win,
    name='distractor', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
maskLeft = visual.ImageStim(
    win=win,
    name='maskLeft', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
maskRight = visual.ImageStim(
    win=win,
    name='maskRight', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
Cue = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='Cue')
Cue.setVolume(1.0)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)

# Initialize components for Routine "Response100"
Response100Clock = core.Clock()
response_2 = keyboard.Keyboard()
feedback=""
fixation_response_2 = visual.ShapeStim(
    win=win, name='fixation_response_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Feedback100"
Feedback100Clock = core.Clock()
feedBackScreen = visual.TextStim(win=win, name='feedBackScreen',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Set experiment start values for variable component trialNumLoop100
trialNumLoop100 = 0
trialNumLoop100Container = []
# Set experiment start values for variable component numStaricase
numStaricase = 30
numStaricaseContainer = []
# Set experiment start values for variable component trialCongruency
trialCongruency = ''
trialCongruencyContainer = []
trialNumLoop100=0
numStaricase=30
trialCongruency=""
congDur=[]
incongDur=[]

# Initialize components for Routine "Instruction75"
Instruction75Clock = core.Clock()
Instrcution100_2 = visual.TextStim(win=win, name='Instrcution100_2',
    text='2.Aşama(%75 UYUMLU): Bu aşamadaki duyacağınız seslerin %75’i ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız %75 ihtimalle kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
basla_butonu_2 = keyboard.Keyboard()

# Initialize components for Routine "Validity75Trial"
Validity75TrialClock = core.Clock()
target_2 = visual.ImageStim(
    win=win,
    name='target_2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
distractor_2 = visual.ImageStim(
    win=win,
    name='distractor_2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
maskLeft_2 = visual.ImageStim(
    win=win,
    name='maskLeft_2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
maskRight_2 = visual.ImageStim(
    win=win,
    name='maskRight_2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Cue_2 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='Cue_2')
Cue_2.setVolume(1.0)
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "Response75"
Response75Clock = core.Clock()
response = keyboard.Keyboard()
#feedback=""
fixation_response = visual.ShapeStim(
    win=win, name='fixation_response', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Feedback75"
Feedback75Clock = core.Clock()
feedBackScreen_2 = visual.TextStim(win=win, name='feedBackScreen_2',
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

# Initialize components for Routine "Instruction50"
Instruction50Clock = core.Clock()
Instrcution100_3 = visual.TextStim(win=win, name='Instrcution100_3',
    text='3.Aşama (%50 UYUMLU): Bu aşamadaki duyacağınız seslerin %50’si ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız %50 ihtimalle kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
basla_butonu_3 = keyboard.Keyboard()

# Initialize components for Routine "Validity50Trial"
Validity50TrialClock = core.Clock()
target_3 = visual.ImageStim(
    win=win,
    name='target_3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
distractor_3 = visual.ImageStim(
    win=win,
    name='distractor_3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
maskLeft_3 = visual.ImageStim(
    win=win,
    name='maskLeft_3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
maskRight_3 = visual.ImageStim(
    win=win,
    name='maskRight_3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Cue_3 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='Cue_3')
Cue_3.setVolume(1.0)
fixation_3 = visual.ShapeStim(
    win=win, name='fixation_3', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "Response50"
Response50Clock = core.Clock()
response_3 = keyboard.Keyboard()
#feedback=""
fixation_response_3 = visual.ShapeStim(
    win=win, name='fixation_response_3', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Feedback50"
Feedback50Clock = core.Clock()
feedBackScreen_3 = visual.TextStim(win=win, name='feedBackScreen_3',
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

# Initialize components for Routine "InstructionNeutral"
InstructionNeutralClock = core.Clock()
Instrcution100_4 = visual.TextStim(win=win, name='Instrcution100_4',
    text='4.Aşama (Nötr): Bu son aşamadır. Bu aşamada herhangi bir ses duymayacaksınız. Yalnızca önceki aşamalarda olduğu gibi düzgün resmin olduğu tarafı bulmaya çalışınız. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
basla_butonu_4 = keyboard.Keyboard()

# Initialize components for Routine "NeutralTrial"
NeutralTrialClock = core.Clock()
target_4 = visual.ImageStim(
    win=win,
    name='target_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
distractor_4 = visual.ImageStim(
    win=win,
    name='distractor_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
maskLeft_4 = visual.ImageStim(
    win=win,
    name='maskLeft_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
maskRight_4 = visual.ImageStim(
    win=win,
    name='maskRight_4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fixation_4 = visual.ShapeStim(
    win=win, name='fixation_4', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

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

# ------Prepare to start Routine "Instruction_Deney"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu_6.keys = []
basla_butonu_6.rt = []
_basla_butonu_6_allKeys = []
# keep track of which components have finished
Instruction_DeneyComponents = [basla_butonu_6, genel_instruction]
for thisComponent in Instruction_DeneyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction_DeneyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction_Deney"-------
while continueRoutine:
    # get current time
    t = Instruction_DeneyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction_DeneyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *basla_butonu_6* updates
    if basla_butonu_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu_6.frameNStart = frameN  # exact frame index
        basla_butonu_6.tStart = t  # local t and not account for scr refresh
        basla_butonu_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu_6, 'tStartRefresh')  # time at next scr refresh
        basla_butonu_6.status = STARTED
        # keyboard checking is just starting
        basla_butonu_6.clock.reset()  # now t=0
        basla_butonu_6.clearEvents(eventType='keyboard')
    if basla_butonu_6.status == STARTED:
        theseKeys = basla_butonu_6.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_6_allKeys.extend(theseKeys)
        if len(_basla_butonu_6_allKeys):
            basla_butonu_6.keys = _basla_butonu_6_allKeys[-1].name  # just the last key pressed
            basla_butonu_6.rt = _basla_butonu_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *genel_instruction* updates
    if genel_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genel_instruction.frameNStart = frameN  # exact frame index
        genel_instruction.tStart = t  # local t and not account for scr refresh
        genel_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genel_instruction, 'tStartRefresh')  # time at next scr refresh
        genel_instruction.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_DeneyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_Deney"-------
for thisComponent in Instruction_DeneyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu_6.keys in ['', [], None]:  # No response was made
    basla_butonu_6.keys = None
thisExp.addData('basla_butonu_6.keys',basla_butonu_6.keys)
if basla_butonu_6.keys != None:  # we had a response
    thisExp.addData('basla_butonu_6.rt', basla_butonu_6.rt)
thisExp.nextEntry()
# the Routine "Instruction_Deney" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
deneme = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('congruent100.xlsx', selection='0:4'),
    seed=None, name='deneme')
thisExp.addLoop(deneme)  # add the loop to the experiment
thisDeneme = deneme.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDeneme.rgb)
if thisDeneme != None:
    for paramName in thisDeneme:
        exec('{} = thisDeneme[paramName]'.format(paramName))

for thisDeneme in deneme:
    currentLoop = deneme
    # abbreviate parameter names if possible (e.g. rgb = thisDeneme.rgb)
    if thisDeneme != None:
        for paramName in thisDeneme:
            exec('{} = thisDeneme[paramName]'.format(paramName))
    
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
    Validity100TrialComponents = [target, distractor, maskLeft, maskRight, Cue, fixation]
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
        if target.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            if frameN >= (target.frameNStart + currentDur):
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *distractor* updates
        if distractor.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            distractor.frameNStart = frameN  # exact frame index
            distractor.tStart = t  # local t and not account for scr refresh
            distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor, 'tStartRefresh')  # time at next scr refresh
            distractor.setAutoDraw(True)
        if distractor.status == STARTED:
            if frameN >= (distractor.frameNStart + currentDur):
                # keep track of stop time/frame for later
                distractor.tStop = t  # not accounting for scr refresh
                distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor, 'tStopRefresh')  # time at next scr refresh
                distractor.setAutoDraw(False)
        
        # *maskLeft* updates
        if maskLeft.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskLeft.frameNStart = frameN  # exact frame index
            maskLeft.tStart = t  # local t and not account for scr refresh
            maskLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft, 'tStartRefresh')  # time at next scr refresh
            maskLeft.setAutoDraw(True)
        if maskLeft.status == STARTED:
            if frameN >= (maskLeft.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskLeft.tStop = t  # not accounting for scr refresh
                maskLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft, 'tStopRefresh')  # time at next scr refresh
                maskLeft.setAutoDraw(False)
        
        # *maskRight* updates
        if maskRight.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskRight.frameNStart = frameN  # exact frame index
            maskRight.tStart = t  # local t and not account for scr refresh
            maskRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight, 'tStartRefresh')  # time at next scr refresh
            maskRight.setAutoDraw(True)
        if maskRight.status == STARTED:
            if frameN >= (maskRight.frameNStart + durMask):
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
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            if frameN >= (fixation.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001):
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
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
    deneme.addData('target.started', target.tStartRefresh)
    deneme.addData('target.stopped', target.tStopRefresh)
    deneme.addData('maskLeft.started', maskLeft.tStartRefresh)
    deneme.addData('maskLeft.stopped', maskLeft.tStopRefresh)
    Cue.stop()  # ensure sound has stopped at end of routine
    # the Routine "Validity100Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response100"-------
    continueRoutine = True
    # update component parameters for each repeat
    response_2.keys = []
    response_2.rt = []
    _response_2_allKeys = []
    # keep track of which components have finished
    Response100Components = [response_2, fixation_response_2]
    for thisComponent in Response100Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response100"-------
    while continueRoutine:
        # get current time
        t = Response100Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response100Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response_2* updates
        waitOnFlip = False
        if response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_2.status == STARTED and not waitOnFlip:
            theseKeys = response_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _response_2_allKeys.extend(theseKeys)
            if len(_response_2_allKeys):
                response_2.keys = _response_2_allKeys[-1].name  # just the last key pressed
                response_2.rt = _response_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation_response_2* updates
        if fixation_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_response_2.frameNStart = frameN  # exact frame index
            fixation_response_2.tStart = t  # local t and not account for scr refresh
            fixation_response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_response_2, 'tStartRefresh')  # time at next scr refresh
            fixation_response_2.setAutoDraw(True)
        if fixation_response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_response_2.tStartRefresh + 2+currentDur+durMask+0.0001-frameTolerance:
                # keep track of stop time/frame for later
                fixation_response_2.tStop = t  # not accounting for scr refresh
                fixation_response_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_response_2, 'tStopRefresh')  # time at next scr refresh
                fixation_response_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response100Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response100"-------
    for thisComponent in Response100Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if targetPos[1]>0:
        if response_2.keys=='right':
            feedback="Doğru"
            accuracy.append(1)
            deneme.addData('Accuracy', 1)
        elif response_2.keys=='left':
            feedback="Yanlış"
            accuracy.append(0)
            deneme.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response_2.keys=='left':
            feedback="Doğru"
            accuracy.append(1)
            deneme.addData('Accuracy', 1)
        elif response_2.keys=='right':
            feedback="Yanlış"
            accuracy.append(0)
            deneme.addData('Accuracy', 0)
            
               
    # the Routine "Response100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback100"-------
    continueRoutine = True
    # update component parameters for each repeat
    feedBackScreen.setText(feedback)
    deneme.addData('TargetDuration', currentDur*frameDur)
    
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
        deneme.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        deneme.addData('congruentTrialDuration', congDur[trialNumLoop100])
    
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(None)
        deneme.addData('congruentTrialDuration', congDur[trialNumLoop100])
        deneme.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
                
    
    deneme.addData('isCongruent', trialCongruency)
    trialNumLoop100=trialNumLoop100+1
    
    # keep track of which components have finished
    Feedback100Components = [feedBackScreen]
    for thisComponent in Feedback100Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback100"-------
    while continueRoutine:
        # get current time
        t = Feedback100Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback100Clock)
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
        for thisComponent in Feedback100Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback100"-------
    for thisComponent in Feedback100Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'deneme'


# ------Prepare to start Routine "Instruction100"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu.keys = []
basla_butonu.rt = []
_basla_butonu_allKeys = []
# keep track of which components have finished
Instruction100Components = [Instrcution100, basla_butonu]
for thisComponent in Instruction100Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction100"-------
while continueRoutine:
    # get current time
    t = Instruction100Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction100Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrcution100* updates
    if Instrcution100.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrcution100.frameNStart = frameN  # exact frame index
        Instrcution100.tStart = t  # local t and not account for scr refresh
        Instrcution100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrcution100, 'tStartRefresh')  # time at next scr refresh
        Instrcution100.setAutoDraw(True)
    
    # *basla_butonu* updates
    if basla_butonu.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu.frameNStart = frameN  # exact frame index
        basla_butonu.tStart = t  # local t and not account for scr refresh
        basla_butonu.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu, 'tStartRefresh')  # time at next scr refresh
        basla_butonu.status = STARTED
        # keyboard checking is just starting
        basla_butonu.clock.reset()  # now t=0
        basla_butonu.clearEvents(eventType='keyboard')
    if basla_butonu.status == STARTED:
        theseKeys = basla_butonu.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_allKeys.extend(theseKeys)
        if len(_basla_butonu_allKeys):
            basla_butonu.keys = _basla_butonu_allKeys[-1].name  # just the last key pressed
            basla_butonu.rt = _basla_butonu_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction100Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction100"-------
for thisComponent in Instruction100Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu.keys in ['', [], None]:  # No response was made
    basla_butonu.keys = None
thisExp.addData('basla_butonu.keys',basla_butonu.keys)
if basla_butonu.keys != None:  # we had a response
    thisExp.addData('basla_butonu.rt', basla_butonu.rt)
thisExp.nextEntry()
# the Routine "Instruction100" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop100 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('congruent100.xlsx'),
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
    Validity100TrialComponents = [target, distractor, maskLeft, maskRight, Cue, fixation]
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
        if target.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            if frameN >= (target.frameNStart + currentDur):
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *distractor* updates
        if distractor.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            distractor.frameNStart = frameN  # exact frame index
            distractor.tStart = t  # local t and not account for scr refresh
            distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor, 'tStartRefresh')  # time at next scr refresh
            distractor.setAutoDraw(True)
        if distractor.status == STARTED:
            if frameN >= (distractor.frameNStart + currentDur):
                # keep track of stop time/frame for later
                distractor.tStop = t  # not accounting for scr refresh
                distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor, 'tStopRefresh')  # time at next scr refresh
                distractor.setAutoDraw(False)
        
        # *maskLeft* updates
        if maskLeft.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskLeft.frameNStart = frameN  # exact frame index
            maskLeft.tStart = t  # local t and not account for scr refresh
            maskLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft, 'tStartRefresh')  # time at next scr refresh
            maskLeft.setAutoDraw(True)
        if maskLeft.status == STARTED:
            if frameN >= (maskLeft.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskLeft.tStop = t  # not accounting for scr refresh
                maskLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft, 'tStopRefresh')  # time at next scr refresh
                maskLeft.setAutoDraw(False)
        
        # *maskRight* updates
        if maskRight.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskRight.frameNStart = frameN  # exact frame index
            maskRight.tStart = t  # local t and not account for scr refresh
            maskRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight, 'tStartRefresh')  # time at next scr refresh
            maskRight.setAutoDraw(True)
        if maskRight.status == STARTED:
            if frameN >= (maskRight.frameNStart + durMask):
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
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            if frameN >= (fixation.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001):
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
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
    Loop100.addData('target.started', target.tStartRefresh)
    Loop100.addData('target.stopped', target.tStopRefresh)
    Loop100.addData('maskLeft.started', maskLeft.tStartRefresh)
    Loop100.addData('maskLeft.stopped', maskLeft.tStopRefresh)
    Cue.stop()  # ensure sound has stopped at end of routine
    # the Routine "Validity100Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response100"-------
    continueRoutine = True
    # update component parameters for each repeat
    response_2.keys = []
    response_2.rt = []
    _response_2_allKeys = []
    # keep track of which components have finished
    Response100Components = [response_2, fixation_response_2]
    for thisComponent in Response100Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response100"-------
    while continueRoutine:
        # get current time
        t = Response100Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response100Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response_2* updates
        waitOnFlip = False
        if response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_2.status == STARTED and not waitOnFlip:
            theseKeys = response_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _response_2_allKeys.extend(theseKeys)
            if len(_response_2_allKeys):
                response_2.keys = _response_2_allKeys[-1].name  # just the last key pressed
                response_2.rt = _response_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation_response_2* updates
        if fixation_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_response_2.frameNStart = frameN  # exact frame index
            fixation_response_2.tStart = t  # local t and not account for scr refresh
            fixation_response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_response_2, 'tStartRefresh')  # time at next scr refresh
            fixation_response_2.setAutoDraw(True)
        if fixation_response_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_response_2.tStartRefresh + 2+currentDur+durMask+0.0001-frameTolerance:
                # keep track of stop time/frame for later
                fixation_response_2.tStop = t  # not accounting for scr refresh
                fixation_response_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_response_2, 'tStopRefresh')  # time at next scr refresh
                fixation_response_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response100Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response100"-------
    for thisComponent in Response100Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if targetPos[1]>0:
        if response_2.keys=='right':
            feedback="Doğru"
            accuracy.append(1)
            deneme.addData('Accuracy', 1)
        elif response_2.keys=='left':
            feedback="Yanlış"
            accuracy.append(0)
            deneme.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response_2.keys=='left':
            feedback="Doğru"
            accuracy.append(1)
            deneme.addData('Accuracy', 1)
        elif response_2.keys=='right':
            feedback="Yanlış"
            accuracy.append(0)
            deneme.addData('Accuracy', 0)
            
               
    # the Routine "Response100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback100"-------
    continueRoutine = True
    # update component parameters for each repeat
    feedBackScreen.setText(feedback)
    deneme.addData('TargetDuration', currentDur*frameDur)
    
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
        deneme.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        deneme.addData('congruentTrialDuration', congDur[trialNumLoop100])
    
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(None)
        deneme.addData('congruentTrialDuration', congDur[trialNumLoop100])
        deneme.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
                
    
    deneme.addData('isCongruent', trialCongruency)
    trialNumLoop100=trialNumLoop100+1
    
    # keep track of which components have finished
    Feedback100Components = [feedBackScreen]
    for thisComponent in Feedback100Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback100"-------
    while continueRoutine:
        # get current time
        t = Feedback100Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback100Clock)
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
        for thisComponent in Feedback100Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback100"-------
    for thisComponent in Feedback100Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'Loop100'


# ------Prepare to start Routine "Instruction75"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu_2.keys = []
basla_butonu_2.rt = []
_basla_butonu_2_allKeys = []
# keep track of which components have finished
Instruction75Components = [Instrcution100_2, basla_butonu_2]
for thisComponent in Instruction75Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction75Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction75"-------
while continueRoutine:
    # get current time
    t = Instruction75Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction75Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrcution100_2* updates
    if Instrcution100_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrcution100_2.frameNStart = frameN  # exact frame index
        Instrcution100_2.tStart = t  # local t and not account for scr refresh
        Instrcution100_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrcution100_2, 'tStartRefresh')  # time at next scr refresh
        Instrcution100_2.setAutoDraw(True)
    
    # *basla_butonu_2* updates
    if basla_butonu_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu_2.frameNStart = frameN  # exact frame index
        basla_butonu_2.tStart = t  # local t and not account for scr refresh
        basla_butonu_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu_2, 'tStartRefresh')  # time at next scr refresh
        basla_butonu_2.status = STARTED
        # keyboard checking is just starting
        basla_butonu_2.clock.reset()  # now t=0
        basla_butonu_2.clearEvents(eventType='keyboard')
    if basla_butonu_2.status == STARTED:
        theseKeys = basla_butonu_2.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_2_allKeys.extend(theseKeys)
        if len(_basla_butonu_2_allKeys):
            basla_butonu_2.keys = _basla_butonu_2_allKeys[-1].name  # just the last key pressed
            basla_butonu_2.rt = _basla_butonu_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction75Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction75"-------
for thisComponent in Instruction75Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu_2.keys in ['', [], None]:  # No response was made
    basla_butonu_2.keys = None
thisExp.addData('basla_butonu_2.keys',basla_butonu_2.keys)
if basla_butonu_2.keys != None:  # we had a response
    thisExp.addData('basla_butonu_2.rt', basla_butonu_2.rt)
thisExp.nextEntry()
# the Routine "Instruction75" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop75 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('congruent75.xlsx'),
    seed=None, name='Loop75')
thisExp.addLoop(Loop75)  # add the loop to the experiment
thisLoop75 = Loop75.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop75.rgb)
if thisLoop75 != None:
    for paramName in thisLoop75:
        exec('{} = thisLoop75[paramName]'.format(paramName))

for thisLoop75 in Loop75:
    currentLoop = Loop75
    # abbreviate parameter names if possible (e.g. rgb = thisLoop75.rgb)
    if thisLoop75 != None:
        for paramName in thisLoop75:
            exec('{} = thisLoop75[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Validity75Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_2.setPos((targetPos[1], 0))
    target_2.setImage(targetFile)
    distractor_2.setPos((-targetPos[1],0))
    distractor_2.setImage(maskFile)
    maskLeft_2.setPos((-0.4, 0))
    maskLeft_2.setImage(maskFile)
    maskRight_2.setPos((0.4, 0))
    maskRight_2.setImage(maskFile)
    Cue_2.setSound(cueFile, secs=2.0, hamming=True)
    Cue_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    Validity75TrialComponents = [target_2, distractor_2, maskLeft_2, maskRight_2, Cue_2, fixation_2]
    for thisComponent in Validity75TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Validity75TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Validity75Trial"-------
    while continueRoutine:
        # get current time
        t = Validity75TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Validity75TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_2* updates
        if target_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            target_2.setAutoDraw(True)
        if target_2.status == STARTED:
            if frameN >= (target_2.frameNStart + currentDur):
                # keep track of stop time/frame for later
                target_2.tStop = t  # not accounting for scr refresh
                target_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_2, 'tStopRefresh')  # time at next scr refresh
                target_2.setAutoDraw(False)
        
        # *distractor_2* updates
        if distractor_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            distractor_2.frameNStart = frameN  # exact frame index
            distractor_2.tStart = t  # local t and not account for scr refresh
            distractor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor_2, 'tStartRefresh')  # time at next scr refresh
            distractor_2.setAutoDraw(True)
        if distractor_2.status == STARTED:
            if frameN >= (distractor_2.frameNStart + currentDur):
                # keep track of stop time/frame for later
                distractor_2.tStop = t  # not accounting for scr refresh
                distractor_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor_2, 'tStopRefresh')  # time at next scr refresh
                distractor_2.setAutoDraw(False)
        
        # *maskLeft_2* updates
        if maskLeft_2.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskLeft_2.frameNStart = frameN  # exact frame index
            maskLeft_2.tStart = t  # local t and not account for scr refresh
            maskLeft_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft_2, 'tStartRefresh')  # time at next scr refresh
            maskLeft_2.setAutoDraw(True)
        if maskLeft_2.status == STARTED:
            if frameN >= (maskLeft_2.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskLeft_2.tStop = t  # not accounting for scr refresh
                maskLeft_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft_2, 'tStopRefresh')  # time at next scr refresh
                maskLeft_2.setAutoDraw(False)
        
        # *maskRight_2* updates
        if maskRight_2.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskRight_2.frameNStart = frameN  # exact frame index
            maskRight_2.tStart = t  # local t and not account for scr refresh
            maskRight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight_2, 'tStartRefresh')  # time at next scr refresh
            maskRight_2.setAutoDraw(True)
        if maskRight_2.status == STARTED:
            if frameN >= (maskRight_2.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskRight_2.tStop = t  # not accounting for scr refresh
                maskRight_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskRight_2, 'tStopRefresh')  # time at next scr refresh
                maskRight_2.setAutoDraw(False)
        # start/stop Cue_2
        if Cue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cue_2.frameNStart = frameN  # exact frame index
            Cue_2.tStart = t  # local t and not account for scr refresh
            Cue_2.tStartRefresh = tThisFlipGlobal  # on global time
            Cue_2.play(when=win)  # sync with win flip
        if Cue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cue_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Cue_2.tStop = t  # not accounting for scr refresh
                Cue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue_2, 'tStopRefresh')  # time at next scr refresh
                Cue_2.stop()
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            if frameN >= (fixation_2.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001):
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Validity75TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Validity75Trial"-------
    for thisComponent in Validity75TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop75.addData('target_2.started', target_2.tStartRefresh)
    Loop75.addData('target_2.stopped', target_2.tStopRefresh)
    Loop75.addData('maskLeft_2.started', maskLeft_2.tStartRefresh)
    Loop75.addData('maskLeft_2.stopped', maskLeft_2.tStopRefresh)
    Cue_2.stop()  # ensure sound has stopped at end of routine
    # the Routine "Validity75Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response75"-------
    continueRoutine = True
    # update component parameters for each repeat
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    Response75Components = [response, fixation_response]
    for thisComponent in Response75Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response75Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response75"-------
    while continueRoutine:
        # get current time
        t = Response75Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response75Clock)
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
        
        # *fixation_response* updates
        if fixation_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_response.frameNStart = frameN  # exact frame index
            fixation_response.tStart = t  # local t and not account for scr refresh
            fixation_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_response, 'tStartRefresh')  # time at next scr refresh
            fixation_response.setAutoDraw(True)
        if fixation_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_response.tStartRefresh + 2+currentDur+durMask+0.0001-frameTolerance:
                # keep track of stop time/frame for later
                fixation_response.tStop = t  # not accounting for scr refresh
                fixation_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_response, 'tStopRefresh')  # time at next scr refresh
                fixation_response.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response75"-------
    for thisComponent in Response75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if targetPos[1]>0:
        if response.keys=='right':
            feedback="Doğru"
            accuracy.append(1)
            Loop75.addData('Accuracy', 1)
        elif response.keys=='left':
            feedback="Yanlış"
            accuracy.append(0)
            Loop75.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response.keys=='left':
            feedback="Doğru"
            accuracy.append(1)
            Loop75.addData('Accuracy', 1)
        elif response.keys=='right':
            feedback="Yanlış"
            accuracy.append(0)
            Loop75.addData('Accuracy', 0)
            
               
    # the Routine "Response75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback75"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedBackScreen_2.setText(feedback)
    Loop75.addData('TargetDuration', currentDur*frameDur)
    
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
        Loop75.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        Loop75.addData('congruentTrialDuration', congDur[trialNumLoop100])
    
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(None)
        Loop75.addData('congruentTrialDuration', congDur[trialNumLoop100])
        Loop75.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
                
    
    Loop75.addData('isCongruent', trialCongruency)
    trialNumLoop100=trialNumLoop100+1
    
    # keep track of which components have finished
    Feedback75Components = [feedBackScreen_2]
    for thisComponent in Feedback75Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback75Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback75"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback75Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback75Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedBackScreen_2* updates
        if feedBackScreen_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedBackScreen_2.frameNStart = frameN  # exact frame index
            feedBackScreen_2.tStart = t  # local t and not account for scr refresh
            feedBackScreen_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedBackScreen_2, 'tStartRefresh')  # time at next scr refresh
            feedBackScreen_2.setAutoDraw(True)
        if feedBackScreen_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedBackScreen_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedBackScreen_2.tStop = t  # not accounting for scr refresh
                feedBackScreen_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedBackScreen_2, 'tStopRefresh')  # time at next scr refresh
                feedBackScreen_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback75Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback75"-------
    for thisComponent in Feedback75Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'Loop75'


# ------Prepare to start Routine "Instruction50"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu_3.keys = []
basla_butonu_3.rt = []
_basla_butonu_3_allKeys = []
# keep track of which components have finished
Instruction50Components = [Instrcution100_3, basla_butonu_3]
for thisComponent in Instruction50Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction50Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction50"-------
while continueRoutine:
    # get current time
    t = Instruction50Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction50Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrcution100_3* updates
    if Instrcution100_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrcution100_3.frameNStart = frameN  # exact frame index
        Instrcution100_3.tStart = t  # local t and not account for scr refresh
        Instrcution100_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrcution100_3, 'tStartRefresh')  # time at next scr refresh
        Instrcution100_3.setAutoDraw(True)
    
    # *basla_butonu_3* updates
    if basla_butonu_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu_3.frameNStart = frameN  # exact frame index
        basla_butonu_3.tStart = t  # local t and not account for scr refresh
        basla_butonu_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu_3, 'tStartRefresh')  # time at next scr refresh
        basla_butonu_3.status = STARTED
        # keyboard checking is just starting
        basla_butonu_3.clock.reset()  # now t=0
        basla_butonu_3.clearEvents(eventType='keyboard')
    if basla_butonu_3.status == STARTED:
        theseKeys = basla_butonu_3.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_3_allKeys.extend(theseKeys)
        if len(_basla_butonu_3_allKeys):
            basla_butonu_3.keys = _basla_butonu_3_allKeys[-1].name  # just the last key pressed
            basla_butonu_3.rt = _basla_butonu_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction50Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction50"-------
for thisComponent in Instruction50Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu_3.keys in ['', [], None]:  # No response was made
    basla_butonu_3.keys = None
thisExp.addData('basla_butonu_3.keys',basla_butonu_3.keys)
if basla_butonu_3.keys != None:  # we had a response
    thisExp.addData('basla_butonu_3.rt', basla_butonu_3.rt)
thisExp.nextEntry()
# the Routine "Instruction50" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop50 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('congruent50.xlsx'),
    seed=None, name='Loop50')
thisExp.addLoop(Loop50)  # add the loop to the experiment
thisLoop50 = Loop50.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop50.rgb)
if thisLoop50 != None:
    for paramName in thisLoop50:
        exec('{} = thisLoop50[paramName]'.format(paramName))

for thisLoop50 in Loop50:
    currentLoop = Loop50
    # abbreviate parameter names if possible (e.g. rgb = thisLoop50.rgb)
    if thisLoop50 != None:
        for paramName in thisLoop50:
            exec('{} = thisLoop50[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Validity50Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_3.setPos((targetPos[1], 0))
    target_3.setImage(targetFile)
    distractor_3.setPos((-targetPos[1],0))
    distractor_3.setImage(maskFile)
    maskLeft_3.setPos((-0.4, 0))
    maskLeft_3.setImage(maskFile)
    maskRight_3.setPos((0.4, 0))
    maskRight_3.setImage(maskFile)
    Cue_3.setSound(cueFile, secs=2.0, hamming=True)
    Cue_3.setVolume(1.0, log=False)
    # keep track of which components have finished
    Validity50TrialComponents = [target_3, distractor_3, maskLeft_3, maskRight_3, Cue_3, fixation_3]
    for thisComponent in Validity50TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Validity50TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Validity50Trial"-------
    while continueRoutine:
        # get current time
        t = Validity50TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Validity50TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_3* updates
        if target_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            target_3.frameNStart = frameN  # exact frame index
            target_3.tStart = t  # local t and not account for scr refresh
            target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_3, 'tStartRefresh')  # time at next scr refresh
            target_3.setAutoDraw(True)
        if target_3.status == STARTED:
            if frameN >= (target_3.frameNStart + currentDur):
                # keep track of stop time/frame for later
                target_3.tStop = t  # not accounting for scr refresh
                target_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_3, 'tStopRefresh')  # time at next scr refresh
                target_3.setAutoDraw(False)
        
        # *distractor_3* updates
        if distractor_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            distractor_3.frameNStart = frameN  # exact frame index
            distractor_3.tStart = t  # local t and not account for scr refresh
            distractor_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor_3, 'tStartRefresh')  # time at next scr refresh
            distractor_3.setAutoDraw(True)
        if distractor_3.status == STARTED:
            if frameN >= (distractor_3.frameNStart + currentDur):
                # keep track of stop time/frame for later
                distractor_3.tStop = t  # not accounting for scr refresh
                distractor_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(distractor_3, 'tStopRefresh')  # time at next scr refresh
                distractor_3.setAutoDraw(False)
        
        # *maskLeft_3* updates
        if maskLeft_3.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskLeft_3.frameNStart = frameN  # exact frame index
            maskLeft_3.tStart = t  # local t and not account for scr refresh
            maskLeft_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskLeft_3, 'tStartRefresh')  # time at next scr refresh
            maskLeft_3.setAutoDraw(True)
        if maskLeft_3.status == STARTED:
            if frameN >= (maskLeft_3.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskLeft_3.tStop = t  # not accounting for scr refresh
                maskLeft_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskLeft_3, 'tStopRefresh')  # time at next scr refresh
                maskLeft_3.setAutoDraw(False)
        
        # *maskRight_3* updates
        if maskRight_3.status == NOT_STARTED and frameN >= (expInfo['frameRate']*2)+currentDur:
            # keep track of start time/frame for later
            maskRight_3.frameNStart = frameN  # exact frame index
            maskRight_3.tStart = t  # local t and not account for scr refresh
            maskRight_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maskRight_3, 'tStartRefresh')  # time at next scr refresh
            maskRight_3.setAutoDraw(True)
        if maskRight_3.status == STARTED:
            if frameN >= (maskRight_3.frameNStart + durMask):
                # keep track of stop time/frame for later
                maskRight_3.tStop = t  # not accounting for scr refresh
                maskRight_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maskRight_3, 'tStopRefresh')  # time at next scr refresh
                maskRight_3.setAutoDraw(False)
        # start/stop Cue_3
        if Cue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cue_3.frameNStart = frameN  # exact frame index
            Cue_3.tStart = t  # local t and not account for scr refresh
            Cue_3.tStartRefresh = tThisFlipGlobal  # on global time
            Cue_3.play(when=win)  # sync with win flip
        if Cue_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cue_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                Cue_3.tStop = t  # not accounting for scr refresh
                Cue_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue_3, 'tStopRefresh')  # time at next scr refresh
                Cue_3.stop()
        
        # *fixation_3* updates
        if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.tStart = t  # local t and not account for scr refresh
            fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
            fixation_3.setAutoDraw(True)
        if fixation_3.status == STARTED:
            if frameN >= (fixation_3.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001):
                # keep track of stop time/frame for later
                fixation_3.tStop = t  # not accounting for scr refresh
                fixation_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_3, 'tStopRefresh')  # time at next scr refresh
                fixation_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Validity50TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Validity50Trial"-------
    for thisComponent in Validity50TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop50.addData('target_3.started', target_3.tStartRefresh)
    Loop50.addData('target_3.stopped', target_3.tStopRefresh)
    Loop50.addData('maskLeft_3.started', maskLeft_3.tStartRefresh)
    Loop50.addData('maskLeft_3.stopped', maskLeft_3.tStopRefresh)
    Cue_3.stop()  # ensure sound has stopped at end of routine
    # the Routine "Validity50Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response50"-------
    continueRoutine = True
    # update component parameters for each repeat
    response_3.keys = []
    response_3.rt = []
    _response_3_allKeys = []
    # keep track of which components have finished
    Response50Components = [response_3, fixation_response_3]
    for thisComponent in Response50Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response50Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response50"-------
    while continueRoutine:
        # get current time
        t = Response50Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response50Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response_3* updates
        waitOnFlip = False
        if response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_3.frameNStart = frameN  # exact frame index
            response_3.tStart = t  # local t and not account for scr refresh
            response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_3, 'tStartRefresh')  # time at next scr refresh
            response_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_3.status == STARTED and not waitOnFlip:
            theseKeys = response_3.getKeys(keyList=['left', 'right'], waitRelease=False)
            _response_3_allKeys.extend(theseKeys)
            if len(_response_3_allKeys):
                response_3.keys = _response_3_allKeys[-1].name  # just the last key pressed
                response_3.rt = _response_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *fixation_response_3* updates
        if fixation_response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_response_3.frameNStart = frameN  # exact frame index
            fixation_response_3.tStart = t  # local t and not account for scr refresh
            fixation_response_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_response_3, 'tStartRefresh')  # time at next scr refresh
            fixation_response_3.setAutoDraw(True)
        if fixation_response_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_response_3.tStartRefresh + 2+currentDur+durMask+0.0001-frameTolerance:
                # keep track of stop time/frame for later
                fixation_response_3.tStop = t  # not accounting for scr refresh
                fixation_response_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_response_3, 'tStopRefresh')  # time at next scr refresh
                fixation_response_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response50Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response50"-------
    for thisComponent in Response50Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if targetPos[1]>0:
        if response_3.keys=='right':
            feedback="Doğru"
            accuracy.append(1)
            Loop50.addData('Accuracy', 1)
        elif response_3.keys=='left':
            feedback="Yanlış"
            accuracy.append(0)
            Loop50.addData('Accuracy', 0)
            
    elif targetPos[1]<0:
        if response_3.keys=='left':
            feedback="Doğru"
            accuracy.append(1)
            Loop50.addData('Accuracy', 1)
        elif response_3.keys=='right':
            feedback="Yanlış"
            accuracy.append(0)
            Loop50.addData('Accuracy', 0)
            
               
    # the Routine "Response50" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback50"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedBackScreen_3.setText(feedback)
    Loop50.addData('TargetDuration', currentDur*frameDur)
    
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
        Loop50.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
        Loop50.addData('congruentTrialDuration', congDur[trialNumLoop100])
    
    elif cueFile[7:11] not in targetFile[7:11]:
        trialCongruency="incongruent"
        incongDur.append(target.tStopRefresh-target.tStartRefresh)
        congDur.append(None)
        Loop50.addData('congruentTrialDuration', congDur[trialNumLoop100])
        Loop50.addData('incongruentTrialDuration', incongDur[trialNumLoop100])
                
    
    Loop50.addData('isCongruent', trialCongruency)
    trialNumLoop100=trialNumLoop100+1
    
    # keep track of which components have finished
    Feedback50Components = [feedBackScreen_3]
    for thisComponent in Feedback50Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback50Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback50"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback50Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback50Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedBackScreen_3* updates
        if feedBackScreen_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedBackScreen_3.frameNStart = frameN  # exact frame index
            feedBackScreen_3.tStart = t  # local t and not account for scr refresh
            feedBackScreen_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedBackScreen_3, 'tStartRefresh')  # time at next scr refresh
            feedBackScreen_3.setAutoDraw(True)
        if feedBackScreen_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedBackScreen_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedBackScreen_3.tStop = t  # not accounting for scr refresh
                feedBackScreen_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedBackScreen_3, 'tStopRefresh')  # time at next scr refresh
                feedBackScreen_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback50Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback50"-------
    for thisComponent in Feedback50Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Loop50'


# ------Prepare to start Routine "InstructionNeutral"-------
continueRoutine = True
# update component parameters for each repeat
basla_butonu_4.keys = []
basla_butonu_4.rt = []
_basla_butonu_4_allKeys = []
# keep track of which components have finished
InstructionNeutralComponents = [Instrcution100_4, basla_butonu_4]
for thisComponent in InstructionNeutralComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionNeutralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionNeutral"-------
while continueRoutine:
    # get current time
    t = InstructionNeutralClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionNeutralClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrcution100_4* updates
    if Instrcution100_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrcution100_4.frameNStart = frameN  # exact frame index
        Instrcution100_4.tStart = t  # local t and not account for scr refresh
        Instrcution100_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrcution100_4, 'tStartRefresh')  # time at next scr refresh
        Instrcution100_4.setAutoDraw(True)
    
    # *basla_butonu_4* updates
    if basla_butonu_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        basla_butonu_4.frameNStart = frameN  # exact frame index
        basla_butonu_4.tStart = t  # local t and not account for scr refresh
        basla_butonu_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(basla_butonu_4, 'tStartRefresh')  # time at next scr refresh
        basla_butonu_4.status = STARTED
        # keyboard checking is just starting
        basla_butonu_4.clock.reset()  # now t=0
        basla_butonu_4.clearEvents(eventType='keyboard')
    if basla_butonu_4.status == STARTED:
        theseKeys = basla_butonu_4.getKeys(keyList=['space'], waitRelease=False)
        _basla_butonu_4_allKeys.extend(theseKeys)
        if len(_basla_butonu_4_allKeys):
            basla_butonu_4.keys = _basla_butonu_4_allKeys[-1].name  # just the last key pressed
            basla_butonu_4.rt = _basla_butonu_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionNeutralComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionNeutral"-------
for thisComponent in InstructionNeutralComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if basla_butonu_4.keys in ['', [], None]:  # No response was made
    basla_butonu_4.keys = None
thisExp.addData('basla_butonu_4.keys',basla_butonu_4.keys)
if basla_butonu_4.keys != None:  # we had a response
    thisExp.addData('basla_butonu_4.rt', basla_butonu_4.rt)
thisExp.nextEntry()
# the Routine "InstructionNeutral" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
