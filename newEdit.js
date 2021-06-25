/******************************* 
 * Audiovisualexpectation Test *
 *******************************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'AudioVisualExpectation';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Instruction_DeneyRoutineBegin());
flowScheduler.add(Instruction_DeneyRoutineEachFrame());
flowScheduler.add(Instruction_DeneyRoutineEnd());
const denemeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(denemeLoopBegin, denemeLoopScheduler);
flowScheduler.add(denemeLoopScheduler);
flowScheduler.add(denemeLoopEnd);
flowScheduler.add(Instruction100RoutineBegin());
flowScheduler.add(Instruction100RoutineEachFrame());
flowScheduler.add(Instruction100RoutineEnd());
const Loop100LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Loop100LoopBegin, Loop100LoopScheduler);
flowScheduler.add(Loop100LoopScheduler);
flowScheduler.add(Loop100LoopEnd);
flowScheduler.add(Instruction75RoutineBegin());
flowScheduler.add(Instruction75RoutineEachFrame());
flowScheduler.add(Instruction75RoutineEnd());
const Loop75LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Loop75LoopBegin, Loop75LoopScheduler);
flowScheduler.add(Loop75LoopScheduler);
flowScheduler.add(Loop75LoopEnd);
flowScheduler.add(Instruction50RoutineBegin());
flowScheduler.add(Instruction50RoutineEachFrame());
flowScheduler.add(Instruction50RoutineEnd());
const Loop50LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Loop50LoopBegin, Loop50LoopScheduler);
flowScheduler.add(Loop50LoopScheduler);
flowScheduler.add(Loop50LoopEnd);
flowScheduler.add(InstructionNeutralRoutineBegin());
flowScheduler.add(InstructionNeutralRoutineEachFrame());
flowScheduler.add(InstructionNeutralRoutineEnd());
const LoopNeutralLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LoopNeutralLoopBegin, LoopNeutralLoopScheduler);
flowScheduler.add(LoopNeutralLoopScheduler);
flowScheduler.add(LoopNeutralLoopEnd);
flowScheduler.add(end_of_expRoutineBegin());
flowScheduler.add(end_of_expRoutineEachFrame());
flowScheduler.add(end_of_expRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'images/women_03_puzzle.png', 'path': 'images/women_03_puzzle.png'},
    {'name': 'images/malem_03.png', 'path': 'images/malem_03.png'},
    {'name': 'images/ancat_03.png', 'path': 'images/ancat_03.png'},
    {'name': 'images/andog_04.png', 'path': 'images/andog_04.png'},
    {'name': 'images/andog_04_puzzle.png', 'path': 'images/andog_04_puzzle.png'},
    {'name': 'images/malem_05_puzzle.png', 'path': 'images/malem_05_puzzle.png'},
    {'name': 'Sounds/women_01.wav', 'path': 'Sounds/women_01.wav'},
    {'name': 'images/women_04_puzzle.png', 'path': 'images/women_04_puzzle.png'},
    {'name': 'images/andog_02_puzzle.png', 'path': 'images/andog_02_puzzle.png'},
    {'name': 'images/malem_04_puzzle.png', 'path': 'images/malem_04_puzzle.png'},
    {'name': 'images/malem_05.png', 'path': 'images/malem_05.png'},
    {'name': 'images/andog_01_puzzle.png', 'path': 'images/andog_01_puzzle.png'},
    {'name': 'congruent50.xlsx', 'path': 'congruent50.xlsx'},
    {'name': 'c_neutral.xlsx', 'path': 'c_neutral.xlsx'},
    {'name': 'images/women_02_puzzle.png', 'path': 'images/women_02_puzzle.png'},
    {'name': 'images/women_01.png', 'path': 'images/women_01.png'},
    {'name': 'congruent75.xlsx', 'path': 'congruent75.xlsx'},
    {'name': 'images/ancat_04_puzzle.png', 'path': 'images/ancat_04_puzzle.png'},
    {'name': 'images/malem_02.png', 'path': 'images/malem_02.png'},
    {'name': 'images/women_01_puzzle.png', 'path': 'images/women_01_puzzle.png'},
    {'name': 'images/ancat_05.png', 'path': 'images/ancat_05.png'},
    {'name': 'images/malem_03_puzzle.png', 'path': 'images/malem_03_puzzle.png'},
    {'name': 'images/malem_01_puzzle.png', 'path': 'images/malem_01_puzzle.png'},
    {'name': 'images/women_05_puzzle.png', 'path': 'images/women_05_puzzle.png'},
    {'name': 'images/ancat_05_puzzle.png', 'path': 'images/ancat_05_puzzle.png'},
    {'name': 'Sounds/andog_01.wav', 'path': 'Sounds/andog_01.wav'},
    {'name': 'images/women_04.png', 'path': 'images/women_04.png'},
    {'name': 'images/andog_05.png', 'path': 'images/andog_05.png'},
    {'name': 'images/andog_05_puzzle.png', 'path': 'images/andog_05_puzzle.png'},
    {'name': 'images/malem_02_puzzle.png', 'path': 'images/malem_02_puzzle.png'},
    {'name': 'Sounds/ancat_01.wav', 'path': 'Sounds/ancat_01.wav'},
    {'name': 'images/andog_03.png', 'path': 'images/andog_03.png'},
    {'name': 'Sounds/malem_01.wav', 'path': 'Sounds/malem_01.wav'},
    {'name': 'images/ancat_01_puzzle.png', 'path': 'images/ancat_01_puzzle.png'},
    {'name': 'images/women_05.png', 'path': 'images/women_05.png'},
    {'name': 'congruent100.xlsx', 'path': 'congruent100.xlsx'},
    {'name': 'images/ancat_02_puzzle.png', 'path': 'images/ancat_02_puzzle.png'},
    {'name': 'images/andog_01.png', 'path': 'images/andog_01.png'},
    {'name': 'images/ancat_02.png', 'path': 'images/ancat_02.png'},
    {'name': 'images/malem_01.png', 'path': 'images/malem_01.png'},
    {'name': 'images/ancat_03_puzzle.png', 'path': 'images/ancat_03_puzzle.png'},
    {'name': 'images/ancat_04.png', 'path': 'images/ancat_04.png'},
    {'name': 'images/andog_02.png', 'path': 'images/andog_02.png'},
    {'name': 'images/ancat_01.png', 'path': 'images/ancat_01.png'},
    {'name': 'images/women_02.png', 'path': 'images/women_02.png'},
    {'name': 'images/andog_03_puzzle.png', 'path': 'images/andog_03_puzzle.png'},
    {'name': 'images/malem_04.png', 'path': 'images/malem_04.png'},
    {'name': 'images/women_03.png', 'path': 'images/women_03.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var Instruction_DeneyClock;
var basla_butonu_6;
var genel_instruction;
var Validity100TrialClock;
var targetPos;
var targetDur;
var currentDur;
var accuracy;
var durMask;
var target;
var distractor;
var maskLeft;
var maskRight;
var Cue;
var fixation;
var Response100Clock;
var response_2;
var feedback;
var fixation_response_2;
var Feedback100Clock;
var feedBackScreen;
var trialNumLoop100;
var numStaricase;
var trialCongruency;
var congDur;
var incongDur;
var Instruction100Clock;
var Instrcution100;
var basla_butonu;
var Instruction75Clock;
var Instrcution100_2;
var basla_butonu_2;
var Validity75TrialClock;
var target_2;
var distractor_2;
var maskLeft_2;
var maskRight_2;
var Cue_2;
var fixation_2;
var Response75Clock;
var response;
var fixation_response;
var Feedback75Clock;
var feedBackScreen_2;
var Instruction50Clock;
var Instrcution100_3;
var basla_butonu_3;
var Validity50TrialClock;
var target_3;
var distractor_3;
var maskLeft_3;
var maskRight_3;
var Cue_3;
var fixation_3;
var Response50Clock;
var response_3;
var fixation_response_3;
var Feedback50Clock;
var feedBackScreen_3;
var InstructionNeutralClock;
var Instrcution100_4;
var basla_butonu_4;
var NeutralTrialClock;
var target_4;
var distractor_4;
var maskLeft_4;
var maskRight_4;
var fixation_4;
var ResponseNeutralClock;
var response_4;
var fixation_response_4;
var FeedbackNeutralClock;
var feedBackScreen_4;
var end_of_expClock;
var Instrcution100_5;
var basla_butonu_5;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Instruction_Deney"
  Instruction_DeneyClock = new util.Clock();
  basla_butonu_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  genel_instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'genel_instruction',
    text: 'Deneyimize katıldığınız için teşekkür ederiz. Birazdan başlayacak olan deney her biri 4 aşamadan oluşan testler halindedir. Bu aşamalar %100 uyumlu (60 test), %75 uyumlu (240 test), %50 uyumlu (240 test) ve nötr (işitsel ipucunun bulunmadığı durum, 60 test) şeklinde karışık bir şekilde karşınıza çıkacaktır. Deney süresince toplam 600 teste maruz kalacaksınız. \nÖncelikle testler boyunca sizden ekranın ortasında duran sabit noktaya bakmanızı isteyeceğiz. \nBu deneyde ilk olarak 2 saniye boyunca erkek, kadın, kedi veya köpek seslerinden birini duyacaksınız. Hemen ardından çok çok kısa bir süre içinde ekranın bir tarafında düzgün bir resim diğer tarafında ise düzgün olmayan puzzle halinde parçalara ayrılıp karıştırılmış bir resim göreceksiniz. Çok kısa süren bu kısımın ardından tekrar çok çok kısa bir süre için (64 milisaniye) ekranın her iki tarafında puzzle halindeki resimleri göreceksiniz. Bu resimler az önce görmüş olduğunuz resimler ile aynı olacaktır. Ardından boş ekran gelecek ve sizden mümkün olduğunca hızlı bir şekilde ilk gördüğünüz düzgün resmin ekranın hangi tarafında olduğunu belirtmeniz istenecektir. Örneğin: düzgün olan resmi ekranın sağ tarafında gördüyseniz sağ tuşa basınız. Bir sonraki ekranda ise verdiğiniz cevabın doğruluğu ile ilgili bilgiyi göreceksiniz. Bu bilgiyi gördükten sonra hemen otomatik olarak aynı sürece devam edeceksiniz.\nTüm testler sona erdikten sonra ekranda deneyin bittiğine dair bir yazı çıkacaktır. Hazır olduğunuzda space(boşluk) tuşu ile deneme testine geçebiliriz.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Validity100Trial"
  Validity100TrialClock = new util.Clock();
  function shuffle(a) {
      var j, x, i;
      for (i = a.length - 1; i > 0; i--) {
          j = Math.floor(Math.random() * (i + 1));
          x = a[i];
          a[i] = a[j];
          a[j] = x;
      }
      return a;
  }
  
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
  
          targetPos = [0.4, (- 0.4)];
  targetDur = list([1, 2, 3, 4, 5]);
 // currentDur = np.random.choice(targetDur);
 shuffle(targetPos);
  accuracy = [];
  durMask = 4;
  
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  distractor = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  maskLeft = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskLeft', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  maskRight = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskRight', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  Cue = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 2.0,
    });
  Cue.setVolume(1.0);
  fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "Response100"
  Response100Clock = new util.Clock();
  response_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  feedback = "";
  
  fixation_response_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_response_2', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "Feedback100"
  Feedback100Clock = new util.Clock();
  feedBackScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedBackScreen',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  trialNumLoop100 = 0;
  numStaricase = 30;
  trialCongruency = "";
  congDur = [];
  incongDur = [];
  
  // Initialize components for Routine "Instruction100"
  Instruction100Clock = new util.Clock();
  Instrcution100 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrcution100',
    text: '1.Aşama: (%100 UYUMLU) Bu aşamadaki duyacağınız tüm sesler ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  basla_butonu = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Validity100Trial"
  Validity100TrialClock = new util.Clock();

  
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
  
          targetPos = [0.4, (- 0.4)];
  targetDur = list([1, 2, 3, 4, 5]);
  //currentDur = np.random.choice(targetDur);
  shuffle(targetPos);
  accuracy = [];
  durMask = 4;
  
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  distractor = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  maskLeft = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskLeft', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  maskRight = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskRight', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  Cue = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 2.0,
    });
  Cue.setVolume(1.0);
  fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  // Initialize components for Routine "Response100"
  Response100Clock = new util.Clock();
  response_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  feedback = "";
  
  fixation_response_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_response_2', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "Feedback100"
  Feedback100Clock = new util.Clock();
  feedBackScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedBackScreen',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  trialNumLoop100 = 0;
  numStaricase = 30;
  trialCongruency = "";
  congDur = [];
  incongDur = [];
  
  // Initialize components for Routine "Instruction75"
  Instruction75Clock = new util.Clock();
  Instrcution100_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrcution100_2',
    text: '2.Aşama(%75 UYUMLU): Bu aşamadaki duyacağınız seslerin %75’i ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız %75 ihtimalle kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  basla_butonu_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Validity75Trial"
  Validity75TrialClock = new util.Clock();
  
  targetPos = [0.4, (- 0.4)];
  targetDur = list([1, 2, 3, 4, 5]);
  //currentDur = np.random.choice(targetDur);
  shuffle(targetPos);

  var index = Math.floor(Math.random() * targetDur.length);
    currentDur=targetDur[index];  
  accuracy = [];
  durMask = 4;

  target_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  distractor_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  maskLeft_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskLeft_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  maskRight_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskRight_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Cue_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 2.0,
    });
  Cue_2.setVolume(1.0);
  fixation_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_2', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "Response75"
  Response75Clock = new util.Clock();
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  /* Syntax Error: Fix Python code */
  fixation_response = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_response', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "Feedback75"
  Feedback75Clock = new util.Clock();
  feedBackScreen_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedBackScreen_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "Instruction50"
  Instruction50Clock = new util.Clock();
  Instrcution100_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrcution100_3',
    text: '3.Aşama (%50 UYUMLU): Bu aşamadaki duyacağınız seslerin %50’si ile resimler birbiri ile uyumludur. Yani örneğin eğer bir kedi sesi duyduysanız %50 ihtimalle kedi resmi ile karşılaşacaksınız. Düzgün resmin olduğu tarafı hızlıca belirtiniz. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  basla_butonu_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Validity50Trial"
  Validity50TrialClock = new util.Clock();
  targetPos = [0.4, (- 0.4)];
  targetDur = list([1, 2, 3, 4, 5]);
  //currentDur = np.random.choice(targetDur);
  shuffle(targetPos);

  var index = Math.floor(Math.random() * targetDur.length);
    currentDur=targetDur[index];  
  accuracy = [];
  durMask = 4;
  target_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  distractor_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  maskLeft_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskLeft_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  maskRight_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskRight_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Cue_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 2.0,
    });
  Cue_3.setVolume(1.0);
  fixation_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_3', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "Response50"
  Response50Clock = new util.Clock();
  response_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  /* Syntax Error: Fix Python code */
  fixation_response_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_response_3', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "Feedback50"
  Feedback50Clock = new util.Clock();
  feedBackScreen_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedBackScreen_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "InstructionNeutral"
  InstructionNeutralClock = new util.Clock();
  Instrcution100_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrcution100_4',
    text: '4.Aşama (Nötr): Bu son aşamadır. Bu aşamada herhangi bir ses duymayacaksınız. Yalnızca önceki aşamalarda olduğu gibi düzgün resmin olduğu tarafı bulmaya çalışınız. Hazır olduğunuzda space(boşluk) tuşu ile devam edebiliriz.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  basla_butonu_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NeutralTrial"
  NeutralTrialClock = new util.Clock();
  targetPos = [0.4, (- 0.4)];
  targetDur = list([1, 2, 3, 4, 5]);
  //currentDur = np.random.choice(targetDur);
  shuffle(targetPos);

  var index = Math.floor(Math.random() * targetDur.length);
    currentDur=targetDur[index];  
  accuracy = [];
  durMask = 4;
  target_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  distractor_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor_4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  maskLeft_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskLeft_4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  maskRight_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'maskRight_4', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  fixation_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_4', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  // Initialize components for Routine "ResponseNeutral"
  ResponseNeutralClock = new util.Clock();
  response_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  /* Syntax Error: Fix Python code */
  fixation_response_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_response_4', 
    vertices: 'cross', size:[0.01, 0.01],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "FeedbackNeutral"
  FeedbackNeutralClock = new util.Clock();
  feedBackScreen_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedBackScreen_4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "end_of_exp"
  end_of_expClock = new util.Clock();
  Instrcution100_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instrcution100_5',
    text: 'Any text\n\nincluding line breaks',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  basla_butonu_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _basla_butonu_6_allKeys;
