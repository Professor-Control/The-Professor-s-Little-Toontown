import random
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from toontown.toonbase import TTLocalizer
notify = DirectNotifyGlobal.directNotify.newCategory('SuitDialog')

def getBrushOffIndex(suitName):
    if suitName in SuitBrushOffs:
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = ["It's my day off.",
         "I believe you're in the wrong office.",
         'Have your people call my people.',
         "You're in no position to meet with me.",
         'Talk to my assistant.',
         "I'll pretend I don't see you, Toon."]
    num = len(brushoffs)
    chunk = 100 / num
    randNum = random.randint(0, 99)
    count = chunk
    for i in xrange(num):
        if randNum < count:
            return i
        count += chunk

    notify.error('getBrushOffs() - no brush off found!')
    return


def getBrushOffText(suitName, index):
    if suitName in SuitBrushOffs:
        brushoffs = SuitBrushOffs[suitName]
    else:
        brushoffs = ["It's my day off.",
         "I believe you're in the wrong office.",
         'Have your people call my people.',
         "You're in no position to meet with me.",
         'Talk to my assistant.',
         "I'll pretend I don't see you, Toon."]
    return brushoffs[index]


SuitBrushOffs = {'f': ["I'm late for a meeting."],
 'p': ['Push off.'],
 'ym': ['Yes, but maybe another time.'],
 'ds': ["I'm not down for a fight."],
 'tbc': ["Sorry, you're not cultured enough to fight me.",
         "Don't you think I'm too big to fight you?"],
 'bf': ["I'm not interested in trash right now."],
 'dt': ['Talk to the head.'],
 'ac': ["I'm on the run!"],
 'bs': ["Don't worry, I'll be back for you soon.",
        'Back off, Toon.'],
 'sd': ['The doctor is out.',
        "You'll have to make an appointment, I'm busy."],
 'bw': ["Don't you think I'm too big to fight you?",
        "If I'm late, there will be a price toupee."],
 'bfh': ['Just keep swimming, Toon.',
         "Don't you think I'm too big to fight you?"],
 'nd': ["I'm going golfing with 'Glad Hander'."],
 'ms': ["I'm moving away, Toon.",
        'Move out of my way, Toon.'],
 'mh': ["I'm on commercial break."],
 'tl': ["I shouldn't waste my time on you."]}
