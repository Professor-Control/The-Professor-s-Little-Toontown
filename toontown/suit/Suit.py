from direct.actor import Actor
from otp.avatar import Avatar
import SuitDNA
from toontown.toonbase import ToontownGlobals
from panda3d.core import *
from toontown.battle import SuitBattleGlobals
from direct.task.Task import Task
from toontown.battle import BattleProps
from libotp import *
from direct.showbase import AppRunnerGlobal
import string
import os
aSize = 6.06
bSize = 5.29
cSize = 4.14
SuitDialogArray = []
SkelSuitDialogArray = []
AllSuits = (('walk', 'walk'), ('run', 'walk'), ('neutral', 'neutral'))
AllSuitsMinigame = (('victory', 'victory'),
 ('flail', 'flailing'),
 ('tug-o-war', 'tug-o-war'),
 ('slip-backward', 'slip-backward'),
 ('slip-forward', 'slip-forward'))
AllSuitsTutorialBattle = (('lose', 'lose'), ('pie-small-react', 'pie-small'), ('squirt-small-react', 'squirt-small'))
AllSuitsBattle = (('drop-react', 'anvil-drop'),
 ('flatten', 'drop'),
 ('sidestep-left', 'sidestep-left'),
 ('sidestep-right', 'sidestep-right'),
 ('squirt-large-react', 'squirt-large'),
 ('landing', 'landing'),
 ('reach', 'walknreach'),
 ('rake-react', 'rake'),
 ('hypnotized', 'hypnotize'),
 ('soak', 'soak'))
SuitsCEOBattle = (('sit', 'sit'),
 ('sit-eat-in', 'sit-eat-in'),
 ('sit-eat-loop', 'sit-eat-loop'),
 ('sit-eat-out', 'sit-eat-out'),
 ('sit-angry', 'sit-angry'),
 ('sit-hungry-left', 'leftsit-hungry'),
 ('sit-hungry-right', 'rightsit-hungry'),
 ('sit-lose', 'sit-lose'),
 ('tray-walk', 'tray-walk'),
 ('tray-neutral', 'tray-neutral'),
 ('sit-lose', 'sit-lose'))
f = (('throw-paper', 'throw-paper', 3.5), ('phone', 'phone', 3.5), ('shredder', 'shredder', 5), ('pen-squirt', 'fountain-pen', 5), ('watercooler', 'watercooler', 3.5))
p = (('pencil-sharpener', 'pencil-sharpener', 5),
 ('pen-squirt', 'pen-squirt', 5),
 ('hold-eraser', 'hold-eraser', 5),
 ('finger-wag', 'finger-wag', 5),
 ('hold-pencil', 'hold-pencil', 5))