var Instruction_DeneyComponents;
function Instruction_DeneyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instruction_Deney'-------
    t = 0;
    Instruction_DeneyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu_6.keys = undefined;
    basla_butonu_6.rt = undefined;
    _basla_butonu_6_allKeys = [];
    // keep track of which components have finished
    Instruction_DeneyComponents = [];
    Instruction_DeneyComponents.push(basla_butonu_6);
    Instruction_DeneyComponents.push(genel_instruction);
    
    for (const thisComponent of Instruction_DeneyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction_DeneyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instruction_Deney'-------
    // get current time
    t = Instruction_DeneyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *basla_butonu_6* updates
    if (t >= 0.0 && basla_butonu_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu_6.tStart = t;  // (not accounting for frame time here)
      basla_butonu_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu_6.clock.reset();
      basla_butonu_6.start();
      basla_butonu_6.clearEvents();
    }

    if (basla_butonu_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu_6.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_6_allKeys = _basla_butonu_6_allKeys.concat(theseKeys);
      if (_basla_butonu_6_allKeys.length > 0) {
        basla_butonu_6.keys = _basla_butonu_6_allKeys[_basla_butonu_6_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu_6.rt = _basla_butonu_6_allKeys[_basla_butonu_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *genel_instruction* updates
    if (t >= 0.0 && genel_instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      genel_instruction.tStart = t;  // (not accounting for frame time here)
      genel_instruction.frameNStart = frameN;  // exact frame index
      
      genel_instruction.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction_DeneyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction_DeneyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instruction_Deney'-------
    for (const thisComponent of Instruction_DeneyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu_6.keys', basla_butonu_6.keys);
    if (typeof basla_butonu_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu_6.rt', basla_butonu_6.rt);
        routineTimer.reset();
        }
    
    basla_butonu_6.stop();
    // the Routine "Instruction_Deney" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var deneme;
var currentLoop;
function denemeLoopBegin(denemeLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  deneme = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'congruent100.xlsx', '0:4'),
    seed: undefined, name: 'deneme'
  });
  psychoJS.experiment.addLoop(deneme); // add the loop to the experiment
  currentLoop = deneme;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisDeneme of deneme) {
    const snapshot = deneme.getSnapshot();
    denemeLoopScheduler.add(importConditions(snapshot));
    denemeLoopScheduler.add(Validity100TrialRoutineBegin(snapshot));
    denemeLoopScheduler.add(Validity100TrialRoutineEachFrame(snapshot));
    denemeLoopScheduler.add(Validity100TrialRoutineEnd(snapshot));
    denemeLoopScheduler.add(Response100RoutineBegin(snapshot));
    denemeLoopScheduler.add(Response100RoutineEachFrame(snapshot));
    denemeLoopScheduler.add(Response100RoutineEnd(snapshot));
    denemeLoopScheduler.add(Feedback100RoutineBegin(snapshot));
    denemeLoopScheduler.add(Feedback100RoutineEachFrame(snapshot));
    denemeLoopScheduler.add(Feedback100RoutineEnd(snapshot));
    denemeLoopScheduler.add(endLoopIteration(denemeLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function denemeLoopEnd() {
  psychoJS.experiment.removeLoop(deneme);

  return Scheduler.Event.NEXT;
}


var Loop100;
function Loop100LoopBegin(Loop100LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Loop100 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'congruent100.xlsx',
    seed: undefined, name: 'Loop100'
  });
  psychoJS.experiment.addLoop(Loop100); // add the loop to the experiment
  currentLoop = Loop100;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoop100 of Loop100) {
    const snapshot = Loop100.getSnapshot();
    Loop100LoopScheduler.add(importConditions(snapshot));
    Loop100LoopScheduler.add(Validity100TrialRoutineBegin(snapshot));
    Loop100LoopScheduler.add(Validity100TrialRoutineEachFrame(snapshot));
    Loop100LoopScheduler.add(Validity100TrialRoutineEnd(snapshot));
    Loop100LoopScheduler.add(Response100RoutineBegin(snapshot));
    Loop100LoopScheduler.add(Response100RoutineEachFrame(snapshot));
    Loop100LoopScheduler.add(Response100RoutineEnd(snapshot));
    Loop100LoopScheduler.add(Feedback100RoutineBegin(snapshot));
    Loop100LoopScheduler.add(Feedback100RoutineEachFrame(snapshot));
    Loop100LoopScheduler.add(Feedback100RoutineEnd(snapshot));
    Loop100LoopScheduler.add(endLoopIteration(Loop100LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function Loop100LoopEnd() {
  psychoJS.experiment.removeLoop(Loop100);

  return Scheduler.Event.NEXT;
}


var Loop75;
function Loop75LoopBegin(Loop75LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Loop75 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'congruent75.xlsx',
    seed: undefined, name: 'Loop75'
  });
  psychoJS.experiment.addLoop(Loop75); // add the loop to the experiment
  currentLoop = Loop75;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoop75 of Loop75) {
    const snapshot = Loop75.getSnapshot();
    Loop75LoopScheduler.add(importConditions(snapshot));
    Loop75LoopScheduler.add(Validity75TrialRoutineBegin(snapshot));
    Loop75LoopScheduler.add(Validity75TrialRoutineEachFrame(snapshot));
    Loop75LoopScheduler.add(Validity75TrialRoutineEnd(snapshot));
    Loop75LoopScheduler.add(Response75RoutineBegin(snapshot));
    Loop75LoopScheduler.add(Response75RoutineEachFrame(snapshot));
    Loop75LoopScheduler.add(Response75RoutineEnd(snapshot));
    Loop75LoopScheduler.add(Feedback75RoutineBegin(snapshot));
    Loop75LoopScheduler.add(Feedback75RoutineEachFrame(snapshot));
    Loop75LoopScheduler.add(Feedback75RoutineEnd(snapshot));
    Loop75LoopScheduler.add(endLoopIteration(Loop75LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function Loop75LoopEnd() {
  psychoJS.experiment.removeLoop(Loop75);

  return Scheduler.Event.NEXT;
}


var Loop50;
function Loop50LoopBegin(Loop50LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Loop50 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'congruent50.xlsx',
    seed: undefined, name: 'Loop50'
  });
  psychoJS.experiment.addLoop(Loop50); // add the loop to the experiment
  currentLoop = Loop50;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoop50 of Loop50) {
    const snapshot = Loop50.getSnapshot();
    Loop50LoopScheduler.add(importConditions(snapshot));
    Loop50LoopScheduler.add(Validity50TrialRoutineBegin(snapshot));
    Loop50LoopScheduler.add(Validity50TrialRoutineEachFrame(snapshot));
    Loop50LoopScheduler.add(Validity50TrialRoutineEnd(snapshot));
    Loop50LoopScheduler.add(Response50RoutineBegin(snapshot));
    Loop50LoopScheduler.add(Response50RoutineEachFrame(snapshot));
    Loop50LoopScheduler.add(Response50RoutineEnd(snapshot));
    Loop50LoopScheduler.add(Feedback50RoutineBegin(snapshot));
    Loop50LoopScheduler.add(Feedback50RoutineEachFrame(snapshot));
    Loop50LoopScheduler.add(Feedback50RoutineEnd(snapshot));
    Loop50LoopScheduler.add(endLoopIteration(Loop50LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function Loop50LoopEnd() {
  psychoJS.experiment.removeLoop(Loop50);

  return Scheduler.Event.NEXT;
}


var LoopNeutral;
function LoopNeutralLoopBegin(LoopNeutralLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  LoopNeutral = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'c_neutral.xlsx',
    seed: undefined, name: 'LoopNeutral'
  });
  psychoJS.experiment.addLoop(LoopNeutral); // add the loop to the experiment
  currentLoop = LoopNeutral;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoopNeutral of LoopNeutral) {
    const snapshot = LoopNeutral.getSnapshot();
    LoopNeutralLoopScheduler.add(importConditions(snapshot));
    LoopNeutralLoopScheduler.add(NeutralTrialRoutineBegin(snapshot));
    LoopNeutralLoopScheduler.add(NeutralTrialRoutineEachFrame(snapshot));
    LoopNeutralLoopScheduler.add(NeutralTrialRoutineEnd(snapshot));
    LoopNeutralLoopScheduler.add(ResponseNeutralRoutineBegin(snapshot));
    LoopNeutralLoopScheduler.add(ResponseNeutralRoutineEachFrame(snapshot));
    LoopNeutralLoopScheduler.add(ResponseNeutralRoutineEnd(snapshot));
    LoopNeutralLoopScheduler.add(FeedbackNeutralRoutineBegin(snapshot));
    LoopNeutralLoopScheduler.add(FeedbackNeutralRoutineEachFrame(snapshot));
    LoopNeutralLoopScheduler.add(FeedbackNeutralRoutineEnd(snapshot));
    LoopNeutralLoopScheduler.add(endLoopIteration(LoopNeutralLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function LoopNeutralLoopEnd() {
  psychoJS.experiment.removeLoop(LoopNeutral);

  return Scheduler.Event.NEXT;
}


var Validity100TrialComponents;
function Validity100TrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Validity100Trial'-------
    t = 0;
    Validity100TrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    shuffle(targetPos);
    
    target.setPos([targetPos[1], 0]);
    target.setImage(targetFile);
    distractor.setPos([(- targetPos[1]), 0]);
    distractor.setImage(maskFile);
    maskLeft.setPos([(- 0.4), 0]);
    maskLeft.setImage(maskFile);
    maskRight.setPos([0.4, 0]);
    maskRight.setImage(maskFile);
    Cue = new sound.Sound({
    win: psychoJS.window,
    value: cueFile,
    secs: 2.0,
    });
    Cue.secs=2.0;
    Cue.setVolume(1.0);
    // keep track of which components have finished
    Validity100TrialComponents = [];
    Validity100TrialComponents.push(target);
    Validity100TrialComponents.push(distractor);
    Validity100TrialComponents.push(maskLeft);
    Validity100TrialComponents.push(maskRight);
    Validity100TrialComponents.push(Cue);
    Validity100TrialComponents.push(fixation);
    
    for (const thisComponent of Validity100TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Validity100TrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Validity100Trial'-------
    // get current time
    t = Validity100TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target* updates
    if (t >= 2.0 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      //target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      target.tStartRefresh =target.frameNStart*frameDur ;
      target.setAutoDraw(true);
    }

    frameRemains = 2.0 + currentDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        //target.tStop = t; 
        target.frameNStop = frameN;
        target.tStopRefresh =target.frameNStop*frameDur ;
      target.setAutoDraw(false);
    }
    
    // *distractor* updates
    if (t >= 2.0 && distractor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor.tStart = t;  // (not accounting for frame time here)
      distractor.frameNStart = frameN;  // exact frame index
      
      distractor.setAutoDraw(true);
    }

    if (distractor.status === PsychoJS.Status.STARTED && frameN >= (distractor.frameNStart + currentDur)) {
      distractor.setAutoDraw(false);
    }
    
    // *maskLeft* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskLeft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskLeft.tStart = t;  // (not accounting for frame time here)
      maskLeft.frameNStart = frameN;  // exact frame index
      
      maskLeft.setAutoDraw(true);
    }

    if (maskLeft.status === PsychoJS.Status.STARTED && frameN >= (maskLeft.frameNStart + durMask)) {
      maskLeft.setAutoDraw(false);
    }
    
    // *maskRight* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskRight.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskRight.tStart = t;  // (not accounting for frame time here)
      maskRight.frameNStart = frameN;  // exact frame index
      
      maskRight.setAutoDraw(true);
    }

    if (maskRight.status === PsychoJS.Status.STARTED && frameN >= (maskRight.frameNStart + durMask)) {
      maskRight.setAutoDraw(false);
    }
    // start/stop Cue
    if (t >= 0.0 && Cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cue.tStart = t;  // (not accounting for frame time here)
      Cue.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Cue.play(); });  // screen flip
      Cue.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2.0 > 0.5) {  Cue.stop();  // stop the sound (if longer than duration)
        Cue.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    if (fixation.status === PsychoJS.Status.STARTED && frameN >= (fixation.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001)) {
      fixation.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Validity100TrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Validity100TrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Validity100Trial'-------
    for (const thisComponent of Validity100TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Cue.stop();  // ensure sound has stopped at end of routine
    // the Routine "Validity100Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _response_2_allKeys;
var Response100Components;
function Response100RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Response100'-------
    t = 0;
    Response100Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    response_2.keys = undefined;
    response_2.rt = undefined;
    _response_2_allKeys = [];
    // keep track of which components have finished
    Response100Components = [];
    Response100Components.push(response_2);
    Response100Components.push(fixation_response_2);
    
    for (const thisComponent of Response100Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Response100RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Response100'-------
    // get current time
    t = Response100Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response_2* updates
    if (t >= 0.0 && response_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_2.tStart = t;  // (not accounting for frame time here)
      response_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response_2.clearEvents(); });
    }

    if (response_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = response_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _response_2_allKeys = _response_2_allKeys.concat(theseKeys);
      if (_response_2_allKeys.length > 0) {
        response_2.keys = _response_2_allKeys[_response_2_allKeys.length - 1].name;  // just the last key pressed
        response_2.rt = _response_2_allKeys[_response_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation_response_2* updates
    if (t >= 0.0 && fixation_response_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_response_2.tStart = t;  // (not accounting for frame time here)
      fixation_response_2.frameNStart = frameN;  // exact frame index
      
      fixation_response_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2+currentDur+durMask+0.0001 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_response_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_response_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Response100Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Response100RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Response100'-------
    for (const thisComponent of Response100Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    response_2.stop();
    if ((targetPos[1] > 0)) {
        if ((response_2.keys === "right")) {
            feedback = "Do\u011fru";
            accuracy.push(1);
            deneme.addData("Accuracy", 1);
        } else {
            if ((response_2.keys === "left")) {
                feedback = "Yanl\u0131\u015f";
                accuracy.push(0);
                deneme.addData("Accuracy", 0);
            }
        }
    } else {
        if ((targetPos[1] < 0)) {
            if ((response_2.keys === "left")) {
                feedback = "Do\u011fru";
                accuracy.push(1);
                deneme.addData("Accuracy", 1);
            } else {
                if ((response_2.keys === "right")) {
                    feedback = "Yanl\u0131\u015f";
                    accuracy.push(0);
                    deneme.addData("Accuracy", 0);
                }
            }
        }
    }
    
    // the Routine "Response100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var Feedback100Components;
function Feedback100RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback100'-------
    t = 0;
    Feedback100Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    feedBackScreen.setText(feedback);
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    deneme.addData("TargetDuration", (currentDur * frameDur));
    if ((accuracy.slice((- 1))[0] === 0)) {
        currentDur = (currentDur + 1);
    } else {
        if (((currentDur > 1) && (accuracy.length >= 2))) {
            if (((accuracy.slice((- 1))[0] === 1) && (accuracy.slice((- 2))[0] === 1))) {
                currentDur = (currentDur - 1);
            }
        } else {
            currentDur = currentDur;
        }
    }
    if (_pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11))) {
        trialCongruency = "congruent";
        congDur.push((target.tStopRefresh - target.tStartRefresh));
        incongDur.push(NaN);
        deneme.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        deneme.addData("congruentTrialDuration", congDur[trialNumLoop100]);
    } else {
        if ((! _pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11)))) {
            trialCongruency = "incongruent";
            incongDur.push((target.tStopRefresh - target.tStartRefresh));
            congDur.push(NaN);
            deneme.addData("congruentTrialDuration", congDur[trialNumLoop100]);
            deneme.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        }
    }
    deneme.addData("isCongruent", trialCongruency);
    trialNumLoop100 = (trialNumLoop100 + 1);
    
    // keep track of which components have finished
    Feedback100Components = [];
    Feedback100Components.push(feedBackScreen);
    
    for (const thisComponent of Feedback100Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Feedback100RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Feedback100'-------
    // get current time
    t = Feedback100Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedBackScreen* updates
    if (t >= 0.0 && feedBackScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedBackScreen.tStart = t;  // (not accounting for frame time here)
      feedBackScreen.frameNStart = frameN;  // exact frame index
      
      feedBackScreen.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedBackScreen.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedBackScreen.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Feedback100Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Feedback100RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Feedback100'-------
    for (const thisComponent of Feedback100Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Feedback100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _basla_butonu_allKeys;
var Instruction100Components;
function Instruction100RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instruction100'-------
    t = 0;
    Instruction100Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu.keys = undefined;
    basla_butonu.rt = undefined;
    _basla_butonu_allKeys = [];
    // keep track of which components have finished
    Instruction100Components = [];
    Instruction100Components.push(Instrcution100);
    Instruction100Components.push(basla_butonu);
    
    for (const thisComponent of Instruction100Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction100RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instruction100'-------
    // get current time
    t = Instruction100Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instrcution100* updates
    if (t >= 0.0 && Instrcution100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instrcution100.tStart = t;  // (not accounting for frame time here)
      Instrcution100.frameNStart = frameN;  // exact frame index
      
      Instrcution100.setAutoDraw(true);
    }

    
    // *basla_butonu* updates
    if (t >= 0.0 && basla_butonu.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu.tStart = t;  // (not accounting for frame time here)
      basla_butonu.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu.clock.reset();
      basla_butonu.start();
      basla_butonu.clearEvents();
    }

    if (basla_butonu.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_allKeys = _basla_butonu_allKeys.concat(theseKeys);
      if (_basla_butonu_allKeys.length > 0) {
        basla_butonu.keys = _basla_butonu_allKeys[_basla_butonu_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu.rt = _basla_butonu_allKeys[_basla_butonu_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction100Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction100RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instruction100'-------
    for (const thisComponent of Instruction100Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu.keys', basla_butonu.keys);
    if (typeof basla_butonu.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu.rt', basla_butonu.rt);
        routineTimer.reset();
        }
    
    basla_butonu.stop();
    // the Routine "Instruction100" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _basla_butonu_2_allKeys;
var Instruction75Components;
function Instruction75RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instruction75'-------
    t = 0;
    Instruction75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu_2.keys = undefined;
    basla_butonu_2.rt = undefined;
    _basla_butonu_2_allKeys = [];
    // keep track of which components have finished
    Instruction75Components = [];
    Instruction75Components.push(Instrcution100_2);
    Instruction75Components.push(basla_butonu_2);
    
    for (const thisComponent of Instruction75Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction75RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instruction75'-------
    // get current time
    t = Instruction75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instrcution100_2* updates
    if (t >= 0.0 && Instrcution100_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instrcution100_2.tStart = t;  // (not accounting for frame time here)
      Instrcution100_2.frameNStart = frameN;  // exact frame index
      
      Instrcution100_2.setAutoDraw(true);
    }

    
    // *basla_butonu_2* updates
    if (t >= 0.0 && basla_butonu_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu_2.tStart = t;  // (not accounting for frame time here)
      basla_butonu_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu_2.clock.reset();
      basla_butonu_2.start();
      basla_butonu_2.clearEvents();
    }

    if (basla_butonu_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu_2.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_2_allKeys = _basla_butonu_2_allKeys.concat(theseKeys);
      if (_basla_butonu_2_allKeys.length > 0) {
        basla_butonu_2.keys = _basla_butonu_2_allKeys[_basla_butonu_2_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu_2.rt = _basla_butonu_2_allKeys[_basla_butonu_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction75Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction75RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instruction75'-------
    for (const thisComponent of Instruction75Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu_2.keys', basla_butonu_2.keys);
    if (typeof basla_butonu_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu_2.rt', basla_butonu_2.rt);
        routineTimer.reset();
        }
    
    basla_butonu_2.stop();
    // the Routine "Instruction75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Validity75TrialComponents;
function Validity75TrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Validity75Trial'-------
    t = 0;
    Validity75TrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    shuffle(targetPos);
    target_2.setPos([targetPos[1], 0]);
    target_2.setImage(targetFile);
    distractor_2.setPos([(- targetPos[1]), 0]);
    distractor_2.setImage(maskFile);
    maskLeft_2.setPos([(- 0.4), 0]);
    maskLeft_2.setImage(maskFile);
    maskRight_2.setPos([0.4, 0]);
    maskRight_2.setImage(maskFile);
    Cue_2 = new sound.Sound({
    win: psychoJS.window,
    value: cueFile,
    secs: 2.0,
    });
    Cue_2.secs=2.0;
    Cue_2.setVolume(1.0);
    // keep track of which components have finished
    Validity75TrialComponents = [];
    Validity75TrialComponents.push(target_2);
    Validity75TrialComponents.push(distractor_2);
    Validity75TrialComponents.push(maskLeft_2);
    Validity75TrialComponents.push(maskRight_2);
    Validity75TrialComponents.push(Cue_2);
    Validity75TrialComponents.push(fixation_2);
    
    for (const thisComponent of Validity75TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Validity75TrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Validity75Trial'-------
    // get current time
    t = Validity75TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_2* updates
    // *target* updates
    if (t >= 2.0 && target_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      //target_2.tStart = t;  // (not accounting for frame time here)
      target_2.frameNStart = frameN;  // exact frame index
      target_2.tStartRefresh =target_2.frameNStart*frameDur ;
      target_2.setAutoDraw(true);
    }

    frameRemains = 2.0 + currentDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        //target_2.tStop = t; 
        target_2.frameNStop = frameN;
        target_2.tStopRefresh =target_2.frameNStop*frameDur ;
      target_2.setAutoDraw(false);
    }
    
    // *distractor_2* updates
    if (t >= 2.0 && distractor_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor_2.tStart = t;  // (not accounting for frame time here)
      distractor_2.frameNStart = frameN;  // exact frame index
      
      distractor_2.setAutoDraw(true);
    }

    if (distractor_2.status === PsychoJS.Status.STARTED && frameN >= (distractor_2.frameNStart + currentDur)) {
      distractor_2.setAutoDraw(false);
    }
    
    // *maskLeft_2* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskLeft_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskLeft_2.tStart = t;  // (not accounting for frame time here)
      maskLeft_2.frameNStart = frameN;  // exact frame index
      
      maskLeft_2.setAutoDraw(true);
    }

    if (maskLeft_2.status === PsychoJS.Status.STARTED && frameN >= (maskLeft_2.frameNStart + durMask)) {
      maskLeft_2.setAutoDraw(false);
    }
    
    // *maskRight_2* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskRight_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskRight_2.tStart = t;  // (not accounting for frame time here)
      maskRight_2.frameNStart = frameN;  // exact frame index
      
      maskRight_2.setAutoDraw(true);
    }

    if (maskRight_2.status === PsychoJS.Status.STARTED && frameN >= (maskRight_2.frameNStart + durMask)) {
      maskRight_2.setAutoDraw(false);
    }
    // start/stop Cue_2
    if (t >= 0.0 && Cue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cue_2.tStart = t;  // (not accounting for frame time here)
      Cue_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Cue_2.play(); });  // screen flip
      Cue_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Cue_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2.0 > 0.5) {  Cue_2.stop();  // stop the sound (if longer than duration)
        Cue_2.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *fixation_2* updates
    if (t >= 0.0 && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    if (fixation_2.status === PsychoJS.Status.STARTED && frameN >= (fixation_2.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001)) {
      fixation_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Validity75TrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Validity75TrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Validity75Trial'-------
    for (const thisComponent of Validity75TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Cue_2.stop();  // ensure sound has stopped at end of routine
    // the Routine "Validity75Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _response_allKeys;
var Response75Components;
function Response75RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Response75'-------
    t = 0;
    Response75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    // keep track of which components have finished
    Response75Components = [];
    Response75Components.push(response);
    Response75Components.push(fixation_response);
    
    for (const thisComponent of Response75Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Response75RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Response75'-------
    // get current time
    t = Response75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response* updates
    if (t >= 0.0 && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }

    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation_response* updates
    if (t >= 0.0 && fixation_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_response.tStart = t;  // (not accounting for frame time here)
      fixation_response.frameNStart = frameN;  // exact frame index
      
      fixation_response.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2+currentDur+durMask+0.0001 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_response.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Response75Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Response75RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Response75'-------
    for (const thisComponent of Response75Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    response.stop();
    if ((targetPos[1] > 0)) {
        if ((response.keys === "right")) {
            feedback = "Do\u011fru";
            accuracy.push(1);
            Loop75.addData("Accuracy", 1);
        } else {
            if ((response.keys === "left")) {
                feedback = "Yanl\u0131\u015f";
                accuracy.push(0);
                Loop75.addData("Accuracy", 0);
            }
        }
    } else {
        if ((targetPos[1] < 0)) {
            if ((response.keys === "left")) {
                feedback = "Do\u011fru";
                accuracy.push(1);
                Loop75.addData("Accuracy", 1);
            } else {
                if ((response.keys === "right")) {
                    feedback = "Yanl\u0131\u015f";
                    accuracy.push(0);
                    Loop75.addData("Accuracy", 0);
                }
            }
        }
    }
    
    // the Routine "Response75" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Feedback75Components;
function Feedback75RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback75'-------
    t = 0;
    Feedback75Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedBackScreen_2.setText(feedback);
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    Loop75.addData("TargetDuration", (currentDur * frameDur));
    if ((accuracy.slice((- 1))[0] === 0)) {
        currentDur = (currentDur + 1);
    } else {
        if (((currentDur > 1) && (accuracy.length >= 2))) {
            if (((accuracy.slice((- 1))[0] === 1) && (accuracy.slice((- 2))[0] === 1))) {
                currentDur = (currentDur - 1);
            }
        } else {
            currentDur = currentDur;
        }
    }
    if (_pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11))) {
        trialCongruency = "congruent";
        congDur.push((target.tStopRefresh - target.tStartRefresh));
        incongDur.push(NaN);
        Loop75.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        Loop75.addData("congruentTrialDuration", congDur[trialNumLoop100]);
    } else {
        if ((! _pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11)))) {
            trialCongruency = "incongruent";
            incongDur.push((target.tStopRefresh - target.tStartRefresh));
            congDur.push(NaN);
            Loop75.addData("congruentTrialDuration", congDur[trialNumLoop100]);
            Loop75.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        }
    }
    Loop75.addData("isCongruent", trialCongruency);
    trialNumLoop100 = (trialNumLoop100 + 1);
    
    // keep track of which components have finished
    Feedback75Components = [];
    Feedback75Components.push(feedBackScreen_2);
    
    for (const thisComponent of Feedback75Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Feedback75RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Feedback75'-------
    // get current time
    t = Feedback75Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedBackScreen_2* updates
    if (t >= 0.0 && feedBackScreen_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedBackScreen_2.tStart = t;  // (not accounting for frame time here)
      feedBackScreen_2.frameNStart = frameN;  // exact frame index
      
      feedBackScreen_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedBackScreen_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedBackScreen_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Feedback75Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Feedback75RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Feedback75'-------
    for (const thisComponent of Feedback75Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _basla_butonu_3_allKeys;
var Instruction50Components;
function Instruction50RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instruction50'-------
    t = 0;
    Instruction50Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu_3.keys = undefined;
    basla_butonu_3.rt = undefined;
    _basla_butonu_3_allKeys = [];
    // keep track of which components have finished
    Instruction50Components = [];
    Instruction50Components.push(Instrcution100_3);
    Instruction50Components.push(basla_butonu_3);
    
    for (const thisComponent of Instruction50Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction50RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instruction50'-------
    // get current time
    t = Instruction50Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instrcution100_3* updates
    if (t >= 0.0 && Instrcution100_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instrcution100_3.tStart = t;  // (not accounting for frame time here)
      Instrcution100_3.frameNStart = frameN;  // exact frame index
      
      Instrcution100_3.setAutoDraw(true);
    }

    
    // *basla_butonu_3* updates
    if (t >= 0.0 && basla_butonu_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu_3.tStart = t;  // (not accounting for frame time here)
      basla_butonu_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu_3.clock.reset();
      basla_butonu_3.start();
      basla_butonu_3.clearEvents();
    }

    if (basla_butonu_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu_3.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_3_allKeys = _basla_butonu_3_allKeys.concat(theseKeys);
      if (_basla_butonu_3_allKeys.length > 0) {
        basla_butonu_3.keys = _basla_butonu_3_allKeys[_basla_butonu_3_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu_3.rt = _basla_butonu_3_allKeys[_basla_butonu_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction50Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction50RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instruction50'-------
    for (const thisComponent of Instruction50Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu_3.keys', basla_butonu_3.keys);
    if (typeof basla_butonu_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu_3.rt', basla_butonu_3.rt);
        routineTimer.reset();
        }
    
    basla_butonu_3.stop();
    // the Routine "Instruction50" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Validity50TrialComponents;
function Validity50TrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Validity50Trial'-------
    t = 0;
    Validity50TrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
        shuffle(targetPos);

    target_3.setPos([targetPos[1], 0]);
    target_3.setImage(targetFile);
    distractor_3.setPos([(- targetPos[1]), 0]);
    distractor_3.setImage(maskFile);
    maskLeft_3.setPos([(- 0.4), 0]);
    maskLeft_3.setImage(maskFile);
    maskRight_3.setPos([0.4, 0]);
    maskRight_3.setImage(maskFile);
    Cue_3 = new sound.Sound({
    win: psychoJS.window,
    value: cueFile,
    secs: 2.0,
    });
    Cue_3.secs=2.0;
    Cue_3.setVolume(1.0);
    // keep track of which components have finished
    Validity50TrialComponents = [];
    Validity50TrialComponents.push(target_3);
    Validity50TrialComponents.push(distractor_3);
    Validity50TrialComponents.push(maskLeft_3);
    Validity50TrialComponents.push(maskRight_3);
    Validity50TrialComponents.push(Cue_3);
    Validity50TrialComponents.push(fixation_3);
    
    for (const thisComponent of Validity50TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Validity50TrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Validity50Trial'-------
    // get current time
    t = Validity50TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_3* updates
    if (t >= 2.0 && target_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      //target_3.tStart = t;  // (not accounting for frame time here)
      target_3.frameNStart = frameN;  // exact frame index
      target_3.tStartRefresh =target_3.frameNStart*frameDur ;
      target_3.setAutoDraw(true);
    }

    frameRemains = 2.0 + currentDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        //target_3.tStop = t; 
        target_3.frameNStop = frameN;
        target_3.tStopRefresh =target_3.frameNStop*frameDur ;
      target_3.setAutoDraw(false);
    }
    
    // *distractor_3* updates
    if (t >= 2.0 && distractor_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor_3.tStart = t;  // (not accounting for frame time here)
      distractor_3.frameNStart = frameN;  // exact frame index
      
      distractor_3.setAutoDraw(true);
    }

    if (distractor_3.status === PsychoJS.Status.STARTED && frameN >= (distractor_3.frameNStart + currentDur)) {
      distractor_3.setAutoDraw(false);
    }
    
    // *maskLeft_3* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskLeft_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskLeft_3.tStart = t;  // (not accounting for frame time here)
      maskLeft_3.frameNStart = frameN;  // exact frame index
      
      maskLeft_3.setAutoDraw(true);
    }

    if (maskLeft_3.status === PsychoJS.Status.STARTED && frameN >= (maskLeft_3.frameNStart + durMask)) {
      maskLeft_3.setAutoDraw(false);
    }
    
    // *maskRight_3* updates
    if (frameN >= (expInfo['frameRate']*2)+currentDur && maskRight_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskRight_3.tStart = t;  // (not accounting for frame time here)
      maskRight_3.frameNStart = frameN;  // exact frame index
      
      maskRight_3.setAutoDraw(true);
    }

    if (maskRight_3.status === PsychoJS.Status.STARTED && frameN >= (maskRight_3.frameNStart + durMask)) {
      maskRight_3.setAutoDraw(false);
    }
    // start/stop Cue_3
    if (t >= 0.0 && Cue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cue_3.tStart = t;  // (not accounting for frame time here)
      Cue_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Cue_3.play(); });  // screen flip
      Cue_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Cue_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2.0 > 0.5) {  Cue_3.stop();  // stop the sound (if longer than duration)
        Cue_3.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *fixation_3* updates
    if (t >= 0.0 && fixation_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_3.tStart = t;  // (not accounting for frame time here)
      fixation_3.frameNStart = frameN;  // exact frame index
      
      fixation_3.setAutoDraw(true);
    }

    if (fixation_3.status === PsychoJS.Status.STARTED && frameN >= (fixation_3.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001)) {
      fixation_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Validity50TrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Validity50TrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Validity50Trial'-------
    for (const thisComponent of Validity50TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Cue_3.stop();  // ensure sound has stopped at end of routine
    // the Routine "Validity50Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _response_3_allKeys;
var Response50Components;
function Response50RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Response50'-------
    t = 0;
    Response50Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    response_3.keys = undefined;
    response_3.rt = undefined;
    _response_3_allKeys = [];
    // keep track of which components have finished
    Response50Components = [];
    Response50Components.push(response_3);
    Response50Components.push(fixation_response_3);
    
    for (const thisComponent of Response50Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Response50RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Response50'-------
    // get current time
    t = Response50Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response_3* updates
    if (t >= 0.0 && response_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_3.tStart = t;  // (not accounting for frame time here)
      response_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response_3.clearEvents(); });
    }

    if (response_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = response_3.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _response_3_allKeys = _response_3_allKeys.concat(theseKeys);
      if (_response_3_allKeys.length > 0) {
        response_3.keys = _response_3_allKeys[_response_3_allKeys.length - 1].name;  // just the last key pressed
        response_3.rt = _response_3_allKeys[_response_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation_response_3* updates
    if (t >= 0.0 && fixation_response_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_response_3.tStart = t;  // (not accounting for frame time here)
      fixation_response_3.frameNStart = frameN;  // exact frame index
      
      fixation_response_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2+currentDur+durMask+0.0001 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_response_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_response_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Response50Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Response50RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Response50'-------
    for (const thisComponent of Response50Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    response_3.stop();
    if ((targetPos[1] > 0)) {
        if ((response_3.keys === "right")) {
            feedback = "Do\u011fru";
            accuracy.push(1);
            Loop50.addData("Accuracy", 1);
        } else {
            if ((response_3.keys === "left")) {
                feedback = "Yanl\u0131\u015f";
                accuracy.push(0);
                Loop50.addData("Accuracy", 0);
            }
        }
    } else {
        if ((targetPos[1] < 0)) {
            if ((response_3.keys === "left")) {
                feedback = "Do\u011fru";
                accuracy.push(1);
                Loop50.addData("Accuracy", 1);
            } else {
                if ((response_3.keys === "right")) {
                    feedback = "Yanl\u0131\u015f";
                    accuracy.push(0);
                    Loop50.addData("Accuracy", 0);
                }
            }
        }
    }
    
    // the Routine "Response50" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Feedback50Components;
function Feedback50RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback50'-------
    t = 0;
    Feedback50Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedBackScreen_3.setText(feedback);
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    Loop50.addData("TargetDuration", (currentDur * frameDur));
    if ((accuracy.slice((- 1))[0] === 0)) {
        currentDur = (currentDur + 1);
    } else {
        if (((currentDur > 1) && (accuracy.length >= 2))) {
            if (((accuracy.slice((- 1))[0] === 1) && (accuracy.slice((- 2))[0] === 1))) {
                currentDur = (currentDur - 1);
            }
        } else {
            currentDur = currentDur;
        }
    }
    if (_pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11))) {
        trialCongruency = "congruent";
        congDur.push((target.tStopRefresh - target.tStartRefresh));
        incongDur.push(NaN);
        Loop50.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        Loop50.addData("congruentTrialDuration", congDur[trialNumLoop100]);
    } else {
        if ((! _pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11)))) {
            trialCongruency = "incongruent";
            incongDur.push((target.tStopRefresh - target.tStartRefresh));
            congDur.push(NaN);
            Loop50.addData("congruentTrialDuration", congDur[trialNumLoop100]);
            Loop50.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        }
    }
    Loop50.addData("isCongruent", trialCongruency);
    trialNumLoop100 = (trialNumLoop100 + 1);
    
    // keep track of which components have finished
    Feedback50Components = [];
    Feedback50Components.push(feedBackScreen_3);
    
    for (const thisComponent of Feedback50Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Feedback50RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Feedback50'-------
    // get current time
    t = Feedback50Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedBackScreen_3* updates
    if (t >= 0.0 && feedBackScreen_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedBackScreen_3.tStart = t;  // (not accounting for frame time here)
      feedBackScreen_3.frameNStart = frameN;  // exact frame index
      
      feedBackScreen_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedBackScreen_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedBackScreen_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Feedback50Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Feedback50RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Feedback50'-------
    for (const thisComponent of Feedback50Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _basla_butonu_4_allKeys;
var InstructionNeutralComponents;
function InstructionNeutralRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'InstructionNeutral'-------
    t = 0;
    InstructionNeutralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu_4.keys = undefined;
    basla_butonu_4.rt = undefined;
    _basla_butonu_4_allKeys = [];
    // keep track of which components have finished
    InstructionNeutralComponents = [];
    InstructionNeutralComponents.push(Instrcution100_4);
    InstructionNeutralComponents.push(basla_butonu_4);
    
    for (const thisComponent of InstructionNeutralComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionNeutralRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'InstructionNeutral'-------
    // get current time
    t = InstructionNeutralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instrcution100_4* updates
    if (t >= 0.0 && Instrcution100_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instrcution100_4.tStart = t;  // (not accounting for frame time here)
      Instrcution100_4.frameNStart = frameN;  // exact frame index
      
      Instrcution100_4.setAutoDraw(true);
    }

    
    // *basla_butonu_4* updates
    if (t >= 0.0 && basla_butonu_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu_4.tStart = t;  // (not accounting for frame time here)
      basla_butonu_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu_4.clock.reset();
      basla_butonu_4.start();
      basla_butonu_4.clearEvents();
    }

    if (basla_butonu_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu_4.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_4_allKeys = _basla_butonu_4_allKeys.concat(theseKeys);
      if (_basla_butonu_4_allKeys.length > 0) {
        basla_butonu_4.keys = _basla_butonu_4_allKeys[_basla_butonu_4_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu_4.rt = _basla_butonu_4_allKeys[_basla_butonu_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionNeutralComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionNeutralRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'InstructionNeutral'-------
    for (const thisComponent of InstructionNeutralComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu_4.keys', basla_butonu_4.keys);
    if (typeof basla_butonu_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu_4.rt', basla_butonu_4.rt);
        routineTimer.reset();
        }
    
    basla_butonu_4.stop();
    // the Routine "InstructionNeutral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var NeutralTrialComponents;
function NeutralTrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'NeutralTrial'-------
    t = 0;
    NeutralTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
        shuffle(targetPos);

    target_4.setPos([targetPos[1], 0]);
    target_4.setImage(targetFile);
    distractor_4.setPos([(- targetPos[1]), 0]);
    distractor_4.setImage(maskFile);
    maskLeft_4.setPos([(- 0.4), 0]);
    maskLeft_4.setImage(maskFile);
    maskRight_4.setPos([0.4, 0]);
    maskRight_4.setImage(maskFile);
    // keep track of which components have finished
    NeutralTrialComponents = [];
    NeutralTrialComponents.push(target_4);
    NeutralTrialComponents.push(distractor_4);
    NeutralTrialComponents.push(maskLeft_4);
    NeutralTrialComponents.push(maskRight_4);
    NeutralTrialComponents.push(fixation_4);
    
    for (const thisComponent of NeutralTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NeutralTrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'NeutralTrial'-------
    // get current time
    t = NeutralTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_4* updates
    if (t >= 2.0 && target_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      //target_4.tStart = t;  // (not accounting for frame time here)
      target_4.frameNStart = frameN;  // exact frame index
      target_4.tStartRefresh =target_4.frameNStart*frameDur ;
      target_4.setAutoDraw(true);
    }

    frameRemains = 2.0 + currentDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        //target_4.tStop = t; 
        target_4.frameNStop = frameN;
        target_4.tStopRefresh =target_4.frameNStop*frameDur ;
      target_4.setAutoDraw(false);
    }
    
    // *distractor_4* updates
    if (t >= 0.2 && distractor_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor_4.tStart = t;  // (not accounting for frame time here)
      distractor_4.frameNStart = frameN;  // exact frame index
      
      distractor_4.setAutoDraw(true);
    }

    if (distractor_4.status === PsychoJS.Status.STARTED && frameN >= (distractor_4.frameNStart + currentDur)) {
      distractor_4.setAutoDraw(false);
    }
    
    // *maskLeft_4* updates
    if (frameN >= (expInfo['frameRate']*0.2)+currentDur && maskLeft_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskLeft_4.tStart = t;  // (not accounting for frame time here)
      maskLeft_4.frameNStart = frameN;  // exact frame index
      
      maskLeft_4.setAutoDraw(true);
    }

    if (maskLeft_4.status === PsychoJS.Status.STARTED && frameN >= (maskLeft_4.frameNStart + durMask)) {
      maskLeft_4.setAutoDraw(false);
    }
    
    // *maskRight_4* updates
    if (frameN >= (expInfo['frameRate']*0.2)+currentDur && maskRight_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maskRight_4.tStart = t;  // (not accounting for frame time here)
      maskRight_4.frameNStart = frameN;  // exact frame index
      
      maskRight_4.setAutoDraw(true);
    }

    if (maskRight_4.status === PsychoJS.Status.STARTED && frameN >= (maskRight_4.frameNStart + durMask)) {
      maskRight_4.setAutoDraw(false);
    }
    
    // *fixation_4* updates
    if (t >= 0.0 && fixation_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_4.tStart = t;  // (not accounting for frame time here)
      fixation_4.frameNStart = frameN;  // exact frame index
      
      fixation_4.setAutoDraw(true);
    }

    if (fixation_4.status === PsychoJS.Status.STARTED && frameN >= (fixation_4.frameNStart + (expInfo['frameRate']*2)+currentDur+durMask+0.0001)) {
      fixation_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NeutralTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NeutralTrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'NeutralTrial'-------
    for (const thisComponent of NeutralTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "NeutralTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _response_4_allKeys;
var ResponseNeutralComponents;
function ResponseNeutralRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ResponseNeutral'-------
    t = 0;
    ResponseNeutralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    response_4.keys = undefined;
    response_4.rt = undefined;
    _response_4_allKeys = [];
    // keep track of which components have finished
    ResponseNeutralComponents = [];
    ResponseNeutralComponents.push(response_4);
    ResponseNeutralComponents.push(fixation_response_4);
    
    for (const thisComponent of ResponseNeutralComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ResponseNeutralRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ResponseNeutral'-------
    // get current time
    t = ResponseNeutralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response_4* updates
    if (t >= 0.0 && response_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_4.tStart = t;  // (not accounting for frame time here)
      response_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response_4.clearEvents(); });
    }

    if (response_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = response_4.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _response_4_allKeys = _response_4_allKeys.concat(theseKeys);
      if (_response_4_allKeys.length > 0) {
        response_4.keys = _response_4_allKeys[_response_4_allKeys.length - 1].name;  // just the last key pressed
        response_4.rt = _response_4_allKeys[_response_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixation_response_4* updates
    if (t >= 0.0 && fixation_response_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_response_4.tStart = t;  // (not accounting for frame time here)
      fixation_response_4.frameNStart = frameN;  // exact frame index
      
      fixation_response_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2+currentDur+durMask+0.0001 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_response_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_response_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ResponseNeutralComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ResponseNeutralRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ResponseNeutral'-------
    for (const thisComponent of ResponseNeutralComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    response_4.stop();
    if ((targetPos[1] > 0)) {
        if ((response_3.keys === "right")) {
            feedback = "Do\u011fru";
            accuracy.push(1);
            LoopNeutral.addData("Accuracy", 1);
        } else {
            if ((response_3.keys === "left")) {
                feedback = "Yanl\u0131\u015f";
                accuracy.push(0);
                LoopNeutral.addData("Accuracy", 0);
            }
        }
    } else {
        if ((targetPos[1] < 0)) {
            if ((response_3.keys === "left")) {
                feedback = "Do\u011fru";
                accuracy.push(1);
                LoopNeutral.addData("Accuracy", 1);
            } else {
                if ((response_3.keys === "right")) {
                    feedback = "Yanl\u0131\u015f";
                    accuracy.push(0);
                    LoopNeutral.addData("Accuracy", 0);
                }
            }
        }
    }
    
    // the Routine "ResponseNeutral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var FeedbackNeutralComponents;
function FeedbackNeutralRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'FeedbackNeutral'-------
    t = 0;
    FeedbackNeutralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedBackScreen_4.setText(feedback);
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    LoopNeutral.addData("TargetDuration", (currentDur * frameDur));
    if ((accuracy.slice((- 1))[0] === 0)) {
        currentDur = (currentDur + 1);
    } else {
        if (((currentDur > 1) && (accuracy.length >= 2))) {
            if (((accuracy.slice((- 1))[0] === 1) && (accuracy.slice((- 2))[0] === 1))) {
                currentDur = (currentDur - 1);
            }
        } else {
            currentDur = currentDur;
        }
    }
    if (_pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11))) {
        trialCongruency = "congruent";
        congDur.push((target.tStopRefresh - target.tStartRefresh));
        incongDur.push(NaN);
        LoopNeutral.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        LoopNeutral.addData("congruentTrialDuration", congDur[trialNumLoop100]);
    } else {
        if ((! _pj.in_es6(cueFile.slice(7, 11), targetFile.slice(7, 11)))) {
            trialCongruency = "incongruent";
            incongDur.push((target.tStopRefresh - target.tStartRefresh));
            congDur.push(NaN);
            LoopNeutral.addData("congruentTrialDuration", congDur[trialNumLoop100]);
            LoopNeutral.addData("incongruentTrialDuration", incongDur[trialNumLoop100]);
        }
    }
    LoopNeutral.addData("isCongruent", trialCongruency);
    trialNumLoop100 = (trialNumLoop100 + 1);
    
    // keep track of which components have finished
    FeedbackNeutralComponents = [];
    FeedbackNeutralComponents.push(feedBackScreen_4);
    
    for (const thisComponent of FeedbackNeutralComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FeedbackNeutralRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'FeedbackNeutral'-------
    // get current time
    t = FeedbackNeutralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedBackScreen_4* updates
    if (t >= 0.0 && feedBackScreen_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedBackScreen_4.tStart = t;  // (not accounting for frame time here)
      feedBackScreen_4.frameNStart = frameN;  // exact frame index
      
      feedBackScreen_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedBackScreen_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedBackScreen_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FeedbackNeutralComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackNeutralRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'FeedbackNeutral'-------
    for (const thisComponent of FeedbackNeutralComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _basla_butonu_5_allKeys;
var end_of_expComponents;
function end_of_expRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end_of_exp'-------
    t = 0;
    end_of_expClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    basla_butonu_5.keys = undefined;
    basla_butonu_5.rt = undefined;
    _basla_butonu_5_allKeys = [];
    // keep track of which components have finished
    end_of_expComponents = [];
    end_of_expComponents.push(Instrcution100_5);
    end_of_expComponents.push(basla_butonu_5);
    
    for (const thisComponent of end_of_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_of_expRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end_of_exp'-------
    // get current time
    t = end_of_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instrcution100_5* updates
    if (t >= 0.0 && Instrcution100_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instrcution100_5.tStart = t;  // (not accounting for frame time here)
      Instrcution100_5.frameNStart = frameN;  // exact frame index
      
      Instrcution100_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instrcution100_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instrcution100_5.setAutoDraw(false);
    }
    
    // *basla_butonu_5* updates
    if (t >= 0.0 && basla_butonu_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basla_butonu_5.tStart = t;  // (not accounting for frame time here)
      basla_butonu_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      basla_butonu_5.clock.reset();
      basla_butonu_5.start();
      basla_butonu_5.clearEvents();
    }

    if (basla_butonu_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = basla_butonu_5.getKeys({keyList: ['space'], waitRelease: false});
      _basla_butonu_5_allKeys = _basla_butonu_5_allKeys.concat(theseKeys);
      if (_basla_butonu_5_allKeys.length > 0) {
        basla_butonu_5.keys = _basla_butonu_5_allKeys[_basla_butonu_5_allKeys.length - 1].name;  // just the last key pressed
        basla_butonu_5.rt = _basla_butonu_5_allKeys[_basla_butonu_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_of_expComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_of_expRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end_of_exp'-------
    for (const thisComponent of end_of_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('basla_butonu_5.keys', basla_butonu_5.keys);
    if (typeof basla_butonu_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('basla_butonu_5.rt', basla_butonu_5.rt);
        routineTimer.reset();
        }
    
    basla_butonu_5.stop();
    // the Routine "end_of_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
