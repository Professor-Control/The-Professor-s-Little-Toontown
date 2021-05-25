from toontown.suit import SuitDNA
import types
from direct.showbase import PythonUtil
PartsPerSuit = (17,
 14,
 12,
 10)
PartsPerSuitBitmasks = (131071,
 130175,
 56447,
 56411)
AllBits = 131071
MinPartLoss = 2
MaxPartLoss = 4
MeritsPerLevel = ((100,
  130,
  160,
  190,
  220,
  250,
  280,
  800), # Add thirty to previous amount before last which remains 800
 (160,
  210,
  260,
  310,
  360,
  410,
  460,
  1300), # Add fifty to previous amount before last which remains 1300
 (260,
  340,
  420,
  500,
  580,
  660,
  740,
  2100), # Add eighty to previous amount before last which remains 2100
 (420,
  550,
  680,
  810,
  940,
  1070,
  1200,
  3400), # Add 130 to previous amount before last which remains 3400
 (680,
  890,
  1100,
  1310,
  1520,
  1730,
  1950,
  5500), # Add 210 to previous amount before last which remains 5500
 (1100,
  1440,
  1780,
  2120,
  2460,
  2800,
  3140,
  8900), # Add 340 to previous amount before last which remains 8900
 (1780,
  2330,
  2880,
  3430,
  3980,
  4530,
  5080,
  14400), # Add 550 to previous amount before last which remains 14400
 (2880,
  3770,
  4660,
  5550,
  6440,
  7330,
  8220,
  23300), # Add 890 to previous amount before last which remains 23300
 (2880,
  3770,
  4660,
  5550,
  6440,
  7330,
  8220,
  9110,
  10000,
  10890,
  11780,
  12670,
  13560,
  14450,
  15340,
  16230,
  17120,
  18010,
  18900,
  19790,
  20680,
  21570,
  22460,
  23350,
  24240,
  25130,
  26020,
  26910,
  27800,
  28690,
  29580,
  30470,
  31360,
  32250,
  33140,
  34030,
  34920,
  35810,
  36700,
  37590,
  38480,
  0), # Pattern to be determined, current pattern looks off the Defense Attorney's which is to add 890 to the previous amount before the last which remains 0
 (60,
  80,
  100,
  120,
  140,
  160,
  180,
  500), # Add twenty to previous amount before last which remains 500
 (100,
  130,
  160,
  190,
  220,
  250,
  280,
  800), # Add thirty to previous amount before last which remains 800
 (160,
  210,
  260,
  310,
  360,
  410,
  460,
  1300), # Add fifty to previous amount before last which remains 1300
 (260,
  340,
  420,
  500,
  580,
  660,
  740,
  2100), # Add eighty to previous amount before last which remains 2100
 (420,
  550,
  680,
  810,
  940,
  1070,
  1200,
  3400), # Add 130 to previous amount before last which remains 3400
 (680,
  890,
  1100,
  1310,
  1520,
  1730,
  1940,
  5500), # Add 210 to previous amount before last which remains 5500
 (1100,
  1440,
  1780,
  2120,
  2460,
  2800,
  3140,
  8900), # Add 340 to previous amount before last which remains 8900
 (1780,
  2330,
  2880,
  3430,
  3980,
  4530,
  5080,
  14400), # Add 550 to previous amount before last which remains 14400
 (2880,
  3770,
  4660,
  5550,
  6440,
  7330,
  8220,
  9110,
  10000,
  10890,
  11780,
  12670,
  13560,
  14450,
  15340,
  16230,
  17120,
  18010,
  18900,
  19790,
  20680,
  21570,
  22460,
  23350,
  24240,
  25130,
  26020,
  26910,
  27800,
  28690,
  29580,
  30470,
  31360,
  32250,
  33140,
  34030,
  34920,
  35810,
  36700,
  37590,
  38480,
  0), # Add 890 to previous amount before last which remains 0
 (40,
  50,
  60,
  70,
  80,
  90,
  100,
  300), # Add ten to previous amount before last which remains 300
 (60,
  80,
  100,
  120,
  140,
  160,
  180,
  500), # Add twenty to previous amount before last which remains 500
 (100,
  130,
  160,
  190,
  220,
  250,
  280,
  800), # Add thirty to previous amount before last which remains 800
 (160,
  210,
  260,
  310,
  360,
  410,
  460,
  1300), # Add fifty to previous amount before last which remains 1300
 (260,
  340,
  420,
  500,
  580,
  660,
  740,
  2100), # Add eighty to previous amount before last which remains 2100
 (420,
  550,
  680,
  810,
  940,
  1070,
  1200,
  3400), # Add 130 to previous amount before last which remains 3400
 (680,
  890,
  1100,
  1310,
  1520,
  1730,
  1950,
  5500), # Add 210 to previous amount before last which remains 5500
 (1100,
  1440,
  1780,
  2120,
  2460,
  2800,
  3140,
  8900), # Add 340 to previous amount before last which remains 8900
 (1780,
  2330,
  2880,
  3430,
  3980,
  4530,
  5080,
  5630,
  6180,
  6730,
  7280,
  7830,
  8380,
  8930,
  9480,
  10030,
  10580,
  11130,
  11680,
  12230,
  12780,
  13330,
  13880,
  14430,
  14980,
  15530,
  16080,
  16630,
  17180,
  17730,
  18280,
  18830,
  19380,
  19930,
  20480,
  21030,
  21580,
  22130,
  22130,
  22130,
  22130,
  0), # Add 550 to previous amount before last which remains 550
 (20,
  30,
  40,
  50,
  60,
  70,
  80,
  200), # Add ten to previous amount before last which remains 200
 (40,
  50,
  60,
  70,
  80,
  90,
  100,
  300), # Add ten to previous amount before last which remains 300
 (60,
  80,
  100,
  120,
  140,
  160,
  180,
  500), # Add twenty to previous amount before last which remains 500
 (100,
  130,
  160,
  190,
  220,
  250,
  280,
  800), # Add thirty to previous amount before last which remains 800
 (160,
  210,
  260,
  310,
  360,
  410,
  460,
  1300), # Add fifty to previous amount before last which remains 1300
 (260,
  340,
  420,
  500,
  580,
  660,
  740,
  2100), # Add eighty to previous amount before last which remains 2100
 (420,
  550,
  680,
  810,
  940,
  1070,
  1200,
  3400), # Add 130 to previous amount before last which remains 3400
 (680,
  890,
  1100,
  1310,
  1520,
  1730,
  1950,
  5500), # Add 210 to previous amount before last which remains 5500
 (1100,
  1440,
  1780,
  2120,
  2460,
  2800,
  3140,
  3480,
  3820,
  4160,
  4500,
  4840,
  5180,
  5520,
  5860,
  6200,
  6540,
  6880,
  7220,
  7560,
  7900,
  8240,
  8580,
  8920,
  9260,
  9600,
  9940,
  10280,
  10620,
  10960,
  11300,
  11640,
  11980,
  12320,
  12660,
  13000,
  13340,
  13680,
  14020,
  14360,
  14700,
  0), # Add 340 to previous amount before last which remains 0
 (20,
  30,
  40,
  50,
  60,
  70,
  80,
  200), # Add ten to previous amount before last which remains 200
 (40,
  50,
  60,
  70,
  80,
  90,
  100,
  300), # Add ten to previous amount before last which remains 300
 (60,
  80,
  100,
  120,
  140,
  160,
  180,
  500), # Add twenty to previous amount before last which remains 500
 (100,
  130,
  160,
  190,
  220,
  250,
  280,
  800), # Add thirty to previous amount before last which remains 800
 (160,
  210,
  260,
  310,
  360,
  410,
  460,
  1300), # Add fifty to previous amount before last which remains 1300
 (260,
  340,
  420,
  500,
  580,
  660,
  740,
  2100), # Add eighty to previous amount before last which remains 2100
 (420,
  550,
  680,
  810,
  940,
  1070,
  1200,
  3400), # Add 130 to previous amount before last which remains 3400
 (680,
  890,
  1100,
  1310,
  1520,
  1730,
  1950,
  5500), # Add 210 to previous amount before last which remains 5500
 (1100,
  1440,
  1780,
  2120,
  2460,
  2800,
  3140,
  3480,
  3820,
  4160,
  4500,
  4840,
  5180,
  5520,
  5860,
  6200,
  6540,
  6880,
  7220,
  7560,
  7900,
  8240,
  8580,
  8920,
  9260,
  9600,
  9940,
  10280,
  10620,
  10960,
  11300,
  11640,
  11980,
  12320,
  12660,
  13000,
  13340,
  13680,
  14020,
  14360,
  14700,
  0)) # Add 340 to previous amount before last which remains 0
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
upperTorso = torsoLeftShoulder
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper,
 rightLegUpper,
 torsoLeftShoulder,
 leftArmUpper,
 rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper,
 rightLegFoot + rightLegLower + rightLegUpper,
 torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder,
 leftArmHand + leftArmLower + leftArmUpper,
 rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = ('Upper Left Leg',
 'Lower Left Leg',
 'Left Foot',
 'Upper Right Leg',
 'Lower Right Leg',
 'Right Foot',
 'Left Shoulder',
 'Right Shoulder',
 'Chest',
 'Health Meter',
 'Pelvis',
 'Upper Left Arm',
 'Lower Left Arm',
 'Left Hand',
 'Upper Right Arm',
 'Lower Right Arm')