ym = (('throw-paper', 'throw-paper', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('magic3', 'magic3', 5),
 ('rubber-stamp', 'rubber-stamp', 5),
 ('smile', 'smile', 5),
 ('effort', 'effort', 5))
cj = (('pen-squirt', 'fountain-pen', 5), ('effort', 'effort', 3.5))
mm = (('speak', 'speak', 3.5),
 ('effort', 'effort', 3.5),
 ('magic1', 'magic1', 3.5),
 ('pen-squirt', 'fountain-pen', 5),
 ('finger-wag', 'finger-wag', 5))
ds = (('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic3', 'magic3', 5))
hh = (('pen-squirt', 'fountain-pen', 5),
 ('glower', 'glower', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('roll-o-dex', 'roll-o-dex', 5),
 ('magic2', 'magic2', 5))
cr = (('magic1', 'magic1', 3.5), ('pickpocket', 'pickpocket', 5), ('throw-paper', 'throw-paper', 3.5), ('glower', 'glower', 5))
tbc = (('cigar-smoke', 'cigar-smoke', 5),
 ('glower', 'glower', 5),
 ('song-and-dance', 'song-and-dance', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('effort', 'effort', 5))
hho = (('cigar-smoke', 'cigar-smoke', 5), ('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5), ('magic2', 'magic2', 5), ('golf-club-swing', 'golf-club-swing', 5), ('effort', 'effort', 5))
cp = (('golf-club-swing', 'golf-club-swing', 5),
 ('magic2', 'magic2', 5),
 ('effort', 'effort', 5),
 ('speak', 'speak', 5))
dm = (('pen-squirt', 'fountain-pen', 5),
 ('magic1', 'magic1', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic3', 'magic3', 5),
 ('glower', 'glower', 5))
hoo = (('throw-paper', 'throw-paper', 5),
 ('magic2', 'magic2', 5),
 ('magic1', 'magic1', 5),
 ('glower', 'glower', 5),
 ('effort', 'effort', 5),
 ('cigar-smoke', 'cigar-smoke', 5),
 ('golf-club-swing', 'golf-club-swing', 5))
mgr = (('throw-paper', 'throw-paper', 5),
 ('magic2', 'magic2', 5),
 ('magic1', 'magic1', 5),
 ('stomp', 'stomp', 5),
 ('effort', 'effort', 5))
bf = (('pickpocket', 'pickpocket', 5), ('rubber-stamp', 'rubber-stamp', 5), ('shredder', 'shredder', 5), ('watercooler', 'watercooler', 3.5), ('throw-paper', 'throw-paper', 3.5))
b = (('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('magic1', 'magic1', 5), ('pickpocket', 'pickpocket', 5))
dt = (('rubber-stamp', 'rubber-stamp', 5),
 ('throw-paper', 'throw-paper', 5),
 ('speak', 'speak', 5),
 ('finger-wag', 'fingerwag', 5),
 ('throw-object', 'throw-object', 5),
 ('magic3', 'magic3', 5))
ptr = (('speak', 'speak', 5),
 ('pickpocket', 'pickpocket', 5),
 ('phone', 'phone', 5),
 ('throw-object', 'throw-object', 5),
 ('cigar-smoke', 'cigar-smoke', 5))
ac = (('throw-object', 'throw-object', 5),
 ('roll-o-dex', 'roll-o-dex', 5),
 ('stomp', 'stomp', 5),
 ('phone', 'phone', 5),
 ('throw-paper', 'throw-paper', 5),
 ('finger-wag', 'finger-wag', 5))
bs = (('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5), ('finger-wag', 'fingerwag', 5), ('speak', 'speak', 5))
sd = (('magic2', 'magic2', 5),
 ('quick-jump', 'jump', 5),
 ('stomp', 'stomp', 5),
 ('magic3', 'magic3', 5),
 ('hold-pencil', 'hold-pencil', 5),
 ('throw-paper', 'throw-paper', 5),
 ('effort', 'effort', 5))
le = (('finger-wag', 'fingerwag', 5), ('speak', 'speak', 5), ('throw-object', 'throw-object', 5), ('glower', 'glower', 5), ('throw-paper', 'throw-paper', 5))
bw = (('finger-wag', 'fingerwag', 5),
 ('cigar-smoke', 'cigar-smoke', 5),
 ('gavel', 'gavel', 8),
 ('magic1', 'magic1', 5),
 ('throw-object', 'throw-object', 5),
 ('throw-paper', 'throw-paper', 5))
br = (('magic3', 'magic3', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('finger-wag', 'finger-wag', 5), ('speak', 'speak', 5))
oo = (('magic3', 'magic3', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('speak', 'speak', 5))
wsi = (('throw-object', 'throw-object', 5),
 ('magic1', 'magic1', 5),
 ('glower', 'glower', 5),
 ('throw-paper', 'throw-paper', 5))
da = (('throw-paper', 'throw-paper', 5),
 ('finger-wag', 'finger-wag', 5),
 ('quick-jump', 'jump', 5),
 ('throw-object', 'throw-object', 5),
 ('magic1', 'magic1', 5),
 ('effort', 'effort', 5),
 ('hold-pencil', 'hold-pencil', 5),
 ('speak', 'speak', 5),
 ('magic3', 'magic3', 5))
sc = (('throw-paper', 'throw-paper', 3.5), ('watercooler', 'watercooler', 3.5), ('pickpocket', 'pickpocket', 5))
pp = (('throw-paper', 'throw-paper', 5), ('glower', 'glower', 5), ('finger-wag', 'fingerwag', 5), ('pickpocket', 'pickpocket', 5))
tw = (('throw-paper', 'throw-paper', 3.5),
 ('glower', 'glower', 5),
 ('magic2', 'magic2', 5),
 ('finger-wag', 'finger-wag', 5),
 ('pickpocket', 'pickpocket', 5))
bc = (('phone', 'phone', 5), ('hold-pencil', 'hold-pencil', 5))
nc = (('phone', 'phone', 5), ('throw-object', 'throw-object', 5))
mb = (('magic1', 'magic1', 3.5), ('throw-paper', 'throw-paper', 3.5), ('effort', 'effort', 3.5))
ls = (('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('hold-pencil', 'hold-pencil', 5), ('effort', 'effort', 5))
sq = (('magic1', 'magic1', 5), ('effort', 'effort', 5), ('magic3', 'magic3', 5))
rb = (('pickpocket', 'pickpocket', 5), ('glower', 'glower', 5), ('magic1', 'magic1', 5), ('golf-club-swing', 'golf-club-swing', 5))
bfh = (('magic1', 'magic1', 3.5), ('watercooler', 'watercooler', 3.5), ('throw-paper', 'throw-paper', 3.5))
msv = (('magic1', 'magic1', 3.5),
 ('glower', 'glower', 5),
 ('throw-paper', 'throw-paper', 3.5),
 ('pen-squirt', 'fountain-pen', 5))
dam = (('quick-jump', 'jump', 5), ('effort', 'effort', 5))
t = (('throw-paper', 'throw-paper', 5),
 ('hold-pencil', 'hold-pencil', 5),
 ('phone', 'phone', 5),
 ('magic1', 'magic1', 5),
 ('effort', 'effort', 5),
 ('magic3', 'magic3', 5))
cc = (('speak', 'speak', 3.5),
 ('glower', 'glower', 5),
 ('phone', 'phone', 3.5),
 ('effort', 'effort', 3.5),
 ('magic1', 'magic1', 3.5),
 ('watercooler', 'watercooler', 3.5))
tm = (('speak', 'speak', 5),
 ('throw-paper', 'throw-paper', 5),
 ('pickpocket', 'pickpocket', 5),
 ('roll-o-dex', 'roll-o-dex', 5),
 ('finger-wag', 'finger-wag', 5),
 ('phone', 'phone', 5))
nd = (('pickpocket', 'pickpocket', 5),
 ('roll-o-dex', 'roll-o-dex', 5),
 ('magic3', 'magic3', 5),
 ('smile', 'smile', 5))
gh = (('speak', 'speak', 3.5), ('pen-squirt', 'fountain-pen', 5), ('rubber-stamp', 'rubber-stamp', 5))
ms = (('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('stomp', 'stomp', 5), ('quick-jump', 'jump', 5), ('speak', 'speak', 5))
acr = (('speak', 'speak', 5), ('magic1', 'magic1', 5), ('throw-paper', 'throw-paper', 5))
tf = (('phone', 'phone', 5), ('smile', 'smile', 5), ('throw-object', 'throw-object', 5), ('glower', 'glower', 5), ('speak', 'speak', 5), ('magic3', 'magic3', 5))
m = (('speak', 'speak', 5), ('magic2', 'magic2', 5), ('magic1', 'magic1', 5), ('golf-club-swing', 'golf-club-swing', 5), ('smile', 'smile', 5))
mh = (('magic1', 'magic1', 5),
 ('smile', 'smile', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('song-and-dance', 'song-and-dance', 5))
tl = (('cigar-smoke', 'cigar-smoke', 5),
 ('magic1', 'magic1', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('glower', 'glower', 5))
ff = (('throw-paper', 'throw-paper', 5), ('cigar-smoke', 'cigar-smoke', 5), ('magic3', 'magic3', 5), ('golf-club-swing', 'golf-club-swing', 5))
dpr = (('speak', 'speak', 3.5), ('effort', 'effort', 3.5), ('magic1', 'magic1', 3.5), ('magic3', 'magic2', 5), ('glower', 'glower', 5))
mdm = (('throw-paper', 'throw-paper', 5),
 ('effort', 'effort', 5),
 ('magic1', 'magic1', 5),
 ('phone', 'phone', 5),
 ('stomp', 'stomp', 5),
 ('quick-jump', 'jump', 5))
crm = (('pickpocket', 'pickpocket', 5),
 ('magic1', 'magic1', 3.5),
 ('glower', 'glower', 5))
sw = (('throw-paper', 'throw-paper', 5),
 ('phone', 'phone', 5),
 ('roll-o-dex', 'roll-o-dex', 5),
 ('pickpocket', 'pickpocket', 5))
fg = (('glower', 'glower', 5),
 ('throw-paper', 'throw-paper', 3.5))
mf = (('throw-object', 'throw-object', 5),
 ('throw-paper', 'throw-paper', 5))
dlr = (('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('pickpocket', 'pickpocket', 5))
asn = (('stomp', 'stomp', 5),
 ('hold-eraser', 'hold-eraser', 5),
 ('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5))
gst = (('magic1', 'magic1', 5),
 ('throw-paper', 'throw-paper', 5),
 ('phone', 'phone', 5))
rt = (('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('golf-club-swing', 'golf-club-swing', 5))
tfk = (('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('glower', 'glower', 5),
 ('cigar-smoke', 'cigar-smoke', 5))
txm = (('magic1', 'magic1', 5), ('pen-squirt', 'fountain-pen', 5), ('glower', 'glower', 5))
gf = (('throw-paper', 'throw-paper', 5),
 ('magic1', 'magic1', 5),
 ('magic2', 'magic2', 5),
 ('glower', 'glower', 5),
 ('golf-club-swing', 'golf-club-swing', 5),
 ('song-and-dance', 'song-and-dance', 5),
 ('speak', 'speak', 5),
 ('cigar-smoke', 'cigar-smoke', 5))
ws = (('speak', 'speak', 5), ('magic2', 'magic2', 5), ('magic1', 'magic1', 5), ('golf-club-swing', 'golf-club-swing', 5), ('smile', 'smile', 5))
if not base.config.GetBool('want-new-cogs', 0):
    ModelDict = {'a': ('/models/char/suitA-', 4),
     'b': ('/models/char/suitB-', 4),
     'c': ('/models/char/suitC-', 3.5)}
    TutorialModelDict = {'a': ('/models/char/suitA-', 4),
     'b': ('/models/char/suitB-', 4),
     'c': ('/models/char/suitC-', 3.5)}
else:
    ModelDict = {'a': ('/models/char/tt_a_ene_cga_', 4),
     'b': ('/models/char/tt_a_ene_cgb_', 4),
     'c': ('/models/char/tt_a_ene_cgc_', 3.5)}
    TutorialModelDict = {'a': ('/models/char/tt_a_ene_cga_', 4),
     'b': ('/models/char/tt_a_ene_cgb_', 4),
     'c': ('/models/char/tt_a_ene_cgc_', 3.5)}
try:
    HeadModelDict = {'a': ('/models/char/suitA-', 4),
     'b': ('/models/char/suitB-', 4),
     'c': ('/models/char/suitC-', 3.5)}
except:
    HeadModelDict = {'a': ('/models/char/', 14),
     'b': ('/models/char/', 14),
     'c': ('/models/char/', 14)}

def loadTutorialSuit():
    loader.loadModel('phase_3.5/models/char/suitC-mod').node()
    loadDialog(1)


def loadSuits(level):
    loadSuitModelsAndAnims(level, flag=1)
    loadDialog(level)


def unloadSuits(level):
    loadSuitModelsAndAnims(level, flag=0)
    unloadDialog(level)


def loadSuitModelsAndAnims(level, flag = 0):
    for key in ModelDict.keys():
        model, phase = ModelDict[key]
        if base.config.GetBool('want-new-cogs', 0):
            headModel, headPhase = HeadModelDict[key]
        else:
            headModel, headPhase = ModelDict[key]
        if flag:
            if base.config.GetBool('want-new-cogs', 0):
                filepath = 'phase_3.5' + model + 'zero'
                if cogExists(model + 'zero.bam'):
                    loader.loadModel(filepath).node()
            else:
                loader.loadModel('phase_3.5' + model + 'mod').node()
            loader.loadModel('phase_' + str(headPhase) + headModel + 'heads').node()
        else:
            if base.config.GetBool('want-new-cogs', 0):
                filepath = 'phase_3.5' + model + 'zero'
                if cogExists(model + 'zero.bam'):
                    loader.unloadModel(filepath)
            else:
                loader.unloadModel('phase_3.5' + model + 'mod')
            loader.unloadModel('phase_' + str(headPhase) + headModel + 'heads')


def cogExists(filePrefix):
    searchPath = DSearchPath()
    if AppRunnerGlobal.appRunner:
        searchPath.appendDirectory(Filename.expandFrom('$TT_3_5_ROOT/phase_3.5'))
    else:
        basePath = os.path.expandvars('$TTMODELS') or './ttmodels'
        searchPath.appendDirectory(Filename.fromOsSpecific(basePath + '/built/phase_3.5'))
    filePrefix = filePrefix.strip('/')
    pfile = Filename(filePrefix)
    found = vfs.resolveFilename(pfile, searchPath)
    if not found:
        return False
    return True


def loadSuitAnims(suit, flag = 1):
    if suit in SuitDNA.suitHeadTypes:
        try:
            animList = eval(suit)
        except NameError:
            animList = ()

    else:
        print 'Invalid suit name: ', suit
        return -1
    for anim in animList:
        phase = 'phase_' + str(anim[2])
        filePrefix = ModelDict[bodyType][0]
        animName = filePrefix + anim[1]
        if flag:
            loader.loadModel(animName).node()
        else:
            loader.unloadModel(animName)


def loadDialog(level):
    global SuitDialogArray
    if len(SuitDialogArray) > 0:
        return
    else:
        SuitSounds = ['grunt',
         'murmur',
         'statement',
         'question']
        for sound in SuitSounds:
            SuitDialogArray.append(base.loader.loadSfx('phase_3.5/audio/dial/COG_VO_' + sound + '.ogg'))

        SuitDialogArray.append(SuitDialogArray[2])
        SuitDialogArray.append(SuitDialogArray[2])


def loadSkelDialog():
    global SkelSuitDialogArray
    if len(SkelSuitDialogArray) > 0:
        return
    else:
        grunt = loader.loadSfx('phase_5/audio/dial/Skel_COG_VO_grunt.ogg')
        murmur = loader.loadSfx('phase_5/audio/dial/Skel_COG_VO_murmur.ogg')
        statement = loader.loadSfx('phase_5/audio/dial/Skel_COG_VO_statement.ogg')
        question = loader.loadSfx('phase_5/audio/dial/Skel_COG_VO_question.ogg')
        SkelSuitDialogArray = [grunt,
         murmur,
         statement,
         question,
         statement,
         statement]


def unloadDialog(level):
    global SuitDialogArray
    SuitDialogArray = []


def unloadSkelDialog():
    global SkelSuitDialogArray
    SkelSuitDialogArray = []


def attachSuitHead(node, suitName):
    suitIndex = SuitDNA.suitHeadTypes.index(suitName)
    suitDNA = SuitDNA.SuitDNA()
    suitDNA.newSuit(suitName)
    suit = Suit()
    suit.setDNA(suitDNA)
    headParts = suit.getHeadParts()
    head = node.attachNewNode('head')
    for part in headParts:
        copyPart = part.copyTo(head)
        copyPart.setDepthTest(1)
        copyPart.setDepthWrite(1)

    suit.delete()
    suit = None
    p1 = Point3()
    p2 = Point3()
    head.calcTightBounds(p1, p2)
    d = p2 - p1
    biggest = max(d[0], d[2])
    column = suitIndex % SuitDNA.suitsPerDept
    if not biggest:
        biggest = 1
    s = (0.2 + column / 100.0) / biggest
    pos = -0.14 + (SuitDNA.suitsPerDept - column - 1) / 135.0
    head.setPosHprScale(0, 0, pos, 180, 0, 0, s, s, s)
    return head


class Suit(Avatar.Avatar):
    healthColors = (Vec4(0, 1, 0, 1),
     Vec4(0.5, 1, 0, 1),
     Vec4(0.75, 1, 0, 1),
     Vec4(1, 1, 0, 1),
     Vec4(1, 0.86, 0, 1),
     Vec4(1, 0.6, 0, 1),
     Vec4(1, 0.5, 0, 1),
     Vec4(1, 0.25, 0, 1.0),
     Vec4(1, 0, 0, 1),
     Vec4(0.3, 0.3, 0.3, 1))
    healthGlowColors = (Vec4(0.25, 1, 0.25, 0.5),
     Vec4(0.5, 1, 0.25, .5),
     Vec4(0.75, 1, 0.25, .5),
     Vec4(1, 1, 0.25, 0.5),
     Vec4(1, 0.866, 0.25, .5),
     Vec4(1, 0.6, 0.25, .5),
     Vec4(1, 0.5, 0.25, 0.5),
     Vec4(1, 0.25, 0.25, 0.5),
     Vec4(1, 0.25, 0.25, 0.5),
     Vec4(0.3, 0.3, 0.3, 0))
    medallionColors = {'c': Vec4(0.863, 0.776, 0.769, 1.0),
     'l': Vec4(0.749, 0.776, 0.824, 1.0),
     'm': Vec4(0.749, 0.769, 0.749, 1.0),
     's': Vec4(0.843, 0.745, 0.745, 1.0),
     'g': Vec4(0.863, 0.776, 0.769, 1.0)}

    def __init__(self):
        try:
            self.Suit_initialized
            return
        except:
            self.Suit_initialized = 1

        Avatar.Avatar.__init__(self)
        self.setFont(ToontownGlobals.getSuitFont())
        self.setPlayerType(NametagGroup.CCSuit)
        self.setPickable(1)
        self.leftHand = None
        self.rightHand = None
        self.shadowJoint = None
        self.nametagJoint = None
        self.headParts = []
        self.healthBar = None
        self.healthCondition = 0
        self.isSkeleton = 0
        self.isDisguised = 0
        self.isWaiter = 0
        self.isRental = 0
        self.isBloodsucker = 0
        self.isExecutive = 0
        self.isManager = 0
        return

    def delete(self):
        try:
            self.Suit_deleted
        except:
            self.Suit_deleted = 1
            if self.leftHand:
                self.leftHand.removeNode()
                self.leftHand = None
            if self.rightHand:
                self.rightHand.removeNode()
                self.rightHand = None
            if self.shadowJoint:
                self.shadowJoint.removeNode()
                self.shadowJoint = None
            if self.nametagJoint:
                self.nametagJoint.removeNode()
                self.nametagJoint = None
            for part in self.headParts:
                part.removeNode()

            self.headParts = []
            self.removeHealthBar()
            Avatar.Avatar.delete(self)

        return

    def setHeight(self, height):
        Avatar.Avatar.setHeight(self, height)
        self.nametag3d.setPos(0, 0, height + 1.0)

    def getRadius(self):
        return 2

    def setDNAString(self, dnaString):
        self.dna = SuitDNA.SuitDNA()
        self.dna.makeFromNetString(dnaString)
        self.setDNA(self.dna)

    def setDNA(self, dna):
        if self.style:
            pass
        else:
            self.style = dna
            self.generateSuit()
            self.initializeDropShadow()
            self.initializeNametag3d()

    def generateSuit(self):
        dna = self.style
        self.headParts = []
        self.setPickable(1)
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        self.isSkeleton = 0
        self.isWaiter = 0
        self.isRental = 0
        self.isBloodsucker = 0
        self.isExecutive = 0
        self.isManager = 0
        if dna.name == 'f':
            self.scale = 4.0 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('flunky')
            self.generateHead('glasses')
            self.setHeight(4.88)
            self.setName('Flunky')
        elif dna.name == 'p':
            self.scale = 3.35 / bSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('pencilpusher')
            self.setHeight(5.0)
            self.setName('Pencil Pusher')
        elif dna.name == 'ym':
            self.scale = 4.125 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(5.28)
            self.setName('Yesman')
        elif dna.name == 'cj':
            self.scale = 4.25 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('gladhander')
            self.makeSkeleton()
            self.setHeight(5.28)
        elif dna.name == 'stk':
            self.scale = 4.25 / aSize
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(5.28)
        elif dna.name == 'mm':
            self.scale = 2.5 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('micromanager')
            self.setHeight(3.25)
            self.setName('Micro\x03manager')
        elif dna.name == 'ds':
            self.scale = 4.5 / bSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(6.08)
            self.setName('Downsizer')
        elif dna.name == 'hh':
            self.scale = 6.5 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('headhunter')
            self.setHeight(7.45)
            self.setName('Head Hunter')
        elif dna.name == 'cr':
            self.scale = 6.75 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.headTexture = 'corporate-raider.png'
            self.generateHead('flunky')
            self.setHeight(8.23)
            self.setName('Corporate Raider')
        elif dna.name == 'tbc':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(0.75, 0.95, 0.75, 1.0)
            self.generateBody()
            self.generateHead('bigcheese')
            self.setHeight(9.34)
            self.setName('The Big Cheese')
        elif dna.name == 'hho':
            self.scale = 7.3 / aSize
            self.handColor = VBase4(0.45, 0.45, 0.45, 1)
            self.generateBody()
            self.generateHead('headhoncho')
            self.setHeight(9.5)
        elif dna.name == 'acd':
            self.scale = 4.5 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(6.71)
        elif dna.name == 'cp':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(8.95)
        elif dna.name == 'dm':
            self.scale = 4.5 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.makeManager()
            self.generateBody()
            # self.headTexture = 'derrick.png'
            self.generateHead('grey-hat')
            self.setHeight(6.71)
        elif dna.name == 'hoo':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('headhunter')
            self.makeSkeleton()
            self.setHeight(8.27)
            self.setName('Head of Operations')
        elif dna.name == 'bf':
            self.scale = 4.0 / cSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'bottom-feeder.png'
            self.generateHead('tightwad')
            self.setHeight(4.81)
            self.setName('Bottom Feeder')
        elif dna.name == 'b':
            self.scale = 4.375 / bSize
            self.handColor = VBase4(0.95, 0.95, 1.0, 1.0)
            self.generateBody()
            self.makeBloodsucker()
            self.headTexture = 'blood-sucker.png'
            self.generateHead('movershaker')
            self.setHeight(6.17)
            self.setName('Bloodsucker')
        elif dna.name == 'dt':
            self.scale = 4.25 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'double-talker.png'
            self.generateHead('twoface')
            self.setHeight(5.63)
            self.setName('Double Talker')
            self.isSkeleton = 0
        elif dna.name == 'ptr':
            self.scale = 4.35 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(5.75)
            self.setName('Patronizer')
        elif dna.name == 'ac':
            self.scale = 4.35 / bSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('ambulancechaser')
            self.setHeight(6.39)
            self.setName('Ambulance Chaser')
        elif dna.name == 'bs':
            self.scale = 4.5 / aSize
            self.handColor = VBase4(0.5, 0.4, 0.75, 1.0)
            self.generateBody()
            self.generateHead('backstabber')
            self.setHeight(6.71)
            self.setName('Back Stabber')
        elif dna.name == 'sd':
            self.scale = 5.65 / bSize
            self.handColor = VBase4(0.5, 0.8, 0.75, 1.0)
            self.generateBody()
            self.headTexture = 'spin-doctor.png'
            self.generateHead('telemarketer')
            self.setHeight(7.9)
            self.setName('Spin Doctor')
        elif dna.name == 'cnt':
            self.setScale = 6.0 / aSize
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(7.5)
            self.setName('Canonist')
        elif dna.name == 'le':
            self.scale = 7.125 / aSize
            self.handColor = VBase4(0.25, 0.25, 0.5, 1.0)
            self.generateBody()
            self.generateHead('legaleagle')
            self.setHeight(8.27)
            self.setName('Legal Eagle')
        elif dna.name == 'bw':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.generateBody()
            self.generateHead('bigwig')
            self.setHeight(8.69)
            self.setName('Big Wig')
        elif dna.name == 'br':
            self.scale = 7.0 / bSize
            self.handColor = VBase4(0.45, 0.45, 0.45, 1)
            self.generateBody()
            self.generateHead('barrister')
            self.setHeight(8.69)
            self.setName('Barrister')
        elif dna.name == 'oo':
            self.scale = 7.0 / bSize
            self.handColor = SuitDNA.legalPolyColor
            self.setPickable(0)
            self.generateBody()
            self.headTexture = 'spin-doctor.png'
            self.generateHead('telemarketer')
            self.makeSkeleton()
            self.setHeight(8.69)
            self.setName('Office Overseer')
        elif dna.name == 'wsi':
            self.scale = 7.125 / aSize
            self.handColor = SuitDNA.legalPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('legaleagle')
            self.makeManager()
            self.makeSkeleton()
            self.setHeight(8.27)
            self.setName('The Witness Stand-\x04in')
        elif dna.name == 'sc':
            self.scale = 3.6 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.77)
            self.setName('Short Change')
            self.isSkeleton = 0
            self.isRental = 0
        elif dna.name == 'pp':
            self.scale = 3.55 / aSize
            self.handColor = VBase4(1.0, 0.5, 0.6, 1.0)
            self.generateBody()
            self.generateHead('pennypincher')
            self.setHeight(5.26)
            self.setName('Penny Pincher')
            self.isSkeleton = 0
        elif dna.name == 'tw':
            self.scale = 4.5 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('tightwad')
            self.setHeight(5.41)
            self.setName('Tightwad')
        elif dna.name == 'bc':
            self.scale = 4.4 / bSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(5.95)
            self.setName('Bean Counter')
        elif dna.name == 'nc':
            self.scale = 5.25 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('numbercruncher')
            self.setHeight(7.22)
            self.setName('Number Cruncher')
        elif dna.name == 'mbr':
            self.scale = 5.3 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('moneybags')
            self.makeSkeleton()
            self.setHeight(6.97)
            self.setName('Money Burner')
        elif dna.name == 'mb':
            self.scale = 5.7 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('moneybags')
            self.setHeight(7.32)
            self.setName('Money Bags')
        elif dna.name == 'ls':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0.5, 0.85, 0.75, 1.0)
            self.generateBody()
            self.generateHead('loanshark')
            self.setHeight(8.58)
            self.setName('Loan Shark')
        elif dna.name == 'sq':
            self.scale = 6.5 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.headTexture = 'slay-queen.png'
            self.generateHead('twoface')
            self.setHeight(8.5)
            self.setName('Slay Queen')
        elif dna.name == 'rb':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.headTexture = 'robber-baron.png'
            self.generateHead('yesman')
            self.setHeight(8.95)
            self.setName('Robber Baron')
        elif dna.name == 'bfh':
            self.scale = 7.8 / cSize
            self.handColor = VBase4(1.0, 0.3, 0.3, 1.0)
            self.generateBody()
            self.generateHead('bigfish')
            self.setHeight(9.7)
        elif dna.name == 'mpz':
            self.scale = 8.3 / aSize
            self.handColor = SuitDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(9.7)
        elif dna.name == 'msv':
            self.scale = 6.5 / cSize
            self.handColor = SuitDNA.moneyPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('gladhander')
            self.makeSkeleton()
            self.setHeight(7.5)
        elif dna.name == 'dam':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0.5, 0.85, 0.75, 1.0)
            self.setPickable(0)
            self.generateBody()
            self.generateHead('loanshark')
            self.makeSkeleton()
            self.setHeight(8.58)
        elif dna.name == 'cc':
            self.scale = 3.5 / cSize
            self.handColor = VBase4(0.55, 0.65, 1.0, 1.0)
            self.headColor = VBase4(0.25, 0.35, 1.0, 1.0)
            '''self.makeExecutive()'''
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.63)
        elif dna.name == 'tm':
            self.scale = 3.75 / bSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('telemarketer')
            self.setHeight(5.24)
        elif dna.name == 'nd':
            self.scale = 4.35 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'name-dropper.png'
            self.generateHead('numbercruncher')
            self.setHeight(5.98)
        elif dna.name == 'gh':
            self.scale = 4.75 / cSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('gladhander')
            self.setHeight(6.4)
        elif dna.name == 'ms':
            self.scale = 4.75 / bSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.headTexture = 'mover_shaker.png'
            self.generateHead('movershaker')
            self.setHeight(6.7)
        elif dna.name == 'acr':
            self.scale = 5.0 / bSize
            self.handColor = SuitDNA.salesPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('movershaker')
            self.makeSkeleton()
            self.setHeight(6.7)
        elif dna.name == 'tf':
            self.scale = 5.25 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('twoface')
            self.setHeight(6.95)
        elif dna.name == 'm':
            self.scale = 5.75 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'mingler.png'
            self.generateHead('twoface')
            self.setHeight(7.61)
        elif dna.name == 'opt':
            self.scale = 6.5 / aSize
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(7.0)
        elif dna.name == 'mh':
            self.scale = 7.0 / aSize
            self.handColor = SuitDNA.corpPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(8.95)
        elif dna.name == 'tl':
            self.scale = 7.3 / aSize
            self.handColor = VBase4(1.0, 1.0, 0.29, 1)
            self.generateBody()
            self.headTexture = 'skull.png'
            self.generateHead('toxicleader')
            self.setHeight(10)
        elif dna.name == 'gro':
            self.scale = 4.75 / bSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.generateHead('movershaker')
            self.makeSkeleton()
            self.setHeight(6.7)
        elif dna.name == 'ff':
            self.scale = 6.0 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('yesman')
            self.makeSkeleton()
            self.setHeight(7)
        elif dna.name == 'dpr':
            self.scale = 7.0 / cSize
            self.handColor = SuitDNA.salesPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('gladhander')
            self.makeManager()
            self.makeSkeleton()
            self.setHeight(8.95)
        elif dna.name == 'arc':
            self.scale = 5.25 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.setPickable(0)
            self.generateBody()
            self.generateHead('twoface')
            self.makeSkeleton()
            self.setHeight(6.95)
        elif dna.name == 'ws':
            self.scale = 5.75 / aSize
            self.handColor = SuitDNA.salesPolyColor
            self.generateBody()
            self.setPickable(0)
            self.generateHead('twoface')
            self.setHeight(7.61)
        if self.isExecutive and not self.style.name == 'acd':
            self.setName('Executive ' + SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        else:
            self.setName(SuitBattleGlobals.SuitAttributes[dna.name]['name'])
        self.getGeomNode().setScale(self.scale)
        self.generateHealthBar()
        if self.isSkeleton:
            pass
        else:
            self.generateCorporateMedallion()
        return

    def generateBody(self):
        animDict = self.generateAnimDict()
        filePrefix, bodyPhase = ModelDict[self.style.body]
        if base.config.GetBool('want-new-cogs', 0):
            if cogExists(filePrefix + 'zero.bam'):
                self.loadModel('phase_3.5' + filePrefix + 'zero')
            else:
                self.loadModel('phase_3.5' + filePrefix + 'mod')
        else:
            self.loadModel('phase_3.5' + filePrefix + 'mod')
        self.loadAnims(animDict)
        self.setSuitClothes()

    def generateAnimDict(self):
        animDict = {}
        filePrefix, bodyPhase = ModelDict[self.style.body]
        for anim in AllSuits:
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllSuitsMinigame:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]

        for anim in AllSuitsTutorialBattle:
            filePrefix, bodyPhase = TutorialModelDict[self.style.body]
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllSuitsBattle:
            animDict[anim[0]] = 'phase_5' + filePrefix + anim[1]

        if not base.config.GetBool('want-new-cogs', 0):
            if self.style.body == 'a':
                animDict['neutral'] = 'phase_4/models/char/suitA-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitA-' + anim[1]

            elif self.style.body == 'b':
                animDict['neutral'] = 'phase_4/models/char/suitB-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitB-' + anim[1]

            elif self.style.body == 'c':
                animDict['neutral'] = 'phase_3.5/models/char/suitC-neutral'
                for anim in SuitsCEOBattle:
                    animDict[anim[0]] = 'phase_12/models/char/suitC-' + anim[1]

        try:
            animList = eval(self.style.name)
        except NameError:
            animList = ()

        for anim in animList:
            phase = 'phase_' + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]

        return animDict

    def initializeBodyCollisions(self, collIdStr):
        Avatar.Avatar.initializeBodyCollisions(self, collIdStr)
        if not self.ghostMode:
            self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | ToontownGlobals.PieBitmask)

    def setSuitClothes(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        dept = self.style.dept

        def __doItTheOldWay__():
            if self.isExecutive or self.isManager:
                torsoTex = loader.loadTexture('phase_14/maps/e_blazer_%s.png' % (dept))
            else:
                if dept == 'g':
                    torsoTex = loader.loadTexture('phase_14/maps/g_blazer.png')
                else:
                    torsoTex = loader.loadTexture('phase_3.5/maps/%s_blazer.png' % (dept))
            torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
            torsoTex.setMagfilter(Texture.FTLinear)
            if self.isExecutive or self.isManager:
                legTex = loader.loadTexture('phase_14/maps/e_leg_%s.png' % (dept))
            else:
                if dept == 'g':
                    legTex = loader.loadTexture('phase_14/maps/g_leg.png')
                else:
                    legTex = loader.loadTexture('phase_3.5/maps/%s_leg.png' % (dept))
            legTex.setMinfilter(Texture.FTLinearMipmapLinear)
            legTex.setMagfilter(Texture.FTLinear)
            if self.isExecutive or self.isManager:
                armTex = loader.loadTexture('phase_14/maps/e_sleeve_%s.png' % (dept))
            else:
                if dept == 'g':
                    armTex = loader.loadTexture('phase_14/maps/g_sleeve.png')
                else:
                    armTex = loader.loadTexture('phase_3.5/maps/%s_sleeve.png' % (dept))
            armTex.setMinfilter(Texture.FTLinearMipmapLinear)
            armTex.setMagfilter(Texture.FTLinear)
            modelRoot.find('**/torso').setTexture(torsoTex, 1)
            modelRoot.find('**/arms').setTexture(armTex, 1)
            modelRoot.find('**/legs').setTexture(legTex, 1)
            modelRoot.find('**/hands').setColor(self.handColor)
            self.leftHand = self.find('**/joint_Lhold')
            self.rightHand = self.find('**/joint_Rhold')
            self.shadowJoint = self.find('**/joint_shadow')
            self.nametagJoint = self.find('**/joint_nameTag')

        if base.config.GetBool('want-new-cogs', 0):
            if dept == 'c':
                texType = 'bossbot'
            elif dept == 'l':
                texType = 'lawbot'
            elif dept == 'm':
                texType = 'cashbot'
            elif dept == 's':
                texType = 'sellbot'
            elif dept == 'g':
                texType = 'boardbot'
            if self.find('**/body').isEmpty():
                __doItTheOldWay__()
            else:
                filepath = 'phase_3.5/maps/tt_t_ene_' + texType + '.png'
                if cogExists('/maps/tt_t_ene_' + texType + '.png'):
                    bodyTex = loader.loadTexture(filepath)
                    self.find('**/body').setTexture(bodyTex, 1)
                self.leftHand = self.find('**/def_joint_left_hold')
                self.rightHand = self.find('**/def_joint_right_hold')
                self.shadowJoint = self.find('**/def_shadow')
                self.nametagJoint = self.find('**/def_nameTag')
        else:
            __doItTheOldWay__()

    def makeWaiter(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isWaiter = 1
        if self.isSkeleton:
            pass
        else:
            torsoTex = loader.loadTexture('phase_3.5/maps/waiter_blazer.png')
            torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
            torsoTex.setMagfilter(Texture.FTLinear)
            legTex = loader.loadTexture('phase_14/maps/e_leg_l.png')
            legTex.setMinfilter(Texture.FTLinearMipmapLinear)
            legTex.setMagfilter(Texture.FTLinear)
            armTex = loader.loadTexture('phase_14/maps/count_sleeve.png')
            armTex.setMinfilter(Texture.FTLinearMipmapLinear)
            armTex.setMagfilter(Texture.FTLinear)
            modelRoot.find('**/torso').setTexture(torsoTex, 1)
            modelRoot.find('**/arms').setTexture(armTex, 1)
            modelRoot.find('**/legs').setTexture(legTex, 1)

    def makeBloodsucker(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isBloodsucker = 1
        torsoTex = loader.loadTexture('phase_14/maps/count_blazer.png')
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_14/maps/e_leg_l.png')
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_14/maps/count_sleeve.png')
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)

    def makeExecutive(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isExecutive = 1
        dept = self.style.dept
        torsoTex = loader.loadTexture('phase_14/maps/e_blazer_%s.png' % (dept))
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_14/maps/e_leg_%s.png' % (dept))
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_14/maps/e_sleeve_%s.png' % (dept))
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)

    def makeManager(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isManager = 1
        dept = self.style.dept
        torsoTex = loader.loadTexture('phase_14/maps/e_blazer_%s.png' % (dept))
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_14/maps/e_leg_%s.png' % (dept))
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_14/maps/e_sleeve_%s.png' % (dept))
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        nameInfo = '%(name)s\n%(dept)s\nLevel %(level)s\nManager' % {'name': self._name,
         'dept': dept,
         'level': self.getActualLevel()}

    def makeRentalSuit(self, suitType, modelRoot = None):
        if not modelRoot:
            modelRoot = self.getGeomNode()
        handTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_hand.png')
        if suitType == 'g':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_boardbotRental_blazer.png')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_boardbotRental_leg.png')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_boardbotRental_sleeve.png')
        elif suitType == 's':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_blazer.png')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_leg.png')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_sleeve.png')
        elif suitType == 'm':
            torsoTex = loader.loadTexture('phase_14/maps/ttr_t_ene_cashbotRental_blazer.png')
            legTex = loader.loadTexture('phase_14/maps/ttr_t_ene_cashbotRental_leg.png')
            armTex = loader.loadTexture('phase_14/maps/ttr_t_ene_cashbotRental_sleeve.png')
        elif suitType == 'l':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_lawbotRental_blazer.jpg')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_lawbotRental_leg.jpg')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_lawbotRental_sleeve.jpg')
        elif suitType == 'c':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_bossbotRental_blazer.jpg')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_bossbotRental_leg.jpg')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_bossbotRental_sleeve.jpg')
        else:
            self.notify.warning('No rental suit for cog type %s' % suitType)
            return
        self.isRental = 1
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
        modelRoot.find('**/hands').setTexture(handTex, 1)

    def generateHead(self, headType):
        if base.config.GetBool('want-new-cogs', 0):
            filePrefix, phase = HeadModelDict[self.style.body]
        else:
            filePrefix, phase = ModelDict[self.style.body]
        try:
            headModel = loader.loadModel('phase_' + str(phase) + filePrefix + 'heads')
        except:
            headModel = loader.loadModel('phase_14/models/char/')
        headReferences = headModel.findAllMatches('**/' + headType)
        for i in xrange(0, headReferences.getNumPaths()):
            if base.config.GetBool('want-new-cogs', 0):
                headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'to_head')
                if not headPart:
                    headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint_head')
            else:
                headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint_head')
            if self.headTexture:
                try:
                    headTex = loader.loadTexture('phase_' + str(phase) + '/maps/' + self.headTexture)
                except:
                    headTex = loader.loadTexture('phase_14/maps/' + self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex, 1)
            if self.headColor:
                headPart.setColor(self.headColor)
            self.headParts.append(headPart)

        headModel.removeNode()

    def generateCorporateTie(self, modelPath = None):
        if not modelPath:
            modelPath = self
        dept = self.style.dept
        tie = modelPath.find('**/tie')
        if tie.isEmpty():
            self.notify.warning('Skelecog has no tie model!')
            return
        if self.style.name == 'hoo':
            if self.isExecutive or self.isManager:
                tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_sales_exec.png')
            else:
                tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_sales.png')
        elif self.style.name == 'acd':
            tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_boss_exec.png')
        else:
            if dept == 'c':
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_boss_exec.png')
                else:
                    tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_boss.png')
            elif dept == 'l':
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_legal_exec.png')
                else:
                    tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_legal.png')
            elif dept == 'm':
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_money_exec.png')
                else:
                    tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_money.png')
            elif dept == 's':
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_sales_exec.png')
                else:
                    tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_sales.png')
            elif dept == 'g':
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_board_exec.png')
                else:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_board.png')
            else:
                if self.isExecutive or self.isManager:
                    tieTex = loader.loadTexture('phase_14/maps/cog_robot_tie_exec.png')
                else:
                    pass
        tieTex.setMinfilter(Texture.FTLinearMipmapLinear)
        tieTex.setMagfilter(Texture.FTLinear)
        tie.setTexture(tieTex, 1)

    def generateCorporateMedallion(self):
        icons = loader.loadModel('phase_3/models/gui/cog_icons')
        dept = self.style.dept
        if base.config.GetBool('want-new-cogs', 0):
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint_attachMeter')
        else:
            chestNull = self.find('**/joint_attachMeter')
        if dept == 'c':
            self.corpMedallion = icons.find('**/CorpIcon').copyTo(chestNull)
        elif dept == 'l':
            self.corpMedallion = icons.find('**/LegalIcon').copyTo(chestNull)
        elif dept == 'm':
            self.corpMedallion = icons.find('**/MoneyIcon').copyTo(chestNull)
        elif dept == 's':
            self.corpMedallion = icons.find('**/SalesIcon').copyTo(chestNull)
        elif dept == 'g':
            self.corpMedallion = icons.find('**/CorpIcon').copyTo(chestNull)
        self.corpMedallion.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
        self.corpMedallion.setColor(self.medallionColors[dept])
        icons.removeNode()

    def generateHealthBar(self):
        self.removeHealthBar()
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        if base.config.GetBool('want-new-cogs', 0):
            chestNull = self.find('**/def_joint_attachMeter')
            if chestNull.isEmpty():
                chestNull = self.find('**/joint_attachMeter')
        else:
            chestNull = self.find('**/joint_attachMeter')
        button.reparentTo(chestNull)
        self.healthBar = button
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(self.healthGlowColors[0])
        button.flattenLight()
        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0

    def reseatHealthBarForSkele(self):
        self.healthBar.setPos(0.0, 0.1, 0.0)

    def updateHealthBar(self, hp, forceUpdate = 0):
        if hp > self.currHP:
            hp = self.currHP
        self.currHP -= hp
        health = float(self.currHP) / float(self.maxHP)
        if health > 0.95:
            condition = 0
        elif health > 0.9:
            condition = 1
        elif health > 0.8:
            condition = 2
        elif health > 0.7:
            condition = 3
        elif health > 0.6:
            condition = 4
        elif health > 0.5:
            condition = 5
        elif health > 0.3:
            condition = 6
        elif health > 0.15:
            condition = 7
        elif health > 0.05:
            condition = 8
        elif health > 0.0:
            condition = 9
        else:
            condition = 10
        if self.healthCondition != condition or forceUpdate:
            if condition == 9:
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            elif condition == 10:
                if self.healthCondition == 9:
                    taskMgr.remove(self.uniqueName('blink-task'))
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            else:
                self.healthBar.setColor(self.healthColors[condition], 1)
                self.healthBarGlow.setColor(self.healthGlowColors[condition], 1)
            self.healthCondition = condition

    def __blinkRed(self, task):
        self.healthBar.setColor(Vec4(1, 0, 0, 1), 1)
        self.healthBarGlow.setColor(Vec4(1, 0.25, 0.25, 0.5), 1) # If failure is present: self.healthBarGlow.setColor(self.healthGlowColors[8], 1)
        if self.healthCondition == 10:
            self.healthBar.setScale(1.17)
        return Task.done

    def __blinkGray(self, task):
        if not self.healthBar:
            return
        self.healthBar.setColor(Vec4(0.3, 0.3, 0.3, 1), 1)
        self.healthBarGlow.setColor(Vec4(0.3, 0.3, 0.3, 0), 1)
        if self.healthCondition == 10:
            self.healthBar.setScale(1.0)
        return Task.done

    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        if self.healthCondition == 9 or self.healthCondition == 10:
            taskMgr.remove(self.uniqueName('blink-task'))
        self.healthCondition = 0
        return

    def getLoseActor(self):
        if base.config.GetBool('want-new-cogs', 0):
            if self.find('**/body'):
                return self
        if self.loseActor == None:
            if not self.isSkeleton:
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseModel = 'phase_' + str(phase) + filePrefix + 'lose-mod'
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                loseNeck = self.loseActor.find('**/joint_head')
                for part in self.headParts:
                    part.instanceTo(loseNeck)

                if self.isWaiter:
                    self.makeWaiter(self.loseActor)
                elif self.isExecutive:
                    self.makeExecutive(self.loseActor)
                elif self.isManager:
                    self.makeManager(self.loseActor)
                elif self.isBloodsucker:
                    self.makeBloodsucker(self.loseActor)
                else:
                    self.setSuitClothes(self.loseActor)
            else:
                loseModel = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-lose-mod'
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                self.generateCorporateTie(self.loseActor)
        self.loseActor.setScale(self.scale)
        self.loseActor.setPos(self.getPos())
        self.loseActor.setHpr(self.getHpr())
        shadowJoint = self.loseActor.find('**/joint_shadow')
        dropShadow = loader.loadModel('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        dropShadow.reparentTo(shadowJoint)
        return self.loseActor

    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if self.loseActor != None:
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        self.loseActor = None
        return

    def makeSkeleton(self):
        model = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-zero'
        anims = self.generateAnimDict()
        anim = self.getCurrentAnim()
        dept = self.style.dept
        self.removePart('modelRoot')
        self.loadModel(model)
        self.loadAnims(anims)
        self.getGeomNode().setScale(self.scale * 1.0173)
        if self.style.name == 'acd':
            self.getGeomNode().setColor(0.95, 0.75, 0.75, 1.0)
        else:
            if self.isExecutive or self.isManager:
                if dept == 'c':
                    self.getGeomNode().setColor(0.95, 0.75, 0.75, 1.0)
                elif dept == 'l':
                    self.getGeomNode().setColor(0.75, 0.75, 0.95, 1.0)
                elif dept == 'm':
                    self.getGeomNode().setColor(0.65, 0.95, 0.85, 1.0)
                elif dept == 's':
                    self.getGeomNode().setColor(0.95, 0.75, 0.95, 1.0)
                elif dept == 'g':
                    self.getGeomNode().setColor(0.45, 0.45, 0.45, 1.0)
                else:
                    self.getGeomNode().setColor(0.5, 0.5, 0.5, 1.0)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        self.generateCorporateTie()
        self.setHeight(self.height)
        parts = self.findAllMatches('**/pPlane*')
        for partNum in xrange(0, parts.getNumPaths()):
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)

        
        if self.isExecutive:
            self.setName('Executive Skelecog')
            nameInfo = '%(name)s\n%(dept)s\n%(level)s' % {'name': 'Executive Skelecog',
             'dept': dept,
             'level': self.getActualLevel()}
        else:
            self.setName('Skelecog')
            nameInfo = '%(name)s\n%(dept)s\n%(level)s' % {'name': 'Skelecog',
             'dept': dept,
             'level': self.getActualLevel()}
        self.leftHand = self.find('**/joint_Lhold')
        self.rightHand = self.find('**/joint_Rhold')
        self.nametagNull = self.find('**/joint_nameTag')
        self.loop(anim)
        self.isSkeleton = 1
    
    
    # Placeholder until this can be called from SuitBase.py successfully.
    def getActualLevel(self):
        if hasattr(self, 'dna'):
            return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1
        else:
            self.notify.warning('called getActualLevel with no DNA, returning 1 for level')
            return 1

    # Placeholder until this can be called from SuitBase.py successfully.
    def getStyleDept(self):
        if hasattr(self, 'dna') and self.dna:
            return SuitDNA.getDeptFullname(self.dna.dept)
        else:
            self.notify.error('called getStyleDept() before dna was set!')
            return 'unknown'

    def getHeadParts(self):
        return self.headParts

    def getRightHand(self):
        return self.rightHand

    def getLeftHand(self):
        return self.leftHand

    def getShadowJoint(self):
        return self.shadowJoint

    def getNametagJoints(self):
        return []

    def getDialogueArray(self):
        if self.isSkeleton or self.style.name == 'br':
            loadSkelDialog()
            return SkelSuitDialogArray
        else:
            return SuitDialogArray
    
    def getModel(self):
        return model
