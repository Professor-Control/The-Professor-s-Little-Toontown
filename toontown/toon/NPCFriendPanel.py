from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *
import NPCToons
import ToonHead
import ToonDNA
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals

class NPCFriendPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('NPCFriendPanel')

    def __init__(self, parent = aspect2d, **kw):
        optiondefs = (('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent=parent)
        self.cardList = []
        self.updateLayout()
        self.initialiseoptions(NPCFriendPanel)
        self.accept(localAvatar.uniqueName('maxNPCFriendsChange'), self.updateLayout)
        return None

    def update(self, friendDict, fCallable = 0):
        friendList = friendDict.keys()
        for i in xrange(self.maxNPCFriends):
            card = self.cardList[i]
            try:
                NPCID = friendList[i]
                count = friendDict[NPCID]
            except IndexError:
                NPCID = None
                count = 0

            card.update(NPCID, count, fCallable)

        return

    def updateLayout(self):
        for card in self.cardList:
            card.destroy()

        self.cardList = []
        self.maxNPCFriends = localAvatar.getMaxNPCFriends()
        rotateCard = False
        if self.maxNPCFriends == 8:
            rotateCard = True
            xOffset = -5.25
            yOffset = 2.3
            yOffset2 = -4.7
        elif self.maxNPCFriends == 16:
            xOffset = -5.2
            yOffset = 3.5
            yOffset2 = -2.45
        else:
            self.notify.error('got wrong max SOS cards %s' % self.maxNPCFriends)
        count = 0
        for i in xrange(self.maxNPCFriends):
            card = NPCFriendCard(parent=self, rotateCard=rotateCard, doneEvent=self['doneEvent'])
            self.cardList.append(card)
            card.setPos(xOffset, 1, yOffset)
            card.setScale(0.75)
            xOffset += 3.5
            count += 1
            if count % 4 == 0:
                xOffset = -5.25
                yOffset += yOffset2


class NPCFriendCard(DirectFrame):
    normalTextColor = (0.3, 0.25, 0.2, 1)
    maxRarity = 5
    sosTracks = ToontownBattleGlobals.Tracks + ToontownBattleGlobals.NPCTracks

    def __init__(self, parent = aspect2dp, rotateCard = False, **kw):
        optiondefs = (('NPCID', 'Uninitialized', None), ('relief', None, None), ('doneEvent', None, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent=parent)
        self.initialiseoptions(NPCFriendCard)
        cardModel = loader.loadModel('phase_3.5/models/gui/playingCard')
        self.front = DirectFrame(parent=self, relief=None, image=cardModel.find('**/card_front'))
        self.front.hide()
        self.back = DirectFrame(parent=self, relief=None, image=cardModel.find('**/card_back'), geom=cardModel.find('**/logo'))
        callButtonPosZ = -0.9
        textWordWrap = 16.0
        textScale = 0.35
        textPosZ = 1.15
        nameScale = 0.4
        namePosZ = -0.45
        rarityScale = 0.2
        rarityPosZ = -1.2
        self.NPCHeadDim = 1.2
        self.NPCHeadPosZ = 0.45
        self.sosCountInfoPosZ = -0.9
        self.sosCountInfoScale = 0.4
        self.sosCountInfo2PosZ = -0.9
        self.sosCountInfo2Scale = 0.5
        if rotateCard:
            self.front.component('image0').configure(pos=(0, 0, 0.22), hpr=(0, 0, -90), scale=1.35)
            self.back.component('image0').configure(hpr=(0, 0, -90), scale=(-1.35, 1.35, 1.35))
            callButtonPosZ = -2.1
            textWordWrap = 7.0
            textScale = 0.5
            textPosZ = 2.0
            nameScale = 0.5
            namePosZ = -0.89
            rarityScale = 0.25
            rarityPosZ = -2.4
            self.NPCHeadDim = 1.8
            self.NPCHeadPosZ = 0.4
            self.sosCountInfoPosZ = -2.1
            self.sosCountInfoScale = 0.4
            self.sosCountInfo2PosZ = -2.0
            self.sosCountInfo2Scale = 0.55
        self.sosTypeInfo = DirectLabel(parent=self.front, relief=None, text='', text_font=ToontownGlobals.getMinnieFont(), text_fg=self.normalTextColor, text_scale=textScale, text_align=TextNode.ACenter, text_wordwrap=textWordWrap, pos=(0, 0, textPosZ))
        self.NPCHead = None
        self.NPCName = DirectLabel(parent=self.front, relief=None, text='', text_fg=self.normalTextColor, text_scale=nameScale, text_align=TextNode.ACenter, text_wordwrap=8.0, pos=(0, 0, namePosZ))
        buttonModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        upButton = buttonModels.find('**/InventoryButtonUp')
        downButton = buttonModels.find('**/InventoryButtonDown')
        rolloverButton = buttonModels.find('**/InventoryButtonRollover')
        self.sosCallButton = DirectButton(parent=self.front, relief=None, text=TTLocalizer.NPCCallButtonLabel, text_fg=self.normalTextColor, text_scale=0.28, text_align=TextNode.ACenter, image=(upButton,
         downButton,
         rolloverButton,
         upButton), image_color=(1.0, 0.2, 0.2, 1), image0_color=Vec4(1.0, 0.4, 0.4, 1), image3_color=Vec4(1.0, 0.4, 0.4, 0.4), image_scale=(4.4, 1, 3.6), image_pos=Vec3(0, 0, 0.08), pos=(-1.15, 0, callButtonPosZ), scale=1.25, command=self.__chooseNPCFriend)
        self.sosCallButton.hide()
        self.sosCountInfo = DirectLabel(parent=self.front, relief=None, text='', text_fg=self.normalTextColor, text_scale=0.75, text_align=TextNode.ALeft, textMayChange=1, pos=(0.0, 0, -1.0))
        star = loader.loadModel('phase_3.5/models/gui/name_star')
        self.rarityStars = []
        for i in xrange(self.maxRarity):
            label = DirectLabel(parent=self.front, relief=None, image=star, image_scale=rarityScale, image_color=Vec4(0.502, 0.251, 0.251, 1.0), pos=(1.1 - i * 0.24, 0, rarityPosZ))
            label.hide()
            self.rarityStars.append(label)

        return

    def __chooseNPCFriend(self):
        if self['NPCID'] and self['doneEvent']:
            doneStatus = {}
            doneStatus['mode'] = 'NPCFriend'
            doneStatus['friend'] = self['NPCID']
            messenger.send(self['doneEvent'], [doneStatus])

    def destroy(self):
        if self.NPCHead:
            self.NPCHead.detachNode()
            self.NPCHead.delete()
        DirectFrame.destroy(self)

    def update(self, NPCID, count = 0, fCallable = 0):
        oldNPCID = self['NPCID']
        self['NPCID'] = NPCID
        if NPCID != oldNPCID:
            if self.NPCHead:
                self.NPCHead.detachNode()
                self.NPCHead.delete()
            if NPCID is None:
                self.showBack()
                return
            self.front.show()
            self.back.hide()
            self.NPCName['text'] = {20000: 'Tutorial Tom',
             999: 'Toon Tailor',
             1000: 'Toon HQ',
             20001: 'Flippy',
             2001: 'Flippy',
             2002: 'Banker Bob',
             2003: 'Professor Pete',
             2004: 'Tammy the Tailor',
             2005: 'Librarian Larry',
             2006: 'Clerk Clark',
             2007: 'HQ Officer',
             2008: 'HQ Officer',
             2009: 'HQ Officer',
             2010: 'HQ Officer',
             2011: 'Clerk Clara',
             2012: 'Fisherman Freddy',
             2013: 'Clerk Poppy',
             2014: 'Clerk Peppy',
             2015: 'Clerk Pappy',
             2016: 'Party Planner Pumpkin',
             2017: 'Party Planner Polly',
             2018: 'Duff..err..TIP Man',
             2018: 'Doctor Surlee',
             2019: 'Doctor Dimm',
             2020: 'Professor Prepostera',
             2101: 'Dentist Daniel',
             2102: 'Sheriff Sherry',
             2103: 'Sneezy Kitty',
             2104: 'HQ Officer',
             2105: 'HQ Officer',
             2106: 'HQ Officer',
             2107: 'HQ Officer',
             2108: 'Canary Coalmine',
             2109: 'Babbles Blowhard',
             2110: 'Bill Board',
             2111: 'Dancing Diego',
             2112: 'Dr. Tom',
             2113: 'Rollo the Amazing',
             2114: 'Roz Berry',
             2115: 'Patty Papercut',
             2116: 'Bruiser McDougal',
             2117: 'Ma Putrid',
             2118: 'Jesse Jester',
             2119: 'Honey Haha',
             2120: 'Professor Binky',
             2121: 'Madam Chuckle',
             2122: 'Harry Ape',
             2123: 'Spamonia Biggles',
             2124: 'T.P. Rolle',
             2125: 'Lazy Hal',
             2126: 'Professor Guffaw',
             2127: 'Woody Nickel',
             2128: 'Loony Louis',
             2129: 'Frank Furter',
             2130: 'Joy Buzzer',
             2131: 'Feather Duster',
             2132: 'Daffy Don',
             2133: 'Dr. I.M. Euphoric',
             2134: 'Silent Simone',
 2135: 'Mary',
 2136: 'Sal Snicker',
 2137: 'Happy Heikyung',
 2138: 'Muldoon',
 2139: 'Dan Dribbles',
 2140: 'Fisherman Billy',
 2201: 'Postmaster Pete',
 2202: 'Shirley U. Jest',
 2203: 'HQ Officer',
 2204: 'HQ Officer',
 2205: 'HQ Officer',
 2206: 'HQ Officer',
 2207: 'Will Wiseacre',
 2208: 'Sticky Lou',
 2209: 'Charlie Chortle',
 2210: 'Tee Hee',
 2211: 'Sally Spittake',
 2212: 'Weird Warren',
 2213: 'Lucy Tires',
 2214: 'Sam Stain',
 2215: 'Sid Seltzer',
 2216: 'Nona Seeya',
 2217: 'Sharky Jones',
 2218: 'Fanny Pages',
 2219: 'Chef Knucklehead',
 2220: 'Rick Rockhead',
 2221: 'Clovinia Cling',
 2222: 'Shorty Fuse',
 2223: 'Sasha Sidesplitter',
 2224: 'Smokey Joe',
 2225: 'Fisherman Droopy',
 2226: 'Inky Joe',
 2301: 'Dr. Pulyurleg',
 2302: 'Professor Wiggle',
 2303: 'Nurse Nancy',
 2304: 'HQ Officer',
 2305: 'HQ Officer',
 2306: 'HQ Officer',
 2307: 'HQ Officer',
 2308: 'Nancy Gas',
 2309: 'Big Bruce',
 2310: 'Professor Control',
 2311: 'Franz Neckvein',
 2312: 'Dr. Sensitive',
 2313: 'Lucy Shirtspot',
 2314: 'Ned Slinger',
 2315: 'Chewy Morsel',
 2316: 'Cindy Sprinkles',
 2318: 'Tony Maroni',
 2319: 'Zippy',
 2320: 'Crunchy Alfredo',
 2321: 'Fisherman Punchy',
 1001: 'Clerk Will',
 1002: 'Clerk Bill',
 1003: 'HQ Officer',
 1004: 'HQ Officer',
 1005: 'HQ Officer',
 1006: 'HQ Officer',
 1007: 'Longjohn Leroy',
 1008: 'Fisherman Furball',
 1009: 'Clerk Barky',
 1010: 'Clerk Purr',
 1011: 'Clerk Bloop',
 1012: 'Party Planner Pickles',
 1013: 'Party Planner Patty',
 1101: 'Billy Budd',
 1102: 'Captain Carl',
 1103: 'Fishy Frank',
 1104: 'Doctor Squall',
 1105: 'Admiral Hook',
 1106: 'Mrs. Starch',
 1107: 'Cal Estenicks',
 1108: 'HQ Officer',
 1109: 'HQ Officer',
 1110: 'HQ Officer',
 1111: 'HQ Officer',
 1112: 'Gary Glubglub',
 1113: 'Lisa Luff',
 1114: 'Charlie Chum',
 1115: 'Sheila Squid, Atty.',
 1116: 'Barnacle Bessie',
 1117: 'Captain Yucks',
 1118: 'Choppy McDougal',
 1121: 'Linda Landlubber',
 1122: 'Salty Stan',
 1123: 'Electra Eel',
 1124: 'Flappy Docksplinter',
 1125: 'Eileen Overboard',
 1126: 'Fisherman Barney',
 1201: 'Barnacle Barbara',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'Rocky Shores',
 1205: 'HQ Officer',
 1206: 'HQ Officer',
 1207: 'HQ Officer',
 1208: 'HQ Officer',
 1209: 'Professor Plank',
 1210: 'Gang Wei',
 1211: 'Wynn Bag',
 1212: 'Toby Tonguestinger',
 1213: 'Dante Dolphin',
 1214: 'Gusty Kate',
 1215: 'Dinah Down',
 1216: 'Rod Reel',
 1217: 'CC Weed',
 1218: 'Pacific Tim',
 1219: 'Brian Beachead',
 1220: 'Carla Canal',
 1221: 'Blisters McKee',
 1222: 'Shep Ahoy',
 1223: 'Sid Squid',
 1224: 'Emily Eel',
 1225: 'Bonzo Bilgepump',
 1226: 'Heave Ho',
 1227: 'Coral Reef',
 1228: 'Fisherman Reed',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: 'HQ Officer',
 1306: 'HQ Officer',
 1307: 'HQ Officer',
 1308: 'HQ Officer',
 1309: 'Seafoam',
 1310: 'Ted Tackle',
 1311: 'Topsy Turvey',
 1312: 'Ethan Keel',
 1313: 'William Wake',
 1314: 'Rusty Ralph',
 1315: 'Doctor Drift',
 1316: 'Wilma Wobble',
 1317: 'Paula Pylon',
 1318: 'Dinghy Dan',
 1319: 'Davey Drydock',
 1320: 'Ted Calm',
 1321: 'Dinah Docker',
 1322: 'Whoopie Cushion',
 1323: 'Stinky Ned',
 1324: 'Pearl Diver',
 1325: 'Ned Setter',
 1326: 'Felicia Chips',
 1327: 'Cindy Splat',
 1328: 'Fred Flounder',
 1329: 'Shelly Seaweed',
 1330: 'Porter Hole',
 1331: 'Rudy Rudder',
 1332: 'Fisherman Shane',
 3001: 'Betty Freezes',
 3002: 'HQ Officer',
 3003: 'HQ Officer',
 3004: 'HQ Officer',
 3005: 'HQ Officer',
 3006: 'Clerk Lenny',
 3007: 'Clerk Penny',
 3008: 'Warren Bundles',
 3009: 'Fisherman Frizzy',
 3010: 'Clerk Skip',
 3011: 'Clerk Dip',
 3012: 'Clerk Kipp',
 3013: 'Party Planner Pete',
 3014: 'Party Planner Penny',
 3101: 'Mr. Cow',
 3102: 'Auntie Freeze',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Frosty Freddy',
 3106: 'Gus Gooseburger',
 3107: 'Patty Passport',
 3108: 'Toboggan Ted',
 3109: 'Kate',
 3110: 'Chicken Boy',
 3111: 'Snooty Sinjin',
 3112: 'Lil Oldman',
 3113: 'Hysterical Harry',
 3114: 'Henry the Hazard',
 3115: 'HQ Officer',
 3116: 'HQ Officer',
 3117: 'HQ Officer',
 3118: 'HQ Officer',
 3119: 'Creepy Carl',
 3120: 'Mike Mittens',
 3121: 'Joe Shockit',
 3122: 'Lucy Luge',
 3123: 'Frank Lloyd Ice',
 3124: 'Lance Iceberg',
 3125: 'Colonel Crunchmouth',
 3126: 'Colestra Awl',
 3127: 'Ifalla Yufalla',
 3128: 'Sticky George',
 3129: 'Baker Bridget',
 3130: 'Sandy',
 3131: 'Lazy Lorenzo',
 3132: 'Ashy',
 3133: 'Dr. Friezeframe',
 3134: 'Lounge Lassard',
 3135: 'Soggy Nell',
 3136: 'Happy Sue',
 3137: 'Mr. Freeze',
 3138: 'Chef Bumblesoup',
 3139: 'Granny Icestockings',
 3140: 'Fisherman Lucille',
 3201: 'Aunt Arctic',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'Dr. Ivanna Cee',
 3205: 'Bumpy Noggin',
 3206: 'Vidalia VaVoom',
 3207: 'Dr. Mumbleface',
 3208: 'Grumpy Phil',
 3209: 'Giggles McGhee',
 3210: 'Simian Sam',
 3211: 'Fanny Freezes',
 3212: 'Frosty Fred',
 3213: 'HQ Officer',
 3214: 'HQ Officer',
 3215: 'HQ Officer',
 3216: 'HQ Officer',
 3217: 'Sweaty Pete',
 3218: 'Blue Lou',
 3219: 'Tom Tandemfrost',
 3220: 'Mr. Sneeze',
 3221: 'Nelly Snow',
 3222: 'Mindy Windburn',
 3223: 'Chappy',
 3224: 'Freida Frostbite',
 3225: 'Blake Ice',
 3226: 'Santa Paws',
 3227: 'Solar Ray',
 3228: 'Wynne Chill',
 3229: 'Hernia Belt',
 3230: 'Balding Benjy',
 3231: 'Choppy',
 3232: 'Fisherman Albert',
 3301: 'Paisley Patches',
 3302: 'Bjorn Bord',
 3303: 'Dr. Peepers',
 3304: 'Eddie the Yeti',
 3305: 'Mack Ramay',
 3306: 'Paula Behr',
 3307: 'Fisherman Fredrica',
 3308: 'Donald Frump',
 3309: 'Bootsy',
 3310: 'Professor Flake',
 3311: 'Connie Ferris',
 3312: 'March Harry',
 3313: 'HQ Officer',
 3314: 'HQ Officer',
 3315: 'HQ Officer',
 3316: 'HQ Officer',
 3317: 'Kissy Krissy',
 3318: 'Johnny Cashmere',
 3319: 'Sam Stetson',
 3320: 'Fizzy Lizzy',
 3321: 'Pickaxe Paul',
 3322: 'Flue Lou',
 3323: 'Dallas Borealis',
 3324: 'Snaggletooth Stu',
 3325: 'Groovy Garland',
 3326: 'Blanche',
 3327: 'Chuck Roast',
 3328: 'Shady Sadie',
 3329: 'Treading Ed',
 4001: 'Molly Molloy',
 4002: 'HQ Officer',
 4003: 'HQ Officer',
 4004: 'HQ Officer',
 4005: 'HQ Officer',
 4006: 'Clerk Doe',
 4007: 'Clerk Ray',
 4008: 'Tailor Harmony',
 4009: 'Fisherman Fanny',
 4010: 'Clerk Chris',
 4011: 'Clerk Neil',
 4012: 'Clerk Westin Girl',
 4013: 'Party Planner Preston',
 4014: 'Party Planner Penelope',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Dr. Fret',
 4104: 'HQ Officer',
 4105: 'HQ Officer',
 4106: 'HQ Officer',
 4107: 'HQ Officer',
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'Metra Gnome',
 4111: 'Tom Hum',
 4112: 'Fa',
 4113: 'Madam Manners',
 4114: 'Offkey Eric',
 4115: 'Barbara Seville',
 4116: 'Piccolo',
 4117: 'Mandy Lynn',
 4118: 'Attendant Abe',
 4119: 'Moe Zart',
 4120: 'Viola Padding',
 4121: 'Gee Minor',
 4122: 'Minty Bass',
 4123: 'Lightning Ted',
 4124: 'Riff Raff',
 4125: 'Melody Wavers',
 4126: 'Mel Canto',
 4127: 'Happy Feet',
 4128: 'Luciano Scoop',
 4129: 'Tootie Twostep',
 4130: 'Metal Mike',
 4131: 'Abraham Armoire',
 4132: 'Lowdown Sally',
 4133: 'Scott Poplin',
 4134: 'Disco Dave',
 4135: 'Sluggo Songbird',
 4136: 'Patty Pause',
 4137: 'Tony Deff',
 4138: 'Cliff Cleff',
 4139: 'Harmony Swell',
 4140: 'Clumsy Ned',
 4141: 'Fisherman Jed',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'Lumber Jack',
 4204: 'HQ Officer',
 4205: 'HQ Officer',
 4206: 'HQ Officer',
 4207: 'HQ Officer',
 4208: 'Hedy',
 4209: 'Corny Canter',
 4211: 'Carl Concerto',
 4212: 'Detective Dirge',
 4213: 'Fran Foley',
 4214: 'Tina Toehooks',
 4215: 'Tim Tailgater',
 4216: 'Gummy Whistle',
 4217: 'Handsome Anton',
 4218: 'Wilma Wind',
 4219: 'Sid Sonata',
 4220: 'Curtis Finger',
 4221: 'Moe Madrigal',
 4222: 'John Doe',
 4223: 'Penny Prompter',
 4224: 'Jungle Jim',
 4225: 'Holly Hiss',
 4226: 'Thelma Throatreacher',
 4227: 'Quiet Francesca',
 4228: 'August Winds',
 4229: 'June Loon',
 4230: 'Julius Wheezer',
 4231: 'Steffi Squeezebox',
 4232: 'Hedly Hymn',
 4233: 'Charlie Carp',
 4234: 'Leed Guitar',
 4235: 'Fisherman Larry',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: 'HQ Officer',
 4305: 'HQ Officer',
 4306: 'HQ Officer',
 4307: 'HQ Officer',
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Martha Mopp',
 4311: 'Sea Shanty',
 4312: 'Moe Saj',
 4313: 'Dumb Dolph',
 4314: 'Dana Dander',
 4315: 'Karen Clockwork',
 4316: 'Tim Tango',
 4317: 'Stubby Toe',
 4318: 'Bob Marlin',
 4319: 'Rinky Dink',
 4320: 'Cammy Coda',
 4321: 'Luke Lute',
 4322: 'Randy Rythm',
 4323: 'Hanna Hogg',
 4324: 'Ellie',
 4325: 'Banker Bran',
 4326: 'Fran Fret',
 4327: 'Flim Flam',
 4328: 'Wagner',
 4329: 'Telly Prompter',
 4330: 'Quentin',
 4331: 'Mellow Costello',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Fast Freddie',
 4335: 'Fisherman Walden',
 5001: 'HQ Officer',
 5002: 'HQ Officer',
 5003: 'HQ Officer',
 5004: 'HQ Officer',
 5005: 'Clerk Peaches',
 5006: 'Clerk Herb',
 5007: 'Bonnie Blossom',
 5008: 'Fisherman Flora',
 5009: 'Clerk Bo Tanny',
 5010: 'Clerk Tom A. Dough',
 5011: 'Clerk Doug Wood',
 5012: 'Party Planner Pierce',
 5013: 'Party Planner Peggy',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Bud',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Barber Bjorn',
 5107: 'Postman Felipe',
 5108: 'Innkeeper Janet',
 5109: 'HQ Officer',
 5110: 'HQ Officer',
 5111: 'HQ Officer',
 5112: 'HQ Officer',
 5113: 'Dr. Spud',
 5114: 'Wilt',
 5115: 'Honey Dew',
 5116: 'Vegetable Vern',
 5117: 'Petal',
 5118: 'Pop Corn',
 5119: 'Barry Medly',
 5120: 'Gopher',
 5121: 'Paula Peapod',
 5122: 'Leif Pyle',
 5123: 'Diane Vine',
 5124: 'Soggy Bottom',
 5125: 'Sanjay Splash',
 5126: 'Madam Mum',
 5127: 'Polly Pollen',
 5128: 'Shoshanna Sap',
 5129: 'Fisherman Sally',
 5201: 'Jake',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Dan D. Lion',
 5206: 'Vine Green',
 5207: 'Sofie Squirt',
 5208: 'Samantha Spade',
 5209: 'HQ Officer',
 5210: 'HQ Officer',
 5211: 'HQ Officer',
 5212: 'HQ Officer',
 5213: 'Big Galoot',
 5214: 'Itchie Bumps',
 5215: 'Tammy Tuber',
 5216: 'Stinky Jim',
 5217: 'Greg Greenethumb',
 5218: 'Rocky Raspberry',
 5219: 'Lars Bicep',
 5220: 'Lacy Underalls',
 5221: 'Pink Flamingo',
 5222: 'Whiny Wilma',
 5223: 'Wet Will',
 5224: 'Uncle Bumpkin',
 5225: 'Pamela Puddle',
 5226: 'Pete Moss',
 5227: 'Begonia Biddlesmore',
 5228: 'Digger Mudhands',
 5229: 'Fisherman Lily',
 5301: 'HQ Officer',
 5302: 'HQ Officer',
 5303: 'HQ Officer',
 5304: 'HQ Officer',
 5305: 'Crystal',
 5306: 'S. Cargo',
 5307: 'Fun Gus',
 5308: 'Naggy Nell',
 5309: 'Ro Maine',
 5310: 'Timothy',
 5311: 'Judge McIntosh',
 5312: 'Eugene',
 5313: 'Coach Zucchini',
 5314: 'Aunt Hill',
 5315: 'Uncle Mud',
 5316: 'Uncle Spud',
 5317: 'Detective Lima',
 5318: 'Caesar',
 5319: 'Rose',
 5320: 'April',
 5321: 'Professor Ivy',
 5322: 'Fisherman Rose',
 8001: 'Graham Pree',
 8002: 'Ivona Race',
 8003: 'Anita Winn',
 8004: 'Phil Errup',
 9001: "Snoozin' Susan",
 9002: 'Sleeping Tom',
 9003: 'Drowsy Dennis',
 9004: 'HQ Officer',
 9005: 'HQ Officer',
 9006: 'HQ Officer',
 9007: 'HQ Officer',
 9008: 'Clerk Jill',
 9009: 'Clerk Phil',
 9010: 'Worn Out Waylon',
 9011: 'Fisherman Freud',
 9012: 'Clerk Sarah Snuze',
 9013: 'Clerk Kat Knap',
 9014: 'Clerk R. V. Winkle',
 9015: 'Party Planner Pebbles',
 9016: 'Party Planner Pearl',
 9101: 'Ed',
 9102: 'Big Mama',
 9103: 'P.J.',
 9104: 'Sweet Slumber',
 9105: 'Professor Yawn',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Winky Wilbur',
 9109: 'Dreamy Daphne',
 9110: 'Kathy Nip',
 9111: 'Powers Erge',
 9112: 'Lullaby Lou',
 9113: 'Jacques Clock',
 9114: 'Smudgy Mascara',
 9115: 'Babyface MacDougal',
 9116: 'Dances with Sheep',
 9117: 'Afta Hours',
 9118: 'Starry Knight',
 9119: 'Rocco',
 9120: 'Sarah Slumber',
 9121: 'Serena Shortsheeter',
 9122: 'Puffy Ayes',
 9123: 'Teddy Blair',
 9124: 'Nina Nitelight',
 9125: 'Dr. Bleary',
 9126: 'Wyda Wake',
 9127: 'Tabby Tucker',
 9128: "Hardy O'Toole",
 9129: 'Bertha Bedhog',
 9130: 'Charlie Chamberpot',
 9131: 'Susan Siesta',
 9132: 'HQ Officer',
 9133: 'HQ Officer',
 9134: 'HQ Officer',
 9135: 'HQ Officer',
 9136: 'Fisherman Taylor',
 9137: 'Big Ben',
 9201: 'Bernie',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Claire de Loon',
 9205: 'Zen Glen',
 9206: 'Skinny Ginny',
 9207: 'Jane Drain',
 9208: 'Drowsy Dave',
 9209: 'Dr. Floss',
 9210: 'Master Mike',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Rooster Rick',
 9214: 'Dr. Blinky',
 9215: 'Rip',
 9216: 'Cat',
 9217: 'Lawful Linda',
 9218: 'Waltzing Matilda',
 9219: 'The Countess',
 9220: 'Grumpy Gordon',
 9221: 'Zari',
 9222: 'Cowboy George',
 9223: 'Mark the Lark',
 9224: 'Sandy Sandman',
 9225: 'Fidgety Bridget',
 9226: 'William Teller',
 9227: 'Bed Head Ted',
 9228: 'Whispering Willow',
 9229: 'Rose Petals',
 9230: 'Tex',
 9231: 'Harry Hammock',
 9232: 'Honey Moon',
 9233: 'HQ Officer',
 9234: 'HQ Officer',
 9235: 'HQ Officer',
 9236: 'HQ Officer',
 9237: 'Fisherman Jung',
 9301: 'Phil Bettur',
 9302: 'Emma Phatic',
 9303: 'GiggleMesh',
 9304: 'Anne Ville',
 9305: 'Bud Erfingerz',
 9306: 'J.S. Bark',
 9307: 'Bea Sharpe',
 9308: 'Otto Toon',
 9309: 'Al Capella',
 9310: 'Des Traction',
 9311: 'Dee Version',
 9312: 'Bo Nanapeel',
 7001: 'M. Prisoned',
     7002: 'R.E. Leaseme',
     7003: 'Lemmy Owte',
     7004: 'T. Rapped',
     7005: 'Little Helphere',
     7006: 'Gimmy Ahand',
     7007: 'Dewin Tymme',
     7008: 'Ima Cagedtoon',
     7009: 'Jimmy Thelock',
             7010: 'K.G.'}[NPCID]
            self.NPCHead = self.createNPCToonHead(NPCID, dimension=self.NPCHeadDim)
            self.NPCHead.reparentTo(self.front)
            self.NPCHead.setZ(self.NPCHeadPosZ)
            track, level, hp, rarity = NPCToons.getNPCTrackLevelHpRarity(NPCID)
            sosText = self.sosTracks[track]
            if track == ToontownBattleGlobals.NPC_RESTOCK_GAGS:
                if level == -1:
                    sosText += ' All'
                else:
                    sosText += ' ' + self.sosTracks[level]
            sosText = TextEncoder.upper(sosText)
            self.sosTypeInfo['text'] = sosText
            for i in xrange(self.maxRarity):
                if i < rarity:
                    self.rarityStars[i].show()
                else:
                    self.rarityStars[i].hide()

        if fCallable:
            self.sosCallButton.show()
            self.sosCountInfo.setPos(-0.4, 0, self.sosCountInfoPosZ)
            self.sosCountInfo['text_scale'] = self.sosCountInfoScale
            self.sosCountInfo['text_align'] = TextNode.ALeft
        else:
            self.sosCallButton.hide()
            self.sosCountInfo.setPos(0, 0, self.sosCountInfo2PosZ)
            self.sosCountInfo['text_scale'] = self.sosCountInfo2Scale
            self.sosCountInfo['text_align'] = TextNode.ACenter
        if count > 0:
            countText = TTLocalizer.NPCFriendPanelRemaining % count
            self.sosCallButton['state'] = DGG.NORMAL
        else:
            countText = 'Unavailable'
            self.sosCallButton['state'] = DGG.DISABLED
        self.sosCountInfo['text'] = countText
        return

    def showFront(self):
        self.front.show()
        self.back.hide()

    def showBack(self):
        self.front.hide()
        self.back.show()

    def createNPCToonHead(self, NPCID, dimension = 0.5):
        NPCInfo = NPCToons.NPCToonDict[NPCID]
        dnaList = NPCInfo[2]
        gender = NPCInfo[3]
        if dnaList == 'r':
            dnaList = NPCToons.getRandomDNA(NPCID, gender)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties(*dnaList)
        head = ToonHead.ToonHead()
        head.setupHead(dna, forGui=1)
        self.fitGeometry(head, fFlip=1, dimension=dimension)
        return head

    def fitGeometry(self, geom, fFlip = 0, dimension = 0.5):
        p1 = Point3()
        p2 = Point3()
        geom.calcTightBounds(p1, p2)
        if fFlip:
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = dimension / biggest
        mid = (p1 + d / 2.0) * s
        geomXform = hidden.attachNewNode('geomXform')
        for child in geom.getChildren():
            child.reparentTo(geomXform)

        geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], 180, 0, 0, s, s, s)
        geomXform.reparentTo(geom)
