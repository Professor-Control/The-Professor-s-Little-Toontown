from panda3d.core import *
from panda3d.toontown import *
from direct.distributed.ClockDelta import *
import math
import random
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
import SuitTimings
import SuitDNA
TIME_BUFFER_PER_WPT = 0.25
TIME_DIVISOR = 100
DISTRIBUTE_TASK_CREATION = 0

class SuitBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitBase')

    def __init__(self):
        self.level = 0
        self.dna = None
        self.maxHP = 10
        self.currHP = 10
        self.isSkelecog = 0
        self.isExecutive = 0
        self.isManager = 0
        self.isBloodsucker = 0
        return

    def delete(self):
        pass

    def getStyleName(self):
        if hasattr(self, 'dna') and self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'

    def getStyleDept(self):
        if hasattr(self, 'dna') and self.dna:
            return SuitDNA.getDeptFullname(self.dna.dept)
        else:
            self.notify.error('called getStyleDept() before dna was set!')
            return 'unknown'

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level
        if self.isManager:
            nameWLevel = '%(name)s\n%(dept)s\nLevel %(level)s\nManager' % {'name': self.name,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
        else:
            nameWLevel = '%(name)s\n%(dept)s\nLevel %(level)s' % {'name': self.name,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
        self.setDisplayName(nameWLevel)
        attributes = SuitBattleGlobals.SuitAttributes[self.dna.name]
        if self.isExecutive:
            self.maxHP = attributes['hp'][self.level] * 1.5
        else:
            self.maxHP = attributes['hp'][self.level]
        self.currHP = self.maxHP

    def getSkelecog(self):
        return self.isSkelecog

    def setSkelecog(self, flag):
        self.isSkelecog = flag

    def getBloodsucker(self):
        return self.isBloodsucker

    def setBloodsucker(self, flag):
        self.isBloodsucker = flag

    def getExecutive(self):
        return self.isExecutive

    def setExecutive(self, flag):
        self.isExecutive = flag

    def getManager(self):
        return self.isManager

    def setManager(self, flag):
        self.isManager = flag

    def getActualLevel(self):
        if hasattr(self, 'dna'):
            return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1
        else:
            self.notify.warning('called getActualLevel with no DNA, returning 1 for level')
            return 1

    def setPath(self, path):
        self.path = path
        self.pathLength = self.path.getNumPoints()

    def getPath(self):
        return self.path

    def printPath(self):
        print '%d points in path' % self.pathLength
        for currPathPt in xrange(self.pathLength):
            indexVal = self.path.getPointIndex(currPathPt)
            print '\t', self.sp.dnaStore.getSuitPointWithIndex(indexVal)

    def makeLegList(self):
        self.legList = SuitLegList(self.path, self.sp.dnaStore, self.sp.suitWalkSpeed, SuitTimings.fromSky, SuitTimings.toSky, SuitTimings.fromSuitBuilding, SuitTimings.toSuitBuilding, SuitTimings.toToonBuilding)