SimplePartNameStrings = ('Upper Torso',)
PartsQueryNames = ({1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: PartNameStrings[6],
  128: PartNameStrings[7],
  256: PartNameStrings[8],
  512: PartNameStrings[9],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: 'Right Hand'},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: 'Right Hand'},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]})
suitTypes = PythonUtil.Enum(('NoSuit', 'NoMerits', 'FullSuit'))

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    needMask = PartsPerSuitBitmasks[dept] & PartsQueryMasks[partIndex]
    haveMask = parts[dept] & PartsQueryMasks[partIndex]
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        index += 1


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in xrange(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0

    return 1


def isPaidSuitComplete(av, parts, dept):
    isPaid = 0
    base = getBase()
    if av and av.getGameAccess() == 2:
        isPaid = 1
    if isPaid:
        if isSuitComplete(parts, dept):
            return 1
    return 0


def getTotalMerits(toon, index):
    from toontown.battle import SuitBattleGlobals
    cogIndex = toon.cogTypes[index] + SuitDNA.suitsPerDept * index
    cogTypeStr = SuitDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, len(MeritsPerLevel[cogIndex]) - 1), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 32):
    sum = 0
    for shift in xrange(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)

    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1

    str = ''
    for i in xrange(0, len(array)):
        str = str + array[i]

    return str


def asNumber(bitstring):
    num = 0
    for i in xrange(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)

    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = SuitDNA.suitDepts.index(dept)
    return dept
