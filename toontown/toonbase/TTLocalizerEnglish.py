from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.iterkeys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
NametagFonts = ('phase_3/models/fonts/AnimGothic',
 'phase_3/models/fonts/Aftershock',
 'phase_3/models/fonts/JiggeryPokery',
 'phase_3/models/fonts/Ironwork',
 'phase_3/models/fonts/HastyPudding',
 'phase_3/models/fonts/Comedy',
 'phase_3/models/fonts/Humanist',
 'phase_3/models/fonts/Portago',
 'phase_3/models/fonts/Musicals',
 'phase_3/models/fonts/Scurlock',
 'phase_3/models/fonts/Danger',
 'phase_3/models/fonts/Alie',
 'phase_3/models/fonts/OysterBar',
 'phase_3/models/fonts/RedDogSaloon')
NametagFontNames = ('Member',
 'Shivering',
 'Wonky',
 'Fancy',
 'Silly',
 'Zany',
 'Practical',
 'Nautical',
 'Whimsical',
 'Spooky',
 'Action',
 'Poetic',
 'Boardwalk',
 'Western')
NametagLabel = ' Nametag'
UnpaidNameTag = 'Basic'
GM_NAMES = ('TOON COUNCIL',
 'TOON TROOPER',
 'RESISTANCE RANGER',
 'GC')
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
ProductPrefix = 'TT'
Mickey = 'Mickey'
VampireMickey = 'VampireMickey'
Minnie = 'Minnie'
WitchMinnie = 'WitchMinnie'
Donald = 'Donald'
DonaldDock = 'DonaldDock'
FrankenDonald = 'FrankenDonald'
Daisy = 'Daisy'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Goofy'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Chip'
Dale = 'Dale'
JailbirdDale = 'JailbirdDale'
PoliceChip = 'PoliceChip'
lTheBrrrgh = 'The Brrrgh'
lDaisyGardens = 'Daisy Gardens'
lDonaldsDock = "Donald's Dock"
lDonaldsDreamland = "Donald's Dreamland"
lMinniesMelodyland = "Minnie's Melodyland"
lToontownCentral = 'Toontown Central'
lToonHQ = 'Toon HQ'
lSellbotHQ = 'Sellbot HQ'
lGoofySpeedway = 'Goofy Speedway'
lOutdoorZone = "Chip 'n Dale's Acorn Acres"
lGolfZone = "Chip 'n Dale's MiniGolf"
lPartyHood = 'Party Grounds'
GlobalStreetNames = {20000: ('to', 'on', 'Tutorial Terrace'),
 1000: ('to the', 'in the', 'Playground'),
 1100: ('to', 'on', 'Barnacle Boulevard'),
 1200: ('to', 'on', 'Seaweed Street'),
 1300: ('to', 'on', 'Lighthouse Lane'),
 2000: ('to the', 'in the', 'Playground'),
 2100: ('to', 'on', 'Silly Street'),
 2200: ('to', 'on', 'Loopy Lane'),
 2300: ('to', 'on', 'Punchline Place'),
 3000: ('to the', 'in the', 'Playground'),
 3100: ('to', 'on', 'Walrus Way'),
 3200: ('to', 'on', 'Sleet Street'),
 3300: ('to', 'on', 'Polar Place'),
 4000: ('to the', 'in the', 'Playground'),
 4100: ('to', 'on', 'Alto Avenue'),
 4200: ('to', 'on', 'Baritone Boulevard'),
 4300: ('to', 'on', 'Tenor Terrace'),
 5000: ('to the', 'in the', 'Playground'),
 5100: ('to', 'on', 'Elm Street'),
 5200: ('to', 'on', 'Maple Street'),
 5300: ('to', 'on', 'Oak Street'),
 6000: ('to the', 'in the', 'Playground'),
 8000: ('to the', 'in the', 'Playground'),
 9000: ('to the', 'in the', 'Playground'),
 9100: ('to', 'on', 'Lullaby Lane'),
 9200: ('to', 'on', 'Pajama Place'),
 10000: ('to the', 'in the', 'Bossbot HQ Country Club'),
 10100: ('to the', 'in the', 'Bossbot HQ Lobby'),
 10200: ('to the', 'in the', 'Clubhouse'),
 10500: ('to the', 'in the', 'Front Three'),
 10600: ('to the', 'in the', 'Middle Six'),
 10700: ('to the', 'in the', 'Back Nine'),
 11000: ('to the', 'in the', 'Sellbot HQ Courtyard'),
 11100: ('to the', 'in the', 'Sellbot HQ Lobby'),
 11200: ('to the', 'in the', 'Sellbot Factory'),
 11500: ('to the', 'in the', 'Sellbot Factory'),
 12000: ('to the', 'in the', 'Cashbot Train Yard'),
 12100: ('to the', 'in the', 'Cashbot HQ Lobby'),
 12500: ('to the', 'in the', 'Cashbot Coin Mint'),
 12600: ('to the', 'in the', 'Cashbot Dollar Mint'),
 12700: ('to the', 'in the', 'Cashbot Bullion Mint'),
 13000: ('to the', 'in the', 'Lawbot HQ Courtyard'),
 13100: ('to the', 'in the', 'Courthouse Lobby'),
 13200: ('to the', 'in the', "DA's Office Lobby"),
 13300: ('to the', 'in the', 'Lawbot A Office'),
 13400: ('to the', 'in the', 'Lawbot B Office'),
 13500: ('to the', 'in the', 'Lawbot C Office'),
 13600: ('to the', 'in the', 'Lawbot D Office'),
 17000: ('to the', 'in the', 'Playground'),}
DonaldsDock = ('to', 'in', "Donald's Dock")
ToontownCentral = ('to', 'in', 'Toontown Central')
TheBrrrgh = ('to', 'in', 'the Brrrgh')
MinniesMelodyland = ('to', 'in', "Minnie's Melodyland")
DaisyGardens = ('to', 'in', 'Daisy Gardens')
OutdoorZone = ('to', 'in', "Chip 'n Dale's Acorn Acres")
FunnyFarm = ('to the', 'in the', 'Funny Farm')
GoofySpeedway = ('to', 'in', lGoofySpeedway)
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'Bossbot HQ')
SellbotHQ = ('to', 'in', 'Sellbot HQ')
CashbotHQ = ('to', 'in', 'Cashbot HQ')
LawbotHQ = ('to', 'in', 'Lawbot HQ')
Tutorial = ('to the', 'in the', 'Toon-\x03torial')
MyEstate = ('to', 'in', 'your house')
WelcomeValley = ('to', 'in', 'Welcome Valley')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
Office = 'Office'
FactoryNames = {0: 'Factory Mockup',
 11500: 'Cog Factory',
 13300: 'Lawbot Cog Office'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes'
lNo = 'No'
sleep_auto_reply = '%s is sleeping right now.'
sleep_auto_reply_retro = '%s is sleeping right now'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'The Cogs'
ASkeleton = 'a Skelecog'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
Foreman = 'Factory Foreman'
ForemanP = 'Factory Foremen'
AForeman = 'a Factory Foreman'
CogVP = Cog + ' C.M.O.'
CogVPs = Cog + " C.M.O.'s"
ACogVP = ACog + ' C.M.O.'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
CogCFO = Cog + ' C.F.O.'
CogCFOs = "Cog C.F.O.'s"
ACogCFO = ACog + ' C.F.O.'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsProfessorControlGreeting = "Welcome ta' de Professa's Circuit Circus, 'ome o' de finest circuitry o' Toontown!  Me name's Professa' Control; 'ow may I 'elp ya?\x07Ye ain't 'ere fa' circuitry?  Den what'cha 'ere fo'?",
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Looks like you still have more work to do on that task!',
 'Keep up the good work, _avName_!',
 'Keep trying to finish that task.  I know you can do it!',
 'Keep trying to complete that task, we are counting on you!',
 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Good luck!',
 'Have fun in Toontown!',
 'See you later!')
QuestsDefaultReject = ('Hello.',
 'Can I help you?',
 'How are you?',
 'Hello there.',
 "I'm a little busy now, _avName_.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it going?",
 'Did you know you can open your Shticker Book by hitting F8?',
 'You can use your map to teleport back to the playground!',
 'You can make friends with other players by clicking on them.',
 'You can discover more about a Cog by clicking on it.',
 'Gather treasures in the playgrounds to fill your Laff meter.',
 'Cog buildings are dangerous places! Do not go in alone!',
 'When you lose a battle, the Cogs take all your Gags.',
 'To get more jellybeans, play Trolley games!',
 'You can get more Laff points by completing ToonTasks.',
 'Every ToonTask gives you a reward.',
 'Some rewards let you carry more gags.',
 'If you win a battle, you get ToonTask credit for every Cog defeated.',
 'If you recapture a Cog building, go back inside to see a special thank-you from its owner!',
 'If you press the Page Up key, you can look up!',
 'If you press the Tab key, you can see different views of your surroundings!',
 "To show True Friends what you're thinking, enter a '.' before your thought.",
 'If a Cog is stunned, it is more difficult for them to avoid falling objects.',
 'Each kind of Cog building has a distinct look.',
 'Defeating Cogs on the higher floors of a building will give you greater skill rewards.')
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.', "Hi! I can't give you a new ToonTask until you finish your current ones.")
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Help a new Toon defeat %s'
QuestsCogNewNewbieQuestCaption = 'Help a new Toon %d Laff or less'
QuestsCogOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less defeat %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Help a Toon %d Laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five+')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'INFILTRATE'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to infiltrate %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'INFILTRATE'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestsRescueNewNewbieQuestObjective = 'Help a new Toon rescue %s'
QuestsRescueOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less rescue %(objective)s'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsCogPartNewNewbieQuestObjective = 'Help a new Toon retrieve %s'
QuestsCogPartOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less retrieve %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose between %(trackA)s and %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose between %(trackA)s and %(trackB)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d new Toons'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with new Toons'
QuestsMinigameNewbieQuestSCString = 'I need to play minigames with new Toons.'
QuestsMinigameNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsMinigameNewbieQuestAux = 'Play:'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'You get 1 jellybean.'
QuestsMoneyRewardPlural = 'You get %s jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s jellybeans'
QuestsMaxMoneyRewardSingular = 'You can now carry 1 jellybean.'
QuestsMaxMoneyRewardPlural = 'You can now carry %s jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Reward: Carry 1 jellybean'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'You can change your clothes'
QuestsClothingTicketRewardPoster = 'Reward: Clothing Ticket'
TIPQuestsClothingTicketReward = 'You can change your shirt for a TIP shirt'
TIPQuestsClothingTicketRewardPoster = 'Reward: TIP Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"...\x07...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Now you are ready.\x07Go out and walk the earth until you know which track you would like to choose.\x07Choose wisely, because this is your final track.\x07When you are certain, return to me.',
 INCOMPLETE_PROGRESS: 'Choose wisely.',
 INCOMPLETE_WRONG_NPC: 'Choose wisely.',
 COMPLETE: 'Very wise choice!',
 LEAVING: 'Good luck.  Return to me when you have mastered your new skill.'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on the spring.\x07The final item is a counter weight.\x07Stop by and see _toNpcName_ and bring back whatever you can get._where_'}
QuestDialogDict = {161: {GREETING: '',
       QUEST: "Ok, now I think you are ready for something more rewarding.\x07Come back after you defeat 3 Lawbots and I'll have a little something for you.",
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 162: {GREETING: '',
       QUEST: 'Okay, now I think you are ready for something more rewarding.\x07Defeat 3 Cashbots and come back here to claim the bounty.',
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 163: {GREETING: '',
       QUEST: "Ok, now I think you are ready for something more rewarding.\x07Come see us after you defeat 3 Sellbots and we'll hook you up.",
       INCOMPLETE_PROGRESS: TheCogs + ' are out in the streets, through the tunnels.',
       INCOMPLETE_WRONG_NPC: 'Good job defeating those Cogs. Now go to the Toon Headquarters for your next step!',
       COMPLETE: QuestsDefaultComplete,
       LEAVING: QuestsDefaultLeaving},
 175: {GREETING: '',
       QUEST: "Did you know you have your very own Toon house?\x07Clarabelle Cow runs a phone catalog where you can order furniture to decorate your house.\x07You can also buy SpeedChat phrases, clothing, and other fun things!\x07I'll tell Clarabelle to send you your first catalog now.\x07You get a catalog with new items every week!\x07Go to your home and use your phone to call Clarabelle.",
       INCOMPLETE_PROGRESS: 'Go home and use your phone to call Clarabelle.',
       COMPLETE: 'Hope you have fun ordering things from Clarabelle!\x07I just finished redecorating my house. It looks Toontastic!\x07Keep doing ToonTasks to get more rewards!',
       LEAVING: ('Bye!', 'Goodbye!', 'So long, _avName_.', 'See ya, _avName_!', 'Good luck!', 'Have fun in Toontown!', 'See you later!')},
 164: {QUEST: 'You look like you could use some new gags.\x07Go see %s, maybe he can help you out._where_' % Flippy},
 165: {QUEST: 'Hi there.\x07Looks like you need to practice training your gags.\x07Every time you hit a Cog with one of your gags, your experience increases.\x07When you get enough experience, you will be able to use an even better gag.\x07Go practice your gags by defeating 4 Cogs.'},
 166: {QUEST: "Nice work defeating those Cogs!\x07You know, the Cogs come in four different types.\x07There are Sellbots for marketing...\x07...Cashbots for accounting...\x07...Lawbots for legal advice...\x07...and Bossbots to keep them all in line.\x07You can tell them apart by their coloring and their name labels.\x07Here, let's practice.  Go defeat a Bossbot."},
 167: {QUEST: 'Splendid!\x07Now, go defeat a Lawbot.'},
 168: {QUEST: 'Amazing!\x07Now, go defeat a Cashbot.'},
 169: {QUEST: 'Excellent!\x07Now, go defeat a Sellbot.'},
 170: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 171: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - he can give you some expert advice._where_'},
 172: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNpcName_ to choose your next gag track - she can give you some expert advice._where_'},
 173: {QUEST: 'Nice work, now you know the difference between the 4 types of Cogs.\x07I think you are ready to start training for your third gag track.\x07Go talk to _toNPCName_ to choose your next gag track - he can give you some expert advice._where_'},
 1044: {QUEST: 'Oh, thanks for stopping by.  I really need some help.\x07As you can see, I have no customers.\x07My secret recipe book is lost and nobody comes to my restaurant anymore.\x07I last saw it just before those Cogs took over my building.\x07Can you help me by recovering four of my famous recipes?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my recipes?'},
 1045: {QUEST: 'Thank you so much!\x07Before long I will have the entire collection and can reopen my restaurant.\x07Oh, I have a note here for you - something about teleport access?\x07It says thanks for helping my friend and to deliver this to Toon Headquarters.\x07Well, thanks indeed - bye!',
        LEAVING: '',
        COMPLETE: 'Ah, yes, says here you have been a great help to some of the fine folks out on Loopy Lane.\x07Says you need teleport access to Toontown Central.\x07Well, consider it done.\x07Now you can teleport back to the playground from almost anywhere in Toontown.\x07Just open your map and click on "Go to Toontown Central".'},
 1046: {QUEST: 'The Cashbots have really been bothering the Funny Money Savings and Loan.\x07Stop by there and see if there is anything you can do._where_'},
 1047: {QUEST: 'Cashbots have been sneaking into the bank and stealing our machines.\x07Please recover 5 adding machines from Cashbots.\x07To save you from running back and forth, just bring them all back at once.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Still looking for adding machines?'},
 1048: {QUEST: 'Wow!  Thanks for finding our adding machines.\x07Hm... They look a little damaged.\x07Say, could you take them over to _toNpcName_ over at her shop, "Tickle Machines" on this street?\x07See if she can fix them.',
        LEAVING: ''},
 1049: {QUEST: "What's that?  Broken adding machines?\x07Cashbots you say?\x07Well, let's have a look see...\x07Yep, gears are stripped, but I'm out of that part...\x07You know what might work - some Cog gears, large ones, from larger Cogs...\x07Level 3 Cog gears should do the trick.  I'll need 2 for each machine, so 10 total.\x07Bring them back all at once and I'll fix 'em up!",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Remember, I need 10 gears to fix the machines.'},
 1053: {QUEST: "Ah yes, that should do the trick indeedy.\x07All fixed now, free of charge.\x07Take these back to Funny Money, and tell 'im I said howdy.",
        LEAVING: '',
        COMPLETE: "Adding machines all fixed up?\x07Nice work.  I'm sure I've got something around here to reward you with..."},
 1054: {QUEST: '_toNpcName_ needs some help with his clown cars._where_'},
 1055: {QUEST: "Yowza!  I can't find the tires to this here clown car anywhere!\x07Do ya think you could help me out?\x07I think Loopy Bob may have tossed them in the pond in the " + lToontownCentral + ' playground.\x07If you stand on one of the docks there you can try and fish out the tires for me.',
        GREETING: 'Woohoo!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you having trouble fishing out all 4 tires?'},
 1056: {QUEST: 'Fan-flying-tastic!  Now I can get this old clown car on the road again!\x07Hey, I thought I had an air pump around here to inflate these tires...\x07Maybe _toNpcName_ borrowed it?\x07Could you go ask for it back for me?_where_',
        LEAVING: ''},
 1076: {QUEST: "There's been some trouble over at 14 Karat Goldfish.\x07_toNpcName_ could probably use a hand._where_"},
 1077: {QUEST: "Thanks for coming - the Cogs stole all my goldfish.\x07I think the Cogs want to sell them to make a quick buck.\x07Those 5 fish have been my only companions in this tiny store for so many years...\x07If you could get them back for me I'd really appreciate it.\x07I'm sure one of the Cogs has my fish.\x07Defeat Cogs until you find my goldfish.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Please return my goldfish to me.'},
 1078: {QUEST: "Oh, you have my fish!\x07Huh?  What's this - a receipt?\x07Sigh, I guess they are Cogs, after all.\x07I can't make heads or tails out of this receipt.  Could you take it to _toNpcName_ and see if he can read it?_where_",
        INCOMPLETE: 'What did _toNpcName_ have to say about the receipt?',
        LEAVING: ''},
 1079: {QUEST: "Mmm, let me see that receipt.\x07...Ah Yes, it says that 1 goldfish was sold to a Flunky.\x07It doesn't seem to mention what happened to the other 4 fish.\x07Maybe you should try and find that Flunky.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x07Why don't you try and find that goldfish?"},
 1092: {QUEST: "Mmm, let me see that receipt.\x07...Ah Yes, it says that 1 goldfish was sold to a Short Change.\x07It doesn't seem to mention what happened to the other 4 fish.\x07Maybe you should try and find that Short Change.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I don't think there's anything else I can help you with.\x07Why don't you try and find that goldfish?"},
 1080: {QUEST: "Oh thank heavens!  You found Oscar - he's my favorite.\x07What's that, Oscar?  Uh huh... they did? ... they are?\x07Oscar says the other 4 escaped into the pond in the playground.\x07Could you go round them up for me?\x07Just fish them out of the pond.",
        LEAVING: '',
        COMPLETE: 'Ahh, I am sooo happy!  To be reunited with my little buddies!\x07You deserve a handsome reward for this!',
        INCOMPLETE_PROGRESS: 'Are you having trouble finding those fish?'},
 1081: {QUEST: '_toNpcName_ appears to be in a sticky situation. He sure could use a hand._where_'},
 1082: {QUEST: "I spilled quick dry glue and I'm stuck - stuck cold!\x07If there were a way out, I sure would be sold.\x07That gives me an idea, if you are feeling loyal.\x07Defeat some Sellbots and bring back some oil.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Have you got the oil?  I'm beginning to broil!"},
 1083: {QUEST: "Well, oil helped a little, but I still cannot budge.\x07What else would help?  It's hard to judge.\x07That gives me an idea; it's worth a try at least.\x07Defeat some Lawbots and bring back some grease.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Oh please, oh please, oh please, go fetch me some grease!'},
 1084: {QUEST: "Nope, that didn't help.  This is really not funny.\x07I put the grease right there on the money.\x07That gives me an idea, before I forget it.\x07Defeat some Cashbots; bring back water to soak it.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Hooray, I'm free of this quick drying glue!\x07As a reward I give this gift to you!\x07You can laugh a little longer while battling and then...\x07Oh, no!  I'm already stuck here again!",
        INCOMPLETE_PROGRESS: "There really isn't any time; I can't think of another rhyme!"},
 1085: {QUEST: '_toNpcName_ is conducting some research on the Cogs.\x07Go talk to him if you want to help out._where_'},
 1086: {QUEST: "That's right, I'm conducting a study of the Cogs.\x07I want to know what makes them tick.\x07It sure would help me if you could gather some gears from Cogs.\x07Make sure they're from at least level 2 Cogs so they're big enough to examine.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Can't find enough gears?"},
 1089: {QUEST: "Okay, let's take a look.  These are excellent specimens!\x07Mmmm...\x07Okay, here's my report.  Take this back to Toon Headquarters right away.",
        INCOMPLETE: 'Have you delivered my report to Headquarters?',
        COMPLETE: "Good work _avName_, we'll take this one from here.",
        LEAVING: ''},
 1090: {QUEST: '_toNpcName_ has some useful information for you._where_'},
 1091: {QUEST: 'I hear that Toon Headquarters is working on a sort of Cog Radar.\x07It will let you see where the Cogs are so that it will be easier to find them.\x07That Cog Page in your Shticker Book is the key.\x07By defeating enough Cogs, you can tune in to their signals and actually track where they are.\x07Keep defeating Cogs, so you will be ready.',
        COMPLETE: 'Good work!  You could probably use this...',
        LEAVING: ''},
 401: {GREETING: '',
       QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
       INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
       INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
       COMPLETE: 'A wise decision...',
       LEAVING: QuestsDefaultLeaving},
 2201: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 2202: {QUEST: "Hi, _avName_. Thank goodness you're here. A mean looking Penny Pincher was just in here and he made off with an inner tube.\x07I fear they may use it for their vile purposes.\x07Please see if you can find him and bring it back.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my inner tube?',
        COMPLETE: 'You found my inner tube! You ARE good. Here, take your reward...'},
 2203: {QUEST: TheCogs + ' are wreaking havoc over at the bank.\x07Go see Captain Carl and see what you can do._where_'},
 2204: {QUEST: "Welcome aboard, matey.\x07Argh! Those rapscallion Cogs smashed my monocle and I can't sort me change without it.\x07Be a good landlubber and take this prescription to _toNpcName_ and fetch me a new one._where_",
        GREETING: '',
        LEAVING: ''},
 2205: {QUEST: "What's this?\x07Oh, I'd love to fill this prescription but the Cogs have been pilfering my supplies.\x07If you can get me the eyeglass frames off a Flunky I can probably help you out.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sorry. No Flunky frames, no monocle.'},
 2206: {QUEST: 'Excellent!\x07Just a second...\x07Your prescription is filled. Please take this monocle straight to Captain Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Avast Ye!\x07You're gonna earn your sea legs after all.\x07Here ye be."},
 2207: {QUEST: "Barnacle Barbara has a Cog in her shop!\x07You'd better get over there pronto._where_"},
 2208: {QUEST: "Gosh! You just missed him, sweetie.\x07There was a Back Stabber in here. He took my big, white wig.\x07He said it was for his boss and something about 'legal precedent.'\x07If you can get it back I'd be forever grateful.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Still haven't found him?\x07He's tall and has a pointy head",
        COMPLETE: "You found it!?!?\x07Aren't you a darling!\x07You've more than earned this..."},
 2209: {QUEST: 'Melville is preparing for an important voyage.\x07Pop in and see what you can do to help sort him out._where_'},
 2210: {QUEST: "I can use your help.\x07I've been asked by Toon HQ to take a voyage and see if I can find where the Cogs are coming from.\x07I'll need a few things for my ship but I don't have many jellybeans.\x07Stop by and pick up some ballast from Alice. You'll have to do a favor for her to get it._where_",
        GREETING: 'Howdy, _avName_',
        LEAVING: ''},
 2211: {QUEST: "So Melville wants ballast, does he?\x07He still owes me for the last bushel.\x07I'll give it to you if you can clear five Micromanagers off my street.",
        INCOMPLETE_PROGRESS: 'No, silly! I said FIVE micromanagers...',
        GREETING: 'What can I do for you?',
        LEAVING: ''},
 2212: {QUEST: "A deal's a deal.\x07Here's your ballast for that cheapskate Melville._where_",
        GREETING: 'Well, look what the cat dragged in...',
        LEAVING: ''},
 2213: {QUEST: "Excellent work. I knew she'd be reasonable.\x07Next I'll need a sailing chart from Art.\x07I don't think my credit is good there either so you'll have to work something out with him._where_",
        GREETING: '',
        LEAVING: ''},
 2214: {QUEST: "Yes, I have the sea chart Melville wants.\x07And if you're willing to work for it I'll let you have it.\x07I'm trying to build an astrolabe to navigate by the stars.\x07I could use three Cog gears to build it.\x07Come back when you've found them.",
        INCOMPLETE_PROGRESS: "How's it coming with those Cog gears?",
        GREETING: 'Welcome!',
        LEAVING: 'Good luck!'},
 2215: {QUEST: "Ooh! These gears will do rather nicely.\x07Here's the chart. Give it to Melville with my compliments._where_",
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Well, that just about does it. I'm ready to sail!\x07I'd take you with me if you weren't so green. Take this instead."},
 901: {QUEST: "If you're up for it Ahab could use some assistance over at his place..._where_"},
 2902: {QUEST: "Are you the new recruit?\x07Good, good. Maybe you can help me.\x07I'm building a giant prefab crab to confuse the Cogs.\x07I could use a clovis though. Go see Claggart and bring one back, please._where_"},
 2903: {QUEST: "Hi there!\x07Yes, I heard about the giant crab Ahab's working on.\x07The best clovis I have is a little on the dirty side though.\x07Be a sport and run it by the cleaners for me before you drop it off._where_",
        LEAVING: 'Thanks!'},
 2904: {QUEST: 'You must be the one that Claggart sent over.\x07I think I can clean that up in short order.\x07Just a minute...\x07There you are. Good as new!\x07Tell Ahab I said hello._where_'},
 2905: {QUEST: "Ah, now this is exactly what I was looking for.\x07While you're here, I'm also going to need a very large clock spring.\x07Take a walk over to Hook's place and see if he has one._where_"},
 2906: {QUEST: "A large spring, eh?\x07I'm sorry but the largest spring I have is still quite small.\x07Perhaps I could assemble one out of squirt gun trigger springs.\x07Bring me three of these gags and I'll see what I can do."},
 2907: {QUEST: "Let's have a look then...\x07Smashing. Simply Smashing.\x07Sometimes I even surprise myself.\x07Here you go: one large spring for Ahab!_where_",
        LEAVING: 'Bon Voyage!'},
 2911: {QUEST: "I'd be happy to help the cause, _avName_.\x07But I'm afraid the streets are no longer safe.\x07Why don't you go take out some Cashbot Cogs and we'll talk.",
        INCOMPLETE_PROGRESS: 'I still think you need to make the streets safer.'},
 2916: {QUEST: 'Yes, I have a weight that Ahab can have.\x07I think it would be safer if you defeated a couple Sellbots first though.',
        INCOMPLETE_PROGRESS: 'Not yet. Defeat some more Sellbots.'},
 2921: {QUEST: "Hmmm, I suppose I could give up a weight.\x07I'd feel a lot better about it if there weren't so many Bossbot Cogs creeping around.\x07Defeat six and then come see me.",
        INCOMPLETE_PROGRESS: "I don't think its safe yet..."},
 2925: {QUEST: "All done?\x07Well, I guess it's safe enough now.\x07Here's the counter weight for Ahab._where_"},
 2926: {QUEST: "Well, that's everything.\x07Let's see if it works.\x07Hmmm, one small problem.\x07I'm not getting any power because that Cog building is blocking my solar panel.\x07Could you retake it for me?",
        INCOMPLETE_PROGRESS: 'Still no power. How about that building?',
        COMPLETE: 'Super! You are one heck of a Cog crusher! Here, take this as your reward...'},
 3200: {QUEST: "I just got a call in from _toNpcName_.\x07He's having a hard day. Maybe you can help him out!\x07Drop by and see what he needs._where_"},
 3201: {QUEST: 'Oh, thanks for coming!\x07I need someone to take this new silk tie to _toNpcName_.\x07Would you be able to do that for me?_where_'},
 3203: {QUEST: 'Oh, this must be the tie I ordered! Thanks!\x07It matches a pinstripe suit I just finished, right over here.\x07Hey, what happened to that suit?\x07Oh no! The Cogs must have stolen my new suit!\x07Defeat Cogs until you find my suit, and bring it back to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Have you found my suit yet? I'm sure the Cogs took it!",
        COMPLETE: 'Hooray! You found my new suit!\x07See, I told you the Cogs had it! Here is your reward...'},
 3204: {QUEST: "_toNpcName_ just called to report a theft.\x07Why don't you stop by and see if you can sort things out?_where_"},
 3205: {QUEST: "Hello, _avName_! Have you come to help me?\x07I just chased a Bloodsucker out of my shop. Whew! That was scary.\x07But now I can't find my scissors anywhere! I'm sure that Bloodsucker took them.\x07Find that Bloodsucker, and recover my scissors for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Are you still looking for my scissors?',
        COMPLETE: 'My scissors! Thank you so much! Here is your reward...'},
 3206: {QUEST: 'It sounds like _toNpcName_ is having problems with some Cogs.\x07Go see if you can help him out._where_'},
 3207: {QUEST: 'Hi, _avName_! Thanks for coming by!\x07A bunch of Double Talkers just broke in and stole a stack of postcards from my counter.\x07Please go out and defeat all those Double Talkers to get my postcards back!',
        INCOMPLETE_PROGRESS: "That's not enough postcards! Keep looking!",
        COMPLETE: 'Oh, thank you! Now I can deliver the mail on time! Here is your reward...'},
 3208: {QUEST: "We've been getting complaints from the residents lately about all of the Cold Callers.\x07See if you can defeat 10 Cold Callers to help out your fellow Toons in " + lDaisyGardens + '.'},
 3209: {QUEST: 'Thanks for taking care of those Cold Callers!\x07But now the Telemarketers have gotten out of hand.\x07Defeat 10 Telemarketers in ' + lDaisyGardens + ' and come back here for your reward.'},
 3247: {QUEST: "We've been getting complaints from the residents lately about all of the Bloodsuckers.\x07See if you can defeat 20 Bloodsuckers to help out your fellow Toons in " + lDaisyGardens + '.'},
 3210: {QUEST: 'Oh no, The Squirting Flower on Maple Street just ran out of flowers!\x07Take them ten of your own squirting flowers to help out.\x07Make sure you have 10 squirting flowers in your inventory first.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I need to have 10 squirting flowers. You don't have enough!"},
 3211: {QUEST: "Oh, thank you so much! Those squirting flowers will save the day.\x07But I'm scared of the Cogs outside.\x07Can you help me out and defeat some of those Cogs?\x07Come back to me after you have defeated 20 Cogs on this street.",
        INCOMPLETE_PROGRESS: 'There are still Cogs out there to defeat!  Keep it up!',
        COMPLETE: "Oh, thank you! That helps a lot. Here's your reward."},
 3212: {QUEST: '_toNpcName_ needs some help looking for something she lost.\x07Go visit her and see what you can do._where_'},
 3213: {QUEST: 'Hi, _avName_. Can you help me?\x07I seem to have misplaced my pen. I think maybe some Cogs took it.\x07Defeat Cogs to find my stolen pen.',
        INCOMPLETE_PROGRESS: 'Have you found my pen yet?'},
 3214: {QUEST: "Yes, that's my pen! Thanks so much!\x07But while you were gone I realized my inkwell was missing too.\x07Defeat Cogs to find my inkwell.",
        INCOMPLETE_PROGRESS: "I'm still looking for my inkwell!"},
 3215: {QUEST: "Great! Now I have my pen and my inkwell back!\x07But wouldn't you know it?\x07My notepad is gone! They must have stolen it too!\x07Defeat Cogs to find my stolen notepad, and then bring it back for your reward.",
        INCOMPLETE_PROGRESS: 'Any word on that notepad yet?'},
 3216: {QUEST: "That's my notepad! Hooray! Your reward is...\x07Hey! Where did it go?\x07I had your reward right here in my office lockbox. But the whole lockbox is gone!\x07Can you believe it? Those Cogs stole your reward!\x07Defeat Cogs to recover my lockbox.\x07When you bring it back to me I'll give you your reward.",
        INCOMPLETE_PROGRESS: 'Keep looking for that lockbox!  It has your reward inside it!',
        COMPLETE: 'Finally! I had your new gag bag in that lockbox. Here it is...'},
 3217: {QUEST: "We've been performing some studies on Sellbot mechanics.\x07We still need to study some pieces more closely.\x07Bring us a sprocket from a Name Dropper.\x07You can catch one when the Cog is exploding."},
 3218: {QUEST: 'Good job! Now we need a sprocket from a Glad Hander for comparison.\x07These sprockets are harder to catch, so keep trying.'},
 3219: {QUEST: 'Great! Now we need just one more sprocket.\x07This time, we need a sprocket from a Mover & Shaker.\x07You might need to look inside some Sellbot buildings to find these Cogs.\x07When you catch one, bring it back for your reward.'},
 3244: {QUEST: "We've been performing some studies on Lawbot mechanics.\x07We still need to study some pieces more closely.\x07Bring us a sprocket from an Ambulance Chaser.\x07You can catch one when the Cog is exploding."},
 3245: {QUEST: 'Good job! Now we need a sprocket from a Back Stabber for comparison.\x07These sprockets are harder to catch, so keep trying.'},
 3246: {QUEST: 'Great! Now we need just one more sprocket.\x07This time, we need a sprocket from a Spin Doctor.\x07When you catch one, bring it back for your reward.'},
 3220: {QUEST: "I just heard that _toNpcName_ was asking around for you.\x07Why don't you drop by and see what she wants?_where_"},
 3221: {QUEST: 'Hi, _avName_! There you are!\x07I heard you were quite an expert in squirt attacks.\x07I need someone to set a good example for all the Toons in ' + lDaisyGardens + '.\x07Use your squirt attacks to defeat a bunch of Cogs.\x07Encourage your friends to use squirt too.\x07When you have defeated 20 Cogs, come back here for a reward!'},
 3222: {QUEST: "It's time to demonstrate your Toonmanship.\x07If you successfully reclaim a number of Cog buildings, you'll earn the right to carry three quests.\x07First, defeat any two Cog buildings.\x07Feel free to call on your friends to help you out."},
 3223: {QUEST: 'Great job on those buildings!\x07Now, defeat two more buildings.\x07These buildings must be at least two stories high, or higher.'},
 3224: {QUEST: 'Fantastic!\x07Now just defeat two more buildings.\x07These buildings must be at least three stories high.\x07When you finish, come back for your reward!',
        COMPLETE: 'You did it, _avName_!\x07You demonstrated your superior Toonmanship.',
        GREETING: ''},
 3225: {QUEST: "_toNpcName_ says she needs some help.\x07Why don't you go see what you can do to help out?_where_"},
 3235: {QUEST: "Oh, this is the salad I ordered!\x07Thank you for bringing it to me.\x07All those Cogs must have frightened away _toNpcName_'s regular delivery person again.\x07Why don't you do us a favor and defeat some of the Cogs out there?\x07Defeat 10 Cogs in " + lDaisyGardens + ' and then report back to _toNpcName_.',
        INCOMPLETE_PROGRESS: "You're working on defeating Cogs for me?\x07That's wonderful! Keep up the good work!",
        COMPLETE: 'Oh, thank you so much for defeating those Cogs!\x07Now maybe I can keep my regular delivery schedule.\x07Your reward is...',
        INCOMPLETE_WRONG_NPC: "Go tell _toNpcName_ about the Cogs you've defeated._where_"},
 3236: {QUEST: 'There are far too many Lawbots out there.\x07You can do your part to help!\x07Defeat 3 Lawbot buildings.'},
 3237: {QUEST: 'Great job on those Lawbot buildings!\x07But now there are too many Sellbots!\x07Defeat 3 Sellbot buildings, then come back for your reward.'},
 3238: {QUEST: 'Oh no! A Mingler Cog has stolen the Key to ' + lDaisyGardens + '!\x07See if you can recover it.\x07Remember, Minglers can be found only inside Sellbot buildings.'},
 3239: {QUEST: "You found a key all right, but it isn't the right one!\x07We need the Key to " + lDaisyGardens + '.\x07Keep looking! A Mingler Cog still has it!'},
 3242: {QUEST: 'Oh no! A Legal Eagle Cog has stolen the Key to ' + lDaisyGardens + '!\x07See if you can recover it.\x07Remember, Legal Eagles can be found only inside Lawbot buildings.'},
 3243: {QUEST: "You found a key all right, but it isn't the right one!\x07We need the Key to " + lDaisyGardens + '.\x07Keep looking! A Legal Eagle Cog still has it!'},
 3240: {QUEST: "I've just heard from _toNpcName_ that a Legal Eagle stole a bag of his bird seed.\x07Defeat Legal Eagles until you recover Bud's bird seed, and take it to him.\x07Legal Eagles are only found inside Lawbot buildings._where_",
        COMPLETE: 'Oh, thank you so much for finding my bird seed!\x07Your reward is...',
        INCOMPLETE_WRONG_NPC: 'Good job getting that bird seed back!\x07Now take it to _toNpcName_._where_'},
 3241: {QUEST: 'Some of the Cog buildings out there are getting too tall for our comfort.\x07See if you can bring down some of the tallest buildings.\x07Rescue 5 3-story buildings or taller and come back for your reward.'},
 3250: {QUEST: 'Detective Lima over on Oak Street has heard some reports of a Sellbot Headquarters.\x07Head over there and help her investigate.'},
 3251: {QUEST: "There is something strange going on around here.\x07There are so many Sellbots!\x07I've heard they have organized their own headquarters at the end of this street.\x07Head down the street and see if you can get to the bottom of this.\x07Find Sellbot Cogs in their headquarters, defeat 5 of them, and report back."},
 3252: {QUEST: "Ok, spill the beans.\x07What's that you say?\x07Sellbot Headquarters?? Oh no!!! Something must be done.\x07We must notify Judge McIntosh - she'll know what to do.\x07Go at once and tell her what you have found out. She's just down the street."},
 3253: {QUEST: "Yes, can I help you? I'm very busy.\x07Eh? Cog Headquarters?\x07Eh? Nonsense. That could never happen.\x07You must be mistaken. Preposterous.\x07Eh? Don't argue with me.\x07Ok then, bring back some proof.\x07If Sellbots really are building this Cog HQ, any Cog there will be carrying blueprints.\x07Cogs love paperwork, you know?\x07Defeat Sellbots in there until you find blueprints.\x07Bring them back here and maybe I'll believe you."},
 3254: {QUEST: "You again, eh? Blueprints? You have them?\x07Let me see those! Hmmm... A factory?\x07That must be where they are building the Sellbots... And what's this?\x07Yes, just what I suspected. I knew it all along.\x07They are building a Sellbot Cog Headquarters.\x07This is not good. Must make some phone calls. Very busy. Goodbye!\x07Eh? Oh yes, take these blueprints back to Detective Lima.\x07She can make more sense of them.",
        COMPLETE: "What did Judge McIntosh say?\x07We were right? Oh no. Let's see those blueprints.\x07Hmmm... Looks like Sellbots constructed a factory with machinery for building Cogs.\x07Sounds very dangerous. Stay out until you have more Laff points.\x07When you have more Laff points, we have much more to learn about Sellbot HQ.\x07For now, you should take this reward."},
 3255: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3256: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3257: {QUEST: '_toNpcName_ is investigating Sellbot Headquarters.\x07Go see if you can help._where_'},
 3258: {QUEST: 'There is much confusion about what the Cogs are up to in their new headquarters.\x07I need you to bring back some information directly from them.\x07If we can get four internal memos from Sellbots inside their HQ, that will clear things up.\x07Bring back your first memo to me so we can learn more.'},
 3259: {QUEST: 'Great! This let\'s see what the memo says....\x07"Attn Sellbots:"\x07"I\'ll be in my office at the top of Sellbot Towers promoting Cogs to higher levels."\x07"When you earn enough merits enter the elevator in the lobby to see me."\x07"Break time\'s over - back to work!"\x07"Signed, Sellbot V.P."\x07A-ha.... Flippy will want to see this. I\'ll send it to him right now.\x07Please go get your second memo and bring it back.'},
 3260: {QUEST: 'Oh good, you\'re back. Let\'s see what you found....\x07"Attn Sellbots:"\x07"Sellbot Towers has installed a new security system to keep all Toons out."\x07"Toons caught in Sellbot Towers will be detained for questioning."\x07"Please meet in the lobby for appetizers to discuss."\x07"Signed, Mingler"\x07Very interesting... I\'ll pass on this information immediately.\x07Please bring a third memo back.'},
 3261: {QUEST: 'Excellent job _avName_! What does the memo say?\x07"Attn Sellbots:"\x07"Toons have somehow found a way to infiltrate Sellbot Towers."\x07"I\'ll call you tonight during dinner to give you the details."\x07"Signed, Telemarketer"\x07Hmmm... I wonder how Toons are breaking in....\x07Please bring back one more memo and I think we\'ll have enough info for now.',
        COMPLETE: 'I knew you could do it! Ok, the memo says....\x07"Attn Sellbots:"\x07"I was having lunch with Mr. Hollywood yesterday."\x07"He reports that the V.P. is very busy these days."\x07"He will only be taking appointments from Cogs that deserve a promotion."\x07"Forgot to mention, Glad Hander is golfing with me on Sunday."\x07"Signed, Name Dropper"\x07Well, _avName_, this has been very helpful.\x07Here is your reward.'},
 3262: {QUEST: "_toNpcName_ has some new information about the Sellbot HQ Factory.\x07Go see what he's got._where_"},
 3263: {GREETING: 'Hi buddy!',
        QUEST: 'I\'m Coach Zucchini, but you can just call me Coach Z.\x07I put the "squash" in squash and stretch, if you know what I mean.\x07Listen, Sellbots have finished an enormous factory to pump out Sellbots 24 hours a day.\x07Get a group of Toon buddies together and squash the factory!\x07Inside Sellbot HQ, look for the tunnel to the Factory then board the Factory elevator.\x07Make sure you have full gags, full Laff points, and some strong Toons as guides.\x07Defeat the Foreman inside the factory to slow the Cog-making progress.\x07Sounds like a real workout, if you know what I mean.',
        LEAVING: 'See ya buddy!'},
 3264: {QUEST: 'Hey buddy, nice work on that Factory!\x07Looks like you found part of a Cog suit.\x07It must be left over from their Cog manufacturing process.\x07That may come in handy. Keep collecting these when you have spare time.\x07Maybe when you collect an entire Cog suit it could be useful for something...\x07You should speak with Professor Control about this._where_',
        COMPLETE: "Come fa' circuitry dis time?\x07No?  Den what'cha 'ere fo'?\x07Oh!  Coach Zucchini sent'cha?  Cog suit part?\x07Ah, ja... Interestin'...\x07Keep ya' guard up.  I'm sort o' interested in what ya' can do wit' a full suit.\x07Oh!  Ye deserve a reward fa' ya' work!"},
 4001: {GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving},
 4002: {GREETING: '',
        QUEST: 'Now you get to choose the next gag track you want to learn.\x07Take your time deciding, and come back here when you are ready to choose.',
        INCOMPLETE_PROGRESS: 'Think about your decision before choosing.',
        INCOMPLETE_WRONG_NPC: 'Think about your decision before choosing.',
        COMPLETE: 'A wise decision...',
        LEAVING: QuestsDefaultLeaving},
 4214: {GREETING: '',
        LEAVING: '',
        QUEST: "I just don't understand it!\x07Still not a SINGLE customer.\x07Maybe we need to go to the source.\x07Try reclaiming a Cashbot Cog building.\x07That Should do the trick...",
        INCOMPLETE_PROGRESS: 'Oh, please! Just one little building...',
        COMPLETE: "Still not a soul in here.\x07But you know, come to think of it.\x07I didn't have any customers before the Cogs invaded either!\x07I really appreciate all your help though.\x07This should help you get around."},
 4215: {QUEST: "Anna desperately needs someone to help her.\x07Why don't you drop in and see what you can do._where_"},
 4216: {QUEST: "Thanks for coming so quickly!\x07Seems like the Cogs have made off with several of my customers' cruise tickets.\x07Yuki said she saw a Glad Hander leaving here with his glad hands full of them.\x07See if you can get Lumber Jack's ticket to Alaska back.",
        INCOMPLETE_PROGRESS: 'Those Glad Handers could be anywhere now...'},
 4217: {QUEST: "Oh, great. You found it!\x07Now be a trooper and run in by Jack's for me, would you?_where_"},
 4218: {QUEST: "Great Googely Moogely!\x07Alaska here I come!\x07I can't take these infernal Cogs anymore.\x07Say, I think Anna needs you again._where_"},
 4219: {QUEST: "Yup, you guessed it.\x07I need you to shake down those pesky Glad Handers for Tabitha's ticket to Jazzfest.\x07You know the procedure...",
        INCOMPLETE_PROGRESS: "There's more out there somewhere..."},
 4220: {QUEST: 'Sweet!\x07Could you swing this one by his place for me too?_where_'},
 4221: {GREETING: '',
        LEAVING: 'Be cool...',
        QUEST: "Cool, daddio!\x07Now I'm in fat city, _avName_.\x07Before you split, you better go check out Anna Banana again..._where_"},
 4222: {QUEST: "This is the last one, I promise!\x07Now you are looking for Barry's ticket to the big singing contest.",
        INCOMPLETE_PROGRESS: "C'mon, _avName_.\x07Barry is counting on you."},
 4223: {QUEST: "This should put a smile on Barry's face._where_"},
 4224: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hello, hello, HELLO!\x07Terrific!\x07I just know me and the boys are going to clean up this year.\x07Anna says to swing back by and get your reward._where_\x07Goodbye, goodbye, GOODBYE!',
        COMPLETE: 'Thanks for all your help, _avName_.\x07You really are an asset here in Toontown.\x07Speaking of assets...'},
 902: {QUEST: 'Go see Leo.\x07He needs someone to deliver a message for him._where_'},
 4903: {QUEST: 'Dude!\x07My castanets are all cloudy and I have a big show tonight.\x07Take them to Carlos and see if he can polish them up._where_'},
 4904: {QUEST: 'Jes, I tink I can polish dees.\x07But I need soma de blue ink from de squid.',
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: "Juo can find de squid wherever dere's a fishing pier"},
 4905: {QUEST: "Jes! Dat's it!\x07Now I need a leetle time to polish dees.\x07Why don juo go reclaim a Cog beelding while I work?",
        GREETING: 'Hola!',
        LEAVING: 'Adios!',
        INCOMPLETE_PROGRESS: 'Jest anodder minute...'},
 4906: {QUEST: 'Bery good!\x07Here are de castanets for Leo._where_'},
 4907: {GREETING: '',
        QUEST: "Cool, dude!\x07They look awesome!\x07Now I need you to get a copy of the lyrics to 'A Beat Christmas' from Hedy._where_"},
 4908: {QUEST: "Hello there!\x07Hmmm, I don't have a copy of that song handy.\x07If you give me a little while I could transcribe it from memory.\x07Why don't you run along and reclaim a two story building while I write?"},
 4909: {QUEST: "I'm sorry.\x07My memory is getting a little fuzzy.\x07If you go reclaim a three story building I'm sure I'll be done when you get back..."},
 4910: {QUEST: 'All done!\x07Sorry it took so long.\x07Take this back to Leo._where_',
        GREETING: '',
        COMPLETE: 'Awesome, dude!\x07My concert is gonna rock!\x07Speaking of rock, you can rock some Cogs with this...'},
 5247: {QUEST: 'This neighborhood is pretty tough...\x07You might want to learn some new tricks.\x07_toNpcName_ taught me everything I know, so maybe he can help you too._where_'},
 5248: {GREETING: 'Ahh, yes.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You appear to be struggling with my assignment.',
        QUEST: 'Ahh, so welcome, new apprentice.\x07I know all there is to know about the pie game.\x07But before we can begin your training, a small demonstration is necessary.\x07Go out and defeat ten of the largest Cogs.'},
 5249: {GREETING: 'Mmmmm.',
        QUEST: 'Excellent!\x07Now demonstrate your skill as a fisherman.\x07I dropped three fuzzy dice in the pond yesterday.\x07Fish them out and bring them to me.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'It seems you may not be so clever with the rod and reel.'},
 5250: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Lawbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5258: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Bossbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Cashbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5260: {GREETING: '',
        LEAVING: '',
        QUEST: 'Aha!  These dice will look great hanging from the rearview mirror of my ox cart!\x07Now, show me that you can tell your enemies from one another.\x07Return when you have restored two of the tallest Sellbot buildings.',
        INCOMPLETE_PROGRESS: 'Do the buildings give you trouble?'},
 5200: {QUEST: 'Those sneaky Cogs are at it again.\x07_toNpcName_ has reported another missing item. Stop by and see if you can straighten it out._where_'},
 5201: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Head Hunters came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5261: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Two-Faces came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5262: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Money Bags came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5263: {GREETING: '',
        QUEST: 'Hi, _avName_.  I reckon I should thank you for coming.\x07A group of those Spin Doctors came in and stole my soccer ball.\x07The leader told me that I had to make some cutbacks and just grabbed it away from me!\x07Can you get my ball back?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck finding my soccer ball?',
        COMPLETE: 'Yeehaw! You found it!\x07 Here, take your reward...'},
 5202: {QUEST: lTheBrrrgh + " has been overrun with some of the toughest Cogs we've seen yet.\x07You will probably want to carry more gags around here.\x07I hear _toNpcName_ may have a large bag you can use to carry more gags._where_"},
 5203: {GREETING: 'Huh?  Are you on my sledding team?',
        QUEST: "What's that?  You want a bag?\x07I had one somewhere around here... maybe it's in my toboggan?\x07Only... I haven't seen my toboggan since the big race!\x07Maybe one of those Cogs took it?",
        LEAVING: 'Have you seen my toboggan?',
        INCOMPLETE_PROGRESS: "Who are you again?  Sorry, I'm a little woozy from the crash."},
 5204: {GREETING: '',
        LEAVING: '',
        QUEST: "Is that my toboggan?  I don't see any bag here.\x07I think Bumpy Noggin was on the team... maybe he has it?_where_"},
 5205: {GREETING: 'Ohhh, my head!',
        LEAVING: '',
        QUEST: "Huh?  Ted who?  A bag?\x07Oh, maybe he was on our toboggan team?\x07My head hurts so much I can't think straight.\x07Could you fish me out some ice cubes from the frozen pond for my head?",
        INCOMPLETE_PROGRESS: "Oww, my head's killing me!  Got any ice?"},
 5206: {GREETING: '',
        LEAVING: '',
        QUEST: "Ahhh, that feels much better!\x07So you're looking for Ted's bag, huh?\x07I think it ended up on Sam Simian's head after the crash._where_"},
 5207: {GREETING: 'Eeeep!',
        LEAVING: '',
        QUEST: 'What is bag?  Who is Bompy?\x07Me scared of buildings!  You beat buildings, I give you bag!',
        INCOMPLETE_PROGRESS: 'More buildings!  Me still scared!',
        COMPLETE: 'Ooooh!  Me like you!'},
 5208: {GREETING: '',
        LEAVING: 'Eeeek!',
        QUEST: 'Ooooh!  Me like you!\x07Go to Ski Clinic. Bag there.'},
 5209: {GREETING: 'Dude!',
        LEAVING: 'Later!',
        QUEST: "Man, that Simian Sam is crazy!\x07If you're wild like Sam, I'll give you your bag, man.\x07Go bag some Cogs for your bag, man! Hey now!",
        INCOMPLETE_PROGRESS: "Are you sure you're extreme enough?  Go bag some more Cogs.",
        COMPLETE: "Hey, you are pretty wild!  That was a heap of Cogs you bagged!\x07Here's your bag!"},
 5210: {QUEST: '_toNpcName_ is secretly in love with someone in the neighborhood.\x07If you help her, she may reward you handsomely._where_'},
 5211: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Cogs with a beak came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5264: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Cogs with a fin came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5265: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Mingler Cogs came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5266: {GREETING: 'Boo hoo.',
        QUEST: 'I spent all last night writing a letter to the dog I love.\x07But before I could deliver it, one of those nasty Corporate Raiders came in and took it.\x07Can you get it back for me?',
        LEAVING: 'Boo hoo.',
        INCOMPLETE_PROGRESS: 'Please find my letter.'},
 5212: {QUEST: 'Oh, thank you for finding my letter!\x07Please, please, please could you deliver it to the most handsome dog in the neighborhood?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "You didn't deliver my letter, did you?"},
 5213: {GREETING: "Charmed, I'm sure.",
        QUEST: "I can't be bothered with your letter, you see.\x07All my doggies have been taken from me!\x07If you bring them back, maybe we can talk then.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'My poor little doggies!'},
 5214: {GREETING: '',
        LEAVING: 'Toodleloo!',
        QUEST: "Thank you for bringing back my little beauties.\x07Let's take a look at your letter now...\nMmmm, it seems I have yet another secret admirer.\x07This calls for a trip to my dear friend Carl.\x07I'm sure you'll like him immensely._where_"},
 5215: {GREETING: 'Heh, heh...',
        LEAVING: 'Come back, yes, yes.',
        INCOMPLETE_PROGRESS: "There are still some big ones around.  Comes back to us when they're gone.",
        QUEST: "Who sent you to us?  We don't like Snootsies much, we don't...\x07But we likes Cogs even less...\x07Run the big ones off and we'll helps you we will."},
 5216: {QUEST: 'We told you we would helps you.\x07So take this ring to the girl.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You still haves the ring???',
        COMPLETE: 'Oh darrrling!!! Thank you!!!\x07Oh, and I have something special for you as well.'},
 5217: {QUEST: 'It sounds like _toNpcName_ could use some help._where_'},
 5218: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm sure there are more Minglers around somewhere.",
        QUEST: "Help!!! Help!!! I can't take it anymore!\x07Those Minglers are driving me batty!!!"},
 5219: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "That can't be all of them.  I just saw one!!!",
        QUEST: "Oh, thanks, but now it's the Corporate Raiders!!!\x07You've got to help me!!!"},
 5220: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No, no, no there was one just here!',
        QUEST: "I realize now that it's those Loan Sharks!!!\x07I thought you were going to save me!!!"},
 5221: {GREETING: '',
        LEAVING: '',
        QUEST: "You know what, maybe it isn't the Cogs at all!\x07Could you ask Fanny to make me a soothing potion?  Maybe that would help...._where_"},
 5222: {LEAVING: '',
        QUEST: "Oh, that Harry, he sure is a card!\x07I'll whip up something that will fix him right up!\x07Oh, I appear to be out of sardine whiskers...\x07Be a dear and run down to the pond and catch some for me.",
        INCOMPLETE_PROGRESS: 'Got those whiskers for me yet?'},
 5223: {QUEST: 'Okay.  Thanks, hon.\x07Here, now take this to Harry.  It should calm him right down.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go on now, take the potion to Harry.'},
 5224: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Go get those Legal Eagles for me, will you?',
        QUEST: "Oh thank goodness you're back!\x07Give me the potion, quick!!!\x07Glug, glug, glug...\x07That tasted awful!\x07You know, what, though?  I feel much calmer.  Now that I can think clearly, I realize that...\x07It was the Legal Eagles that were driving me crazy all this time!!!",
        COMPLETE: "Oh boy!  Now I can relax!\x07I'm sure there's something here I can give you.  Oh, take this!"},
 5225: {QUEST: 'Ever since the incident with the turnip bread, Grumpy Phil has been mad at _toNpcName_.\x07Maybe you could help Gus fix things between them?_where_'},
 5226: {QUEST: 'Yeah, you probably heard Grumpy Phil is mad at me...\x07I was just trying to be nice with that turnip bread.\x07Maybe you can help cheer him up.\x07Phil really hates those Cashbot Cogs, especially their buildings.\x07If you reclaim some Cashbot buildings, it might help.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Maybe a few more buildings?'},
 5227: {QUEST: "That's terrific!  Go tell Phil what you've done._where_"},
 5228: {QUEST: 'Oh he did, did he?\x07That Gus thinks he can get off so easy, does he?\x07Only broke my tooth, he did, with that turnip bread of his!\x07Maybe if you took my tooth to Dr. Mumbleface for me he could fix it.',
        GREETING: 'Mmmmrrphh.',
        LEAVING: 'Grumble, grumble.',
        INCOMPLETE_PROGRESS: 'You again?  I thought you were going to get my tooth fixed for me.'},
 5229: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Cashbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5267: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Sellbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5268: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Lawbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5269: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I'm still working on the tooth.  It will be a bit longer.",
        QUEST: "Yes, that tooth looks pretty bad, alrighty.\x07Maybe I can do something, but it will be a little while.\x07Maybe you could clear some of those Bossbot Cogs off the streets while you're waiting?\x07They're scaring off my customers."},
 5230: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Robber Baron came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5270: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Big Cheese came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5271: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately Mr. Hollywood came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5272: {GREETING: '',
        QUEST: "I'm glad you're back!\x07I gave up trying to fix that old tooth, and made a new gold tooth for Phil instead.\x07Unfortunately a Big Wig came in and took it from me.\x07Maybe you can catch him if you hurry.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find that tooth yet?'},
 5231: {QUEST: "Great, that's the tooth alrighty!\x07Why don't you just run it over to Phil for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I bet Phil would like to see his new tooth.'},
 5232: {QUEST: "Oh, thanks.\x07Mmmrrrphhhh\x07How's that look, huh?\x07Okay, you can tell Gus that I forgive him.",
        LEAVING: '',
        GREETING: ''},
 5233: {QUEST: "Oh, that's great to hear.\x07I figured old Phil couldn't stay mad at me.\x07As a gesture of goodwill, I baked him this Pine cone bread.\x07Could you run it over to him for me?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Better hurry.  Pine cone bread is better when it's hot.",
        COMPLETE: "Oh, what's this?  For me?\x07Munch, munch...\x07Owwww!  My tooth!  That Gus Gooseburger!\x07Oh well, it wasn't your fault.  Here, you can have this for your trouble."},
 903: {QUEST: 'You may be ready to see _toNpcName_ the Blizzard Wizard for your final test._where_'},
 5234: {GREETING: '',
        QUEST: 'Aha, you are back.\x07Before we begin, we must eat.\x07Bring us some lumpy cheese for our broth.\x07Lumpy cheese can only be gathered from Big Cheese Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need lumpy cheese'},
 5278: {GREETING: '',
        QUEST: 'Aha, you are back.\x07Before we begin, we must eat.\x07Bring us some caviar for our broth.\x07Caviar can only be gathered from Mr. Hollywood Cogs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'We still need caviar'},
 5235: {GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x07A Cog took my simple spoon, so I simply can not eat.\x07Return my spoon to me.  I think a Robber Baron took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.'},
 5279: {GREETING: '',
        QUEST: 'A simple man eats with a simple spoon.\x07A Cog took my simple spoon, so I can not eat.\x07Return my spoon to me.  I think a Big Wig took it.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I simply must have my spoon.'},
 5236: {GREETING: '',
        QUEST: 'Many thanks.\x07Slurp, slurp...\x07Ahhh, now you must catch a talking toad.  Try fishing in the pond.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that talking toad?'},
 5237: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You have not yet obtained dessert.',
        QUEST: "Oh, that is certainly a talking toad.  Give him to me.\x07What's that you say, toad?\x07Uh huh.\x07Uh huh...\x07The toad has spoken.  We need dessert.\x07Bring us some ice cream cones from _toNpcName_.\x07The toad likes red bean flavored ice cream for some reason._where_"},
 5238: {GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x07You see, a bunch of Cogs came in and just took them.\x07They said they were for Mr. Hollywood, or some such nonsense.\x07I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?'},
 5280: {GREETING: '',
        QUEST: "So the wizard sent you.  I'm sad to say we're fresh out of red bean ice cream cones.\x07You see, a bunch of Cogs came in and just took them.\x07They said they were for The Big Cheese, or some such nonsense.\x07I'd sure appreciate if you could round them back up for me.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Have you found all my ice cream cones yet?'},
 5239: {QUEST: "Thanks for bringing back my ice cream cones!\x07Here's one for Lil Oldman.",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'You better bring that ice cream to Lil Oldman before it melts.'},
 5240: {GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x07Slurp, slurp...\x07Okay, now we are almost ready.\x07If you can just bring me some powder to dry my hands.\x07I think those Big Wig Cogs sometimes have powder from their wigs.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?'},
 5281: {GREETING: '',
        QUEST: 'Very good.  Here you go toad...\x07Slurp, slurp...\x07Okay, now we are almost ready.\x07If you can just bring me some powder to dry my hands.\x07I think those Mr. Hollywood Cogs sometimes keep powder for their noses.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Did you find any powder?'},
 5241: {QUEST: 'Okay.\x07As I once said, to truly throw a pie, you must throw not with the hand...\x07...but with the soul.\x07I know not what that means, so I will sit and contemplate while you restore buildings.\x07Return when you have completed your task.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Your task is not yet complete.'},
 5242: {GREETING: '',
        QUEST: 'Although I still know not what I am talking about, you truly are worthy.\x07I give you a final task...\x07The talking toad would like a girlfriend.\x07Find another talking toad.  The toad has spoken.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Where is that other talking toad?',
        COMPLETE: 'Whew!  I am tired from all this effort.  I must rest now.\x07Here, take your reward and be off.'},
 5243: {QUEST: 'Sweaty Pete is starting to stink up the street.\x07Can you talk him into taking a shower or something?_where_'},
 5244: {GREETING: '',
        QUEST: "Yeah, I guess I do work up quite a sweat in here.\x07Mmmm, maybe if I could fix that leaky pipe in my shower...\x07I figure a gear from one of those tiny Cogs would do the trick.\x07Go find a gear from a Micromanager and we'll try it.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Where's that gear you were going to get?"},
 5245: {GREETING: '',
        QUEST: 'Yup, that seemed to do the trick.\x07But I get lonely when I shower...\x07Could you go fish me up a rubber ducky to keep me company?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Any luck with that duck?'},
 5246: {QUEST: "The ducky's great, but...\x07All those buildings around here make me nervous.\x07I'd feel a lot more relaxed if there were fewer buildings around.",
        LEAVING: '',
        COMPLETE: "Okay, I'll shower up now.  And here's something for you too.",
        INCOMPLETE_PROGRESS: "I'm still worried about buildings."},
 5251: {QUEST: 'Lounge Lassard is supposed to be playing a gig tonight.\x07I hear he might be having some trouble with his equipment._where_'},
 5252: {GREETING: '',
        QUEST: 'Oh yeah!  I could sure use some help.\x07Those Cogs came in and swiped all my gear while I was unloading the van.\x07Can you give me a hand and get back my microphone?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Hey man, I can't sing without my microphone."},
 5253: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Corporate Raiders got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5273: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Minglers got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5274: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Loan Sharks got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5275: {GREETING: '',
        QUEST: "Yeah, that's my microphone all right.\x07Thanks for getting it for me, but...\x07I really need my keyboard so I can tickle the ivories.\x07I think one of those Legal Eagles got my keyboard.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'No luck finding my keboard?'},
 5254: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Mr. Hollywood, if I had to guess.",
        LEAVING: '',
        COMPLETE: "All right!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5282: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Big Cheese, if I had to guess.",
        LEAVING: '',
        COMPLETE: "All right!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5283: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Robber Baron, if I had to guess.",
        LEAVING: '',
        COMPLETE: "All right!!  I'm ready now.\x07Hello, Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5284: {GREETING: '',
        QUEST: "All right!  Now I'm in business.\x07If only they hadn't taken my platform shoes...\x07Those shoes probably ended up with a Big Wig, if I had to guess.",
        LEAVING: '',
        COMPLETE: "All right!!  I'm ready now.\x07Hello Brrrgh!!!\x07Huh?  Where is everyone?\x07Okay, take this and round me up some fans, huh?",
        INCOMPLETE_PROGRESS: "I can't perform barefoot, can I?"},
 5255: {QUEST: 'You look like you could use more Laff points.\x07Maybe _toNpcName_ could sort you out._where_'},
 5256: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for Laff points, huh?\x07Have I got a deal for you!\x07Simply take care of a few Bossbot Cogs for me...\x07And I'll make it worth your while."},
 5276: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "A deal's a deal.",
        QUEST: "So you're looking for Laff points, huh?\x07Have I got a deal for you!\x07Simply take care of a few Lawbot Cogs for me...\x07And I'll make it worth your while."},
 5257: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x07Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x07You must have misunderstood, our deal was for Sellbot Cogs.\x07I'm sure I told you to defeat some Sellbot Cogs for me."},
 5277: {GREETING: '',
        LEAVING: '',
        COMPLETE: "Okay, but I'm certain I told you to round up some Lawbot Cogs.\x07Well, if you say so, but you owe me one.",
        INCOMPLETE_PROGRESS: "I don't think you're done yet.",
        QUEST: "You say you're done?  Defeated all the Cogs?\x07You must have misunderstood, our deal was for Cashbot Cogs.\x07I'm sure I told you to defeat some Cashbot Cogs for me."},
 5301: {QUEST: "I can't help you with Laff points, but maybe _toNpcName_ will cut you a deal.\x07He's a little on tempermental side though..._where_"},
 5302: {GREETING: '',
        LEAVING: '',
        COMPLETE: "I told you what?!?!\x07Thanks a bunch! Here's your Laff point!",
        INCOMPLETE_PROGRESS: 'Hi!\x07What are you doing in here again!',
        QUEST: 'A Laff point? I dont think so!\x07Sure, but only if you clear out some of these pesky Lawbots first.'},
 5303: {QUEST: lTheBrrrgh + " is teeming with very dangerous Cogs.\x07If I were you, I'd carry more gags around here.\x07I hear _toNpcName_ can make you a large bag if you are willing to do the legwork._where_"},
 5304: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'There should be plenty of Lawbots out there.\x07So get to it!',
        QUEST: "A bigger bag?\x07I could probably whip one up for ya.\x07I'll need some yarn though.\x07Some Lawbots made off with mine yesterday morning."},
 5305: {GREETING: 'Howdy!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Go get some more cogs.\x07This color hasn't taken yet.",
        QUEST: "That there's some fine yarn!\x07Not my first choice of color though.\x07Tell you what...\x07You go out there and beat up some of the tougher cogs...\x07And I'll get to work dyeing this yarn."},
 5306: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'They gotta be down there somewhere...',
        QUEST: "Well, the yarn is all dyed. But we've got a small problem.\x07I can't find my knitting needles anywhere.\x07Last place I saw them was down at the pond."},
 5307: {GREETING: '',
        LEAVING: 'Much obliged!',
        INCOMPLETE_PROGRESS: "Rome wasn't knit in a day!",
        QUEST: "Those are my needles alright.\x07While I'm knitting, why don't you go clear some of them big buildings?",
        COMPLETE: "Great work!\x07And speaking of great work...\x07Here's your new bag!"},
 5308: {GREETING: '',
        LEAVING: '',
        QUEST: 'I hear _toNpcName_ is having some legal troubles.\x07Can you stop by and check it out?_where_'},
 5309: {GREETING: "I'm glad you're here...",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Please hurry! The street is crawling with them!',
        QUEST: "The Lawbots have really taken over out there.\x07I'm afraid they are going to take me to court.\x07Do you think you could help get them off of this street?"},
 5310: {GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'I think I hear them coming for me...',
        QUEST: "Thanks. I feel a little better now.\x07 But there is one more thing...\x07Could you drop by _toNpcName_'s and get me an alibi?_where_"},
 5311: {GREETING: 'WHAAAA!!!!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "I can't help him if you can't find it!",
        QUEST: "Alibi?! Why that's a great idea!\x07You'd better make it two!\x07I bet a Legal Eagle would have some..."},
 5312: {GREETING: 'Finally!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '',
        COMPLETE: "Whew! Am I ever relieved to have this.\x07Here's your reward...",
        QUEST: "Super! You'd better run these back to _toNpcName_!"},
 6201: {QUEST: 'Powers Erge needs some help. Could you drop by and lend her a hand?_where_'},
 6202: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, a customer! Great! What can I do for you?\x07What do you mean, what can you do for me? OH! You're not a customer.\x07I remember now. You're here to help with those dreadful Cogs.\x07Well I could certainly use the help even if you're not a customer.\x07If you clean up the streets a bit, I'll have a little something for you.",
        INCOMPLETE_PROGRESS: "If you don't want electricity, I can't help you until you defeat those Cogs.",
        COMPLETE: "Good job on those Cogs, _avName_.\x07Now, are you sure I can't interest you in some electricity? Might come in handy....\x07No? OK, suit yourself.\x07Hunh? Oh yeah, I remember. Here ya go. This is sure to help with those nasty Cogs.\x07Keep up the good work!"},
 6206: {QUEST: "Well, _avName_, I don't have anything for you right now.\x07Wait! I think Susan Siesta was looking for help. Why don't you go see her?_where_"},
 6207: {GREETING: '',
        LEAVING: '',
        QUEST: "I'll never get rich with those darn Cogs driving away all my business!\x07You've got to help me, _avName_.\x07Clear out a few Cog buildings for the sake of the neighborhood and I'll add to your riches.",
        INCOMPLETE_PROGRESS: "Poor me! Can't you get rid of those buildings?",
        COMPLETE: "Now I'll be in the money! I can see it now!\x07I'll spend all my time fishing. Now, let me enrich your life a little.\x07There you go!"},
 6211: {QUEST: 'Hey _avName_! I heard Lawful Linda was looking for you.\x07You should stop by and pay her a visit._where_'},
 6212: {GREETING: '',
        LEAVING: '',
        QUEST: "Hi there! Wow, am I glad to see you!\x07I've been working on this answering machine in my spare time but I'm short a couple of parts.\x07I need three more rods and the ones from Bean Counters seem to work pretty well.\x07Could you see if you could find some rods for me?",
        INCOMPLETE_PROGRESS: 'Still trying to find those rods?'},
 6213: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, those will do nicely.\x07That's funny. I was sure I had a spare drive belt around here but I can't find it.\x07Could you please get one from a Money Bags for me? Thanks!",
        INCOMPLETE: "Well, I can't help you until I get that drive belt."},
 6214: {GREETING: '',
        LEAVING: '',
        QUEST: "Ah, that's it. Now it should run like a charm.\x07Where'd my pliers go? I can't tighten this up without the pliers.\x07Maybe pincers from a Penny Pincher would do the job?\x07If you'd go find one, I could give you a little something to help you with those Cogs.",
        INCOMPLETE_PROGRESS: 'No pincers yet, hunh? Keep looking.',
        COMPLETE: "Great! Now I'll just tighten this up.\x07It seems to be working now. Back in business!\x07Well, except that we don't have a phone. But I'm glad for the help, anyway.\x07I think this'll help you out with those Cogs. Good luck!"},
 6221: {QUEST: 'I heard Rocco was looking for help. See what you can do for him._where_'},
 6222: {GREETING: '',
        LEAVING: '',
        QUEST: "Yo! Youse came to da right place. I ain't too happy.\x07Yeah, I was lookin for some help wid dose Cogs. Dey always come and boss me around.\x07If you can retire some of dem Bossbots, I'll make it worth your while.",
        INCOMPLETE_PROGRESS: "Hey, _avName_, what's up wid youse?\x07You gotta keep after dem Bossbots. We got a deal, remember?\x07Rocco always keeps his word.",
        COMPLETE: "Yo, _avName_! Youse ok in my book.\x07Dem Bossbots ain't so bossy now, is they?\x07Here ya go! A nice big boost. Now, you stay outta trouble, ya hear!"},
 6231: {QUEST: 'Nat over on Pajama Place heard rumors about a Cashbot Headquarters.\x07Head over there and see if you can help him out._where_'},
 6232: {GREETING: '',
        LEAVING: '',
        QUEST: "I got a nibble about some strange goings on.\x07Well, maybe it's the fleas but something is going on anyway.\x07All these Cashbots!\x07I think they've opened another headquarters right off Pajama Place.\x07P.J. knows his way around.\x07Go see _toNpcName_ _where_ Ask him if he's heard anything.",
        INCOMPLETE_PROGRESS: "You haven't seen P.J. yet? What's keeping you?\x07Oh, these darn fleas!"},
 6233: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there _avName_, where are you headed?\x07Cashbot Headquarters?? I haven't seen anything.\x07Could you go to the end of Pajama Place and see if it's true?\x07Find some Cashbot Cogs in their headquarters, defeat a few of them, and come tell me about it.",
        INCOMPLETE_PROGRESS: "Found the HQ yet? You'll need to defeat some Cashbots there to scope it out."},
 6234: {GREETING: '',
        LEAVING: '',
        QUEST: "What?! There really IS a Cashbot HQ?\x07You better go tell Nat right away!\x07Who would have guessed there'd be a Cog HQ right down the street from him?",
        INCOMPLETE_PROGRESS: "What did Nat have to say? You haven't seen him yet?"},
 6235: {GREETING: '',
        LEAVING: '',
        QUEST: "So, I'm itching to hear what P.J. had to say.\x07Hmm...we need more information about this Cog business but I've got to get rid of these fleas!\x07I know! YOU can go find out more!\x07Go defeat Cashbots at the HQ until you find some plans then come right back!",
        INCOMPLETE_PROGRESS: "No plans yet? Keep searching those Cogs!\x07They're bound to have some plans!",
        COMPLETE: "You got the plans?\x07Great! Let's see what they say.\x07I see... the Cashbots built a Mint to make Cogbucks.\x07It must be FULL of Cashbots. We should find out more about this.\x07Maybe if you had a disguise. Hmmm...wait! I think I've got part of a Cog suit here somewhere....\x07Here it is! Why don't you take this for your trouble? Thanks again for your help!"},
 6241: {QUEST: "The Countess has been looking everywhere for you! Please pay her a visit so she'll stop calling._where_"},
 6242: {GREETING: '',
        LEAVING: '',
        QUEST: "_avName_, I'm counting on you to help me!\x07You see, these Cogs are making so much noise that I simply can't concentrate.\x07I keep losing count of my sheep!\x07If you'll cut down on the noise, I'll help you out too! You can count on it!\x07Now, where was I? Right, one hundred thirty-six, one hundred thirty-seven....",
        INCOMPLETE_PROGRESS: "Four hundred forty-two...four hundred forty-three...\x07What? You're back already? But it's still so noisy!\x07Oh no, I've lost count again.\x07 One...two...three....",
        COMPLETE: "Five hundred ninety-three...five hundred ninety-four...\x07Hello? Oh, I knew I could count on you! It's much quieter now.\x07Here you go, for all those Number Crunchers.\x07Number? Now I need to start counting all over again! One...two...."},
 6251: {QUEST: "Poor Zari broke her zipper and now she can't make deliveries to her customers. She could sure use your help._where_"},
 6252: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, hi _avName_. You're here to help with my deliveries?\x07That's terrific! This broken zipper makes it tough to zip around.\x07Let me see...ok, this should be easy. Cowboy George ordered a zither last week.\x07Could you please bring it over to him? _where_",
        INCOMPLETE_PROGRESS: 'Oh, hi! Did you forget something? Cowboy George is waiting for that zither.'},
 6253: {GREETING: '',
        LEAVING: '',
        QUEST: "My zither! At last! Gosh, I can't wait to play it.\x07Go tell Zari that I said thanks, would you?",
        INCOMPLETE_PROGRESS: "Thanks again for the zither. Doesn't Zari have more deliveries for you to do?"},
 6254: {GREETING: '',
        LEAVING: '',
        QUEST: "That was fast. What's next on my list?\x07Right. Master Mike ordered a Zamboni. That zany guy.\x07Could you bring this to him, please?_where_",
        INCOMPLETE_PROGRESS: 'That Zamboni needs to go to Master Mike._where_'},
 6255: {GREETING: '',
        LEAVING: '',
        QUEST: "All-right! The Zamboni I ordered!\x07Now, if only there weren't so many Cogs around, I might have some time to use it.\x07Be a sport and take care of a few of those Cashbots for me, would you?",
        INCOMPLETE_PROGRESS: 'Those Cashbots are tough, hunh? They make it hard to test my Zamboni.'},
 6256: {GREETING: '',
        LEAVING: '',
        QUEST: "Excellent! Now I can go try out my Zamboni.\x07Tell Zari that I'll be in next week to place my next order, please.",
        INCOMPLETE_PROGRESS: "That's all I need for now. Isn't Zari waiting for you?"},
 6257: {GREETING: '',
        LEAVING: '',
        QUEST: "So, Master Mike was happy with his Zamboni? Great.\x07Who's next? Oh, Zen Glen ordered a zebra-striped zabuton.\x07Here it is! Could you zoom over to his place, please?_where_",
        INCOMPLETE_PROGRESS: 'I think Zen Glen needs that zabuton to meditate.'},
 6258: {GREETING: '',
        LEAVING: '',
        QUEST: "Ah, my zabuton at last. Now I can meditate.\x07Who could focus with that racket going on? All those Cogs!\x07Since you're already here, maybe you could take care of some of these Cogs?\x07Then I could use my zabuton in peace.",
        INCOMPLETE_PROGRESS: 'Still so noisy with those Cogs! Who could focus?'},
 6259: {GREETING: '',
        LEAVING: '',
        QUEST: 'Peace and quiet at last. Thanks, _avName_.\x07Please tell Zari how happy I am. OM....',
        INCOMPLETE_PROGRESS: 'Zari called looking for you. You should go see what she needs.'},
 6260: {GREETING: '',
        LEAVING: '',
        QUEST: "I'm glad to hear that Zen Glen is happy with his zebra zabuton.\x07Oh, these zinnias just came in for Rose Petals.\x07Since you seem to have some zeal for deliveries, perhaps you could take them over to her?_where_",
        INCOMPLETE_PROGRESS: "Those zinnias will wilt if you don't deliver them soon."},
 6261: {GREETING: '',
        LEAVING: '',
        QUEST: 'What lovely zinnias! Zari sure does deliver.\x07Oh, well, I guess YOU deliver, _avName_. Please thank Zari for me!',
        INCOMPLETE_PROGRESS: "Don't forget to thank Zari for the zinnias!"},
 6262: {GREETING: '',
        LEAVING: '',
        QUEST: "Welcome back, _avName_. You're pretty zippy.\x07Let's see...what's next on my list to deliver? Zydeco records for Wyda Wake._where_",
        INCOMPLETE_PROGRESS: "I'm sure Wyda Wake is waiting for those Zydeco records."},
 6263: {GREETING: '',
        LEAVING: '',
        QUEST: "Zydeco records? I don't remember asking for Zydeco records.\x07Oh, I bet Lullaby Lou ordered them._where_",
        INCOMPLETE_PROGRESS: 'No, those Zydeco records are for Lullaby Lou._where_'},
 6264: {GREETING: '',
        LEAVING: '',
        QUEST: "At last, my Zydeco records! I thought Zari had forgotten.\x07Could you please bring this zucchini to her? She'll find someone who wants one. Thanks!",
        INCOMPLETE_PROGRESS: "Oh, I've got plenty of zucchini already. Take that one to Zari."},
 6265: {GREETING: '',
        LEAVING: '',
        QUEST: "Zucchini? Hmm. Well, someone will want it, I'm sure.\x07Ok, we're nearly done with my list. One more delivery to make.\x07Babyface MacDougal ordered a zoot suit._where_",
        INCOMPLETE_PROGRESS: "If you don't deliver that zoot suit to Babyface MacDougal,\x07 it'll get all wrinkled."},
 6266: {GREETING: '',
        LEAVING: '',
        QUEST: "Once upon a time...oh! You're not here for a story, are you?\x07You're delivering my zoot suit? Great! Wow, that's something.\x07Hey, could you give Zari a message for me? I'll be needing zircon cufflinks to go with the suit. Thanks!",
        INCOMPLETE_PROGRESS: 'Did you give Zari my message?',
        COMPLETE: "Zircon cufflinks, hunh? Well, I'll see what I can do for him.\x07Anyway, you've been the very zenith of helpfulness and I can't let you leave with zilch.\x07Here's a BIG boost to help you zap those Cogs!"},
 6271: {QUEST: "Drowsy Dave is having some trouble that you might be able to help with. Why don't you stop by his shop?_where_"},
 6272: {GREETING: '',
        LEAVING: '',
        QUEST: "What? Huh? Oh, I must've fallen asleep.\x07You know, those Cogs buildings are full of machinery that makes me really sleepy.\x07I listen to them humming all day and...\x07Huh? Oh, yeah, right. If you could get rid of some of those Cog buildings, I could stay awake.",
        INCOMPLETE_PROGRESS: "Zzzzz...huh? Oh, it's you, _avName_.\x07Back already? I was just taking a little nap.\x07Come back when you're done with those buildings.",
        COMPLETE: "What? I dropped off to sleep for a minute there.\x07Now that those Cog buildings are gone I can finally relax.\x07Thanks for your help, _avName_.\x07See you later! I think maybe I'll take a little nap."},
 6281: {QUEST: "Head over and call on Teddy Blair. He's got a job for you._where_"},
 6282: {GREETING: '',
        LEAVING: '',
        QUEST: "What did you say? No, I don't have a fob for you.\x07Oh, a job! Why didn't you say so? You'll need to speak up.\x07Those Cogs make it hard to hibernate. If you'll help make Dreamland quieter,\x07I'll give you a little something.",
        INCOMPLETE_PROGRESS: "You beat the bogs? What bogs?\x07Oh, the Cogs! Why didn't you say so?\x07Hmm, it's still pretty loud. How 'bout you defeat a few more?",
        COMPLETE: "You had fun? Huh? Oh!\x07You're done! Great. Really nice of you to help out this way.\x07I found this in the back room but I don't have any use for it.\x07Maybe you'll find something to do with it. So long, _avName_!"},
 6291: {QUEST: 'Cogs broke into the First Security Blanket Bank! Go see William Teller and see if you can help.'},
 6292: {QUEST: 'Oh those darn Cashbot Cogs! They stole my reading lamps!\x07I need them back right away. Can you go look for them?\x07If you can get my reading lamps, I might be able to help you get into see the C.F.O.\x07Hurry!',
        INCOMPLETE_PROGRESS: 'I need those lamps back. Keep looking for them!',
        COMPLETE: "You're back! And you got my lamps!\x07I can't thank you enough but I can give you this."},
 7201: {QUEST: 'Nina Nightlight was looking for you, _avName_. She needs some help._where_'},
 7202: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I could use some help!\x07Those darn Cogs have kept the delivery folks away and I have no beds in stock.\x07Could you go see Hardy O'Toole and bring me back a bed?_where_ ",
        INCOMPLETE_PROGRESS: "Did Hardy have any beds? I was sure he'd have one.",
        COMPLETE: ''},
 7203: {GREETING: '',
        LEAVING: '',
        QUEST: 'A bed? Sure, here\'s one all ready to go.\x07Just bring it over to her for me, would you? Get it?\x07"WOOD" you? Hee-hee!\x07Pretty funny. No? Well, take it over there anyway, please?',
        INCOMPLETE_PROGRESS: 'Did Nina like the bed?',
        COMPLETE: ''},
 7204: {GREETING: '',
        LEAVING: '',
        QUEST: "This bed isn't right. It's much too plain.\x07Go see if he has anything fancier, would you?\x07I'm sure it won't take but a minute.",
        INCOMPLETE_PROGRESS: "I'm certain that Hardy has a fancier bed.",
        COMPLETE: ''},
 7205: {GREETING: '',
        LEAVING: '',
        QUEST: "Didn't hit the nail on the head with that bed, huh? I've got one here that will do the job.\x07One small problem though - it needs to be assembled first.\x07While I hammer out this problem, could you get rid of some of those Cogs that are outside?\x07Those awful Cogs throw a wrench in the works.\x07Come back when you're done and the bed will be ready.",
        INCOMPLETE_PROGRESS: "Not quite done with assembling the bed.\x07When you're done with the Cogs, it'll be ready.",
        COMPLETE: ''},
 7206: {GREETING: '',
        LEAVING: '',
        QUEST: 'Hey there _avName_!\x07You did a bang-up job on those Cogs.\x07The bed is all ready. Could you please deliver it for me?\x07Now that those Cogs are gone, business will be brisk!',
        INCOMPLETE_PROGRESS: "I think Nina's waiting for that bed delivery.",
        COMPLETE: 'What a lovely bed!\x07Now my customers will be happy. Thanks, _avName_.\x07Say, you might be able to use this. Someone left it here.'},
 7209: {QUEST: 'Go see Honey Moon. She needs some help._where_'},
 7210: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh! I'm so glad to see you, _avName_. I really need some help!\x07I haven't been able to get my beauty sleep for ages. You see, those Cogs stole my bedspread.\x07Say, could you please run over and see if Ed's got anything in blue?_where_",
        INCOMPLETE_PROGRESS: 'What did Ed have to say about a blue bedspread?',
        COMPLETE: ''},
 7211: {GREETING: '',
        LEAVING: '',
        QUEST: "So, Honey wants a bedspread, huh?\x07What color? BLUE?!\x07Well, I'd have to make that for her special. Everything I've got is red.\x07Tell ya what...if you'll go deal with some of those Cogs out there, I'll make a special blue bedspread just for her.\x07Blue bedspreads...what'll it be next?",
        INCOMPLETE_PROGRESS: 'Still working on this blue bedspread, _avName_. Keep at those Cogs!',
        COMPLETE: ''},
 7212: {GREETING: '',
        LEAVING: '',
        QUEST: "Nice to see you again. I've got something for you!\x07Here's the bedspread and it's blue. She'll love it.",
        INCOMPLETE_PROGRESS: 'Did Honey like the bedspread?',
        COMPLETE: ''},
 7213: {GREETING: '',
        LEAVING: '',
        QUEST: "My bedspread? No, that's not right.\x07It's PLAID! How can anyone sleep with such a LOUD pattern?\x07You'll just have to take it back and get a different one.\x07I'm sure he'll have others.",
        INCOMPLETE_PROGRESS: 'I simply will not accept a plaid bedspread. See what Ed can do about it.',
        COMPLETE: ''},
 7214: {GREETING: '',
        LEAVING: '',
        QUEST: "What? She doesn't like PLAID?\x07Hmm...let me see what we've got here.\x07This will take a while. Why don't you go take care of a few Cogs while I try to find something else?\x07I'll have something by the time you get back here.",
        INCOMPLETE_PROGRESS: "I'm still looking for another bedspread. How's it going with the Cogs?",
        COMPLETE: ''},
 7215: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey, good job on those Cogs!\x07Here you go, it's blue and it's not plaid.\x07Sure hope she likes paisley.\x07Bring the bedspread back to Honey.",
        INCOMPLETE_PROGRESS: "That's all I've got for you right now.\x07Please bring that bedspread to Honey.",
        COMPLETE: "Oh! That's lovely! Paisley suits me quite well.\x07Time for my beauty sleep, then! So long, _avName_.\x07What? You're still here? Can't you see I'm trying to sleep?\x07Here, take this and let me rest. I must look a fright!"},
 7218: {QUEST: 'Dreamy Daphne could use a hand._where_'},
 7219: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, _avName_, I'm glad to see you! Those Cogs took my pillows.\x07Could you go see if Tex has some pillows?_where_\x07I'm sure he can help.",
        INCOMPLETE_PROGRESS: 'Does Tex have any pillows for me? ',
        COMPLETE: ''},
 7220: {GREETING: '',
        LEAVING: '',
        QUEST: "Howdy! Daphne needs some pillows, huh? Well, you came to the right place, pardner!\x07More pillows in here than there's spines on a cactus.\x07Here you go, _avName_. Take these back over to Daphne with my compliments.\x07Always glad to help a gal out.",
        INCOMPLETE_PROGRESS: 'Were those pillows soft enough for the little lady?',
        COMPLETE: ''},
 7221: {GREETING: '',
        LEAVING: '',
        QUEST: "You got the pillows! Great!\x07Hey, wait a second! These pillows are awfully soft.\x07Much too soft for me. I need harder pillows.\x07Take these back to Tex and see what else he's got. Thanks.",
        INCOMPLETE_PROGRESS: 'Nope! Too soft. Ask Tex for different pillows.',
        COMPLETE: ''},
 7222: {GREETING: '',
        LEAVING: '',
        QUEST: "Too soft, huh? Well, let me see what I've got....\x07Hmm...seems I had me a whole passel of hard pillows. Where'd they get to?\x07Oh! I remember. I was fixing to send them back so they're in storage.\x07How 'bout you clean up some of those Cog buildings out there while I get 'em out of storage, pardner?",
        INCOMPLETE_PROGRESS: "Cog buildings are hard. But these pillows aren't.\x07I'll keep looking.",
        COMPLETE: ''},
 7223: {GREETING: '',
        LEAVING: '',
        QUEST: "Back already? Well, that's jess fine. See, I found those pillows Daphne wanted.\x07Now, you jess take these over to her. They're hard enough to break a tooth on!",
        INCOMPLETE_PROGRESS: "Yeah, those pillows are mighty hard. I hope Daphne fancies 'em.",
        COMPLETE: 'I knew Tex would have some harder pillows.\x07Oh yes, those are perfect. Nice and hard.\x07Would you have a use for this piece of a Cog suit? Might as well take it with you.'},
 7226: {QUEST: "Drop by to see Sandy Sandman. She's lost her pajamas._where_"},
 7227: {GREETING: '',
        LEAVING: '',
        QUEST: "I have no pajamas! They're missing!\x07What will I do? Oh! I know!\x07Go see Big Mama. She'll have pajamas for me._where_",
        INCOMPLETE_PROGRESS: 'Does Big Mama have pajamas for me?',
        COMPLETE: ''},
 7228: {GREETING: '',
        LEAVING: '',
        QUEST: "Hey there, little toon! Big Mama's got the best pajamas from the Bahamas.\x07Oh, something for Sandy Sandman, huh? Well, let me see what I've got.\x07Here's a little something. Now she can sleep in style!\x07Would you run these back over to her for me? I can't leave the shop just now.\x07Thanks, _avName_. See you around!",
        INCOMPLETE_PROGRESS: 'You need to take those pajamas to Sandy._where_',
        COMPLETE: ''},
 7229: {GREETING: '',
        LEAVING: '',
        QUEST: "Big Mama sent these for me? Oh...\x07Doesn't she have any pajamas with feet on them?\x07I always wear pajamas with feet. Doesn't everybody?\x07Take these back and ask her to find some with feet.",
        INCOMPLETE_PROGRESS: 'My pajamas must have feet. See what Big Mama can do.',
        COMPLETE: ''},
 7230: {GREETING: '',
        LEAVING: '',
        QUEST: "Feet? Let me think....\x07Wait! I've got just the thing!\x07Ta-dah! Pajamas with feet. Nice blue pajamas with feet. Best ones on any island.\x07Please take them back to her, would you? Thanks!",
        INCOMPLETE_PROGRESS: 'Did Sandy like the blue footie pajamas?',
        COMPLETE: ''},
 7231: {GREETING: '',
        LEAVING: '',
        QUEST: "Well, these DO have feet, but I can't wear blue pajamas!\x07Ask Big Mama if she has a different color.",
        INCOMPLETE_PROGRESS: "I'm sure Big Mama has footie pajamas in a different color.",
        COMPLETE: ''},
 7232: {GREETING: '',
        LEAVING: '',
        QUEST: "That's too bad. These are the only pajamas with feet I have.\x07Oh, I've got an idea. Go ask Cat. She may have some pajamas with feet._where_",
        INCOMPLETE_PROGRESS: "Nope, those are all the pajamas I've got. Go see what Cat has._where_",
        COMPLETE: ''},
 7233: {GREETING: '',
        LEAVING: '',
        QUEST: "Pajamas with feet? Sure thing.\x07What do you mean, these are blue? She doesn't want blue?\x07Oh, that's a little trickier. Here, try these.\x07They're not blue and they DO have feet.",
        INCOMPLETE_PROGRESS: "I just love puce, don't you?\x07I hope Sandy likes them....",
        COMPLETE: ''},
 7234: {GREETING: '',
        LEAVING: '',
        QUEST: "No, these aren't blue but no one with my complexion could possibly wear puce.\x07Absolutely not. Back they go and you with them! See what else Cat has.",
        INCOMPLETE_PROGRESS: 'Cat must have more pajamas. No puce for me!',
        COMPLETE: ''},
 7235: {GREETING: '',
        LEAVING: '',
        QUEST: "Not puce either. Hmm....\x07By my whiskers, I know I have some other ones.\x07They'll take a little while to find. Let's make a deal.\x07I'll find the other pajamas if you'll get rid of some of these Cog buildings. They're very unsettling.\x07I'll have the pajamas ready when you get back, _avName_.",
        INCOMPLETE_PROGRESS: 'You need to clear out a few more Cog buildings while I look for other pajamas.',
        COMPLETE: ''},
 7236: {GREETING: '',
        LEAVING: '',
        QUEST: 'You did a great job on those Cogs! Thanks!\x07I found those pajamas for Sandy; hope she likes them.\x07Bring them over to her. Thank you.',
        INCOMPLETE_PROGRESS: "Sandy's waiting for those pajamas, _avName_.",
        COMPLETE: "Fuchsia pajamas with feet! Purr-fect!\x07Ah, now I'm all set. Let's see....\x07Oh, I suppose I should give you something for helping me out.\x07Maybe you can use this. Someone left it here."},
 7239: {QUEST: "Go see Smudgy Mascara. She's been looking for some help._where_"},
 7240: {GREETING: '',
        LEAVING: '',
        QUEST: 'Those darn Cogs took my wrinkle cream!\x07My customers simply MUST have wrinkle cream while I work on them.\x07Go see Rip and see if he has my special formula in stock._where_',
        INCOMPLETE_PROGRESS: 'I refuse to work on anyone without wrinkle cream.\x07See what Rip has for me.'},
 7241: {GREETING: '',
        LEAVING: '',
        QUEST: "Oh, that Smudgy's a picky character. She won't settle for my usual formula.\x07That means I'll need some cauliflower coral, my super-secret special ingredient. But I haven't any in stock.\x07Could you go fish some out of the pond for me? As soon as you get the coral, I'll whip up a batch for Smudgy.",
        INCOMPLETE_PROGRESS: "I'll need that cauliflower coral to make a batch of wrinkle cream."},
 12002: {GREETING: '',
         LEAVING: '',
         QUEST: "_toNpcName_ needs more help, if you're up for it._where_"},
 12003: {GREETING: '',
         LEAVING: '',
         QUEST: 'Another disguise part?\x07Certainly...\x07but only if you defeat a Pencil Pusher.',
         INCOMPLETE_PROGRESS: 'Pencil Pushers can be found in the streets.',
         COMPLETE: "He was a real pushover!\x07Here's your second disguise part."},
 12004: {GREETING: '',
         LEAVING: '',
         QUEST: "There's really only one place to go for Bossbot parts._where_"},
 12005: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now I need a Yesman.',
         INCOMPLETE_PROGRESS: 'Yesmen can be found in the streets.',
         COMPLETE: "Yes! Man, you are good.\x07Here's your third disguise part."},
 12006: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ has more parts for you...'},
 12007: {GREETING: '',
         LEAVING: '',
         QUEST: "If you defeat a Micromanager I'll give you another part.",
         INCOMPLETE_PROGRESS: 'Try looking on %s' % GlobalStreetNames[1100][-1],
         COMPLETE: "You managed that quite well!\x07Here's your fourth disguise part."},
 12008: {GREETING: '',
         LEAVING: '',
         QUEST: 'Head on over to..._where_'},
 12009: {GREETING: '',
         LEAVING: '',
         QUEST: "I'm after a Downsizer now...",
         INCOMPLETE_PROGRESS: 'Having trouble? Try looking on %s' % GlobalStreetNames[3100][-1],
         COMPLETE: "He went down hard!\x07Here's your fifth disguise part."},
 12010: {GREETING: '',
         LEAVING: '',
         QUEST: 'I think you know where to go by now..._where_'},
 12011: {GREETING: '',
         LEAVING: '',
         QUEST: 'A Head Hunter is next on my list.',
         INCOMPLETE_PROGRESS: 'You might have better luck looking buildings.',
         COMPLETE: "I see you had no problem hunting one down.\x07Here's your sixth disguise part."},
 12012: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ needs more Bossbots.'},
 12013: {GREETING: '',
         LEAVING: '',
         QUEST: "Next I'll need you to track down a Corporate Raider.",
         INCOMPLETE_PROGRESS: 'You might have better luck looking buildings.',
         COMPLETE: "You're quite the little raider yourself!\x07Here's your seventh disguise part."},
 12014: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you want more disguise parts, go to..._where_'},
 12015: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now the coup de grace: The Big Cheese!',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "I knew I could count on you to cut...\x07Ah, never mind.\x07Here's your next disguise part."},
 12016: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ was looking for you...'},
 12017: {GREETING: '',
         LEAVING: '',
         QUEST: 'Now I need you to defeat one of the new, more treacherous Bossbot Cogs.',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'They are tougher than they look, huh?\x07I guess I owe you a disguise part.'},
 12018: {GREETING: '',
         LEAVING: '',
         QUEST: 'Could you swing by..._where_'},
 12019: {GREETING: '',
         LEAVING: '',
         QUEST: 'These Version 2.0 Cogs are very interesting.\x07Please go defeat another one.',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Thanks!\x07Another disguise part coming right up.'},
 12020: {GREETING: '',
         LEAVING: '',
         QUEST: 'If you get a chance, stop by and see _toNpcName_.'},
 12021: {GREETING: '',
         LEAVING: '',
         QUEST: 'I wonder if they can keep regenerating...',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "I guess not.\x07Here's your part..."},
 12022: {GREETING: '',
         LEAVING: '',
         QUEST: 'You know..._where_'},
 12023: {GREETING: '',
         LEAVING: '',
         QUEST: "Maybe they aren't Bossbots at all...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Hmmm, I guess they are Bossbots after all.\x07Help yourself to another part.'},
 12024: {GREETING: '',
         LEAVING: '',
         QUEST: "You probably know what I'm going to say already..."},
 12025: {GREETING: '',
         LEAVING: '',
         QUEST: 'Perhaps they are related to the Skelecogs somehow...',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "That was inconclusive...\x07Here's your disguise part."},
 12026: {GREETING: '',
         LEAVING: '',
         QUEST: 'Please go see _toNpcName_ again.'},
 12027: {GREETING: '',
         LEAVING: '',
         QUEST: "I'm still not convinced they aren't some type of Skelecog...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Well, maybe not.\x07Here's your next part."},
 12028: {GREETING: '',
         LEAVING: '',
         QUEST: "It's probably the last place you want to go, but..."},
 12029: {GREETING: '',
         LEAVING: '',
         QUEST: 'I am still quite baffled by these new cogs.\x07Could you go defeat another, please?',
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: 'Fascinating. Simply fascinating.\x07A disguise part for your troubles.'},
 12030: {GREETING: '',
         LEAVING: '',
         QUEST: '_toNpcName_ is starting to sound like a broken record...'},
 12031: {GREETING: '',
         LEAVING: '',
         QUEST: "I've almost determined what these new Cogs are.\x07Just one more...",
         INCOMPLETE_PROGRESS: 'Try looking in %s' % GlobalStreetNames[10000][-1],
         COMPLETE: "Yes, I think I'm onto something.\x07Oh, yes.\x07This is for you..."}}
ChatGarblerDog = ['woof', 'arf', 'rruff', 'bark']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerRabbit = ['eek', 'eepr', 'eepy', 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDeer = ['vveh', 'behh', 'mah']
ChatGarblerCrocodile = ['rarr', 'rraw', 'chomp']
ChatGarblerDefault = ['blah']
BossbotS = 'a Bossbot'
LawbotS = 'a Lawbot'
CashbotS = 'a Cashbot'
SellbotS = 'a Sellbot'
DarkbotS = 'a Darkbot'
BossbotSkelS = 'a Bossbot Skelecog'
LawbotSkelS = 'a Lawbot Skelecog'
CashbotSkelS = 'a Cashbot Skelecog'
SellbotSkelS = 'a Sellbot Skelecog'
DarkbotSkelS = 'a Darkbot Skelecog'
BossbotSkelP = 'Bossbot Skelecogs'
LawbotSkelP = 'Lawbot Skelecogs'
CashbotSkelP = 'Cashbot Skelecogs'
SellbotSkelP = 'Sellbot Skelecogs'
DarkbotSkelP = 'Darkbot Skelecogs'
SkeleRevivePostFix = '\nVersion 2.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelPlayer = 'Player: %(player)s\nWorld: %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nWorld: %(world)s\nLocation: %(location)s'
AvatarDetailPanelRealLife = 'Offline'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s'
AvatarDetailPanelOnlinePlayer = 'District: %(district)s\nLocation: %(location)s\nPlayer: %(player)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline'
AvatarShowPlayer = 'Show Player'
OfflineLocation = 'Offline'
PlayerToonName = 'Toon: %(toonname)s'
PlayerShowToon = 'Show Toon'
PlayerPanelDetail = 'Player Details'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelSecrets = 'True Friends'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Stop Ignoring'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupRetract = 'Retract Invitation'
AvatarPanelGroupMember = 'Already In Group'
AvatarPanelGroupMemberKick = 'Remove'
ReportPanelTitle = 'Report A Player'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelBodyPlayer = 'This feature is still being worked on and will be coming soon. In the meantime you can do the following:\n\n  - Go to DXD and break the friendship there.\n - Tell a parent about what happened.'
ReportPanelCategoryLanguage = 'Foul Language'
ReportPanelCategoryPii = 'Sharing/Requesting Personal Info'
ReportPanelCategoryRude = 'Rude or Mean Behavior'
ReportPanelCategoryName = 'Bad Name'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s is being unsafe by giving out or requesting a phone number, address, last name, email address, password or account name.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow this server's rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "We take reporting very seriously. Your report will be viewed by a Moderator who will take appropriate action for anyone breaking our rules. If your account is found to have participated in breaking the rules, or if you make false reports or abuse the 'Report a Player' system, a Moderator may take action against your account. Are you absolutely sure you want to report this player?"
ReportPanelThanks = 'Thank you! Your report has been sent to a Moderator for review. There is no need to contact us again about the issue. The moderation team will take appropriate action for a player found breaking our rules.'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelRemovedPlayerFriend = 'We have automatically removed %s as a Player friend so as such you will not see them as your friend in any linked products.'
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Ignore A Player'
IgnorePanelAddIgnore = 'Would you like to ignore %s for the rest of this session?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
IgnorePanelAddFriendPlayer = '%s (%s)is your friend, you cannot ignore them while you are friends.'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Play dead',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of JellyBeans! How'bout giving me a slice of pie?", "How'bout a Red JellyBean? I'm tired of the Green ones!", "Oh, those JellyBeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!", "You didn't think I understood you, huh?", 'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'Mmm, jellybeans, mmm!',
                'Does it GET any better than this?',
                "Happy April Toons' Week!"],
 'sadness': ["Don't go, don't go, don't go, don't go, don't go, don't go, don't go, don't go, don't go, don't go, don't go...", "I'll be good, I promise!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, let's play, let's play, let's play, let's play, let's play, let's play, let's play, let's play...", 'Play with me or I dig up some flowers!', 'Lets run around and around and around and around and around and around...'],
 'loneliness': ['Where have you been?', 'Wanna cuddle?', 'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!', 'Being a Doodle is exhausting!', 'I gotta get to Dreamland!'],
 'confusion': ['Where am I?  Who are you again?', "What's a Toon-up again?", "Whoa, I'm standing between you and the Cogs!  Run away!"],
 'anger': ['... and you wonder why I never give you a Toon-up?!!!', 'You always leave me behind!', 'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!', 'Toons can talk?!!', 'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!", 'Do you even KNOW how great you are?!?', 'I am SO lucky to be with you!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelUnavailableHood = '%s is not available right now; try again later.'
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District. Playing in a full District can severely slow down game performance. Are you sure you want to switch districts?'
BattleBldgBossTaunt = "I'm the boss."
CogdoBattleBldgBossTaunt = "I don't take meetings with Toons."
FactoryBossTaunt = "I'm the Foreman."
FactoryBossBattleTaunt = 'Let me introduce you to the Foreman.'
MintBossTaunt = "I'm the Supervisor."
MintBossBattleTaunt = 'You need to talk to the Supervisor.'
StageBossTaunt = "I'm the Overseer."
StageBossBattleTaunt = 'You should speak to the Overseer.'
StageBossName = 'Office Overseer'
StageBossNameS = 'an Office Overseer'
StageBossNameP = 'Office Overseers'
CountryClubBossName = 'Club President'
CountryClubBossNameS = 'a Club President'
CountryClubBossNameP = 'Club Presidents'
CountryClubBossTaunt = "I'm the Club President."
CountryClubBossBattleTaunt = 'You need to talk to the Club President.'
ForcedLeaveCountryClubAckMsg = 'The Club President was defeated before you could reach him. You did not recover any Stock Options.'
MovieHealLaughterMisses = ('Hmm...', 'Heh...', 'Ha...', 'Harr harr...')
MovieHealLaughterHits1 = ('Ha ha ha!', 'Hee hee!', 'Tee hee!', 'Ha ha!')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!', 'HEE HEE HEE!')
MovieSOSCallHelp = '%s, HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = '%s, HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSToonsHit = 'Toons always hit!'
MovieNPCSOSCogsMiss = 'Cogs always miss!'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Toon-\x04Up'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = ('Sigh...', 'Come on, %s!', "You're such a good Doodle, too.")
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nAPPROVED\nPRIORITY'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items recovered'
RewardPanelMissedItems = 'Items not recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['Yeah!',
 'Congratulations!',
 'Wow!',
 'Cool!',
 'Awesome!',
 'Toontastic!',
 'Amazing!',
 'Yay!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Stock Options',
 'Jury Notices',
 'Cogbucks',
 'Merits',
 'Warrants']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
CheesyEffectDescriptions = [('Normal Toon', 'you will be normal'),
 ('Big head', 'you will have a big head'),
 ('Small head', 'you will have a small head'),
 ('Big legs', 'you will have big legs'),
 ('Small legs', 'you will have small legs'),
 ('Big toon', 'you will be a little bigger'),
 ('Small toon', 'you will be a little smaller'),
 ('Flat portrait', 'you will be two-\x04dimensional'),
 ('Flat profile', 'you will be two-\x04dimensional'),
 ('Transparent', 'you will be transparent'),
 ('No color', 'you will be colorless'),
 ('Invisible toon', 'you will be invisible')]
CheesyEffectIndefinite = 'Until you choose another effect, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
SuitAttackNames = {'AcidRain': 'Acid Rain!',
 'Audit': 'Audit!',
 'Bite': 'Bite!',
 'Blackball': 'Blackball!',
 'Blacklist': 'Blacklist!',
 'BloodMoney': 'Blood Money!',
 'BounceCheck': 'Bounced Check!',
 'BrainFreeze': 'Brain Freeze!',
 'BrainStorm': 'Brain Storm!',
 'BuzzWord': 'Buzz Word!',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'CashRain': 'Cash Rain!',
 'CeaseandDesist': 'Cease and Desist!',
 'Charter': 'Charter!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Cigar Smoke!',
 'ClipOnTie': 'Clip-\x04On Tie!',
 'ColdHardCash': 'Cold, Hard Cash!',
 'Contract': 'Contract!',
 'Counterclaim': 'Counterclaim!',
 'Crunch': 'Crunch!',
 'Demoralize': 'Demoralize!',
 'Demotion': 'Demotion!',
 'Depression': 'Depression!',
 'DoubleTalk': 'Double Talk!',
 'DoubleWindsor': 'Double Windsor!',
 'Downsize': 'Downsize!',
 'DownPayment': 'Down Payment!',
 'EvictionNotice': 'Eviction Notice!',
 'Evidence': 'Evidence!',
 'EvilEye': 'Evil Eye!',
 'EvilEyeWSI': 'Evil Eye!',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Fill With Graphite!',
 'FiveOClockShadow': "Five O'Clock Shadow!",
 'FingerWag': 'Finger Wag!',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Flood the Market!',
 'FountainPen': 'Fountain Pen!',
 'FreezeAssets': 'Freeze Assets!',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Glower Power!',
 'GuiltTrip': 'Guilt Trip!',
 'GuiltTripWSI': 'Guilt Trip!',
 'HalfWindsor': 'Half Windsor!',
 'HangUp': 'Hang Up!',
 'HeadShrink': 'Head Shrink!',
 'HeatWave': 'Heat Wave!',
 'HotAir': 'Hot Air!',
 'Jargon': 'Jargon!',
 'Jump': 'Jump!',
 'JuryNotice': 'Subponea!',
 'Legalese': 'Legalese!',
 'LegalTender': 'Legal Tender!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Market Crash!',
 'MarketingSpin': 'Marketing Spin!',
 'MindBlow': 'Mind Blow!',
 'MudSling': 'Mud Sling!',
 'Mulligan': 'Mulligan!',
 'MumboJumbo': 'Mumbo Jumbo!',
 'ParadigmShift': 'Paradigm Shift!',
 'PayDay': 'Pay Day!',
 'PeckingOrder': 'Pecking Order!',
 'PeckingOrderWSI': 'Pecking Order!',
 'PennyPinch': 'Penny Pinch!',
 'PickPocket': 'Pick Pocket!',
 'PinkSlip': 'Pink Slip!',
 'PlayHardball': 'Play Hardball!',
 'PositiveReinforcement': 'Positive Reinforcement!',
 'PoundKey': 'Pound Key!',
 'PowerTie': 'Power Tie!',
 'PowerTrip': 'Power Trip!',
 'PowerTripWSI': 'Power Trip!',
 'Quake': 'Quake!',
 'RainOfFire': 'Rain of Fire!',
 'RazzleDazzle': 'Razzle Dazzle!',
 'RedTape': 'Red Tape!',
 'ReOrg': 'Reorganize!',
 'RestrainingOrder': 'Restraining Order!',
 'RestrainingOrderWSI': 'Restraining Order!',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Rubber Stamp!',
 'RubOut': 'Rub Out!',
 'RuthlessEfficiency': 'Ruthless Efficiency!',
 'Sacked': 'Sacked!',
 'SandTrap': 'Sand Trap!',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SnowWave': 'Snow Wave!',
 'SongAndDance': 'Song and Dance!',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'Taunt': 'Taunt!',
 'TeeOff': 'Tee Off!',
 'ThrowBook': 'Throw Book!',
 'ThrowGear': 'Throw Gear!',
 'Tremor': 'Tremor!',
 'TrialByFire': 'Trial By Fire!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Write Off!'}
BuildingWaitingForVictors = ('Waiting for other Toons...',)
ElevatorHopOff = 'Hop off'
ElevatorStayOff = "If you hop off, you'll need to wait\nfor the elevator to leave or empty."
ElevatorLeaderOff = 'Only your leader can decide when to hop off.'
ElevatorHoppedOff = 'You need to wait for the next elevator.'
ElevatorMinLaff = 'You need %s laff points to ride this elevator.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Only your group leader can\n decide when to board.'
KartMinLaff = 'You need %s laff points to ride this kart'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s, Inc.'
CogsInc = 'Cogs, Inc.'
CogsIncRetro = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Field Office'
Cogdominiums = Cog + ' Field Office'
CogdominiumsRetro = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Cold Caller!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Cold Caller to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise by doing ToonTasks in Donald's Dreamland."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Lawbot Disguise first!\n\nBuild your Lawbot Disguise by doing the ToonTasks after Donald's Dreamland."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Bossbot Disguise first!\n\nBuild your Bossbot Disguise by doing the ToonTasks after Donald's Dreamland."
KnockKnockContestJokes = {2100: ['Wally', "Wally's not looking, hit him with a pie!"],
 2200: {28: ['Biscuit', 'Biscuit out of here the Cogs are coming!'],
        41: ['Dewey', 'Dewey want to go defeat some more Cogs?'],
        40: ['Minnie', "Minnie people have asked that, and it's driving me crazy!"],
        27: ['Disguise', 'Disguise where the Cogs fly!']},
 2300: ['Justin', 'Justin other couple of Cog parts and off we go!'],
 3300: {10: ['Aladdin', 'Aladdin HQ wants a word with you.'],
        6: ['Weirdo', 'Weirdo all these Cogs come from?'],
        30: ['Bacon', 'Bacon a cake to throw at the Cogs.'],
        28: ['Isaiah', 'Isaiah we go ride the trolley.'],
        12: ['Juliet', "Juliet me in that Cog building with you and I'll give you a Toon-Up."]}}
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know?'],
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', Donald + ' Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-\x04quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know.  Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub.  I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who!  Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, Izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache.  Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.'],
 ['Alaska', 'Alaska-\x04gain, open the door!'],
 ['Ice cream', 'Ice creamed when banana split.']]
CCharChatterMelodyLand = "Melodyland"
SharedChatterGreetings = ['Hi, %!',
 'Yoo-hoo %, nice to see you.',
 "I'm glad you're here today!",
 'Well, hello there, %.']
SharedChatterComments = ["That's a great name, %.",
 'I like your name.',
 'Watch out for the Cogs.',
 'Looks like the trolley is coming!',
 'I need to play a trolley game to get some pies!',
 'Sometimes I play trolley games just to eat the fruit pie!',
 'Whew, I just stopped a bunch of Cogs. I need a rest!',
 'Yikes, some of those Cogs are big guys!',
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 "I like what you're wearing.",
 "I think I'll go fishing this afternoon.",
 'Have fun in my neighborhood.',
 'I hope you are enjoying your stay in Toontown!',
 "I heard it's snowing at the Brrrgh.",
 'Have you ridden the trolley today?',
 'I like to meet new people.',
 'Wow, there are lots of Cogs in the Brrrgh.',
 'I love to play tag. Do you?',
 'Trolley games are fun to play.',
 'I like to make people laugh.',
 "It's fun helping my friends.",
 "A-hem, are you lost?  Don't forget your map is in your shticker Book.",
 "Try not to get caught up in the Cogs' Paradigm Shift.",
 'I hear Daisy has planted some new flowers in her garden.',
 'If you press the Page Up key, you can look up!',
 'If you help take over Cog buildings, you can earn a bronze star!',
 'If you press the Tab key, you can see different views of your surroundings!',
 'If you press the Ctrl key, you can jump!']
SharedChatterGoodbyes = ['I have to go now, bye!',
 "I think I'll go play a trolley game.",
 "Well, so long. I'll be seeing you, %!",
 "I'd better hurry and get to work stopping those Cogs.",
 "It's time for me to get going.",
 'Sorry, but I have to go.',
 'Good-\x04bye.',
 'See you later, %!',
 "I think I'm going to go practice tossing cupcakes.",
 "I'm going to join a group and stop some " + Cogs + '.',
 'It was nice to see you today, %.',
 "I have a lot to do today. I'd better get busy."]
MickeyChatter = (['Welcome to ' + lToontownCentral + '.', 'Hi, my name is ' + Mickey + ". What's yours?"], ['Hey, have you seen ' + Donald + '?',
  "I'm going to go watch the fog roll in at Donald's Dock.",
  'If you see my pal ' + Goofy + ', say hi to him for me.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.'], ["I'm going to " + CCharChatterMelodyLand + " to see " + Minnie + '!',
  "Gosh, I'm late for my date with " + Minnie + '!',
  "Looks like it's time for " + Pluto + "'s dinner.",
  "I think I'll go swimming at Donald's Dock.",
  "It's time for a nap. I'm going to Dreamland."])
WinterMickeyCChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown... I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Golly, these halls sure are decked!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Just look at those tree lights! What a sight!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Not a creature is stirring, except this mouse!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'I love this time of year!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I'm feeling jolly, how about you?",
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Know any good carols?',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Oh boy! I love Winter Holiday!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
ValentinesMickeyChatter = (["Hi, I'm Mickey!",
  'Welcome to ValenToontown Central!',
  "Happy ValenToon's Day!",
  "Happy ValenToon's Day, %"], ['Love is in the air! And butterflies!',
  'Those hearts are good for Laff boosts!',
  'I hope Minnie likes what I got her!',
  "The Cattlelog has lots of ValenToon's Day gifts!",
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'm taking Minnie out to the Kooky Cafe!",
  'Will Minnie want chocolates or flowers?'], ['I loved having you visit!', "Tell Minnie I'll pick her up soon!"])
WinterMickeyDChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown... I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Golly, these halls sure are decked!',
  'Just look at those tree lights! What a sight!',
  'Not a creature is stirring, except this mouse!',
  'I love this time of year!',
  "I'm feeling jolly, how about you?",
  'Know any good carols?',
  'Oh boy! I love Winter Holiday!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
VampireMickeyChatter = (['Welcome to ' + lToontownCentral + '.',
  'Hi, my name is ' + Mickey + ". What's yours?",
  'Happy Halloween!',
  'Happy Halloween, %!',
  'Welcome to Tombtown... I mean Toontown!'], ['If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "It's fun to dress up for Halloween!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Do you like my costume?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  '%, watch out for Bloodsucker Cogs!',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "Aren't the Halloween decorations great?",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Beware of black cats!',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Did you see the Toon with the pumpkin head?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Boo!  Did I scare you?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "Don't forget to brush your fangs!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "I'm a vampire, but not a Bloodsucker!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "I hope you're enjoying our Halloween fun!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Vampires are really popular this year!'], ["I'm going to check out the cool Halloween decorations.",
  "I'm going to " + CCharChatterMelodyLand + " to surprise " + Minnie + '!',
  "I'm going to sneak up on another Toon!  Shhh!",
  "I'm going trick-or-treating!",
  'Shhh, sneak with me.'])
FieldOfficeMickeyChatter = ['Have you heard about the new Mover & Shaker Field Offices?']
MinnieChatter = (['Welcome to Melodyland.', 'Hi, my name is ' + Minnie + ". What's yours?"], ['The hills are alive with the sound of music!',
  'You have a cool outfit, %.',
  'Hey, have you seen ' + Mickey + '?',
  'If you see my friend ' + Goofy + ', say hi to him for me.',
  'Wow, there are lots of ' + Cogs + ' near ' + Donald + "'s Dreamland.",
  "I heard it's foggy at the Donald's Dock.",
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "I think I'll go catch some tunes.",
  'Hey %, look at that over there.',
  'I love the sound of music.',
  "I bet you didn't know Melodyland is also called TuneTown!  Hee Hee!",
  'I love to play the Matching Game. Do you?',
  'I like to make people giggle.',
  'Boy, trotting around in heels all day is hard on your feet!',
  'Nice shirt, %.',
  'Is that a jellybean on the ground?'], ["Gosh, I'm late for my date with %s!" % Mickey, "Looks like it's time for %s's dinner." % Pluto, "It's time for a nap. I'm going to Dreamland."])
WinterMinnieCChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ["You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Belt out a tune, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Show us how to croon, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Can you carry a melody here in Melodyland?',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Those lamps look warm in their scarves!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "The sing's the thing!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "I'll always like you, for better or verse!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
WinterMinnieDChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Belt out a tune, Toon!',
  'Show us how to croon, Toon!',
  'Can you carry a melody here in Melodyland?',
  'Those lamps look warm in their scarves!',
  "The sing's the thing!",
  "You can't go wrong with a song!",
  "I'll always like you, for better or verse!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
ValentinesMinnieChatter = (["Hello, I'm Minnie!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ['I hope Mickey got me chocolates or flowers!',
  'Those hearts are good for Laff boosts!',
  'I want to go to a ValenToon Party!',
  'I hope Mickey takes me to the Kooky Cafe!',
  'Mickey is such a good ValenToon!',
  'What did you get your ValenToon?',
  "Mickey has never missed a ValenToon's Day!"], ['It was sweet having you visit!'])
WitchMinnieChatter = (['Welcome to Magicland... I mean Melodyland!',
  "Hi, my name is Magic Minnie! What's yours?",
  "Hello, I think you're enchanting!",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  "It's a magical day, don't you think?",
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Now where did I put my spell book',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Abra-Cadabra!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Toontown looks positively spooky today!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Are you seeing stars too?',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Purple is really my color!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope your Halloween is bewitching!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Beware of musical spiders!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope you are enjoying our Halloween fun!'], ["I'm going to disappear now!", 'Time for me to vanish!', 'Mickey is taking me Trick-or-Treating!'])
FieldOfficeMinnieChatter = ['Everyone is talking about the new Mover & Shaker Field Offices!']
DaisyChatter = (['Welcome to my garden!', "Hello, I'm " + Daisy + ". What's your name?", "It's so nice to see you %!"], ['My prize winning flower is at the center of the garden maze.',
  'I just love strolling through the maze.',
  "I haven't seen " + Goofy + ' all day.',
  'I wonder where ' + Goofy + ' is.',
  'Have you seen ' + Donald + "? I can't find him anywhere.",
  'If you see my friend ' + Minnie + ', please say "Hello" to her for me.',
  'The better gardening tools you have the better plants you can grow.',
  'There are far too many ' + Cogs + " near Donald's Dock.",
  'Watering your garden every day keeps your plants happy.',
  'To grow a Pink Daisy plant a yellow and red jellybean together.',
  'Yellow daisies are easy to grow, just plant a yellow jellybean.',
  'If you see sand under a plant it needs water or it will wilt!'], ["I'm going to Melody Land to see %s!" % Minnie,
  "I'm late for my picnic with %s!" % Donald,
  "I think I'll go swimming at Donald's Dock.",
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesDaisyChatter = (["Hi, I'm Daisy!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ["I hope Donald doesn't get me another Amore Eel!",
  'Donald is taking me out to the Deep Sea Diner!',
  'I certainly have enough roses!',
  'Those hearts are good for Laff boosts!',
  "I'd love to go to a ValenToon's Day party!",
  'This is the garden where love grows!',
  "Donald better not sleep through ValenToon's Day again!",
  'Maybe Donald and I can double-date with Mickey and Minnie!'], ["Tell Donald I'll be waiting for him!", "Have a nice ValenToon's Day!"])
WinterDaisyCChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My garden needs more mistletoe!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I need to plant holly for next year!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'Those lights on the lamps are lovely!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That is some jolly holly!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My snowman keeps melting!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That duck is decked out!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
WinterDaisyDChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['My garden needs more mistletoe!',
  'I need to plant holly for next year!',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Those lights on the lamps are lovely!',
  'That is some jolly holly!',
  'My snowman keeps melting!',
  'That duck is decked out!',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
HalloweenDaisyChatter = (['Welcome to Daisy Ghosts... I mean Gardens!', 'Happy Halloween!', 'Happy Halloween, %!'], ['Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Wanna dance?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "I'm a duck with a poodle skirt!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'The pirate tree needs water.',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Trick-or-Tree!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Do you notice anything strange about the trees?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I should grow some pumpkins!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'WHO notices something different about the lamps?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Halloween really grows on me!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Twig-or-Treat!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "Owl bet you didn't notice the spooky lamps!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I hope you are enjoying our Halloween fun!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Be cautious about any Skelecogs roaming about!'], ['Donald is taking me Trick-or-Treating!', "I'm going to check out the fun Halloween decorations."])
FieldOfficeDaisyChatter = ['Those Mover & Shaker Field Offices are popping up like weeds!']
ChipChatter = (['Welcome to %s!' % lOutdoorZone,
  "Hello, I'm " + Chip + ". What's your name?",
  "No, I'm " + Chip + '.',
  "It's so nice to see you %!",
  'We are Chip and Dale!'], ['I like golf.', 'We have the best acorns in Toontown.', 'The golf holes with volcanoes are the most challenging for me.', 'If you see Professor Control, tell him we said hi.'], ["We're going to the " + lTheBrrrgh + ' and play with %s.' % Pluto,
  "We'll visit %s and fix him." % Donald,
  "I think I'll go swimming at Donald's Dock.",
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesChipChatter = (["I'm Chip!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["What did you get me for ValenToon's Day, Dale?",
  'Those hearts are good for Laff boosts!',
  'Will you be my ValenToon, Dale?',
  "What did you get the Cogs for ValenToon's Day?",
  "I love ValenToon's Day!"], ['Come back any time!'])
WinterChipChatter = (['Happy Winter Holiday!', 'Dressed as chipmunks!', 'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Dale!',
  'All this water could freeze any minute!',
  'We should switch the golf balls with snowballs!',
  'If only chipmunks knew how to sing!',
  'Did you remember to store nuts for the winter?',
  'Did you get the Cogs a present?'], ['Go nuts this Winter Holiday!', 'Have a joyful winter Holiday!'])
HalloweenChipChatter = (['Play some MiniGhoul... I mean Golf!', 'Happy Halloween!', 'Happy Halloween, %!'], ["We're nuts about Halloween!",
  "You're under arrest.",
  "You can't outrun the long arm of the law.",
  "I'm a Bobby!",
  'I hope you are enjoying our Halloween fun!',
  'Play golf and get a Howl-In-One.',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
DaleChatter = (["It's so nice to see you %!",
  "Hello, I'm " + Dale + ". What's your name?",
  "Hi I'm " + Chip + '.',
  'Welcome to %s!' % lOutdoorZone,
  'We are Chip and Dale!'], ['I like picnics.', 'Acorns are tasty, try some.', 'Those windmills can be hard too.', "The Professor's a great guy!"], ['Hihihi ' + Pluto + ' is fun to play with.',
  "Yeah, let's fix %s." % Donald,
  'A swim sounds refreshing.',
  "I'm getting tired and could use a nap."])
ValentinesDaleChatter = (["I'm Dale!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ['Same thing as last year. Nothing!',
  'I miss the nuts!',
  'Will you be my ValenToon, Chip?',
  'A pie in the face',
  "Yeah, it's all right."], ['Come back any time!'])
WinterDaleChatter = (['Merry chipmunks!',
  "Hi, we're two merry elves!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Chip!',
  'Better not be on the geyser when it happens!',
  'And the golf clubs with icicles!',
  'Whoever heard of singing chipmunks?',
  'I told YOU to do that!',
  'Yes, a cream pie!'], ['And bring some back for us!', 'Have a joyful Winter Holiday!'])
HalloweenDaleChatter = (['Happy Halloween, %!', 'Play some MiniGhoul... I mean Golf!', 'Happy Halloween!'], ["We're nuts about Halloween!",
  'Great, I could use a rest!',
  'But your arms are short!',
  'I thought you were a Chip!',
  'Play golf and get a Howl-In-One',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
GoofyChatter = (['Welcome to ' + lDaisyGardens + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy it sure is easy to get lost in the garden maze!',
  'Be sure and try the maze here.',
  "I haven't seen " + Daisy + ' all day.',
  'I wonder where ' + Daisy + ' is.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + " near Donald's Dock.",
  'It looks like ' + Daisy + ' has planted some new flowers in her garden.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at Donald's Dock.",
  "It's time for a nap. I'm going to Dreamland."])
WinterGoofyChatter = (["I'm Goofy about the holidays!",
  'Welcome to Snowball Speedway!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Who needs reindeer when you have a fast kart?',
  'Gawrsh! Is it Winter Holiday already?',
  'I need my earmuffs!',
  "I haven't done any shopping yet!",
  "Don't drive your kart on ice!",
  'Seems like it was Winter Holiday only a year ago!',
  'Treat your kart to a present and spruce it up!',
  'These karts are better than any old sleigh!',
  "It's certainly cold on Blizzard Boulevard!"], ['Have a cheery Winter Holiday!', 'Drive safe, now!', 'Watch out for flying reindeer!'])
ValentinesGoofyChatter = (["I'm Goofy about ValenToon's Day!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Gawrsh! Is it ValenToon's Day already?",
  'I LOVE kart racing!',
  'Be sweet to each other out there!',
  'Show your sweetie a new kart!',
  'Toons love their karts!',
  'Make some new friends on the track!'], ['Drive safe, now!', 'Show some love out there!'])
GoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + " near Donald's Dock.",
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at Donald's Dock.",
  "It's time for a nap. I'm going to Dreamland."])
SuperGoofyChatter = (['Welcome to my Super Speedway!',
  "Hi, I'm Super Goof! What's your name?",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I am feeling kind of batty today!',
  'Anybody see my cape around? Oh, there it is!',
  "Gawrsh! I don't know my own strength!",
  'Did somebody call for a superhero?',
  "Beware Cogs, I'll save Halloween!",
  "There's nothing scarier than me in a kart!",
  "I bet you don't know who I am with this mask on!",
  "It's fun to dress up for Halloween!",
  'I hope you are enjoying our Halloween fun!'], ['Gotta fly!',
  'Hi-Ho and away I go!',
  "Should I fly or drive to Donald's Dock?",
  'Gawrsh, have a Happy Halloween!'])
DonaldChatter = (['Welcome to Dreamland.', "Hi, my name is %s. What's yours?" % Donald], ['Sometimes this place gives me the creeps.',
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "Oh boy, I'm having a good day.",
  'Hey, have you seen ' + Mickey + '?',
  'If you see my buddy ' + Goofy + ', say hi to him for me.',
  "I think I'll go fishing this afternoon.",
  'Wow, there are lots of ' + Cogs + ' at my dock.',
  "Hey, didn't I take you on a boat ride at my dock?",
  "I haven't seen " + Daisy + ' all day.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.',
  'Quack.'], ["I'm going to Melody Land to see %s!" % Minnie,
  "Gosh, I'm late for my date with %s!" % Daisy,
  "I think I'll go swimming at my dock.",
  "I think I'll take my boat for a spin at my dock."])
WinterDreamlandCChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I wish I was nestled all snug in my bed!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I'm dreaming of a white Toontown!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I meant to leave out milk and cookies!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'When I wake up, I better see lots of presents!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I hope I don't sleep through the holidays!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I love a long winter's nap!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
WinterDreamlandDChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I wish I was nestled all snug in my bed!',
  "I'm dreaming of a white Toontown!",
  'I meant to leave out milk and cookies!',
  'When I wake up, I better see lots of presents!',
  "I hope I don't sleep through the holidays!",
  "I love a long winter's nap!",
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
HalloweenDreamlandChatter = (['Happy Halloween!', 'Happy Halloween, %!', "Hi, I'm FrankenDonald!"], ['If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'Am I awake or dreaming?',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I'm so scared, I can't fall asleep!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'So this is what Dreamland looks like!',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "Boy, I'm sleepy!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I hope I don't sleep through Halloween this year!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Sleep with the lights on tonight!', 'When I wake up, I am going Trick-or-Treating!', "Don't let the boogeyman get you when you sleep tonight!"])
ValentinesDreamlandChatter = (["Hello, I'm (yawn) Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["I hope I don't sleep through ValenToon's Day!",
  "I'm dreaming of Daisy!",
  "I had a nightmare that I missed ValenToon's Day!",
  'Those hearts are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I couldn't dream of a nicer holiday than ValenToon's Day!",
  'I love sleeping!'], ['Night-night!', "Wake me when it's ValenToon's Day!"])
FieldOfficeDreamlandChatter = ['I dreamed about something called a Field Office...']
HalloweenDonaldChatter = (['Welcome to my Halloween harbor!',
  'Come aboard, if you have treats!',
  'Happy Halloween!',
  'Happy Halloween, %!'], ['If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'm dressed as a sailor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'Pumpkins make great lanterns!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I've never seen palm trees with hairy legs before!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "Maybe I'll be a pirate next Halloween!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I think the best treats are starfish!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'll take you Trick-or-Treating around the harbor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope those spiders stay in the trees!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'What do you call a ghost in the water? A BOO-y!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Set sail for scares!', 'Happy haunting!', "I'm going to check out the spooky Halloween decorations."])
ValentinesDonaldChatter = (["Ahoy, I'm Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Was I supposed to take Daisy somewhere for ValenToon's Day?",
  "Just once more around the dock, then I'll get Daisy something.",
  "What would Daisy like for ValenToon's Day?",
  'Those hearts in the water are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'll have to catch an Amore Eel for Daisy!"], ['Aloha!', 'Give the Cogs my best!'])
WinterDonaldCChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How do you like my duck-orations?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'What is snow doing on the lamp posts?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This water better not ice over!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How did they get the lights up in those trees?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This boat is better than a sleigh! or is it?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I don't need reindeer to pull this boat!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I'm glad I'm not a turkey this time of year!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'My present to you? Free boat rides!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!'], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WinterDonaldDChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['How do you like my duck-orations?',
  'What is snow doing on the lamp posts?',
  'This water better not ice over!',
  'How did they get the lights up in those trees?',
  'This boat is better than a sleigh!--or is it?',
  "I don't need reindeer to pull this boat!",
  "I'm glad I'm not a turkey this time of year!",
  'My present to you? Free boat rides!'], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WesternPlutoChatter = (["Boo! Don't be scared, it's just me ... Pluto!", 'Happy Halloween, pardner!', 'Happy Halloween, %!'], ["Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I do tricks for treats!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Mickey's taking me Trick-or-Treating later!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'It feels more like Winter Holiday than Halloween!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Bark! That's 'Trick-or-Treat' in dog!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I hope you are enjoying our Halloween fun!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I like to chase Black Cat Toons!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "There's a snake in my boot!"], ["I'm going to go dig up a treat!", "I'm going to see if Mickey has some treats!", "I'm going to scare Donald!"])
WinterPlutoCChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brrgh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ["Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I chewed on an icicle and got frost-bite!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'This is like living in a snow globe!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I wish I was beside a warm fire!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'Arf! Arf! I need a scarf!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
WinterPlutoDChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brregh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['I chewed on an icicle and got frost-bite!',
  'This is like living in a snow globe!',
  'I wish I was beside a warm fire!',
  'Arf! Arf! I need a scarf!',
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
AFMickeyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Gardens! I'm " + Daisy + '!',
  "I'm " + Daisy + ', and I love to garden!',
  "April Toons' Week is the silliest week of the year!",
  "What, you've never seen a duck with mouse ears?",
  "Hi, I'm " + Daisy + '! Quack!',
  "It's tough quacking like a duck!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Tell Mickey I said hi!'])
AFMinnieChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lTheBrrrgh + "! I'm " + Pluto + '!',
  "Hi, I'm " + Pluto + "! What's your name?",
  "What, you've never seen a dog with mouse ears?",
  "I'm not feeling like myself today!",
  "Does anyone have a doggie biscuit? I'm hungry!",
  'Bark! My name is ' + Pluto + '!',
  "Isn't this silly?",
  "Don't make me chase you around!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I have to go chase cars now!  Bye!'])
AFDaisyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lToontownCentral + "! I'm " + Mickey + ' Mouse!',
  "Hi, I'm " + Mickey + '! The happiest mouse in Toontown!',
  'If you see ' + Daisy + ', tell her ' + Mickey + ' said hi!',
  "What, you've never seen a mouse with feathers?",
  "Isn't this silly?",
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['Bye! Tell them ' + Mickey + ' sent you!', 'If you go to ' + lDaisyGardens + ', say hi to her for me!'])
AFGoofySpeedwayChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Dreamland! I'm " + Donald + '!',
  "Hello, I'm " + Donald + '! Is it nap time yet?',
  'A duck needs his beauty rest, you know!',
  "What, you've never seen a duck with dog ears?",
  'Gawrsh! I mean -- Quack!',
  'This would make a great race track ... um, I mean place to nap!',
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['If you see ' + Goofy + ', tell him ' + Donald + ' says hi!', 'Bye, and good night!'])
AFDonaldChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Speedway! I'm " + Goofy + '!',
  "I'm " + Goofy + ", and I'm dreaming I'm " + Donald + '!',
  "I've heard of sleep walking, but sleep kart driving?",
  'Gawrsh!  It sure is silly being ' + Goofy + '!',
  'How can I watch the races with my eyes closed?',
  'I better grab a nap before my next race!',
  "April Toons' Week is the silliest week of the year!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I need to work on my karts!  Bye!'])
AFDonaldDockChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Everybody gets April Toons' Week off but me!",
  "I'm the only one who has to work this week!",
  'I only get time off when I sleep!',
  'All my friends are pretending to be somebody else!',
  'Round and round in this boat, all day long!',
  'I heard Daisy is pretending to be Mickey!',
  "The silliest week of the year, and I'm missing it!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Play a joke on the Cogs for me!'])
AFPlutoChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Melodyland!  I'm " + Minnie + '!',
  'Hi, my name is ' + Minnie + ' Mouse!',
  "I'm as happy as a mouse can be!",
  "What, you've never seen a mouse with dog ears?",
  'I love when ' + Mickey + ' and I go for walks!',
  'What, you never heard a mouse talk before?',
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'If you see ' + Pluto + ', tell him ' + Minnie + ' says hi!'])
AFChipChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Dale + '!',
  'How are you today, ' + Chip + '?',
  'I always thought you were ' + Dale + ', ' + Chip + '.',
  "You're sure you're " + Chip + ' and not ' + Dale + ', ' + Chip + '?',
  "April Toons' Week is the silliest week of the year!"], ['Bye from ' + Chip + ' and ' + Dale + '!'])
AFDaleChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Chip + '!',
  'Very well ' + Dale + ', thanks!',
  "Nope, I'm " + Chip + ', ' + Dale + '.',
  'Yes, ' + Dale + ", I'm " + Chip + ', not ' + Dale + '.',
  'It sure is, ' + Chip + '! I mean, ' + Dale + '.'], ['Or ' + Dale + ' and ' + Chip + '!'])
CLGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!",
  "Hi there!  Pardon my dusty clothes I've been busy fixin' that broken Leaderboard."], ['We better get this Leaderboard working soon, Grand Prix Weekend is coming up!',
  "Does anybody want to buy a slightly used kart? It's only been through the Leaderboard once!",
  'Grand Prix Weekend is coming, better get to practicing.',
  'Grand Prix Weekend will be here on Friday, May 22 through Monday, May 25!',
  "I'm gonna need a ladder to get that kart down.",
  'That Toon really wanted to get on the Leaderboard!',
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + " near Donald's Dock.",
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ['I better go get my kart a new paint job for the upcoming Grand Prix Weekend.',
  "Gosh, I better get workin' on this broken Leaderboard!",
  "Hope I'll see y'all on Grand Prix Weekend!  Goodbye!",
  "It's time for a nap. I'm going to Dreamland to dream about winnin' the Grand Prix."])
GPGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Welcome to Grand Prix Weekend!',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!"], ['Are you excited about the Grand Prix Weekend?',
  'Grand Prix Weekend really drives up those scores!',
  'Get more tickets by racing practice laps.',
  "Gawrsh, you're a fast racer!",
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '? He said he was gonna come watch the Grand Prix!',
  'If you see my friend ' + Mickey + ", tell him he's missing some great racing!",
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  "Gawrsh there sure are a lot of Cogs near Donald's Dock.",
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your jellybeans back!"], ['Good luck in the Grand Prix!',
  "I'm going to catch the next race in the Grand Prix!",
  'Gawrsh I think the next race is about to start!',
  'Gosh, I better go check on the new Leaderboard and make sure it is working right!'])
SillyPhase1Chatter = ["If you haven't seen the Silly Meter, head to Toon Hall!",
 'Toontown is getting sillier by the day!',
 "Cause silly surges in battle to boost Toontown's silly levels!",
 'Objects on the street are starting to animate!',
 'I saw a fire hydrant on Silly Street move!']
SillyPhase2Chatter = ['Silly levels are still rising!',
 'The Silly Meter has climbed higher and gotten crazier!',
 'Someone saw a trash can moving on Maple Street!',
 'A lot of hydrants on Silly Street have come alive!',
 'A mailbox on Lighthouse Lane has gone nuts!',
 'Go see the Silly Meter in Toon Hall!',
 'Keep causing those silly surges!']
SillyPhase3Chatter = ['The Cogs hated how silly Toontown was becoming!',
 'Keep a sharp eye out for Cog Invasions!',
 'Cog Invasions have caused the silly levels to drop!',
 'The Silly Meter went down after the Cog Invasions!',
 'Every street of Toontown has animated objects now!',
 'Toontown is sillier than ever!']
SillyPhase4Chatter = ['Fire hydrants make your Squirt Gags squirtier!',
 'Mail Boxes give your Throw Gags a special delivery!',
 'Those crazy Trash Cans can help boost your Toon-up!',
 'Objects on the street can help you in battle!',
 "I just know we'll get the Silly Meter back up soon!",
 'Enjoy the sillier Toontown!']
for chatter in [MickeyChatter,
 DonaldChatter,
 MinnieChatter,
 GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

BoringTopic = 'Boring'
EmceeDialoguePhase1Topic = 'EmceeDialoguePhase1'
EmceeDialoguePhase2Topic = 'EmceeDialoguePhase2'
EmceeDialoguePhase3Topic = 'EmceeDialoguePhase3'
EmceeDialoguePhase3_5Topic = 'EmceeDialoguePhase3.5'
EmceeDialoguePhase4Topic = 'EmceeDialoguePhase4'
EmceeDialoguePhase5Topic = 'EmceeDialoguePhase5'
EmceeDialoguePhase6Topic = 'EmceeDialoguePhase6'
AprilToonsPhasePreTopTopic = 'AprilToonsPhasePreTopTopic'
AprilToonsPhaseTopTopic = 'AprilToonsPhaseTopTopic'
AprilToonsExtPhaseTopTopic = 'AprilToonsExtPhaseTopTopic'
AprilToonsPhasePostTopTopic = 'AprilToonsPhasePostTopTopic'
toontownDialogues = {BoringTopic: {(1, 2018): ['Hello Albert', 'It looks like the sillyness levels are rising', 'Yes and dont forget April Toons!'],
               (2, 2019): ['Hello Newton', 'Yes I wonder how much the parties are contributing to all this'],
               (3, 2020): ['Why hello there Albert and Newton', 'Halloween was pretty silly too!']},
 AprilToonsPhasePreTopTopic: {(1, 2020): ['Gadzooks! The Silly Meter has come back to life!',
                                          "It's rising every day, and will reach the top soon!",
                                          'When it does, something silly is sure to happen!',
                                          'So get ready to get ridiculous!']},
 AprilToonsPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!',
                                       'Doodles are talking, Estates are bouncy!',
                                       "There's only one thing to say\xe2\x80\xa6",
                                       'HAPPY APRIL TOONS!']},
 AprilToonsExtPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!', 'Doodles are talking, Estates are bouncy!']},
 AprilToonsPhasePostTopTopic: {(1, 2020): ['April Toons is over!',
                                           "It's time for us to return to our lab.",
                                           'But when things get REALLY crazy again\xe2\x80\xa6',
                                           'The Silly Meter will return!']},
 EmceeDialoguePhase1Topic: {(1, 2020): ['Fellow Toons, this is the Silly Meter!',
                                        "It is tracking Toontown's rising silly levels...",
                                        'Which are causing objects on the street to animate!',
                                        'And YOU can help push these levels higher!',
                                        'Battle Cogs to cause Silly Surges...',
                                        'Make Toontown sillier than ever...',
                                        "And let's watch the world come alive!",
                                        "Now I'll repeat what I said, but only once more."]},
 EmceeDialoguePhase2Topic: {(1, 2020): ['Good Gag work, Toons!',
                                        "You're keeping those silly levels rising...",
                                        'And Toontown is getting sillier every day!',
                                        'Fire hydrants, trash cans, and mailboxes are springing to life...',
                                        'Making the world more animated than ever!',
                                        "You know the Cogs aren't happy about this...",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3Topic: {(1, 2020): ['Gadzooks! The Silly Meter is even crazier than expected!',
                                        'Your Silly Surges are working wonders...',
                                        'And Toontown is getting more animated every day!',
                                        'Keep up the good Gag work...',
                                        'And lets see how silly we can make Toontown!',
                                        "You know the Cogs aren't happy about what's going on...",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3_5Topic: {(1, 2020): ['YOU DID IT TOONS!',
                                          'You brought the streets of Toontown to life!',
                                          'You deserve a reward!',
                                          'Enter the code SILLYMETER in your Shticker Book...',
                                          '...to get a Silly Meter T-Shirt!']},
 EmceeDialoguePhase4Topic: {(1, 2020): ['Attention all Toons!',
                                        'The sudden Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen...',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful...',
                                        "So perhaps they'll find a way to show their appreciation!",
                                        'Stay Tooned!']},
 EmceeDialoguePhase5Topic: {(1, 2020): ['Attention all Toons!',
                                        'The Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen...',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful...',
                                        'And are showing their appreciation by helping in battle!',
                                        'We may hold off the Cogs yet, so keep up the fight!']},
 EmceeDialoguePhase6Topic: {(1, 2020): ['Congratulations Toons!',
                                        'You all succesfully held off the Cog Invasions...',
                                        'With a little help from our newly animated friends...',
                                        'And brought Toontown back to its usual silly self!',
                                        'We hope to get the Silly Meter rising again soon...',
                                        'So in the meantime, keep up the Cog fight...',
                                        'And enjoy the silliest place ever, Toontown!']}}
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelSecrets = 'True Friend'
FriendsListPanelOnlineFriends = 'ONLINE TOON\nFRIENDS'
FriendsListPanelAllFriends = 'ALL TOON\nFRIENDS'
FriendsListPanelIgnoredFriends = 'IGNORED\nTOONS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelPlayers = 'ALL PLAYER\nFRIENDS'
FriendsListPanelOnlinePlayers = 'ONLINE PLAYER\nFRIENDS'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterToon = 'Toon'
FriendInviterThatToon = 'That toon'
FriendInviterPlayer = 'Player'
FriendInviterThatPlayer = 'That player'
FriendInviterBegin = 'What type of friend would you like to make?'
FriendInviterToonFriendInfo = 'A friend only in Toontown'
FriendInviterPlayerFriendInfo = 'A friend in another game' # Digi......pulse............?
FriendInviterToonTooMany = 'You have too many toon friends to add another one now. You will have to remove some toon friends if you want to make friends with %s. You could also try making player friends them.'
FriendInviterPlayerTooMany = 'You have too many player friends to add another one now. You will have to remove some player friends if you want to make friends with %s. You could also try making toon friends with them.'
FriendInviterToonAlready = '%s is already your toon friend.'
FriendInviterPlayerAlready = '%s is already your player friend.'
FriendInviterStopBeingToonFriends = 'Stop being toon friends'
FriendInviterStopBeingPlayerFriends = 'Stop being player friends'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being toon friends with %s?'
FriendInviterEndFriendshipPlayer = 'Are you sure you want to stop being player friends with %s?'
FriendInviterRemainToon = '\n(You will still be toon friends with %s)'
FriendInviterRemainPlayer = '\n(You will still be player friends with %s)'
DownloadForceAcknowledgeVerbList = ['painted',
 'unpacked',
 'unfolded',
 'drawn',
 'inflated',
 'built']
DownloadForceAcknowledgeMsg = 'Sorry, the %(phase)s area is still being %(verb)s, and will be ready for you in a minute.'
TeaserTop = ''
TeaserBottom = ''
TeaserDefault = ',\nyou need to become a Member.\n\nJoin us!'
TeaserOtherHoods = 'For unlimited adventures in all 6 neighborhoods'
TeaserTypeAName = 'Type in your favorite name for your Toon!'
TeaserSixToons = 'To play more than one Toon'
TeaserClothing = 'To buy items from the Cattlelog \nto customize your toon'
TeaserCogHQ = 'To access awesome Cog HQs'
TeaserSecretChat = 'To use the True Friends Chat feature'
TeaserSpecies = 'To pick this type of Toon'
TeaserFishing = 'To fish in all 6 neighborhoods'
TeaserGolf = 'To play Toon MiniGolf'
TeaserParties = 'To plan a party'
TeaserSubscribe = 'Subscribe'
TeaserContinue = 'Return To Game'
TeaserEmotions = 'To make your Toon more expressive'
TeaserKarting = 'To access unlimited Kart Racing'
TeaserKartingAccessories = 'To customize your Kart'
TeaserGardening = 'To continue gardening at your Toon Estate'
TeaserHaveFun = 'Have more fun!'
TeaserJoinUs = 'Join us!'
TeaserPlantGags = 'To plant these gags'
TeaserPickGags = 'To pick these gags'
TeaserRestockGags = 'To restock these gags'
TeaserGetGags = 'To get these gags'
TeaserUseGags = 'To use these gags'
TeaserMinigames = TeaserOtherHoods
TeaserQuests = TeaserOtherHoods
TeaserOtherGags = TeaserOtherHoods
TeaserTricks = TeaserOtherHoods
LauncherPhaseNames = {0: 'Initialization',
 1: 'Panda',
 2: 'Engine',
 3: 'Make-A-Toon',
 3.5: 'Toontorial',
 4: 'Playground',
 5: 'Streets',
 5.5: 'Estates',
 6: 'Neighborhoods I',
 7: Cog + ' Buildings',
 8: 'Neighborhoods II',
 9: 'Sellbot HQ',
 10: 'Cashbot HQ',
 11: 'Lawbot HQ',
 12: 'Bossbot HQ',
 13: 'Parties'}
LauncherProgress = '%(name)s (%(current)s of %(total)s)'
LauncherStartingMessage = "Starting the Professor's Little Toontown... "
LauncherDownloadFile = 'Downloading update for ' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Downloading update for ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Downloading update for ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Decompressing update for ' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Decompressing update for ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extracting update for ' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extracting update for ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Applying update for ' + LauncherProgress + '...'
LauncherPatchingPercent = 'Applying update for ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Connecting to Toontown: %s (proxy: %s) attempt: %s'
LauncherConnectAttempt = 'Connecting to Toontown: %s attempt %s'
LauncherDownloadServerFileList = 'Updating Toontown...'
LauncherCreatingDownloadDb = 'Updating Toontown...'
LauncherDownloadClientFileList = 'Updating Toontown...'
LauncherFinishedDownloadDb = 'Updating Toontown... '
LauncherStartingGame = "Starting the Professor's Little Toontown..."
LauncherRecoverFiles = 'Updating Toontown. Recovering files...'
LauncherCheckUpdates = 'Checking for updates for ' + LauncherProgress
LauncherVerifyPhase = 'Updating Toontown...'
LoadingDownloadWatcherUpdate = 'Loading %s'
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceSubscribersOnly = 'Subscribe'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeletePasswordText = 'Careful! This will delete %s forever.  To delete this Toon, enter your password.'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever.  If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoicePassword = 'Password'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'That password does not seem to match.  To delete this Toon, enter your password.'
AvatarChoiceDeleteWrongConfirm = 'You did not type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
DateOfBirthEntryDefaultLabel = 'Date of Birth'
AchievePageTitle = 'Achievements\n(Coming Soon)'
PhotoPageTitle = 'Photo\n(Coming Soon)'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'DELETE GAGS'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'SOS Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = "It's Party Time, click Start Party in your Shticker Book Hosting page!"
PartyHasStartedAcceptedInvite = '%s party has started!  Click the host then "Go To Party" in the Shticker Book Invites page.'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'TOONTOWN TIME IS'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d jellybeans back!'
EventsPageCancelPartyResultError = 'Sorry, your party was not cancelled.'
EventsPageCancelPartyAlreadyRefunded = 'Your party was never started. Check your mailbox for your refund!'
EventsPageTooLateToStart = 'Sorry, it is too late to start your party. You can cancel it and plan another one.'
EventsPagePublicPrivateChange = "Changing your party's privacy setting..."
EventsPagePublicPrivateNoGo = "Sorry, you can't change your party's privacy setting right now."
EventsPagePublicPrivateAlreadyStarted = "Sorry, your party has already started, so you can't change your party's privacy setting."
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'My Next Party'
EventsPageHostTabTitleNoParties = 'No Parties'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'Go to a playground\nParty Gate to plan\nyour own party!'
EventsPageHostTabPublicPrivateLabel = 'This party is:'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'Cancel Party'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'Go to\nParty!'
EventsPageUnknownToon = 'Unknown Toon'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Party Invitations'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
EventsPageNewsTabName = 'News'
EventsPageNewsTabTitle = 'News'
EventsPageNewsDownloading = 'Retrieving News...'
EventsPageNewsUnavailable = "Professor Control messed with our articles! News not available."
EventsPageNewsPaperTitle = 'TOONTOWN TIMES'
EventsPageNewsLeftSubtitle = 'Still only 1 jellybean'
EventsPageNewsRightSubtitle = 'Established toon-thousand nine'
NewsPageName = 'News'
NewsPageImportError = 'Whoops! There is an issue loading the "Toon News ... for the Amused!" Please check back later.'
NewsPageDownloadingNewsSubstr = 'Stay Tooned, while we bring you the latest issue of the \n"Toon News ... for the Amused!"'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + ' %s%% Complete.'
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + ' %s%% Complete..'
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + ' %s%% Complete...'
NewsPageErrorDownloadingFile = 'Whoops! Page %s is missing from "Toon News ... for the Amused!" Please check back later.'
NewsPageErrorDownloadingFileCanStillRead = 'Whoops! Page %s \nis missing from the "Toon News ... for the Amused!" \nTurn the page to continue, while we work to get this page back.'
NewsPageNoIssues = 'Whoops! The "Toon News ... for the Amused!" has gone missing! \nStay Tooned ... while we work to bring the news back!'
IssueFrameThisWeek = 'this week'
IssueFrameLastWeek = 'last week'
IssueFrameWeeksAgo = '%d weeks ago'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Toontown Party Planner'
PartyPlannerInstructions = 'Hosting your own party is a lot of fun!\nStart planning with the arrows at the bottom!'
PartyPlannerDateTitle = 'Pick A Day For Your Party'
PartyPlannerTimeTitle = 'Pick A Time For Your Party'
PartyPlannerGuestTitle = 'Choose Your Guests'
PartyPlannerEditorTitle = 'Design Your Party\nPlace Activities and Decorations'
PartyPlannerConfirmTitle = 'Choose Invitations To Send'
PartyPlannerConfirmTitleNoFriends = 'Double Check Your Party'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Party Date and Time'
PartyPlannerPartyNow = 'As Soon As Possible'
PartyPlannerTimeToontownTime = 'Toontown Time:'
PartyPlannerTimeLocalTime = 'Party Local Time : '
PartyPlannerPublicPrivateLabel = 'This party will be:'
PartyPlannerPublicDescription = 'Any Toon\ncan come!'
PartyPlannerPrivateDescription = 'Only\nInvited Toons\ncan come!'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Toontown Time'
PartyPlannerEditorInstructionsIdle = 'Click on the Party Activity or Decoration you would like to purchase.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Click Buy or Drag the Activity Icon onto the Party Grounds Map'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Click Buy or Drag the Decoration onto the Party Grounds Map'
PartyPlannerEditorInstructionsDraggingActivity = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsPartyGrounds = 'Click and Drag items to move them around the Party Grounds Map'
PartyPlannerEditorInstructionsTrash = 'Drag an Activity or Decoration here to remove it.'
PartyPlannerEditorInstructionsNoRoom = 'There is no room to place that activity.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = 'SOLD OUT'
PartyPlannerBuy = 'BUY'
PartyPlannerPaidOnly = 'MEMBERS ONLY'
PartyPlannerPartyGrounds = 'PARTY GROUNDS MAP'
PartyPlannerOkWithGroundsLayout = 'Are you done moving your Party Activities and Decorations around the Party Grounds Map?'
PartyPlannerChooseFutureTime = 'Please choose a time in the future.'
PartyPlannerInviteButton = 'Send Invites'
PartyPlannerInviteButtonNoFriends = 'Plan Party'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValentoonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'Guest Name'
PartyPlannerClosePlanner = 'Close Planner'
PartyPlannerConfirmationAllOkTitle = 'Congratulations!'
PartyPlannerConfirmationAllOkText = 'Your party has been created and your invitations sent out.\nThanks!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Your party has been created!\nThanks!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Sorry, there seems to be a problem\nwith that party.\nPlease go back and try again.'
PartyPlannerConfirmationDatabaseErrorText = "Sorry, I couldn't record all your information.\nPlease try again later.\nDon't worry, no beans were lost."
PartyPlannerConfirmationTooManyText = 'Sorry, you are already hosting a party.\nIf you want to plan another party, please\ncancel your current party.'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'It will have '
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerComingSoon = 'Coming Soon'
PartyPlannerCantBuy = "Can't Buy"
PartyPlannerGenericName = 'Party Planner'
PartyJukeboxOccupied = 'Someone else is using the jukebox. Try again later.'
PartyJukeboxNowPlaying = 'The song you chose is now playing on the jukebox!'
MusicEncntrGeneralBg = 'Encounter With Cogs'
MusicTcSzActivity = 'Toontorial Medley'
MusicTcSz = 'Strolling Along'
MusicCreateAToon = 'The New Toon in Town'
MusicTtTheme = 'The Toontown Theme'
MusicMinigameRace = 'Slow and Steady'
MusicMgPairing = 'Remember Me?'
MusicTcNbrhood = 'Toontown Central'
MusicMgDiving = 'Treasure Lullaby'
MusicMgCannonGame = 'Fire the Cannons!'
MusicMgTwodgame = 'Running Toon'
MusicMgCogthief = 'Catch That Cog!'
MusicMgTravel = 'Traveling Music'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = 'The Jungle Swing'
MusicMgIcegame = 'Slippery Situation'
MusicMgToontag = 'Minigame Medley'
MusicMMatchBg2 = 'Jazzy Minnie'
MusicMgTarget = "Soarin' Over Toontown"
MusicFfSafezone = 'The Funny Farm'
MusicDdSz = 'Waddling Way'
MusicMmNbrhood = "Minnie's Melodyland"
MusicGzPlaygolf = "Let's Play Golf!"
MusicGsSz = 'Goofy Speedway'
MusicOzSz = "Chip n' Dale's Acres"
MusicGsRaceCc = 'Downtown Driving'
MusicGsRaceSs = 'Ready, Set, Go!'
MusicGsRaceRr = 'Route 66'
MusicGzSz = 'The Putt-Putt Polka'
MusicMmSz = 'Dancing in the Streets'
MusicMmSzActivity = 'Here Comes Treble'
MusicDdNbrhood = "Donald's Dock"
MusicGsKartshop = 'Mr. Goofywrench'
MusicDdSzActivity = 'Sea Shanty'
MusicEncntrGeneralBgIndoor = 'Building Excitement'
MusicTtElevator = 'Going Up?'
MusicEncntrToonWinningIndoor = 'Toons Unite!'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'The Brrrgh'
MusicDlNbrhood = "Donald's Dreamland"
MusicDlSzActivity = 'Counting Sheep'
MusicDgSz = 'Waltz of the Flowers'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Snow Problem'
MusicTbSz = 'Shiver and Shimmy'
MusicDgNbrhood = "Daisy's Garden"
MusicEncntrHallOfFame = 'The Hall of Fame'
MusicEncntrSuitHqNbrhood = 'Dollars and Cents'
MusicChqFactBg = 'Cog Factory'
MusicCoghqFinale = 'Triumph of the Toons'
MusicEncntrToonWinning = 'Cashing In!'
MusicEncntrSuitWinning = 'Selling You Short'
MusicEncntrHeadSuitTheme = 'The Big Boss'
MusicLbJurybg = 'Court is in Session'
MusicLbCourtyard = 'Balancing Act'
MusicBossbotCeoV2 = 'Head Honcho'
MusicBossbotFactoryV1 = 'Cog Waltz'
MusicBossbotCeoV1 = 'Bossing You Around'
MusicPartyOriginalTheme = 'Party Time'
MusicPartyPolkaDance = 'Party Polka'
MusicPartySwingDance = 'Party Swing'
MusicPartyWaltzDance = 'Party Waltz'
MusicPartyGenericThemeJazzy = 'Party Jazz'
MusicPartyGenericTheme = 'Party Jingle'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Playing Next:'
JukeboxSongsLabel = 'Pick a Song:'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Currently Playing'
JukeboxCurrentlyPlayingNothing = 'Jukebox is paused.'
JukeboxCurrentSongNothing = 'Add a song to the playlist!'
PartyOverWarningNoName = 'The party has ended! Thanks for coming!'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = ', and'
PartyActivityNameDict = {0: {'generic': 'Jukebox\n20 songs',
     'invite': 'a 20 song Jukebox',
     'editor': 'Jukebox - 20',
     'description': 'Listen to music with your own 20 song jukebox!'},
 1: {'generic': 'Party Cannons',
     'invite': 'Party Cannons',
     'editor': 'Cannons',
     'description': 'Fire yourself out of the cannons and into fun!'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'Collect jellybeans and bounce the highest!'},
 3: {'generic': 'Party Catch',
     'invite': 'Party Catch',
     'editor': 'Party Catch',
     'description': 'Catch fruit to win beans! Dodge those anvils!'},
 4: {'generic': 'Dance Floor\n10 moves',
     'invite': 'a 10 move Dance Floor',
     'editor': 'Dance Floor - 10',
     'description': 'Show off all 10 of your moves, toon style!'},
 5: {'generic': 'Party Tug-of-War',
     'invite': 'Party Tug-of-War',
     'editor': 'Tug-of-War',
     'description': 'Up to 4 on 4 toon tugging craziness!'},
 6: {'generic': 'Party Fireworks',
     'invite': 'Party Fireworks',
     'editor': 'Fireworks',
     'description': 'Launch your very own fireworks show!'},
 7: {'generic': 'Party Clock',
     'invite': 'a Party Clock',
     'editor': 'Party Clock',
     'description': 'Counts down the time left in your party.'},
 8: {'generic': 'Jukebox\n40 songs',
     'invite': 'a 40 song jukebox',
     'editor': 'Jukebox - 40',
     'description': 'Listen to music with your own 40 song jukebox!'},
 9: {'generic': 'Dance Floor\n20 moves',
     'invite': 'a 20 move Dance Floor',
     'editor': 'Dance Floor - 20',
     'description': 'Show off all 20 of your moves, toon style!'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'The team vs. team game of Cog splatting!'},
 11: {'generic': 'Cog Trampoline',
      'invite': 'Cog Trampoline',
      'editor': 'Cog Trampoline',
      'description': "Jump on a Cog's face!"},
 12: {'generic': 'Present Catch',
      'invite': 'Present Catch',
      'editor': 'Present Catch',
      'description': 'Catch presents to win beans! Dodge those anvils!'},
 13: {'generic': 'Holiday Trampoline',
      'invite': 'Holiday Trampoline',
      'editor': 'Holiday Trampoline',
      'description': 'Jump if you love Winter Holidays!'},
 14: {'generic': 'Holiday Cog-O-War',
      'invite': 'Holiday Cog-O-War',
      'editor': 'Holiday Cog-O-War',
      'description': 'The team vs. team game of Cog splattering!'},
 15: {'generic': 'Dance Floor\n10 moves',
      'invite': 'a 10 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 10',
      'description': 'Get your ValenToon Groove On!'},
 16: {'generic': 'Dance Floor\n20 moves',
      'invite': 'a 20 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 20',
      'description': 'Get your ValenToon Groove On!'},
 17: {'generic': 'Jukebox\n20 songs',
      'invite': 'a 20 song Valentoons Jukebox',
      'editor': 'Jukebox - 20',
      'description': 'Nothing sets the mood like music!'},
 18: {'generic': 'Jukebox\n40 songs',
      'invite': 'a 40 song Valentoons jukebox',
      'editor': 'Jukebox - 40',
      'description': 'Nothing sets the mood like music!'},
 19: {'generic': 'Trampoline',
      'invite': 'ValenToons Trampoline',
      'editor': 'Trampoline',
      'description': "Jump to your heart's content!"}}
PartyDecorationNameDict = {0: {'editor': 'Balloon Anvil',
     'description': 'Try to keep the fun from floating away!'},
 1: {'editor': 'Party Stage',
     'description': 'Balloons, stars, what else could you want?'},
 2: {'editor': 'Party Bow',
     'description': 'Wrap up the fun!'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Party Castle',
     'description': "A Toon's home is his castle."},
 5: {'editor': 'Gift Pile',
     'description': 'Gifts for every Toon!'},
 6: {'editor': 'Streamer Horn',
     'description': 'This horn is a hoot! Streamers!'},
 7: {'editor': 'Party Gate',
     'description': 'Multi-colored and crazy!'},
 8: {'editor': 'Noise Makers',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Colorful twirling for everyone!'},
 10: {'editor': 'Gag Globe',
      'description': 'Gag and star globe designed by Olivea'},
 11: {'editor': 'Bean Banner',
      'description': 'A Jellybean banner designed by Cassidy'},
 12: {'editor': 'Gag Cake',
      'description': 'A Topsy Turvy gag cake designed by Felicia'},
 13: {'editor': "Cupid's Heart",
      'description': 'Ready...Aim...\nValenToons!'},
 14: {'editor': 'Candy Hearts\n Banner',
      'description': "Who doesn't love candy hearts?"},
 15: {'editor': 'Flying Heart',
      'description': 'This heart is getting carried away!'},
 16: {'editor': 'Victory Bandstand',
      'description': 'All our new friends are ready to dance!'},
 17: {'editor': 'Victory Banner',
      'description': 'Not just a normal banner!'},
 18: {'editor': 'Confetti Cannons',
      'description': 'BOOM! Confetti! Fun!'},
 19: {'editor': 'Cog & Doodle',
      'description': "Ouch! That's gotta hurt."},
 20: {'editor': 'Cog Flappy Man',
      'description': 'A Cog full of hot air, what a shock!'},
 21: {'editor': 'Cog Ice Cream',
      'description': 'A Cog looking his best.'},
 22: {'editor': 'CogCicle',
      'description': 'A Cog looking his holiday best.'},
 23: {'editor': 'Holiday Bandstand',
      'description': 'Everyone loves a Holiday Party!'},
 24: {'editor': 'Chilly Cog',
      'description': "Ouch! That's gotta hurt."},
 25: {'editor': 'Snowman',
      'description': "So cool, he's hot!"},
 26: {'editor': 'SnowDoodle',
      'description': 'His only trick is being cold!'},
 27: {'editor': 'ValenToons Anvil',
      'description': "We've got your heart on a string!"}}
ActivityLabel = 'Cost - Activity Name'
PartyDoYouWantToPlan = 'Would you like to plan a new party right now?'
PartyPlannerOnYourWay = 'Have fun planning your party!'
PartyPlannerMaybeNextTime = 'Maybe next time.  Have a good day!'
PartyPlannerHostingTooMany = 'You can only host one party at a time, sorry.'
PartyPlannerOnlyPaid = 'Only paid toons can host a party, sorry.'
PartyPlannerNpcComingSoon = 'Parties are coming soon! Try again later.'
PartyPlannerNpcMinCost = 'It costs a minimum of %d jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Do you want to go to the 1st available public party?'
PartyGateTitle = 'Public Parties'
PartyGateGoToParty = 'Go to\nParty!'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Minutes Left'
PartyGateLeftSign = 'Come On In!'
PartyGateRightSign = 'Public Parties Here!'
PartyGatePartyUnavailable = 'Sorry. That party is no longer available.'
PartyGatePartyFull = 'Sorry. That party is full.'
PartyGateInstructions = 'Click on a host, then click on "Go to Party"'
PartyActivityWaitingForOtherPlayers = 'Waiting for other players to join the party game...'
PartyActivityPleaseWait = 'Please wait...'
DefaultPartyActivityTitle = 'Party Game Title'
DefaultPartyActivityInstructions = 'PartyGame Instructions'
PartyOnlyHostLeverPull = 'Only the host can start this activity. Sorry.'
PartyActivityDefaultJoinDeny = 'You cannot join this activity right now. Sorry.'
PartyActivityDefaultExitDeny = 'You cannot leave this activity right now. Sorry.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Party Catch Activity'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'PERFECT GAME!'
PartyCatchActivityFinish = 'Good Game!'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'The game has started. Go play it.'
PartyCatchCannotStart = 'The game could not start right now.'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Party Dance Floor'
PartyDanceActivityInstructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 10 dance moves available. Can you find them all?'
PartyDanceActivity20Title = 'Party Dance Floor'
PartyDanceActivity20Instructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 20 dance moves available. Can you find them all?'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'The Fishertoon'
DanceAnimConked = 'The Headbob'
DanceAnimHappyDance = 'The Happy Dance'
DanceAnimConfused = 'Very Dizzy'
DanceAnimWalk = 'Walking on the Moon'
DanceAnimJump = 'The Jump!'
DanceAnimFirehose = 'The Firetoon'
DanceAnimShrug = 'Who Knows?'
DanceAnimSlipForward = 'The Fall'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Hello Goodbye'
DanceAnimStruggle = 'The Shuffle Hop'
DanceAnimRunningJump = 'The Running Toon'
DanceAnimSlipBackward = 'The Backfall'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'The Putt'
DanceAnimVictory = 'The Victory Dance'
DanceAnimPush = 'The Mimetoon'
DanceAnimAngry = "Rock n' Roll"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'Party Cannons'
PartyCannonActivityInstructions = 'Hit the clouds to change their color and bounce in the air! While IN THE AIR, you can USE THE ARROW KEYS to GLIDE.'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'Hit the "Page Up" key to see better.'
FireworksActivityBeginning = 'Party fireworks are about to start! Enjoy the show!'
FireworksActivityEnding = 'Hope you enjoyed the show!'
PartyFireworksAlreadyActive = 'The fireworks show has already started.'
PartyFireworksAlreadyDone = 'The fireworks show is over.'
PartyTrampolineJellyBeanTitle = 'Jelly Beans Trampoline'
PartyTrampolineTricksTitle = 'Tricks Trampoline'
PartyTrampolineActivityInstructions = 'Use the Control key to jump.\n\nJump when your Toon is at its lowest point on the trampoline to jump higher.'
PartyTrampolineActivityOccupied = 'Trampoline in use.'
PartyTrampolineQuitEarlyButton = 'Hop Off'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean.'
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Time's Up"
PartyTrampolineReady = 'Ready...'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'How high\ncan you jump?'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting  for  %d  player%s\non  each  side...'
PartyTeamActivityForMoreWithBalance = 'Waiting  for  %d  more  player%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Waiting  for  other  players...'
PartyTeamActivityWaitingToStart = 'Starting  in...'
PartyTeamActivityExitButton = 'Hop Off'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Your team won!'
PartyTeamActivityGameTie = "It's a tie!"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Sorry, you cant's switch teams at this time."
PartyTeamActivityTeamFull = 'Sorry, that team is already full!'
PartyTeamActivityRewardMessage = 'You got %d jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogSignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Throw pies at cogs to push them away from your team. ' + "When time's up, the team with most cogs on the other side wins!" + '\n\nThrow with the CONTROL KEY. Move with the ARROW KEYS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Time's up!"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'Hold CONTROL for more power!'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready...'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Good  game!'
PartyTugOfWarTitle = 'Party Tug-of-War'
CalendarShowAll = 'Show All'
CalendarShowOnlyHolidays = 'Show Only Holidays'
CalendarShowOnlyParties = 'Show Only Parties'
CalendarEndsAt = 'Ends at '
CalendarStartedOn = 'Started on '
CalendarEndDash = 'End-'
CalendarEndOf = 'End of '
CalendarPartyGetReady = 'Get ready!'
CalendarPartyGo = 'Go party!'
CalendarPartyFinished = "It's over..."
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'Never Started.'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog Headquarters'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsTabTitle = 'Options\n& Codes'
OptionsPagePurchase = 'Subscribe'
OptionsPageLogout = 'Logout'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusicOnLabel = 'Music is on.'
OptionsPageMusicOffLabel = 'Music is off.'
OptionsPageSFXOnLabel = 'Sound Effects are on.'
OptionsPageSFXOffLabel = 'Sound Effects are off.'
OptionsPageToonChatSoundsOnLabel = '   Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = '   Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageWhisperEnabledLabel = 'Allowing whispers from anyone.'
OptionsPageWhisperDisabledLabel = 'Allowing whispers from friends only.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageDisplayEmbedded = 'In the browser'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer.  It is probably not necessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsEmbedded = 'In the browser'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
OptionsPageCodesTab = 'Enter Code'
CdrPageTitle = 'Enter a Code'
CdrInstructions = 'Enter your code to receive a special item in your mailbox.'
CdrResultSuccess = 'Congratulations! Check your mailbox to claim your item!'
CdrResultInvalidCode = "You've entered an invalid code. Please check the code and try again."
CdrResultExpiredCode = "We're sorry. This code has expired."
CdrResultUnknownError = "We're sorry. This code cannot be applied to your Toon."
CdrResultMailboxFull = 'Your mailbox is full. Please remove an item, then enter your code again.'
CdrResultAlreadyInMailbox = "You've already received this item. Check your mailbox to confirm."
CdrResultAlreadyInQueue = 'Your item is on its way. Check your mailbox in a few minutes to receive it.'
CdrResultAlreadyInCloset = "You've already received this item. Check your closet to confirm."
CdrResultAlreadyBeingWorn = "You've already received this item, and you are wearing it!"
CdrResultAlreadyReceived = "You've already received this item."
CdrResultTooManyFails = "We're sorry. You've tried to enter an incorrect code too many times. Please try again after some time."
CdrResultServiceUnavailable = "We're sorry. This feature is temporarily unavailable. Please try again during your next login."
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new gags!'
TrackPageTraining = 'You are training to use %s gags.\nWhen you complete all 16 tasks you\nwill be able to use %s gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Just for fun!'
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Are you sure you want to delete this ToonTask?'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpWelcomeValley = '  You are currently in the "Welcome Valley" District, within "%s".'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'Sorry, that district is full. Please try another one.'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = '???'
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d jellybean'
FishPageValueP = 'Value: %d jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Flying Fish',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Flower Basket'
GardenPageTitleCollection = 'Flower Album'
GardenPageTitleTrophy = 'Gardening Trophies'
GardenPageTitleSpecials = 'Gardening Specials'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d jellybean'
GardenPageValueP = 'Value: %d jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Large P'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Kart Customizer'
KartPageTitleRecords = 'Personal Best Records'
KartPageTitleTrophy = 'Racing Trophies'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Tickets : '
KartPageConfirmDelete = 'Delete Accessory?'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'Select a Category'
KartShtikerNoAccessories = 'No Accessories Owned'
KartShtikerBodyColors = 'Kart Colors'
KartShtikerAccColors = 'Accessory Colors'
KartShtikerEngineBlocks = 'Hood Accessories'
KartShtikerSpoilers = 'Trunk Accessories'
KartShtikerFrontWheelWells = 'Front Wheel Accessories'
KartShtikerBackWheelWells = 'Back Wheel Accessories'
KartShtikerRims = 'Rim Accessories'
KartShtikerDecals = 'Decal Accessories'
KartShtikerBodyColor = 'Kart Color'
KartShtikerAccColor = 'Accessory Color'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'Front Wheel'
KartShtikerBackWheelWell = 'Back Wheel'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
TIPPageTitle = 'TIP'
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laff meter is smiling!'
InventoryTotalGags = 'Total gags\n%d / %d'
InventroyPinkSlips = '%s Pink Slips'
InventroyPinkSlip = '1 Pink Slip'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryGuestExp = 'Guest Limit'
GuestLostExp = 'Over Guest Limit'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryClickToAttack = 'Click a\ngag to\nattack'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Congratulations!  You found and rode the trolley!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7Retro = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another player and use the New Friend button."
NPCForceAcknowledgeMessage8Retro = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
NPCForceAcknowledgeMessage7 = "You are a cheater!\n\n\n\n\n\n\nHey! Cut it out! You might see something you're not supposed to!"
NPCForceAcknowledgeMessage8 = '\n\n\nAnd now I see\nWith eyes serene\nThe very heart\nOf the machine'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'You received 1 Throw point! When you get 10, you will get a new gag!'
MovieTutorialReward2 = 'You received 1 Squirt point! When you get 10, you will get a new gag!'
MovieTutorialReward3 = 'Good job! You completed your first ToonTask!'
MovieTutorialReward4 = 'Go to Toon Headquarters for your reward!'
MovieTutorialReward5 = 'Have fun!'
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'drop']
BattleGlobalNPCTracks = ['restock', 'toons hit', 'cogs miss']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'Bamboo Cane',
  'Pixie Dust',
  'Juggling Cubes',
  'High Dive'),
 ('Banana Peel',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('$1 bill',
  'Small Magnet',
  '$5 bill',
  'Big Magnet',
  '$10 bill',
  'Hypno Glasses',
  'Presentation'),
 ('Bike Horn',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Elephant Trunk',
  'Foghorn',
  'Opera Singer'),
 ('Cupcake',
  'Fruit Pie Slice',
  'Cream Pie Slice',
  'Whole Fruit Pie',
  'Whole Cream Pie',
  'Birthday Cake',
  'Wedding Cake'),
 ('Squirting Flower',
  'Glass of Water',
  'Squirt Gun',
  'Seltzer Bottle',
  'Fire Hose',
  'Storm Cloud',
  'Geyser'),
 ('Flower Pot',
  'Sandbag',
  'Anvil',
  'Big Weight',
  'Safe',
  'Grand Piano',
  'Oceanliner'))
BattleGlobalAvPropStringsSingular = (('a Feather',
  'a Megaphone',
  'a Lipstick',
  'a Bamboo Cane',
  'a Pixie Dust',
  'a set of Juggling Cubes',
  'a High Dive'),
 ('a Banana Peel',
  'a Rake',
  'a set of Marbles',
  'a patch of Quicksand',
  'a Trapdoor',
  'a stick of TNT',
  'a Railroad'),
 ('a $1 bill',
  'a Small Magnet',
  'a $5 bill',
  'a Big Magnet',
  'a $10 bill',
  'a pair of Hypno Goggles',
  'a Presentation'),
 ('a Bike Horn',
  'a Whistle',
  'a Bugle',
  'an Aoogah',
  'an Elephant Trunk',
  'a Foghorn',
  'an Opera Singer'),
 ('a Cupcake',
  'a Fruit Pie Slice',
  'a Cream Pie Slice',
  'a Whole Fruit Pie',
  'a Whole Cream Pie',
  'a Birthday Cake',
  'a Wedding Cake'),
 ('a Squirting Flower',
  'a Glass of Water',
  'a Squirt Gun',
  'a Seltzer Bottle',
  'a Fire Hose',
  'a Storm Cloud',
  'a Geyser'),
 ('a Flower Pot',
  'a Sandbag',
  'an Anvil',
  'a Big Weight',
  'a Safe',
  'a Grand Piano',
  'an Oceanliner'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Bamboo Canes',
  'Pixie Dusts',
  'sets of Juggling Cubes',
  'High Dives'),
 ('Banana Peels',
  'Rakes',
  'sets of Marbles',
  'patches of Quicksand',
  'Trapdoors',
  'sticks of TNT',
  'Railroads'),
 ('$1 bills',
  'Small Magnets',
  '$5 bills',
  'Big Magnets',
  '$10 bills',
  'pairs of Hypno Glasses',
  'Presentations'),
 ('Bike Horns',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'Elephant Trunks',
  'Foghorns',
  'Opera Singers'),
 ('Cupcakes',
  'Fruit Pie Slices',
  'Cream Pie Slices',
  'Whole Fruit Pies',
  'Whole Cream Pies',
  'Birthday Cakes',
  'Wedding cakes'),
 ('Squirting Flowers',
  'Glasses of Water',
  'Squirt Guns',
  'Seltzer Bottles',
  'Fire Hoses',
  'Storm Clouds',
  'Geysers'),
 ('Flower Pots',
  'Sandbags',
  'Anvils',
  'Big Weights',
  'Safes',
  'Grand Pianos',
  'Oceanliners'))
BattleGlobalAvTrackAccStrings = ('Medium',
 'Perfect',
 'Low',
 'High',
 'Medium',
 'High',
 'Low')
BattleGlobalLureAccLow = 'Low'
BattleGlobalLureAccMedium = 'Medium'
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Loading...'
HeadingToHood = 'Heading %(to)s %(hood)s...'
HeadingToYourEstate = 'Heading to your estate...'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Heading to the Playground...'
HeadingToStreet = 'Heading %(to)s %(street)s...'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH COG?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother players...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your Laff meter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until ' + Mickey + ' says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble.  Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time.  Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly.  Some fish are faster than others.  Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly.  Some fish are slower than others.  Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop Clerk and come back.'
FishingBroke = 'You do not have any more jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingBootItem = 'An old boot'
FishingJellybeanItem = '%s jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hi %s!'
TutorialGreeting2 = 'Hi %s!\nCome over here!'
TutorialGreeting3 = 'Hi %s!\nCome over here!\nUse the arrow keys!'
TutorialMickeyWelcome = 'Welcome to Toontown!'
TutorialFlippyIntro = 'Let me introduce you to my friend %s...' % Flippy
TutorialFlippyHi = 'Hi, %s!'
TutorialQT1 = 'You can talk by using this.'
TutorialQT2 = 'You can talk by using this.\nClick it, then choose "Hi".'
TutorialChat1 = 'You can talk using either of these buttons.'
TutorialChat2 = 'The blue button lets you chat with the keyboard.'
TutorialChat3 = "Be careful!  Most other players won't understand what you say you when you use the keyboard."
TutorialChat4 = 'The green button opens the %s.'
TutorialChat5 = 'Everyone can understand you if you use the %s.'
TutorialChat6 = 'Try saying "Hi".'
TutorialBodyClick1 = 'Very good!'
TutorialBodyClick2 = 'Pleased to meet you! Want to be friends?'
TutorialBodyClick3 = 'To make friends with %s, click on him...' % Flippy
TutorialHandleBodyClickSuccess = 'Good Job!'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on %s...' % Flippy
TutorialFriendsButton = "Now click the 'Friends' button under %s's picture in the right hand corner." % Flippy
TutorialHandleFriendsButton = "And then click on the 'Yes' button.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Would you like to make friends with %s?' % Flippy
TutorialFriendsPanelMickeyChat = "%s has agreed to be your friend. Click 'Ok' to finish up." % Flippy
TutorialFriendsPanelYes = '%s said yes!' % Flippy
TutorialFriendsPanelNo = "That's not very friendly!"
TutorialFriendsPanelCongrats = 'Congratulations! You made your first friend.'
TutorialFlippyChat1 = 'Come see me when you are ready for your first ToonTask!'
TutorialFlippyChat2 = "I'll be in ToonHall!"
TutorialAllFriendsButton = 'You can view all your friends by clicking the friends button. Try it out...'
TutorialEmptyFriendsList = "Right now your list is empty because %s isn't a real player." % Flippy
TutorialCloseFriendsList = "Click the 'Close'\nbutton to make the\nlist go away"
TutorialShtickerButton = 'The button in the lower, right corner opens your Shticker Book. Try it...'
TutorialBook1 = 'The book contains lots of useful information like this map of Toontown.'
TutorialBook2 = 'You can also check the progress of your ToonTasks.'
TutorialBook3 = 'When you are done click the book button again to make it close'
TutorialLaffMeter1 = 'You will also need this...'
TutorialLaffMeter2 = "You will also need this...\nIt's your Laff meter."
TutorialLaffMeter3 = 'When ' + Cogs + ' attack you, it gets lower.'
TutorialLaffMeter4 = 'When you are in playgrounds like this one, it goes back up.'
TutorialLaffMeter5 = 'When you complete ToonTasks, you will get rewards, like increasing your Laff limit.'
TutorialLaffMeter6 = 'Be careful! If the ' + Cogs + ' defeat you, you will lose all your gags.'
TutorialLaffMeter7 = 'To get more gags, play trolley games.'
TutorialTrolley1 = 'Follow me to the trolley!'
TutorialTrolley2 = 'Hop on board!'
TutorialBye1 = 'Play some games!'
TutorialBye2 = 'Play some games!\nBuy some gags!'
TutorialBye3 = 'Go see %s when you are done!' % Flippy
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find %s!' % Mickey
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel.  From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick.  If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog.  Better tricks give better Toon-Ups!"

def getPetGuiAlign():
    from panda3d.core import TextNode
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Next Page'
GardenTutorialPrev = 'Previous Page'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Toon up your Estate with a garden!  You can plant flowers, grow trees, harvest super-powerful gags, and decorate with statues!'
GardenTutorialPage2 = 'Flowers are finicky and require unique jellybean recipes. Once grown, put them in the wheelbarrow to sell them and work toward Laff boosts!'
GardenTutorialPage3 = 'Use a gag from your inventory to plant a tree.  After a few days, that gag will do more damage!  Remember to keep it healthy or the damage boost will go away.'
GardenTutorialPage4 = 'Walk up to these spots to plant, water, dig up or harvest your garden.'
GardenTutorialPage5 = "Statues can be purchased in Clarabelle's Cattlelog. Increase your skill to unlock the more extravagant statues!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = 'Heading to %s...'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the Clerk!'
GolfCourseBossConfrontedMsg = '%s is battling the Club President!'
stageToonEnterElevator = '%s \nhas entered the elevator'
ForcedLeaveStageAckMsg = 'The Law Clerk was defeated before you could reach him. You did not recover any Jury Notices.'
MinigameWaitingForOtherPlayers = 'Waiting for other players to join...'
MinigamePleaseWait = 'Please wait...'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = 'Heading to %s...'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Toon Escape'
TwoDGameInstructions = 'Escape from the ' + Cog + ' den as soon as you can. Use arrow keys to run/jump and Ctrl to squirt a ' + Cog + '. Collect ' + Cog + ' treasures to gain even more points.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match %s' % Minnie
PatternGameInstructions = Minnie + ' will show you a dance sequence. ' + 'Try to repeat ' + Minnie + "'s dance just the way you see it using the arrow keys!"
PatternGameWatch = 'Watch these dance steps...'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGameWaitingOtherPlayers = 'Waiting for other players...'
PatternGamePleaseWait = 'Please wait...'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'You did great!  Now Improv!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other players to choose...'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 jellybeans'
RaceGameJellybeans4 = '4 jellybeans'
RaceGameJellybeans10 = '10 jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other players will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
DivingGameTitle = 'Treasure Dive'
DivingInstructionsSinglePlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Avoid the fish and get the treasures up to the boat!'
DivingInstructionsMultiPlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Work together to get the treasures up to the boat!'
DivingGameTreasuresRetrieved = 'Treasures Retrieved'
TargetGameTitle = 'Toon Slingshot'
TargetGameInstructionsSinglePlayer = 'Land on targets to score points'
TargetGameInstructionsMultiPlayer = 'Land on targets to score points'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Pound left and right arrows for power, stop to launch'
TargetGameFlyHelp = 'Press down to open umbrella'
TargetGameFallHelp = 'Use the arrow keys to land on target'
TargetGameBounceHelp = ' Bouncing can knock you off target'
PhotoGameScoreTaken = '%s: %s\nYou: %s'
PhotoGameScoreBlank = 'Score: %s'
PhotoGameScoreOther = '\n%s'
PhotoGameScoreYou = '\nBest Bonus!'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
PhotoGameInstructions = 'Capture photos matching the toons shown at the bottom. Aim the camera with the mouse, and left click to take a picture. Press Ctrl to zoom in/out, and look around with the arrow keys.  Pictures with higher ratings get more points!'
PhotoGameTitle = 'Photo Fun'
PhotoGameFilm = 'FILM'
PhotoGameScore = 'Team Score: %s\n\nBest Photos: %s\n\nTotal Score: %s'
CogThiefGameTitle = Cog + ' Thief'
CogThiefGameInstructions = 'Keep the ' + Cogs + ' from stealing our gag barrels! Press the Ctrl key to throw a pie. Use the arrow keys to move. Tip: you can move diagonally.'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'No Barrels\nSaved'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
GagShopName = "Goofy's Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s jellybeans to spend'
GagShopYouHaveOne = 'You have 1 jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of jellybeans!'
GagShopWaitingOtherPlayers = 'Waiting for other players...'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
GenderShopQuestionMickey = 'To make a boy toon, click on me!'
GenderShopQuestionMinnie = 'To make a girl toon, click on me!'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'Toon Color'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopParts = 'Multi Color'
ColorShopAll = 'Single Color'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
PromptTutorial = "Congratulations!!\nYou are Toontown's newest citizen!\n\nWould you like to continue to the Toontorial or teleport directly to Toontown Central?"
MakeAToonSkipTutorial = 'Skip Toontorial'
MakeAToonEnterTutorial = 'Enter Toontorial'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your toon.'
CreateYourToonTitle = 'Choose  Boy  or  Girl'
ShapeYourToonTitle = 'Choose  Your  Type'
PaintYourToonTitle = 'Choose  Your  Color'
PickClothesTitle = 'Choose  Your  Clothes'
NameToonTitle = 'Choose  Your  Name'
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PaintYourToon = 'Click the arrows to paint your toon!'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your toon to have a first or last name?"
ApprovalForName1 = "That's it, your toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
PetNameMaster = 'PetNameMasterEnglish.txt'
PetNameIndexMAX = 2713
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their Toons.\nUntil you subscribe\nyour name will be\n'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names must be\napproved by the Toon Council.'
NameMessages = 'Be creative and remember:\nfollow the rules of the server.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
CopyrightedNames = ('mickey',
 'mickey mouse',
 'mickeymouse',
 'minnie',
 'minnie mouse',
 'minniemouse',
 'donald',
 'donald duck',
 'donaldduck',
 'pluto',
 'goofy')
NumToColor = ['White',
 'Peach',
 'Bright Red',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Sea Green',
 'Green',
 'Light Blue',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Royal Blue',
 'Slate Blue',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig',
 'deer': 'Deer',
 'crocodile': 'Crocodile'}
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry.  That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = lToonHQ + ': ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry.  We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on purchasing a Doodle! You can play with your new friend at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt them before someone else does!'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
SuitInvasionBegin1 = lToonHQ + ': A Cog Invasion has begun!!!'
SuitInvasionBegin2 = lToonHQ + ': %s have taken over Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ': The %s Invasion has ended!!!'
SuitInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
SuitInvasionUpdate1 = lToonHQ + ': The Cog Invasion is now at %s Cogs!!!'
SuitInvasionUpdate2 = lToonHQ + ': We must defeat those %s!!!'
SuitInvasionBulletin1 = lToonHQ + ': There is a Cog Invasion in progress!!!'
SuitInvasionBulletin2 = lToonHQ + ': %s have taken over Toontown!!!'
LeaderboardTitle = 'Toon Platoon'
QuestScriptTutorialMickey_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMickey_2 = 'Sure, %s!'
QuestScriptTutorialMickey_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!'
QuestScriptTutorialMickey_4 = 'Come here! Use the arrow keys to move.'
QuestScriptTutorialMinnie_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMinnie_2 = 'Sure, %s!'
QuestScriptTutorialMinnie_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!'
QuestScript101_1 = 'These are Cogs. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of Cogs and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But Cogs can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_7 = 'There are lots of gags, but take these to start.'
QuestScript101_8 = 'Oh! You also need a Laff meter!'
QuestScript101_9 = "If your Laff meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy Toon is a healthy Toon!'
QuestScript101_11 = "OH NO! There's a Cog outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that Cog!'
QuestScript101_13 = 'Here is your first ToonTask!'
QuestScript101_14 = 'Hurry up! Go defeat that Cold Caller!'
QuestScript110_1 = 'Good work defeating that Cold Caller. Let me give you a Shticker Book...'
QuestScript110_2 = 'The book is full of good stuff.'
QuestScript110_3 = "Open it, and I'll show you."
QuestScript110_4 = "The map shows where you've been."
QuestScript110_5 = 'Turn the page to see your gags...'
QuestScript110_6 = 'Uh oh! You have no gags! I will assign you a task.'
QuestScript110_7 = 'Turn the page to see your tasks.'
QuestScript110_8 = 'Take a ride on the trolley, and earn jelly beans to buy gags!'
QuestScript110_9 = 'To get to the trolley, go out the door behind me and head for the playground.'
QuestScript110_10 = 'Now, close the book and find the trolley!'
QuestScript110_11 = 'Return to Toon HQ when you are done. Bye!'
QuestScriptTutorialBlocker_1 = 'Why, hello there!'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to use SpeedChat!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x07Where you are going there are many Toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with other Toons using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = "It's called the Chat button. You need to turn on Speedchat Plus in your Account Manager on the Toontown Web site to use it."
QuestScriptTutorialBlocker_8 = 'Good luck! See you later!'
QuestScriptGagShop_1 = 'Welcome to the Gag Shop!'
QuestScriptGagShop_1a = 'This is where Toons come to buy gags to use against the Cogs.'
QuestScriptGagShop_3 = 'To buy gags, click on the gag buttons. Try getting some now!'
QuestScriptGagShop_4 = 'Good! You can use these gags in battle against the Cogs.'
QuestScriptGagShop_5 = "Here's a peek at the advanced throw and squirt gags..."
QuestScriptGagShop_6 = "When you're done buying gags, click this button to return to the Playground."
QuestScriptGagShop_7 = 'Normally you can use this button to play another Trolley Game...'
QuestScriptGagShop_8 = "...but there's no time for another game right now. You're needed in Toon HQ!"
QuestScript120_1 = "Good job finding the trolley!\x07By the way, have you met Banker Bob?\x07He has quite a sweet tooth.\x07Why don't you introduce yourself by taking him this candy bar as a gift."
QuestScript120_2 = 'Banker Bob is over in the Toontown Bank.'
QuestScript121_1 = "Yum, thank you for the Candy Bar.\x07Say, if you can help me, I'll give you a reward.\x07Those Cogs stole the keys to my safe. Defeat Cogs to find a stolen key.\x07When you find a key, bring it back to me."
QuestScript130_1 = 'Good job finding the trolley!\x07By the way, I received a package for Professor Pete today.\x07It must be his new chalk he ordered.\x07Can you please take it to him?\x07He is over in the school house.'
QuestScript131_1 = 'Oh, thanks for the chalk.\x07What?!?\x07Those Cogs stole my blackboard. Defeat Cogs to find my stolen blackboard.\x07When you find it, bring it back to me.'
QuestScript140_1 = "Good job finding the trolley!\x07By the way, I have this friend, Librarian Larry, who is quite a book worm.\x07I picked this book up for him last time I was over in Donald's Dock.\x07Could you take it over to him?  He is usually in the Library."
QuestScript141_1 = 'Oh, yes, this book almost completes my collection.\x07Let me see...\x07Uh oh...\x07Now where did I put my glasses?\x07I had them just before those Cogs took over my building.\x07Defeat Cogs to find my stolen glasses.\x07When you find them, bring them back to me for a reward.'
QuestScript145_1 = 'I see you had no problem with the trolley!\x07Listen, the Cogs have stolen our blackboard eraser.\x07Go into the streets and fight Cogs until you recover the eraser.\x07To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x07Don't forget, if you need gags, ride the trolley.\x07Also, if you need to recover Laff points, collect ice cream cones in the Playground."
QuestScript150_1 = 'Great work!\x07Toontown is more fun when you have friends!'
QuestScript150_2 = 'To make friends, find another player, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'Chief Marketing Officer'
CashbotBossName = 'Chief Financial Officer'
LawbotBossName = 'Chief Justice'
BossbotBossName = 'Chief Executive Officer'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s.  Congratulations!'
BossCogDoobersAway = {'s': 'Go!  And make that sale!'}
BossCogWelcomeToons = 'Welcome, new Cogs!'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s.  Congratu--'
CagedToonInterruptBoss = 'Hey! Hiya! Hey over there!'
CagedToonRescueQuery = 'So, did you Toons come to rescue me?'
BossCogDiscoverToons = 'Huh?  Toons!  In disguise!'
BossCogAttackToons = 'Attack!!'
CagedToonPrepareBattleTwo = "Look out, he's trying to get away!\x07Help me, everyone--get up here and stop him!"
CagedToonPrepareBattleThree = "Hooray, I'm almost free!\x07Now you need to attack the C.M.O. Cog directly.\x07I've got a whole bunch of water balloons you can use!\x07Jump up and touch the bottom of my cage and I'll give you some water balloons.\x07Press the Delete key to throw water balloons once you've got them!"
BossBattleNeedMorePies = 'You need to get more water balloons!'
BossBattleHowToGetPies = 'Jump up to touch the cage to get water balloons.'
BossBattleHowToThrowPies = 'Press the Delete key to throw water balloons!'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "It's great to be free!\x07Thanks for all your help!\x07I am in your debt.\x07Here's my card. If you ever need a hand in battle, give a shout!\x07Just click on your SOS button."
CagedToonPromotion = "\x07Say, that C.M.O. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
CagedToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep rescuing Toons!"
CagedToonHPBoost = "\x07You've rescued a lot of Toons from this HQ.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
CagedToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'See ya!'
CagedToonBattleThree = {10: 'Nice jump, %(toon)s.  Here are some water balloons!',
 11: 'Hi, %(toon)s!  Have some water balloons!',
 12: "Hey there, %(toon)s!  You've got some water balloons now!",
 20: 'Hey, %(toon)s!  Jump up to my cage and get some pies to throw!',
 21: 'Hi, %(toon)s!  Use the Ctrl key to jump up and touch my cage!',
 22: "You can't attack the C.M.O. without any water balloons, %(toon)s!  Use the Ctrl key below my cage and I'll hand you some water balloons!",
 100: 'Press the Delete key to throw a water balloon.',
 101: 'The blue power meter shows how high your water balloon will go.',
 102: 'First try to lob a water balloon inside his undercarriage to soak up his works.',
 103: 'Wait for the door to open, and throw a water balloon straight inside.',
 104: "When he's dizzy, hit him in the face or chest to knock him back!",
 105: "You'll know you've got a good hit when you see the splat in color.",
 106: 'If you hit a Toon with a water balloon, it gives that Toon a Laff point!'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 22
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "That's it.  I've had enough of these pesky Toons!"
CashbotBossOuttaHere = "I've got a train to catch!"
ResistanceToonName = 'Mata Hairy'
ResistanceToonCongratulations = "You did it!  Congratulations!\x07You're an asset to the Resistance!\x07Here's a special phrase you can use in a tight spot:\x07%s\x07When you say it, %s.\x07But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full Laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their jellybean jars'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
ResistanceToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Get them!!!'
ResistanceToonWelcome = 'Hey, you made it!  Follow me to the main vault before the C.F.O. finds us!'
ResistanceToonTooLate = "Blast it!  We're too late!"
CashbotBossDiscoverToons1 = 'Ah-\x04HAH!'
CashbotBossDiscoverToons2 = 'I thought I smelled something a little toony in here!  Imposters!'
ResistanceToonKeepHimBusy = "Keep him busy!  I'm going to set a trap!"
ResistanceToonWatchThis = 'Watch this!'
CashbotBossGetAwayFromThat = 'Hey!  Get away from that!'
ResistanceToonCraneInstructions1 = 'Control a magnet by stepping up to a podium.'
ResistanceToonCraneInstructions2 = 'Use the arrow keys to move the crane, and press the Ctrl key to grab an object.'
ResistanceToonCraneInstructions3 = "Use Goons to hit the C.F.O.  When he's seeing stars, hit him with a safe!"
ResistanceToonCraneInstructions4 = "If he picks up a helmet, you won't be able to attack him.  You'll need another safe to knock it off."
ResistanceToonGetaway = 'Eek!  Gotta run!'
CashbotCraneLeave = 'Leave Crane'
CashbotCraneAdvice = 'Use the arrow keys to move the overhead crane.'
CashbotMagnetAdvice = 'Hold down the control key to pick things up.'
CashbotCraneLeaving = 'Leaving crane'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
NotYetAvailable = 'This elevator is not yet available.'
SellbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the C.M.O. to attack.\n\nYou won't earn merits or promotions, but you can rescue a Toon for an SOS reward!"
SellbotCogSuitNoMeritsMessage = "Your Sellbot Disguise will get you in, but since you don't have enough merits, you won't earn a promotion.\n\nIf you rescue the trapped Toon, you will earn an SOS Toon reward!"
SellbotCogSuitHasMeritsMessage = "It's Operation: Storm Sellbot!\n\nBring 5 or more Rental Suit Toons with you to defeat the C.M.O. and earn credit towards a reward!"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Fishing Pole'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
GardenTypeName = 'Garden Supplies'
RentalTypeName = 'Rental Item'
GardenStarterTypeName = 'Gardening Kit'
NametagTypeName = 'Name tag'
AccessoryTypeName = 'Accessory'
CatalogItemTypeNames = {0: 'INVALID_ITEM',
 1: FurnitureTypeName,
 2: ChatTypeName,
 3: ClothingTypeName,
 4: EmoteTypeName,
 5: 'WALLPAPER',
 6: 'Window View',
 7: 'FLOORING',
 8: 'MOULDING',
 9: 'WAINSCOTING',
 10: PoleTypeName,
 11: PetTrickTypeName,
 12: BeanTypeName,
 13: GardenTypeName,
 14: RentalTypeName,
 15: GardenStarterTypeName,
 16: NametagTypeName,
 17: 'TOON_STATUE',
 18: 'ANIMATED FURNITURE',
 19: AccessoryTypeName}
HatStylesDescriptions = {'hbb1': 'Green Baseball Cap',
 'hbb2': 'Blue Baseball Cap',
 'hbb3': 'Orange Baseball Cap',
 'hbb4': 'Yellow Baseball Cap',
 'hbb5': 'Red Baseball Cap',
 'hbb6': 'Aqua Baseball Cap',
 'hsf1': 'Beige Safari Hat',
 'hsf2': 'Brown Safari Hat',
 'hsf3': 'Green Safari Hat',
 'hrb1': 'Pink Bow',
 'hrb2': 'Red Bow',
 'hrb3': 'Purple Bow',
 'hrb4': 'Yellow Bow',
 'hrb5': 'Checker Bow',
 'hrb6': 'Light Red Bow',
 'hrb7': 'Rainbow Bow',
 'hht1': 'Pink Heart',
 'hht2': 'Yellow Heart',
 'htp1': 'Black Top Hat',
 'htp2': 'Blue Top Hat',
 'hav1': 'Anvil Hat',
 'hfp1': 'Flower Hat',
 'hsg1': 'Sandbag Hat',
 'hwt1': 'Weight Hat',
 'hfz1': 'Fez Hat',
 'hgf1': 'Golf Hat',
 'hpt1': 'Party Hat',
 'hpt2': 'Toon Party Hat',
 'hpb1': 'Fancy Hat',
 'hcr1': 'Crown',
 'hcw1': 'Cowboy Hat',
 'hpr1': 'Pirate Hat',
 'hpp1': 'Propeller Hat',
 'hfs1': 'Fishing Hat',
 'hsb1': 'Sombrero Hat',
 'hst1': 'Straw Hat',
 'hsu1': 'Sun Hat',
 'hat1': 'Antenna Thingy',
 'hhd1': 'Beehive Hairdo',
 'hbw1': 'Bowler Hat',
 'hch1': 'Chef Hat',
 'hdt1': 'Detective Hat',
 'hft1': 'Fancy Feathers Hat',
 'hfd1': 'Fedora',
 'hmk1': "Mickey's Band Hat",
 'hft2': 'Feather Headband',
 'hhd2': 'Pompadour Hairdo',
 'hpc1': 'Princess Hat',
 'hrh1': 'Archer Hat',
 'hhm1': 'Roman Helmet',
 'hat2': 'Spider Antenna Thingy',
 'htr1': 'Tiara',
 'hhm2': 'Viking Helmet',
 'hwz1': 'Witch Hat',
 'hwz2': 'Wizard Hat',
 'hhm3': 'Conquistador Helmet',
 'hhm4': 'Firefighter Helmet',
 'hfp2': 'Anti-Cog Control Hat',
 'hhm5': 'Miner Hat',
 'hnp1': 'Napoleon Hat',
 'hpc2': 'Pilot Cap',
 'hph1': 'Cop Hat',
 'hwg1': 'Rainbow Wacky Wig',
 'hsl1': 'Sailor Hat',
 'hfr1': 'Samba Hat',
 'hby1': 'Bobby Hat',
 'hrb8': 'Pink Dots Bow',
 'hjh1': 'Jester Hat',
 'hbb7': 'Purple Baseball Cap',
 'hrb9': 'Green Checker Bow',
 'hwt2': 'Winter Hat',
 'hhw1': 'Bandana',
 'hhw2': 'Toonosaur Hat',
 'hob1': 'Jamboree Hat',
 'hbn1': 'Bird Hat by Brianna',
 'hcb1': "Mad Matt's Hat"}
GlassesStylesDescriptions = {'grd1': 'Round Glasses',
 'gmb1': 'White Mini Blinds',
 'gnr1': 'Purple Narrow Glasses',
 'gst1': 'Yellow Star Glasses',
 'g3d1': 'Movie Glasses',
 'gav1': 'Aviator',
 'gce1': 'Cateye Glasses',
 'gdk1': 'Nerd Glasses',
 'gjo1': 'Celebrity Shades',
 'gsb1': 'Scuba Mask',
 'ggl1': 'Goggles',
 'ggm1': 'Groucho Glasses',
 'ghg1': 'Heart Glasses',
 'gie1': 'Bug Eye Glasses',
 'gmt1': 'Black Secret ID Mask',
 'gmt2': 'Blue Secret ID Mask',
 'gmt3': 'Blue Carnivale Mask',
 'gmt4': 'Purple Carnivale Mask',
 'gmt5': 'Aqua Carnivale Mask',
 'gmn1': 'Monocle',
 'gmo1': 'Smooch Glasses',
 'gsr1': 'Square Frame Glasses',
 'ghw1': 'Skull Eyepatch',
 'ghw2': 'Gem Eyepatch',
 'gag1': 'Alien Eyes by Alexandra',
 'gag2': 'Hypno-\x04Glasses'}
BackpackStylesDescriptions = {'bpb1': 'Blue Backpack',
 'bpb2': 'Orange Backpack',
 'bpb3': 'Purple BackPack',
 'bpd1': 'Red Dot Backpack',
 'bpd2': 'Yellow Dot Backpack',
 'bwg1': 'Bat Wings',
 'bwg2': 'Bee Wings',
 'bwg3': 'DragonFly Wings',
 'bst1': 'Scuba Tank',
 'bfn1': 'Shark Fin',
 'baw1': 'White Angel Wings',
 'baw2': 'Rainbow Angel Wings',
 'bwt1': 'Toys Backpack',
 'bwg4': 'Butterfly Wings',
 'bwg5': 'Pixie Wings',
 'bwg6': 'Dragon Wings',
 'bjp1': 'Jet Pack',
 'blg1': 'Bug Backpack',
 'bsa1': 'Plush Bear Pack',
 'bwg7': 'Bird wings',
 'bsa2': 'Plush Cat Pack',
 'bsa3': 'Plush Dog Pack',
 'bap1': 'Airplane Wings',
 'bhw1': 'Pirate Sword',
 'bhw2': 'Super Toon Cape',
 'bhw3': 'Vampire Cape',
 'bhw4': 'Toonosaur Backpack',
 'bob1': 'Jamboree Pack',
 'bfg1': 'Gag Attack Pack',
 'bfl1': 'Cog Pack by Savanah',
 'bfl2': 'Emergency Cream Pack'}
ShoesStylesDescriptions = {'sat1': 'Green Athletic Shoes',
 'sat2': 'Red Athletic Shoes',
 'smb1': 'Green Toon Boots',
 'scs1': 'Green Sneakers',
 'swt1': 'Wingtips',
 'smj1': 'Black Fancy Shoes',
 'sdk1': 'Boat Shoes',
 'sat3': 'Yellow Athletic Shoes',
 'scs2': 'Black Sneakers',
 'scs3': 'White Sneakers',
 'scs4': 'Pink Sneakers',
 'scb1': 'Cowboy Boots',
 'sfb1': 'Purple Boots',
 'sht1': 'Green Hi Top Sneakers',
 'smj2': 'Brown Fancy Shoes',
 'smj3': 'Red Fancy Shoes',
 'ssb1': 'Red Super Toon Boots',
 'sts1': 'Green Tennis Shoes',
 'sts2': 'Pink Tennis Shoes',
 'scs5': 'Red Sneakers',
 'smb2': 'Aqua Toon Boots',
 'smb3': 'Brown Toon Boots',
 'smb4': 'Yellow Toon Boots',
 'sfb2': 'Blue Square Boots',
 'sfb3': 'Green Hearts Boots',
 'sfb4': 'Grey Dots Boots',
 'sfb5': 'Orange Stars Boots',
 'sfb6': 'Pink Stars Boots',
 'slf1': 'Loafers',
 'smj4': 'Purple Fancy Shoes',
 'smt1': 'Motorcycle Boots',
 'sox1': 'Oxfords',
 'srb1': 'Pink Rain Boots',
 'sst1': 'Jolly Boots',
 'swb1': 'Beige Winter Boots',
 'swb2': 'Pink Winter Boots',
 'swk1': 'Work Boots',
 'scs6': 'Yellow Sneakers',
 'smb5': 'Pink Toon Boots',
 'sht2': 'Pink Hi Top Sneakers',
 'srb2': 'Red Dots Rain Boots',
 'sts3': 'Purple Tennis Shoes',
 'sts4': 'Violet Tennis Shoes',
 'sts5': 'Yellow Tennis Shoes',
 'srb3': 'Blue Rain Boots',
 'srb4': 'Yellow Rain Boots',
 'sat4': 'Black Athletic Shoes',
 'shw1': 'Pirate Shoes',
 'shw2': 'Toonosaur Feet'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'glasses unisex ',
 2: 'backpack unisex ',
 3: 'shoes unisex ',
 4: 'hat boy ',
 5: 'glasses boy ',
 6: 'backpack boy ',
 7: 'shoes boy ',
 8: 'hat girl ',
 9: 'glasses girl ',
 10: 'backpack girl ',
 11: 'shoes girl '}
AwardManagerAccessoryNames = {}
AccessoryTypeNames = {}
for accessoryId in CatalogAccessoryItemGlobals.AccessoryTypes.keys():
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    if accessoryInfo[3]:
        AwardManagerAccessoryNames[accessoryId] = AccessoryNamePrefix[accessoryInfo[0]] + accessoryStyleDescription[accessoryInfo[1]]
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

ShirtStylesDescriptions = {'bss1': 'solid',
 'bss2': 'single stripe',
 'bss3': 'collar',
 'bss4': 'double stripe',
 'bss5': 'multiple stripes',
 'bss6': 'collar w/ pocket',
 'bss7': 'hawaiian',
 'bss8': 'collar w/ 2 pockets',
 'bss9': 'bowling shirt',
 'bss10': 'vest (special)',
 'bss11': 'collar w/ ruffles',
 'bss12': 'soccer jersey (special)',
 'bss13': 'lightning bolt (special)',
 'bss14': 'jersey 19 (special)',
 'bss15': 'guayavera',
 'gss1': 'girl solid',
 'gss2': 'girl single stripe',
 'gss3': 'girl collar',
 'gss4': 'girl double stripes',
 'gss5': 'girl collar w/ pocket',
 'gss6': 'girl flower print',
 'gss7': 'girl flower trim (special)',
 'gss8': 'girl collar w/ 2 pockets',
 'gss9': 'girl denim vest (special)',
 'gss10': 'girl peasant',
 'gss11': 'girl peasant w/ mid stripe',
 'gss12': 'girl soccer jersey (special)',
 'gss13': 'girl hearts',
 'gss14': 'girl stars (special)',
 'gss15': 'girl flower',
 'c_ss1': 'yellow hooded - Series 1',
 'c_ss2': 'yellow with palm tree - Series 1',
 'c_ss3': 'purple with stars - Series 2',
 'c_bss1': 'blue stripes (boys only) - Series 1',
 'c_bss2': 'orange (boys only) - Series 1',
 'c_bss3': 'lime green with stripe (boys only) - Series 2',
 'c_bss4': 'red kimono with checkerboard (boys only) - Series 2',
 'c_gss1': 'girl blue with yellow stripes (girls only) - Series 1',
 'c_gss2': 'girl pink and beige with flower (girls only) - Series 1',
 'c_gss3': 'girl Blue and gold with wavy stripes (girls only) - Series 2',
 'c_gss4': 'girl Blue and pink with bow (girls only) - Series 2',
 'c_gss5': 'girl Aqua kimono white stripe (girls only) - UNUSED',
 'c_ss4': 'Tie dye shirt (boys and girls) - Series 3',
 'c_ss5': 'light blue with blue and white stripe (boys only) - Series 3',
 'c_ss6': 'cowboy shirt 1 : Series 4',
 'c_ss7': 'cowboy shirt 2 : Series 4',
 'c_ss8': 'cowboy shirt 3 : Series 4',
 'c_ss9': 'cowboy shirt 4 : Series 4',
 'c_ss10': 'cowboy shirt 5 : Series 4',
 'c_ss11': 'cowboy shirt 6 : Series 4',
 'hw_ss1': 'Halloween Ghost',
 'hw_ss2': 'Halloween Pumpkin',
 'hw_ss3': 'Halloween Vampire',
 'hw_ss4': 'Halloween Turtle',
 'hw_ss5': 'Halloween Bee',
 'hw_ss6': 'Halloween Pirate',
 'hw_ss7': 'Halloween SuperToon',
 'hw_ss8': 'Halloween Vampire NoCape',
 'hw_ss9': 'Halloween Dinosaur',
 'wh_ss1': 'Winter Holiday 1',
 'wh_ss2': 'Winter Holiday 2',
 'wh_ss3': 'Winter Holiday 3',
 'wh_ss4': 'Winter Holiday 4',
 'vd_ss1': 'girl Valentines day, pink with red hearts (girls)',
 'vd_ss2': 'Valentines day, red with white hearts',
 'vd_ss3': 'Valentines day, white with winged hearts (boys)',
 'vd_ss4': ' Valentines day, pink with red flamed heart',
 'vd_ss5': '2009 Valentines day, white with red cupid',
 'vd_ss6': '2009 Valentines day, blue with green and red hearts',
 'vd_ss7': '2010 Valentines day, red with white wings',
 'sd_ss1': "St Pat's Day, four leaf clover shirt",
 'sd_ss2': "St Pat's Day, pot o gold shirt",
 'sd_ss3': 'Ides of March greenToon shirt',
 'tc_ss1': 'T-Shirt Contest, Fishing Vest',
 'tc_ss2': 'T-Shirt Contest, Fish Bowl',
 'tc_ss3': 'T-Shirt Contest, Paw Print',
 'tc_ss4': 'T-Shirt Contest, Backpack',
 'tc_ss5': 'T-Shirt Contest, Lederhosen ',
 'tc_ss6': 'T-Shirt Contest, Watermelon  ',
 'tc_ss7': 'T-Shirt Contest, Race Shirt',
 'j4_ss1': 'July 4th, Flag',
 'j4_ss2': 'July 4th, Fireworks',
 'c_ss12': 'Catalog series 7, Green w/ yellow buttons',
 'c_ss13': 'Catalog series 7, Purple w/ big flower',
 'pj_ss1': 'Blue Banana Pajama shirt',
 'pj_ss2': 'Red Horn Pajama shirt',
 'pj_ss3': 'Purple Glasses Pajama shirt',
 'sa_ss1': 'Award Striped Shirt',
 'sa_ss2': 'Award Fishing Shirt 1',
 'sa_ss3': 'Award Fishing Shirt 2',
 'sa_ss4': 'Award Gardening Shirt 1',
 'sa_ss5': 'Award Gardening Shirt 2',
 'sa_ss6': 'Award Party Shirt 1',
 'sa_ss7': 'Award Party Shirt 2',
 'sa_ss8': 'Award Racing Shirt 1',
 'sa_ss9': 'Award Racing Shirt 2',
 'sa_ss10': 'Award Summer Shirt 1',
 'sa_ss11': 'Award Summer Shirt 2',
 'sa_ss12': 'Award Golf Shirt 1',
 'sa_ss13': 'Award Golf Shirt 2',
 'sa_ss14': 'Award Halloween Bee Shirt',
 'sa_ss15': 'Award Halloween SuperToon Shirt',
 'sa_ss16': 'Award Matathon Shirt 1',
 'sa_ss17': 'Award Save Building Shirt 1',
 'sa_ss18': 'Award Save Building Shirt 2',
 'sa_ss19': 'Award Toontask Shirt 1',
 'sa_ss20': 'Award Toontask Shirt 2',
 'sa_ss21': 'Award Trolley Shirt 1',
 'sa_ss22': 'Award Trolley Shirt 2',
 'sa_ss23': 'Award Winter Shirt 1',
 'sa_ss24': 'Award Halloween Skeleton Shirt',
 'sa_ss25': 'Award Halloween Spider Shirt',
 'sa_ss26': 'Award Most Cogs Defeated Shirt',
 'sa_ss27': 'Award Most V.P.s Defeated Shirt',
 'sa_ss28': 'Award Sellbot Smasher Shirt',
 'sa_ss29': 'Award Most C.J.s Defeated Shirt',
 'sa_ss30': 'Award Lawbot Smasher Shirt',
 'sa_ss31': 'Award Racing Shirt 3',
 'sa_ss32': 'Award Fishing Shirt 4',
 'sa_ss33': 'Award Golf Shirt 3',
 'sa_ss34': 'Award Most Cogs Defeated Shirt 2',
 'sa_ss35': 'Award Racing Shirt 4',
 'sa_ss36': 'Award Save Building Shirt 3',
 'sa_ss37': 'Award Trolley Shirt 3',
 'sa_ss38': 'Award Fishing Shirt 5',
 'sa_ss39': 'Award Golf Shirt 4',
 'sa_ss40': 'Award Halloween Witchy Moon Shirt',
 'sa_ss41': 'Award Winter Holiday Sled Shirt',
 'sa_ss42': 'Award Halloween Batty Moon Shirt',
 'sa_ss43': 'Award Winter Holiday Mittens Shirt',
 'sa_ss44': 'Award Fishing Shirt 6',
 'sa_ss45': 'Award Fishing Shirt 7',
 'sa_ss46': 'Award Golf Shirt 5',
 'sa_ss47': 'Award Racing Shirt 5',
 'sa_ss48': 'Award Racing Shirt 6',
 'sa_ss49': 'Award Most Cogs Defeated shirt 3',
 'sa_ss50': 'Award Most Cogs Defeated shirt 4',
 'sa_ss51': 'Award Trolley shirt 4',
 'sa_ss52': 'Award Trolley shirt 5',
 'sa_ss53': 'Award Save Building Shirt 4',
 'sa_ss54': 'Award Save Building Shirt 5',
 'sa_ss55': 'Award Anniversary',
 'sc_1': 'Scientist top 1',
 'sc_2': 'Scientist top 2',
 'sc_3': 'Scientist top 3',
 'sil_1': 'Silly Mailbox Shirt',
 'sil_2': 'Silly Trash Can Shirt',
 'sil_3': 'Loony Labs Shirt',
 'sil_4': 'Silly Hydrant Shirt',
 'sil_5': 'Sillymeter Whistle Shirt',
 'sil_6': 'Silly Cog-Crusher Shirt',
 'sil_7': 'Victory Party Shirt 1',
 'sil_8': 'Victory Party Shirt 2',
 'emb_us1': 'placeholder emblem shirt 1',
 'emb_us2': 'placeholder emblem shirt 2',
 'emb_us3': 'placeholder emblem shirt 3',
 'sb_1': 'Sellbot Icon Shirt',
 'lb_1': 'Lawbot Icon Shirt',
 'jb_1': 'Jellybean Shirt',
 'jb_2': 'Doodle Shirt',
 'ugcms': 'Get Connected Mover & Shaker',
 'spt1': 'Sellbot Shirt',
 'spt2': 'Cashbot Shirt',
 'spt3': 'Lawbot Shirt',
 'spt4': 'Bossbot Shirt'}
BottomStylesDescriptions = {'bbs1': 'plain w/ pockets',
 'bbs2': 'belt',
 'bbs3': 'cargo',
 'bbs4': 'hawaiian',
 'bbs5': 'side stripes (special)',
 'bbs6': 'soccer shorts',
 'bbs7': 'side flames (special)',
 'bbs8': 'denim',
 'vd_bs1': 'Valentines shorts',
 'vd_bs2': 'Green with red heart',
 'vd_bs3': 'Blue denim with green and red heart',
 'c_bs1': 'Orange with blue side stripes',
 'c_bs2': 'Blue with gold cuff stripes',
 'c_bs5': 'Green stripes - series 7',
 'sd_bs1': 'St. Pats leprechaun shorts',
 'sd_bs2': 'Ides of March greenToon shorts',
 'pj_bs1': 'Blue Banana Pajama pants',
 'pj_bs2': 'Red Horn Pajama pants',
 'pj_bs3': 'Purple Glasses Pajama pants',
 'wh_bs1': 'Winter Holiday Shorts Style 1',
 'wh_bs2': 'Winter Holiday Shorts Style 2',
 'wh_bs3': 'Winter Holiday Shorts Style 3',
 'wh_bs4': 'Winter Holiday Shorts Style 4',
 'hw_bs1': 'Halloween Bee Shorts male',
 'hw_bs2': 'Halloween Pirate Shorts male',
 'hw_bs5': 'Halloween SuperToon Shorts male',
 'hw_bs6': 'Halloween Vampire NoCape Shorts male',
 'hw_bs7': 'Halloween Dinosaur Shorts male',
 'sil_bs1': 'Silly Cog-Crusher Shorts',
 'gsk1': 'solid',
 'gsk2': 'polka dots (special)',
 'gsk3': 'vertical stripes',
 'gsk4': 'horizontal stripe',
 'gsk5': 'flower print',
 'gsk6': '2 pockets (special) ',
 'gsk7': 'denim skirt',
 'gsh1': 'plain w/ pockets',
 'gsh2': 'flower',
 'gsh3': 'denim shorts',
 'c_gsk1': 'blue skirt with tan border and button',
 'c_gsk2': 'purple skirt with pink and ribbon',
 'c_gsk3': 'teal skirt with yellow and star',
 'vd_gs1': 'red skirt with hearts',
 'vd_gs2': 'Pink flair skirt with polka hearts',
 'vd_gs3': 'Blue denim skirt with green and red heart',
 'c_gsk4': 'rainbow skirt - Series 3',
 'sd_gs1': 'St. Pats day shorts',
 'sd_gs2': 'Ides of March greenToon skirt',
 'c_gsk5': 'Western skirts 1',
 'c_gsk6': 'Western skirts 2',
 'c_bs3': 'Western shorts 1',
 'c_bs4': 'Western shorts 2',
 'j4_bs1': 'July 4th shorts',
 'j4_gs1': 'July 4th Skirt',
 'c_gsk7': 'Blue with flower - series 7',
 'pj_gs1': 'Blue Banana Pajama pants',
 'pj_gs2': 'Red Horn Pajama pants',
 'pj_gs3': 'Purple Glasses Pajama pants',
 'wh_gsk1': 'Winter Holiday Skirt Style 1',
 'wh_gsk2': 'Winter Holiday Skirt Style 2',
 'wh_gsk3': 'Winter Holiday Skirt Style 3',
 'wh_gsk4': 'Winter Holiday Skirt Style 4',
 'sa_bs1': 'Award Fishing Shorts',
 'sa_bs2': 'Award Gardening Shorts',
 'sa_bs3': 'Award Party Shorts',
 'sa_bs4': 'Award Racing Shorts',
 'sa_bs5': 'Award Summer Shorts',
 'sa_bs6': 'Award Golf Shorts 1',
 'sa_bs7': 'Award Halloween Bee Shorts',
 'sa_bs8': 'Award Halloween SuperToon Shorts',
 'sa_bs9': 'Award Save Building Shorts 1',
 'sa_bs10': 'Award Trolley Shorts 1',
 'sa_bs11': 'Award Halloween Spider Shorts',
 'sa_bs12': 'Award Halloween Skeleton Shorts',
 'sa_bs13': 'Award Sellbot Smasher Shorts male',
 'sa_bs14': 'Award Lawbot Smasher Shorts male',
 'sa_bs15': 'Award Racing Shorts 1',
 'sa_bs16': 'Award Golf Shorts 3',
 'sa_bs17': 'Award Racing Shorts 4',
 'sa_bs18': 'Award Golf Shorts 4',
 'sa_bs19': 'Award Golf Shorts 5',
 'sa_bs20': 'Award Racing Shorts 5',
 'sa_bs21': 'Award Racing Shorts 6',
 'sa_gs1': 'Award Fishing Skirt',
 'sa_gs2': 'Award Gardening Skirt',
 'sa_gs3': 'Award Party Skirt',
 'sa_gs4': 'Award Racing Skirt',
 'sa_gs5': 'Award Summer Skirt',
 'sa_gs6': 'Award Golf Skirt 1',
 'sa_gs7': 'Award Halloween Bee Skirt',
 'sa_gs8': 'Award Halloween SuperToon Skirt',
 'sa_gs9': 'Award Save Building Skirt 1',
 'sa_gs10': 'Award Trolley Skirt 1',
 'sa_gs11': 'Award Halloween Skeleton Skirt',
 'sa_gs12': 'Award Halloween Spider Skirt',
 'sa_gs13': 'Award Sellbot Smasher Shorts female',
 'sa_gs14': 'Award Lawbot Smasher Shorts female',
 'sa_gs15': 'Award Racing Skirt 1',
 'sa_gs16': 'Award Golf Skirt 2',
 'sa_gs17': 'Award Racing Skirt 4',
 'sa_gs18': 'Award Golf Skirt 3',
 'sa_gs19': 'Award Golf Skirt 4',
 'sa_gs20': 'Award Racing Skirt 5',
 'sa_gs21': 'Award Racing Skirt 6',
 'sc_bs1': 'Scientist bottom male 1',
 'sc_bs2': 'Scientist bottom male 2',
 'sc_bs3': 'Scientist bottom male 3',
 'sc_gs1': 'Scientist bottom female 1',
 'sc_gs2': 'Scientist bottom female 2',
 'sc_gs3': 'Scientist bottom female 3',
 'sil_bs1': 'Silly Cog-Crusher Shorts male',
 'sil_gs1': 'Silly Cog-Crusher Shorts female',
 'hw_bs3': 'Halloween Vampire Shorts male',
 'hw_gs3': 'Halloween Vampire Shorts female',
 'hw_bs4': 'Halloween Turtle Shorts male',
 'hw_gs4': 'Halloween Turtle Shorts female',
 'hw_gs1': 'Halloween Bee Shorts female',
 'hw_gs2': 'Halloween Pirate Shorts female',
 'hw_gs5': 'Halloween SuperToon Shorts female',
 'hw_gs6': 'Halloween Vampire NoCape Shorts female',
 'hw_gs7': 'Halloween Dinosaur Shorts female',
 'hw_gsk1': 'Halloween Pirate Skirt',
 'sbt1': 'Sellbot Shorts',
 'sbt2': 'Cashbot Shorts',
 'sbt3': 'Lawbot Shorts',
 'sbt4': 'Bossbot Shorts'}
AwardMgrBoy = 'boy'
AwardMgrGirl = 'girl'
AwardMgrUnisex = 'unisex'
AwardMgrShorts = 'shorts'
AwardMgrSkirt = 'skirt'
AwardMgrShirt = 'shirt'
SpecialEventMailboxStrings = {1: 'A special item from the Toon Council just for you!',
 2: "Here is your Melville's Fishing Tournament prize! Congratulations!",
 3: "Here is your Billy Budd's Fishing Tournament prize! Congratulations!",
 4: 'Here is your Acorn Acres April Invitational prize! Congratulations!',
 5: 'Here is your Acorn Acres C.U.P. Championship prize! Congratulations!',
 6: 'Here is your Gift-Giving Extravaganza prize! Congratulations!',
 7: "Here is your Top Toons New Year's Day Marathon prize! Congratulations!",
 8: 'Here is your Perfect Trolley Games Weekend prize! Congratulations!',
 9: 'Here is your Trolley Games Madness prize! Congratulations!',
 10: 'Here is your Grand Prix Weekend prize! Congratulations!',
 11: 'Here is your ToonTask Derby prize! Congratulations!',
 12: 'Here is your Save a Building Marathon prize! Congratulations!',
 13: 'Here is your Most Cogs Defeated Tournament prize! Congratulations!',
 14: 'Here is your Most V.P.s Defeated Tournament prize! Congratulations!',
 15: 'Here is your Operation: Storm Sellbot prize! Congratulations!',
 16: 'Here is your Most C.J.s Defeated Tournament prize! Congratulations!',
 17: 'Here is your Operation: Lawbots Lose prize! Congratulations!'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Game Table!'
EstateCannonGameEnd = 'The Cannon Game rental is over.'
GameTableRentalEnd = 'The Game Table rental is over.'
MessageConfirmRent = 'Begin rental? Cancel to save the rental for later'
MessageConfirmGarden = 'Are you sure you want to start a garden?'
NametagPaid = 'Citizen Name Tag'
NametagAction = 'Action Name Tag'
NametagFrilly = 'Frilly Name Tag'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
FurnitureYourOldTrunk = 'your old trunk'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Desk Chair',
 130: 'Log Chair',
 140: 'Lobster Chair',
 145: 'Lifejacket Chair',
 150: 'Saddle Stool',
 160: 'Native Chair',
 170: 'Cupcake Chair',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Round Fireplace',
 430: 'Fireplace',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace",
 460: "Erin's Lit Fireplace",
 470: 'Lit Fireplace',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplace',
 491: 'Lit Fireplace',
 492: 'Apple Lit Fireplace',
 500: 'Wardrobe',
 502: '15 item Wardrobe',
 504: '20 item Wardrobe',
 506: '25 item Wardrobe',
 508: '50 item Wardrobe',
 510: 'Wardrobe',
 512: '15 item Wardrobe',
 514: '20 item Wardrobe',
 516: '25 item Wardrobe',
 518: '50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp',
 625: 'Table Lamp',
 630: 'Daisy Lamp',
 640: 'Daisy Lamp',
 650: 'Jellyfish Lamp',
 660: 'Jellyfish Lamp',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair',
 705: 'Cushioned Chair',
 710: 'Couch',
 715: 'Couch',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan",
 1000: 'Large Rug',
 1010: 'Round Rug',
 1015: 'Round Rug',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet',
 1110: 'Display Cabinet',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table',
 1215: 'Small Table',
 1220: 'Coffee Table',
 1230: 'Coffee Table',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '1000 Bean Bank',
 1310: '2500 Bean Bank',
 1320: '5000 Bean Bank',
 1330: '7500 Bean Bank',
 1340: '10000 Bean Bank',
 1350: '12000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1600: 'Short Vase',
 1610: 'Tall Vase',
 1620: 'Short Vase',
 1630: 'Tall Vase',
 1640: 'Short Vase',
 1650: 'Short Vase',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl',
 1810: 'Fish Bowl',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
AwardManagerFurnitureNames = {100: 'Armchair A - Series 1',
 105: 'Armchair A - Series 7',
 110: 'Chair - Series 1',
 120: 'Desk Chair - Series 2',
 130: 'Log Chair - Series 2',
 140: 'Lobster Chair - Series 3',
 145: 'Lifejacket Chair - Series 3',
 150: 'Saddle Stool - Series 4',
 160: 'Native Chair - Series 4',
 170: 'Cupcake Chair - Series 6',
 200: "Bed Boy's bed - Initial Furniture",
 205: "Bed Boy's bed Series 7",
 210: "Bed Girl's bed - Series 1",
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed - Trolley Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace - Square Fireplace Initial Furniture',
 410: 'Fireplace - Girly Fireplace Series 1',
 420: 'Round Fireplace',
 430: 'Fireplace - bug room series 2',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace - coral",
 460: "Erin's Lit Fireplace - coral",
 470: 'Lit Fireplace - square fireplace with fire',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplac - girl fireplace with firee',
 491: 'Lit Fireplace - bug room fireplace',
 492: 'Apple Lit Fireplace',
 500: 'boy Wardrobe - 10 items initial',
 502: 'boy 15 item Wardrobe',
 504: 'boy 20 item Wardrobe',
 506: 'boy 25 item Wardrobe',
 508: 'boy 50 item Wardrobe',
 510: 'girl Wardrobe -  10 items initial',
 512: 'girl 15 item Wardrobe',
 514: 'girl 20 item Wardrobe',
 516: 'girl 25 item Wardrobe',
 518: 'girl 50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp - Series 1',
 625: 'Table Lamp - Series 7',
 630: 'Daisy Lamp 1',
 640: 'Daisy Lamp 2',
 650: 'Jellyfish Lamp 1',
 660: 'Jellyfish Lamp 2',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair - Series 1',
 705: 'Cushioned Chair - Series 7',
 710: 'Couch - series 1',
 715: 'Couch - series 7',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack - series 1',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack - underwater',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan - gag fan",
 1000: 'Large Rug',
 1010: 'Round Rug - Series 1',
 1015: 'Round Rug - Series 7',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet - Red',
 1110: 'Display Cabinet - Yellow',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table - series 1 ',
 1215: 'Small Table - series 7',
 1220: 'Coffee Table sq',
 1230: 'Coffee Table bw',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '1000 Bean Bank',
 1310: '2500 Bean Bank',
 1320: '5000 Bean Bank',
 1330: '7500 Bean Bank',
 1340: '10000 Bean Bank',
 1350: '12000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio A series 2',
 1510: 'Radio B series 1',
 1520: 'Radio C series 2',
 1530: 'Television',
 1600: 'Short Vase A',
 1610: 'Tall Vase A',
 1620: 'Short Vase B',
 1630: 'Tall Vase B',
 1640: 'Short Vase C',
 1650: 'Short Vase D',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl skull',
 1810: 'Fish Bowl lizard',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ghost Shirt',
 1002: 'Pumpkin Shirt',
 1112: 'Bee Shirt',
 1113: 'Pirate Shirt',
 1114: 'Super Toon Shirt',
 1115: 'Vampire Shirt',
 1116: 'Toonosaur Shirt',
 1117: 'Bee Shorts',
 1118: 'Pirate Shorts',
 1119: 'Super Toon Shorts',
 1120: 'Vampire Shorts',
 1121: 'Toonosaur Shorts',
 1122: 'Bee Shorts',
 1123: 'Pirate Shorts',
 1124: 'Super Toon Shorts',
 1125: 'Vampire Shorts',
 1126: 'Toonosaur Shorts',
 1127: 'Pirate Skirt',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Matthew's Shirt",
 1401: "Jessica's Shirt",
 1402: "Marissa's Shirt",
 1600: 'Trap Outfit',
 1601: 'Sound Outfit',
 1602: 'Lure Outfit',
 1603: 'Trap Outfit',
 1604: 'Sound Outfit',
 1605: 'Lure Outfit',
 1606: 'Trap Outfit',
 1607: 'Sound Outfit',
 1608: 'Lure Outfit',
 1723: 'Bee Shirt',
 1724: 'SuperToon Shirt',
 1734: 'Bee Shorts',
 1735: 'SuperToon Shorts',
 1739: 'Bee Skirt',
 1740: 'SuperToon Skirt',
 1743: 'Skeleton Shirt',
 1744: 'Spider Shirt',
 1745: 'Spider Shorts',
 1746: 'Skeleton Shorts',
 1747: 'Skeleton Skirt',
 1748: 'Spider Skirt',
 1749: 'Silly Mailbox Shirt',
 1750: 'Silly Trash Can Shirt',
 1751: 'Loony Labs Shirt',
 1752: 'Silly Hydrant Shirt',
 1753: 'Silly Meter Shirt',
 1754: 'Cog-Crusher Shirt',
 1755: 'Cog-Crusher Shorts',
 1756: 'Cog-Crusher Shorts',
 1757: 'Victory Party Shirt',
 1758: 'Relaxed Victory Shirt',
 1763: 'Smashed Sellbot Shirt',
 1764: 'Most V.P.s Defeated Shirt',
 1765: 'Sellbot Smasher Shirt',
 1766: 'Sellbot Smasher Shorts',
 1767: 'Sellbot Smasher Shorts',
 1768: 'Jellybean Bank Shirt',
 1769: 'Doodle Shirt',
 1770: 'Vampire Shirt',
 1771: 'Turtle Shirt',
 1772: 'Vampire Shorts',
 1773: 'Vampire Shorts',
 1774: 'Turtle Shorts',
 1775: 'Turtle Shorts',
 1776: 'Get Connected Mover & Shaker Shirt',
 1777: 'Smashed Lawbot Shirt',
 1778: 'Most C.J.s Defeated Shirt',
 1779: 'Lawbot Smasher Shirt',
 1780: 'Lawbot Smasher Shorts',
 1781: 'Lawbot Smasher Shorts',
 1782: 'Racing Shirt 3',
 1783: 'Racing Shorts 1',
 1784: 'Racing Skirt 1',
 1801: 'Batty Moon Shirt',
 1802: 'Mittens Shirt'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Spring Garden',
 2100: 'Formal Garden',
 2200: 'Race Day',
 2300: 'Touchdown!',
 2400: 'Cloud 9',
 2500: 'Climbing Vine',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Angel Fish',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Go Fish',
 3300: 'Stop Fish',
 3400: 'Sea Horse',
 3500: 'Sea Shells',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Cowboy Hat',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Hardwood Floor',
 1010: 'Carpet',
 1020: 'Diamond Tile',
 1030: 'Diamond Tile',
 1040: 'Grass',
 1050: 'Beige Bricks',
 1060: 'Red Bricks',
 1070: 'Square Tile',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Wood Tile',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Beach Tile',
 1160: 'Beach Tile',
 1170: 'Beach Tile',
 1180: 'Beach Tile',
 1190: 'Sand',
 10000: 'Ice Cube',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Winter Lights 1',
 1085: 'Winter Lights 2',
 1090: 'Winter Lights 3',
 1100: "ValenToon's Cupid",
 1110: "ValenToon's Heart 1",
 1120: "ValenToon's Heart 2"}
WainscotingNames = {1000: 'Painted',
 1010: 'Wood Panel',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Large Garden',
 20: 'Wild Garden',
 30: 'Greek Garden',
 40: 'Cityscape',
 50: 'Wild West',
 60: 'Under the Sea',
 70: 'Tropical Island',
 80: 'Starry Night',
 90: 'Tiki Pool',
 100: 'Frozen Frontier',
 110: 'Farm Country',
 120: 'Native Camp',
 130: 'Main Street'}
SpecialEventNames = {1: 'Generic Award',
 2: "Melville's Fishing Tournament",
 3: "Billy Budd's Fishing Tournament",
 4: 'Acorn Acres April Invitational',
 5: 'Acorn Acres C.U.P. Championship',
 6: 'Gift-Giving Extravaganza',
 7: "Top Toons New Year's Day Marathon",
 8: 'Perfect Trolley Games Weekend',
 9: 'Trolley Games Madness',
 10: 'Grand Prix Weekend',
 11: 'ToonTask Derby',
 12: 'Save a Building Marathon',
 13: 'Most Cogs Defeated',
 14: 'Most V.P.s Defeated',
 15: 'Operation Storm Sellbot Event',
 16: 'Most C.J.s Defeated',
 17: 'Operation Lawbots Lose Event'}
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has just arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived!  You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Your mailbox is empty right now.  Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way.  Check back later!'
DistributedMailboxReady = 'Your order has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
DistributedPhoneEmpty = "You can use any phone to order special items for you and your house.  New items will become available to order over time.\n\nYou don't have any items available to order right now, but check back later!"
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailBoxDiscard = 'Discard this item'
MailboxAcceptInvite = 'Accept this invite'
MailBoxRejectInvite = 'Reject this invite'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogLoyalty = 'SPECIAL'
CatalogEmblem = 'EMBLEM'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = ['Bye now!',
 'Call back soon!',
 'Thanks for calling!',
 'Ok, bye now!',
 'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogGiftFor = 'Buy Gift for:'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Stop Gifting'
CatalogGiftToggleOff = 'Buy Gifts'
CatalogGiftToggleWait = 'Trying!...'
CatalogGiftToggleNoAck = 'Unavailable'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase!  You can start using it right away.'
CatalogPurchaseGiftItemAvailable = 'Excellent!  %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full.  You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogPurchaseNoTrunk = 'In order to wear this item, you need to buy a trunk.\n\nDo you still want to purchase this item?'
CatalogPurchaseTrunkFull = 'Your trunk is full. If you purchase this item, you\xe2\x80\x99ll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full.  You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptNoTrunk = "You don't have a trunk. You must buy a trunk before you can take this item out of your mailbox."
CatalogAcceptTrunkFull = 'Your trunk is full.  You must delete something from your trunk before you can take this item out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptShorts = 'You are now wearing your new shorts.  What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptHat = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptGlasses = 'You are now wearing your new glasses.  The glasses you were wearing before have been moved to your trunk.'
CatalogAcceptBackpack = 'You are now wearing your new backpack.  The backpack you were wearing before has been moved to your trunk.'
CatalogAcceptShoes = 'You are now wearing your new shoes.  The shoes you were wearing before have been moved to your trunk.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogAcceptChat = 'You now have a new SpeedChat!'
CatalogAcceptEmote = 'You now have a new Emotion!'
CatalogAcceptBeans = 'You received some jelly beans!'
CatalogAcceptRATBeans = 'Your Toon recruit reward has arrived!'
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = 'Your new name tag has arrived!'
CatalogAcceptGarden = 'Your garden supplies have arrived!'
CatalogAcceptPet = 'You now have a new Pet Trick!'
CatalogPurchaseHouseFull = 'Your house is full.  You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full. You can not accept this item until you free up some room. Would you like to discard this item now?'
CatalogAcceptInAttic = 'Your new item is now in your attic.  You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic.  You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full!  You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full!  You can't purchase this item."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order.  You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they've already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "You don't have any place to put this. You'll have to get rid of something."
CatalogAcceptLimitError = "You already have as many of these as you can handle. You'll have to get rid of something."
CatalogAcceptFitError = "This won't fit you!"
CatalogAcceptInvalidError = 'This item has gone out of style!'
CatalogAcceptClosetError = 'You already have a bigger closet!'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full.  You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {'DoneMoving': 'Finish room decorating.',
 'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
 'Room': 'Show list of items in room. Useful for finding lost items.',
 'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
 'ZoomIn': 'Get a closer view of room.',
 'ZoomOut': 'Get a farther view of room.',
 'SendToAttic': 'Send the current furniture item to attic for storage.',
 'RotateLeft': 'Turn left.',
 'RotateRight': 'Turn right.',
 'DeleteEnter': 'Change to delete mode.',
 'DeleteExit': 'Exit delete mode.',
 'FurnitureItemPanelDelete': 'Send %s to trash.',
 'FurnitureItemPanelAttic': 'Place %s in room.',
 'FurnitureItemPanelRoom': 'Return %s to attic.',
 'FurnitureItemPanelTrash': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogCurrent = 'Current'
CatalogGiftedText = 'Gifted\nTo You'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'No Room'
CatalogNotAGift = 'Not a Gift'
CatalogNoFit = "Doesn't\nFit"
CatalogMembersOnly = 'Members\nOnly!'
CatalogSndOnText = 'Snd On'
CatalogSndOffText = 'Snd Off'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s jellybeans, %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s jellybeans and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s jellybeans and %(silver)s silver emblems?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver emblems?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold emblems?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogCurrentButtonText = 'To Current Items'
CatalogPastButtonText = 'To Past Items'
TutorialHQOfficerName = 'HQ Harry'
zone2TitleDict = {2513: ('Toon Hall', ''),
 2514: ('Toontown Bank', ''),
 2516: ('Toontown School House', ''),
 2518: ('Toontown Library', ''),
 2519: ('Gag Shop', ''),
 2520: ('Toon HQ', ''),
 2521: ('Clothing Shop', ''),
 2522: ('Pet Shop', ''),
 2601: ('All Smiles Tooth Repair', ''),
 2602: ('', ''),
 2603: ('One-Liner Miners', ''),
 2604: ('Hogwash & Dry', ''),
 2605: ('Toontown Sign Factory', ''),
 2606: ('', ''),
 2607: ('Jumping Beans', ''),
 2610: ('Dr. Tom Foolery', ''),
 2611: ('', ''),
 2616: ("Weird Beard's Disguise Shop", ''),
 2617: ('Silly Stunts', ''),
 2618: ('All That Razz', ''),
 2621: ('Paper Airplanes', ''),
 2624: ('Happy Hooligans', ''),
 2625: ('House of Bad Pies', ''),
 2626: ("Jesse's Joke Repair", ''),
 2629: ("The Laughin' Place", ''),
 2632: ('Clown Class', ''),
 2633: ('Tee-Hee Tea Shop', ''),
 2638: ('Toontown Playhouse', ''),
 2639: ('Monkey Tricks', ''),
 2643: ('Canned Bottles', ''),
 2644: ('Impractical Jokes', ''),
 2649: ('All Fun and Games Shop', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Laughing Lessons', ''),
 2655: ('Funny Money Savings & Loan', ''),
 2656: ('Used Clown Cars', ''),
 2657: ("Frank's Pranks", ''),
 2659: ('Joy Buzzers to the World', ''),
 2660: ('Tickle Machines', ''),
 2661: ('Daffy Taffy', ''),
 2662: ('Dr. I.M. Euphoric', ''),
 2663: ('Toontown Cinerama', ''),
 2664: ('The Merry Mimes', ''),
 2665: ("Mary's Go Around Travel Company", ''),
 2666: ('Laughing Gas Station', ''),
 2667: ('Happy Times', ''),
 2669: ("Muldoon's Maroon Balloons", ''),
 2670: ('Soup Forks', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Movie Multiplex', ''),
 2705: ("Wiseacre's Noisemakers", ''),
 2708: ('Blue Glue', ''),
 2711: ('Toontown Post Office', ''),
 2712: ('Chortle Cafe', ''),
 2713: ('Laughter Hours Cafe', ''),
 2714: ('Kooky CinePlex', ''),
 2716: ('Soup and Crack Ups', ''),
 2717: ('Bottled Cans', ''),
 2720: ('Crack Up Auto Repair', ''),
 2725: ('', ''),
 2727: ('Seltzer Bottles and Cans', ''),
 2728: ('Vanishing Cream', ''),
 2729: ('14 Karat Goldfish', ''),
 2730: ('News for the Amused', ''),
 2731: ('', ''),
 2732: ('Spaghetti and Goofballs', ''),
 2733: ('Cast Iron Kites', ''),
 2734: ('Suction Cups and Saucers', ''),
 2735: ('The Kaboomery', ''),
 2739: ("Sidesplitter's Mending", ''),
 2740: ('Used Firecrackers', ''),
 2741: ('', ''),
 2742: ('', ''),
 2743: ('', ''),
 2744: ('', ''),
 2747: ('Visible Ink', ''),
 2748: ('Jest for Laughs', ''),
 2801: ('Sofa Whoopee Cushions', ''),
 2802: ('Inflatable Wrecking Balls', ''),
 2803: ('The Karnival Kid', ''),
 2804: ('Dr. Pulyurleg, Chiropractor', ''),
 2805: ("The Professor's Circuit Circus", ''),
 2809: ('The Punch Line Gym', ''),
 2814: ('Toontown Theatre', ''),
 2818: ('The Flying Pie', ''),
 2821: ('', ''),
 2822: ('Rubber Chicken Sandwiches', ''),
 2823: ('Sundae Funnies Ice Cream', ''),
 2824: ('Punchline Movie Palace', ''),
 2829: ('Phony Baloney', ''),
 2830: ("Zippy's Zingers", ''),
 2831: ("Professor Wiggle's House of Giggles", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Funny Bone Emergency Room', ''),
 2836: ('', ''),
 2837: ('Hardy Harr Seminars', ''),
 2839: ('Barely Palatable Pasta', ''),
 2841: ("Daphne's Hideout", ''),
 1506: ('Gag Shop', ''),
 1507: ('Toon Headquarters', ''),
 1508: ('Clothing Shop', ''),
 1510: ('', ''),
 1602: ('Used Life Preservers', ''),
 1604: ('Wet Suit Dry Cleaners', ''),
 1606: ("Hook's Clock Repair", ''),
 1608: ("Luff 'N Stuff", ''),
 1609: ('Every Little Bait', ''),
 1612: ('Dime & Quarterdeck Bank', ''),
 1613: ('Squid Pro Quo, Attorneys at Law', ''),
 1614: ('Trim the Nail Boutique', ''),
 1615: ("Yacht's All, Folks!", ''),
 1616: ("Blackbeard's Beauty Parlor", ''),
 1617: ('Out to See Optics', ''),
 1619: ('Disembark! Tree Surgeons', ''),
 1620: ('From Fore to Aft', ''),
 1621: ('Poop Deck Gym', ''),
 1622: ('Bait and Switches Electrical Shop', ''),
 1624: ('Soles Repaired While U Wait', ''),
 1626: ('Salmon Chanted Evening Formal Wear', ''),
 1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
 1628: ('Piano Tuna', ''),
 1629: ('', ''),
 1701: ('Buoys and Gulls Nursery School', ''),
 1703: ('Wok the Plank Chinese Food', ''),
 1705: ('Sails for Sale', ''),
 1706: ('Peanut Butter and Jellyfish', ''),
 1707: ('Gifts With a Porpoise', ''),
 1709: ('Windjammers and Jellies', ''),
 1710: ('Barnacle Bargains', ''),
 1711: ('Deep Sea Diner', ''),
 1712: ('Able-Bodied Gym', ''),
 1713: ("Art's Smart Chart Mart", ''),
 1714: ("Reel 'Em Inn", ''),
 1716: ('Mermaid Swimwear', ''),
 1717: ('Be More Pacific Ocean Notions', ''),
 1718: ('Run Aground Taxi Service', ''),
 1719: ("Duck's Back Water Company", ''),
 1720: ('The Reel Deal', ''),
 1721: ('All For Nautical', ''),
 1723: ("Squid's Seaweed", ''),
 1724: ("That's  a Moray!", ''),
 1725: ("Ahab's Prefab Sea Crab Center", ''),
 1726: ('Root Beer Afloats', ''),
 1727: ('This Oar That', ''),
 1728: ('Good Luck Horseshoe Crabs', ''),
 1729: ('', ''),
 1802: ('Nautical But Nice', ''),
 1804: ('Mussel Beach Gymnasium', ''),
 1805: ('Tackle Box Lunches', ''),
 1806: ('Cap Size Hat Store', ''),
 1807: ('Keel Deals', ''),
 1808: ('Knots So Fast', ''),
 1809: ('Rusty Buckets', ''),
 1810: ('Anchor Management', ''),
 1811: ("What's Canoe With You?", ''),
 1813: ('Pier Pressure Plumbing', ''),
 1814: ('The Yo Ho Stop and Go', ''),
 1815: ("What's Up, Dock?", ''),
 1818: ('Seven Seas Cafe', ''),
 1819: ("Docker's Diner", ''),
 1820: ('Hook, Line, and Sinker Prank Shop', ''),
 1821: ("King Neptoon's Cannery", ''),
 1823: ('The Clam Bake Diner', ''),
 1824: ('Dog Paddles', ''),
 1825: ('Wholly Mackerel! Fish Market', ''),
 1826: ("Claggart's Clever Clovis Closet", ''),
 1828: ("Alice's Ballast Palace", ''),
 1829: ('Seagull Statue Store', ''),
 1830: ('Lost and Flounder', ''),
 1831: ('Kelp Around the House', ''),
 1832: ("Melville's Massive Mizzenmast Mart", ''),
 1833: ('This Transom Man Custom Tailored Suits', ''),
 1834: ('Rudderly Ridiculous!', ''),
 1835: ('', ''),
 4503: ('Gag Shop', ''),
 4504: ('Toon Headquarters', ''),
 4506: ('Clothing Shop', ''),
 4508: ('', ''),
 4603: ("Tom-Tom's Drums", ''),
 4604: ('In Four-Four Time', ''),
 4605: ("Fifi's Fiddles", ''),
 4606: ('Casa De Castanets', ''),
 4607: ('Catchy Toon Apparel', ''),
 4609: ('Do, Rae, Me Piano Keys', ''),
 4610: ('Please Refrain', ''),
 4611: ('Tuning Forks and Spoons', ''),
 4612: ("Dr. Fret's Dentistry", ''),
 4614: ('Shave and a Haircut for a Song', ''),
 4615: ("Piccolo's Pizza", ''),
 4617: ('Happy Mandolins', ''),
 4618: ('Rests Rooms', ''),
 4619: ('More Scores', ''),
 4622: ('Chin Rest Pillows', ''),
 4623: ('Flats Sharpened', ''),
 4625: ('Tuba Toothpaste', ''),
 4626: ('Notations', ''),
 4628: ('Accidental Insurance', ''),
 4629: ("Riff's Paper Plates", ''),
 4630: ('Music Is Our Forte', ''),
 4631: ('Canto Help You', ''),
 4632: ('Dance Around the Clock Shop', ''),
 4635: ('Tenor Times', ''),
 4637: ('For Good Measure', ''),
 4638: ('Hard Rock Shop', ''),
 4639: ('Four Score Antiques', ''),
 4641: ('Blues News', ''),
 4642: ('Ragtime Dry Cleaners', ''),
 4645: ('Club 88', ''),
 4646: ('', ''),
 4648: ('Carry a Toon Movers', ''),
 4649: ('', ''),
 4652: ('Full Stop Shop', ''),
 4653: ('', ''),
 4654: ('Pitch Perfect Roofing', ''),
 4655: ("The Treble Chef's Cooking School", ''),
 4656: ('', ''),
 4657: ('Barbershop Quartet', ''),
 4658: ('Plummeting Pianos', ''),
 4659: ('', ''),
 4701: ('The Schmaltzy Waltz School of Dance', ''),
 4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
 4703: ('I Can Handel It!', ''),
 4704: ("Tina's Concertina Concerts", ''),
 4705: ('Zither Here Nor There', ''),
 4707: ("Doppler's Sound Effects Studio", ''),
 4709: ('On Ballet! Climbing Supplies', ''),
 4710: ('Hurry Up, Slow Polka! School of Driving', ''),
 4712: ('C-Flat Tire Repair', ''),
 4713: ('B-Sharp Fine Menswear', ''),
 4716: ('Four-Part Harmonicas', ''),
 4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
 4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
 4719: ('Madrigal Motor Homes', ''),
 4720: ('Name That Toon', ''),
 4722: ('Overture Understudies', ''),
 4723: ('Haydn Go Seek Playground Supplies', ''),
 4724: ('White Noise for Girls and Boys', ''),
 4725: ('The Baritone Barber', ''),
 4727: ('Vocal Chords Braided', ''),
 4728: ("Sing Solo We Can't Hear You", ''),
 4729: ('Double Reed Bookstore', ''),
 4730: ('Lousy Lyrics', ''),
 4731: ('Toon Tunes', ''),
 4732: ('Etude, Brute? Shakespearian Theatre Company', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Accordions, If You Want In, Just Bellow!', ''),
 4736: ('Her and Hymn Wedding Planners', ''),
 4737: ('Harp Tarps', ''),
 4738: ('Canticle Your Fancy Gift Shop', ''),
 4739: ('', ''),
 4801: ("Marshall's Stacks", ''),
 4803: ('What a Mezzo! Maid Service', ''),
 4804: ('Mixolydian Scales', ''),
 4807: ('Relax the Bach', ''),
 4809: ("I Can't Understanza!", ''),
 4812: ('', ''),
 4817: ('The Ternary Pet Shop', ''),
 4819: ("Yuki's Ukeleles", ''),
 4820: ('', ''),
 4821: ("Anna's Cruises", ''),
 4827: ('Common Time Watches', ''),
 4828: ("Schumann's Shoes for Men", ''),
 4829: ("Pachelbel's Canonballs", ''),
 4835: ('Ursatz for Kool Katz', ''),
 4836: ('Reggae Regalia', ''),
 4838: ('Kazoology School of Music', ''),
 4840: ('Coda Pop Musical Beverages', ''),
 4841: ('Lyre, Lyre, Pants on Fire!', ''),
 4842: ('The Syncopation Corporation', ''),
 4843: ('', ''),
 4844: ('Con Moto Cycles', ''),
 4845: ("Ellie's Elegant Elegies", ''),
 4848: ('Lotsa Lute Savings & Loan', ''),
 4849: ('', ''),
 4850: ('The Borrowed Chord Pawn Shop', ''),
 4852: ('Flowery Flute Fleeces', ''),
 4853: ("Leo's Fenders", ''),
 4854: ("Wagner's Vocational Violin Videos", ''),
 4855: ('The Teli-Caster Network', ''),
 4856: ('', ''),
 4862: ("Quentin's Quintessen\x03tial Quadrilles", ''),
 4867: ("Mr. Costello's Yellow Cellos", ''),
 4868: ('Gag Shop', ''),
 4870: ("Ziggy's Zoo of Zigeuner\x03musik", ''),
 4871: ("Harry's House of Harmonious Humbuckers", ''),
 4872: ("Fast Freddie's Fretless Fingerboards", ''),
 4873: ('', ''),
 5501: ('Gag Shop', ''),
 5502: (lToonHQ, ''),
 5503: ('Clothing Shop', ''),
 5505: ('', ''),
 5601: ('Eye of the Potato Optometry', ''),
 5602: ("Artie Choke's Neckties", ''),
 5603: ('Lettuce Alone', ''),
 5604: ('Cantaloupe Bridal Shop', ''),
 5605: ('Vege-tables and Chairs', ''),
 5606: ('Petals', ''),
 5607: ('Compost Office', ''),
 5608: ('Mom and Pop Corn', ''),
 5609: ('Berried Treasure', ''),
 5610: ("Black-eyed Susan's Boxing Lessons", ''),
 5611: ("Gopher's Gags", ''),
 5613: ('Crop Top Barbers', ''),
 5615: ("Bud's Bird Seed", ''),
 5616: ('Dew Drop Inn', ''),
 5617: ("Flutterby's Butterflies", ''),
 5618: ("Peas and Q's", ''),
 5619: ("Jack's Beanstalks", ''),
 5620: ('Rake It Inn', ''),
 5621: ('Grape Expectations', ''),
 5622: ('Petal Pusher Bicycles', ''),
 5623: ('Bubble Bird Baths', ''),
 5624: ("Mum's the Word", ''),
 5625: ('Leaf It Bees', ''),
 5626: ('Pine Needle Crafts', ''),
 5627: ('', ''),
 5701: ('From Start to Spinach', ''),
 5702: ("Jake's Rakes", ''),
 5703: ("Photo Cynthia's Camera Shop", ''),
 5704: ('Lisa Lemon Used Cars', ''),
 5705: ('Poison Oak Furniture', ''),
 5706: ('14 Carrot Jewelers', ''),
 5707: ('Musical Fruit', ''),
 5708: ("We'd Be Gone Travel Agency", ''),
 5709: ('Astroturf Mowers', ''),
 5710: ('Tuft Guy Gym', ''),
 5711: ('Garden Hosiery', ''),
 5712: ('Silly Statues', ''),
 5713: ('Trowels and Tribulations', ''),
 5714: ('Spring Rain Seltzer Bottles', ''),
 5715: ('Hayseed News', ''),
 5716: ('Take It or Leaf It Pawn Shop', ''),
 5717: ('The Squirting Flower', ''),
 5718: ('The Dandy Lion Exotic Pets', ''),
 5719: ('Trellis the Truth! Private Investi\x03gators', ''),
 5720: ('Vine and Dandy Menswear', ''),
 5721: ('Root 66 Diner', ''),
 5725: ('Barley, Hops, and Malt Shop', ''),
 5726: ("Bert's Dirt", ''),
 5727: ('Gopher Broke Savings & Loan', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Just Vase It', ''),
 5805: ('Snail Mail', ''),
 5809: ('Fungi Clown School', ''),
 5810: ('Honeydew This', ''),
 5811: ('Lettuce Inn', ''),
 5815: ('Grass Roots', ''),
 5817: ('Apples and Oranges', ''),
 5819: ('Green Bean Jeans', ''),
 5821: ('Squash and Stretch Gym', ''),
 5826: ('Ant Farming Supplies', ''),
 5827: ('Dirt. Cheap.', ''),
 5828: ('Couch Potato Furniture', ''),
 5830: ('Spill the Beans', ''),
 5833: ('The Salad Bar', ''),
 5835: ('Flower Bed and Breakfast', ''),
 5836: ("April's Showers and Tubs", ''),
 5837: ('School of Vine Arts', ''),
 9501: ('Lullaby Library', ''),
 9503: ('The Snooze Bar', ''),
 9504: ('Gag Shop', ''),
 9505: (lToonHQ, ''),
 9506: ('Clothing Shop', ''),
 9508: ('', ''),
 9601: ('Snuggle Inn', ''),
 9602: ('Forty Winks for the Price of Twenty', ''),
 9604: ("Ed's Red Bed Spreads", ''),
 9605: ('Cloud Nine Design', ''),
 9607: ("Big Mama's Bahama Pajamas", ''),
 9608: ('Cat Nip for Cat Naps', ''),
 9609: ('Deep Sleep for Cheap', ''),
 9613: ('Clock Cleaners', ''),
 9616: ('Lights Out Electric Co.', ''),
 9617: ('Crib Notes - Music to Sleep By', ''),
 9619: ('Relax to the Max', ''),
 9620: ("PJ's Taxi Service", ''),
 9622: ('Sleepy Time Pieces', ''),
 9625: ('Curl Up Beauty Parlor', ''),
 9626: ('Bed Time Stories', ''),
 9627: ('The Sleepy Teepee', ''),
 9628: ('Call It a Day Calendars', ''),
 9629: ('Silver Lining Jewelers', ''),
 9630: ('Rock to Sleep Quarry', ''),
 9631: ('Down Time Watch Repair', ''),
 9633: ('The Dreamland Screening Room', ''),
 9634: ('Mind Over Mattress', ''),
 9636: ('Insomniac Insurance', ''),
 9639: ('House of Hibernation', ''),
 9640: ('Nightstand Furniture Company', ''),
 9642: ('Sawing Wood Slumber Lumber', ''),
 9643: ('Shut-Eye Optometry', ''),
 9644: ('Pillow Fights Nightly', ''),
 9645: ('The All Tucked Inn', ''),
 9647: ('Make Your Bed! Hardware Store', ''),
 9649: ('Snore or Less', ''),
 9650: ('Crack of Dawn Repairs', ''),
 9651: ('For Richer or Snorer', ''),
 9652: ('', ''),
 9703: ('Fly By Night Travel Agency', ''),
 9704: ('Night Owl Pet Shop', ''),
 9705: ('Asleep At The Wheel Car Repair', ''),
 9706: ('Tooth Fairy Dentistry', ''),
 9707: ("Dawn's Yawn & Garden Center", ''),
 9708: ('Bed Of Roses Florist', ''),
 9709: ('Pipe Dream Plumbers', ''),
 9710: ('REM Optometry', ''),
 9711: ('Wake-Up Call Phone Company', ''),
 9712: ("Counting Sheep - So You Don't Have To!", ''),
 9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
 9714: ('Dreamboat Marine Supply', ''),
 9715: ('First Security Blanket Bank', ''),
 9716: ('Wet Blanket Party Planners', ''),
 9717: ("Baker's Dozin' Doughnuts", ''),
 9718: ("Sandman's Sandwiches", ''),
 9719: ('Armadillo Pillow Company', ''),
 9720: ('Talking In Your Sleep Voice Training', ''),
 9721: ('Snug As A Bug Rug Dealer', ''),
 9722: ('Dream On Talent Agency', ''),
 9725: ("Cat's Pajamas", ''),
 9727: ('You Snooze, You Lose', ''),
 9736: ('Dream Jobs Employment Agency', ''),
 9737: ("Waltzing Matilda's Dance School", ''),
 9738: ('House of Zzzzzs', ''),
 9740: ('Hit The Sack Fencing School', ''),
 9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
 9744: ("Rip Van Winkle's Wrinkle Cream", ''),
 9752: ('Midnight Oil & Gas Company', ''),
 9753: ("Moonbeam's Ice Creams", ''),
 9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
 9755: ('Bedknobs & Broomsticks Movie House', ''),
 9756: ('', ''),
 9759: ('Sleeping Beauty Parlor', ''),
 3507: ('Gag Shop', ''),
 3508: (lToonHQ, ''),
 3509: ('Clothing Shop', ''),
 3511: ('', ''),
 3601: ('Northern Lights Electric Company', ''),
 3602: ("Nor'easter Bonnets", ''),
 3605: ('', ''),
 3607: ('The Blizzard Wizard', ''),
 3608: ('Nothing to Luge', ''),
 3610: ("Mike's Massive Mukluk Mart", ''),
 3611: ("Mr. Cow's Snow Plows", ''),
 3612: ('Igloo Design', ''),
 3613: ('Ice Cycle Bikes', ''),
 3614: ('Snowflakes Cereal Company', ''),
 3615: ('Fried Baked Alaskas', ''),
 3617: ('Cold Air Balloon Rides', ''),
 3618: ('Snow Big Deal! Crisis Management', ''),
 3620: ('Skiing Clinic', ''),
 3621: ('The Melting Ice Cream Bar', ''),
 3622: ('', ''),
 3623: ('The Mostly Toasty Bread Company', ''),
 3624: ('Subzero Sandwich Shop', ''),
 3625: ("Auntie Freeze's Radiator Supply", ''),
 3627: ('St. Bernard Kennel Club', ''),
 3629: ('Pea Soup Cafe', ''),
 3630: ('Icy London, Icy France Travel Agency', ''),
 3634: ('Easy Chair Lifts', ''),
 3635: ('Used Firewood', ''),
 3636: ('Affordable Goosebumps', ''),
 3637: ("Kate's Skates", ''),
 3638: ('Toboggan or Not Toboggan', ''),
 3641: ("Fred's Red Sled Beds", ''),
 3642: ('Eye of the Storm Optics', ''),
 3643: ('Snowball Hall', ''),
 3644: ('Melted Ice Cubes', ''),
 3647: ('The Sanguine Penguin Tuxedo Shop', ''),
 3648: ('Instant Ice', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('Antarctic Antiques', ''),
 3651: ("Frosty Freddy's Frozen Frankfurters", ''),
 3653: ('Ice House Jewelry', ''),
 3654: ('', ''),
 3702: ('Winter Storage', ''),
 3703: ('', ''),
 3705: ('Icicles Built for Two', ''),
 3706: ("Shiverin' Shakes Malt Shop", ''),
 3707: ('Snowplace Like Home', ''),
 3708: ("Pluto's Place", ''),
 3710: ('Dropping Degrees Diner', ''),
 3711: ('', ''),
 3712: ('Go With the Floe', ''),
 3713: ('Chattering Teeth, Subzero Dentist', ''),
 3715: ("Aunt Arctic's Soup Shop", ''),
 3716: ('Road Salt and Pepper', ''),
 3717: ('Juneau What I Mean?', ''),
 3718: ('Designer Inner Tubes', ''),
 3719: ('Ice Cube on a Stick', ''),
 3721: ("Noggin's Toboggan Bargains", ''),
 3722: ('Snow Bunny Ski Shop', ''),
 3723: ("Shakey's Snow Globes", ''),
 3724: ('The Chattering Chronicle', ''),
 3725: ('You Sleigh Me', ''),
 3726: ('Solar Powered Blankets', ''),
 3728: ('Lowbrow Snowplows', ''),
 3729: ('', ''),
 3730: ('Snowmen Bought & Sold', ''),
 3731: ('Portable Fireplaces', ''),
 3732: ('The Frozen Nose', ''),
 3734: ('Icy Fine, Do You? Optometry', ''),
 3735: ('Polar Ice Caps', ''),
 3736: ('Diced Ice at a Nice Price', ''),
 3737: ('Downhill Diner', ''),
 3738: ("Heat-Get It While It's Hot", ''),
 3739: ('', ''),
 3801: ('Toon HQ', ''),
 3806: ('Alpine Chow Line', ''),
 3807: ('Used Groundhog Shadows', ''),
 3808: ('The Sweater Lodge', ''),
 3809: ('Ice Saw It Too', ''),
 3810: ('A Better Built Quilt', ''),
 3811: ('Your Snow Angel', ''),
 3812: ('Mittens for Kittens', ''),
 3813: ("Snowshoes You Can't Refuse", ''),
 3814: ('Malt in Your Mouth Soda Fountain', ''),
 3815: ('The Toupee Chalet', ''),
 3816: ('Just So Mistletoe', ''),
 3817: ('Winter Wonderland Walking Club', ''),
 3818: ('The Shovel Hovel', ''),
 3819: ('Clean Sweep Chimney Service', ''),
 3820: ('Snow Whitening', ''),
 3821: ('Hibernation Vacations', ''),
 3823: ('Precipitation Foundation', ''),
 3824: ('Open Fire Chestnut Roasting', ''),
 3825: ('Cool Cat Hats', ''),
 3826: ('Oh My Galoshes!', ''),
 3827: ('Choral Wreaths', ''),
 3828: ("Snowman's Land", ''),
 3829: ('Pinecone Zone', ''),
 3830: ('Wait and See Goggle Defogging', '')}
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "This isn't your trunk, but you may try on the accessories."
TrunkNotPaidMessage = 'Only Paid Members can wear accessories, but you may try them on.'
TrunkAreYouSureMessage = 'You have deleted some accessories.  Do you really want to delete them?'
TrunkHat = 'this hat'
TrunkGlasses = 'these glasses'
TrunkBackpack = 'this backpack'
TrunkShoes = 'these shoes'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'Delete\nbackpack'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
EstateTargetGameStart = 'The Toon-up Target game has started!'
EstateTargetGameInst = "The more you hit the red target, the more you'll get Tooned up."
EstateTargetGameEnd = 'The Toon-up Target game is now over...'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s jellybeans. Do you want to sell them all?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Sell All'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Always Hungry',
                     'Often Hungry',
                     'Sometimes Hungry',
                     'Rarely Hungry'),
 'boredomThreshold': ('Always Bored',
                      'Often Bored',
                      'Sometimes Bored',
                      'Rarely Bored'),
 'angerThreshold': ('Always Grumpy',
                    'Often Grumpy',
                    'Sometimes Grumpy',
                    'Rarely Grumpy'),
 'forgetfulness': ('Always Forgets',
                   'Often Forgets',
                   'Sometimes Forgets',
                   'Rarely Forgets'),
 'excitementThreshold': ('Very Calm',
                         'Pretty Calm',
                         'Pretty Excitable',
                         'Very Excitable'),
 'sadnessThreshold': ('Always Sad',
                      'Often Sad',
                      'Sometimes Sad',
                      'Rarely Sad'),
 'restlessnessThreshold': ('Always Restless',
                           'Often Restless',
                           'Sometimes Restless',
                           'Rarely Restless'),
 'playfulnessThreshold': ('Rarely Playful',
                          'Sometimes Playful',
                          'Often Playful',
                          'Always Playful'),
 'lonelinessThreshold': ('Always Lonely',
                         'Often Lonely',
                         'Sometimes Lonely',
                         'Rarely Lonely'),
 'fatigueThreshold': ('Always Tired',
                      'Often Tired',
                      'Sometimes Tired',
                      'Rarely Tired'),
 'confusionThreshold': ('Always Confused',
                        'Often Confused',
                        'Sometimes Confused',
                        'Rarely Confused'),
 'surpriseThreshold': ('Always Surprised',
                       'Often Surprised',
                       'Sometimes Surprised',
                       'Rarely Surprised'),
 'affectionThreshold': ('Rarely Affectionate',
                        'Sometimes Affectionate',
                        'Often Affectionate',
                        'Always Affectionate'),
 'loyaltyThreshold': ('Rarely Loyal',
                      'Sometimes Loyal',
                      'Often Loyal',
                      'Always Loyal')}
FireworksInstructions = lToonHQ + ': Hit the "Page Up" key to see the show!'
startFireworksResponse = "Usage: startFireworksShow ['num']\n                                         'num' = %s - New Years\n                                         %s - Party Summer \n                                         %s - 4th of July"
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = lToonHQ + ': Happy New Year! Enjoy the fireworks show!'
FireworksNewYearsEveEnding = lToonHQ + ': Hope you enjoyed the show! Happy New Year!'
FireworksComboBeginning = lToonHQ + ': Enjoy lots of Laffs with Toon fireworks!'
FireworksComboEnding = lToonHQ + ': Thank you, Toons! Hope you enjoyed the show!'
BlockerTitle = 'LOADING TOONTOWN...'
BlockerLoadingTexts = ['Scrubbing pie tins',
 'Baking pie crusts',
 'Heating pie filling',
 'Loading Doodle chow',
 'Stringing Jungle Vines',
 'Uncaging those spiders who crawl down jungle vines',
 'Planting squirting flower seeds',
 'Stretching trampolines',
 'Herding pigs',
 'Tweaking "SPLAT" sounds',
 'Cleaning Hypno-glasses',
 'Unbottling ink for Toon News',
 'Clipping TNT fuses',
 "Setting up 'Under Construction' sign in Acorn Acres",
 'Waking Donald Duck',
 'Teaching new moves to dancing fire hydrants',
 'Binding Shticker Books',
 'Analyzing quacks',
 'Harvesting jellybean pods',
 'Emptying fish buckets',
 'Corralling trashcan trash',
 'Spreading Cog grease',
 'Polishing kart trophies',
 'Balancing scale for weighing 1 Ton weights',
 'Practicing Victory Dances',
 'Preparing wackiness',
 "Giving Mickey Mouse the 'five minutes' sign",
 'Testing white gloves',
 'Bending underwater rings',
 'Spooling red tape',
 'Freezing Brrrgh ice',
 'Tuning falling pianos']
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'TOON TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "Control" key to jump.',
               'Press the "F9" key to take a screenshot, which will be saved in your Toontown folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without a clothing ticket.',
               'Rewards for some ToonTasks allow you to carry more gags and jellybeans.',
               'You can have up to 50 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The Toontown servers continually save all the necessary information.',
               'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.',
               'Some SpeedChat phrases play emotion animations on your Toon.',
               'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.',
               'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.',
               'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.',
               'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!',
               'The names of your True Friends will appear in Blue.',
               'See if you can collect all the fish in Toontown!',
               'Different ponds hold different fish. Try them all!',
               'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.',
               'You can sell your fish to the Fishermen or inside Pet Shops.',
               'Stronger fishing rods catch heavier fish but cost more jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'Heavier fish are worth more jellybeans to the Pet Shop.',
               'Rare fish are worth more jellybeans to the Pet Shop.',
               'You can sometimes find bags of jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more jellybeans.',
               'Adopt a Doodle at the Pet Shop!',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               "Show off your stylin' ride and turbo-boost your Laff limit at Goofy Speedway.",
               'Enter Goofy Speedway through the tire-shaped tunnel in Toontown Central Playground.',
               'Earn Laff points at Goofy Speedway.',
               'Goofy Speedway has six different race tracks. '),
 TIP_STREET: ('There are four types of Cogs: Lawbots, Cashbots, Sellbots, and Bossbots.',
              'Each Gag Track has different amounts of accuracy and damage.',
              'Sound gags will affect all Cogs but will wake up any lured Cogs.',
              'Defeating Cogs in strategic order can greatly increase your chances of winning battles.',
              'The Toon-Up Gag Track lets you heal other Toons in battle.',
              'Gag experience points are doubled during a Cog Invasion!',
              'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.',
              'In battle, gags are used in order from top to bottom as displayed on the Gag Menu.',
              'The row of circular lights over Cog Building elevators show how many floors will be inside.',
              'Click on a Cog to see more details.',
              'Using high level gags against low level Cogs will not earn any experience points.',
              'A gag that will earn experience has a blue background on the Gag Menu in battle.',
              'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.',
              'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.',
              'Each street in Toontown has different Cog levels and types.',
              'Sidewalks are safe from Cogs.',
              'On the streets, side doors tell knock-knock jokes when approached.',
              'Some ToonTasks train you for new Gag Tracks. You only get to choose six of the seven Gag Tracks, so choose carefully!',
              'Traps are only useful if you or your friends coordinate using Lure in battle.',
              'Higher level Lures are less likely to miss.',
              'Lower level gags have a lower accuracy against high level Cogs.',
              'Cogs cannot attack once they have been lured in battle.',
              'When you and your friends defeat a Cog building you are rewarded with portraits inside the rescued Toon Building.',
              'Using a Toon-Up gag on a Toon with a full Laff meter will not earn Toon-Up experience.',
              'Cogs will be briefly stunned when hit by any gag. This increases the chance that other gags in the same round will hit.',
              'Drop gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.',
              'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker Book.',
              'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.',
              'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.',
              'A maximum of four Toons can battle at once.',
              'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.',
              'The two most difficult Cogs of each type are only found in buildings.',
              'Drop gags never work against lured Cogs.',
              'Cogs tend to attack the Toon that has done them the most damage.',
              'Sound gags do not get bonus damage against lured Cogs.',
              'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.',
              'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
 TIP_MINIGAME: ('After you fill up your jellybean jar, any jellybeans you get from Trolley Games automatically spill over into your bank.',
                'You can use the arrow keys instead of the mouse in the "Match Minnie" Trolley Game.',
                'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.',
                'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.',
                'A perfect game of Match Minnie will double your points.',
                'In the Tug-of-War you are awarded more jellybeans if you play against a tougher Cog.',
                'Trolley Game difficulty varies by neighborhood; ' + lToontownCentral + ' has the easiest and ' + lDonaldsDreamland + ' has the hardest.',
                'Certain Trolley Games can only be played in a group.'),
 TIP_COGHQ: ('You must complete your Sellbot Disguise before visiting the V.P.',
             'You must complete your Cashbot Disguise before visiting the C.F.O.',
             'You must complete your Lawbot Disguise before visiting the Chief Justice.',
             'You can jump on Cog Goons to temporarily disable them.',
             'Collect Cog Merits by defeating Sellbot Cogs in battle.',
             'Collect Cogbucks by defeating Cashbot Cogs in battle.',
             'Collect Jury Notices by defeating Lawbot Cogs in battle.',
             'Collect Stock Options by defeating Bossbot Cogs in battle.',
             'You get more Merits, Cogbucks, Jury Notices, or Stock Options from higher level Cogs.',
             'When you collect enough Cog Merits to earn a promotion, go see the Sellbot V.P.!',
             'When you collect enough Cogbucks to earn a promotion, go see the Cashbot C.F.O.!',
             'When you collect enough Jury Notices to earn a promotion, go see the Lawbot Chief Justice!',
             'When you collect enough Stock Options to earn a promotion, go see the Bossbot C.E.O.!',
             'You can talk like a Cog when you are wearing your Cog Disguise.',
             'Up to eight Toons can join together to fight the Sellbot V.P.',
             'Up to eight Toons can join together to fight the Cashbot C.F.O.',
             'Up to eight Toons can join together to fight the Lawbot Chief Justice.',
             'Up to eight Toons can join together to fight the Bossbot C.E.O.',
             'Inside Cog Headquarters follow stairs leading up to find your way.',
             'Each time you battle through a Sellbot HQ factory, you will gain one part of your Sellbot Cog Disguise.',
             'You can check the progress of your Cog Disguise in your Shticker Book.',
             'You can check your promotion progress on your Disguise Page in your Shticker Book.',
             'Make sure you have full gags and a full Laff Meter before going to Cog Headquarters.',
             'As you get promoted, your Cog disguise updates.',
             'You must defeat the ' + Foreman + ' to recover a Sellbot Cog Disguise part.',
             "Earn Cashbot disguise suit parts as rewards for completing ToonTasks in Donald's Dreamland.",
             'Cashbots manufacture and distribute their currency, Cogbucks, in three Mints - Coin, Dollar and Bullion.',
             'Wait until the C.F.O. is dizzy to throw a safe, or he will use it as a helmet! Hit the helmet with another safe to knock it off.',
             'Earn Lawbot disguise suit parts as rewards for completing ToonTasks for Professor Flake.',
             "It pays to be puzzled: the virtual Cogs in Lawbot HQ won't reward you with Jury Notices.",
             'Defeating the V.P. will give an SOS Card from an imprisoned shopkeeper.',
             'Defeating the C.F.O. will give unites of either Toon-Up, Gag-up, or jellybeans.',
             'Defeating the Chief Justice will give Cog summons to call Cogs to a location.',
             'Defeating the C.E.O. will give pink slips which can be used to fire Cogs.'),
 TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!',
              'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.',
              "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.",
              'Reward your Doodle for doing tricks.',
              "If you visit a friend's estate, your Doodle will come too.",
              'Feed your Doodle a jellybean when it is hungry.',
              'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.',
              'Doodles love company. Invite your friends over to play!',
              'All Doodles have unique personalities.',
              'You can return your Doodle and adopt a new one at the Pet Shops.',
              'When a Doodle performs a trick, the Toons around it heal.',
              'Doodles become better at tricks with practice. Keep at it!',
              'More advanced Doodle tricks heal Toons faster.',
              'Experienced Doodles can perform more tricks before getting tired.',
              'You can see a list of nearby Doodles in your Friends List.',
              "Purchase furniture from Clarabelle's Cattlelog to decorate your house.",
              'The bank inside your house holds extra jellybeans.',
              'The closet inside your house holds extra clothes.',
              "Go to your friend's house and try on his clothes.",
              "Purchase better fishing rods from Clarabelle's Cattlelog.",
              'Call Clarabelle using the phone inside your house.',
              'Clarabelle sells a larger closet that holds more clothing.',
              'Make room in your closet before using a Clothing Ticket.',
              'Clarabelle sells everything you need to decorate your house.',
              'Check your mailbox for deliveries after ordering from Clarabelle.',
              "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.",
              "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.",
              "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.",
              'Store extra furniture in your attic.',
              'You will get a notice from Clarabelle when a new Cattlelog is ready.',
              'You will get a notice from Clarabelle when a Cattlelog delivery arrives.',
              'New Cattlelogs are delivered each week.',
              'Look for limited-edition holiday items in the Cattlelog.',
              'Move unwanted furniture to the trash can.',
              'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.',
              'You can invite your friends to your Estate using SpeedChat.',
              'Did you know the color of your house matches the color of your Pick-A-Toon panel?'),
 TIP_KARTING: ("Buy a Roadster, TUV, or Cruiser kart in Goofy's Auto Shop.",
               "Customize your kart with decals, rims and more in Goofy's Auto Shop.",
               'Earn tickets by kart racing at Goofy Speedway.',
               "Tickets are the only currency accepted at Goofy's Auto Shop.",
               'Tickets are required as deposits to race.',
               'A special page in the Shticker Book allows you to customize your kart.',
               'A special page in the Shticker Book allows you to view records on each track.',
               'A special page in the Shticker Book allows you to display trophies.',
               'Screwball Stadium is the easiest track at Goofy Speedway.',
               'Airborne Acres has the most hills and jumps of any track at Goofy Speedway.',
               'Blizzard Boulevard is the most challenging track at Goofy Speedway.'),
 TIP_GOLF: ('Press the Tab key to see a top view of the golf course.', 'Press the Up Arrow key to point yourself towards the golf hole.')}
FishGenusNames = {0: 'Balloon Fish',
 2: 'Cat Fish',
 4: 'Clown Fish',
 6: 'Frozen Fish',
 8: 'Star Fish',
 10: 'Holey Mackerel',
 12: 'Dog Fish',
 14: 'Amore Eel',
 16: 'Nurse Shark',
 18: 'King Crab',
 20: 'Moon Fish',
 22: 'Sea Horse',
 24: 'Pool Shark',
 26: 'Bear Acuda',
 28: 'Cutthroat Trout',
 30: 'Piano Tuna',
 32: 'Peanut Butter & Jellyfish',
 34: 'Devil Ray'}
FishSpeciesNames = {0: ('Balloon Fish',
     'Hot Air Balloon Fish',
     'Weather Balloon Fish',
     'Water Balloon Fish',
     'Red Balloon Fish'),
 2: ('Cat Fish',
     'Siamese Cat Fish',
     'Alley Cat Fish',
     'Tabby Cat Fish',
     'Tom Cat Fish'),
 4: ('Clown Fish',
     'Sad Clown Fish',
     'Party Clown Fish',
     'Circus Clown Fish'),
 6: ('Frozen Fish',),
 8: ('Star Fish',
     'Five Star Fish',
     'Rock Star Fish',
     'Shining Star Fish',
     'All Star Fish'),
 10: ('Holey Mackerel',),
 12: ('Dog Fish',
      'Bull Dog Fish',
      'Hot Dog Fish',
      'Dalmatian Dog Fish',
      'Puppy Dog Fish'),
 14: ('Amore Eel', 'Electric Amore Eel'),
 16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark'),
 18: ('King Crab', 'Alaskan King Crab', 'Old King Crab'),
 20: ('Moon Fish',
      'Full Moon Fish',
      'Half Moon Fish',
      'New Moon Fish',
      'Crescent Moon Fish',
      'Harvest Moon Fish'),
 22: ('Sea Horse',
      'Rocking Sea Horse',
      'Clydesdale Sea Horse',
      'Arabian Sea Horse'),
 24: ('Pool Shark',
      'Kiddie Pool Shark',
      'Swimming Pool Shark',
      'Olympic Pool Shark'),
 26: ('Brown Bear Acuda',
      'Black Bear Acuda',
      'Koala Bear Acuda',
      'Honey Bear Acuda',
      'Polar Bear Acuda',
      'Panda Bear Acuda',
      'Kodiac Bear Acuda',
      'Grizzly Bear Acuda'),
 28: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
 30: ('Piano Tuna',
      'Grand Piano Tuna',
      'Baby Grand Piano Tuna',
      'Upright Piano Tuna',
      'Player Piano Tuna'),
 32: ('Peanut Butter & Jellyfish',
      'Grape PB&J Fish',
      'Crunchy PB&J Fish',
      'Strawberry PB&J Fish',
      'Concord Grape PB&J Fish'),
 34: ('Devil Ray',)}
SellbotLegFactorySpecMainEntrance = 'Front Entrance'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Lobby Hallway'
SellbotLegFactorySpecGearRoom = 'Gear Room'
SellbotLegFactorySpecBoilerRoom = 'Boiler Room'
SellbotLegFactorySpecEastCatwalk = 'East Catwalk'
SellbotLegFactorySpecPaintMixer = 'Paint Mixer'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Paint Mixer Storage Room'
SellbotLegFactorySpecPipeRoom = 'Pipe Room'
SellbotLegFactorySpecDuctRoom = 'Duct Room'
SellbotLegFactorySpecSideEntrance = 'Side Entrance'
SellbotLegFactorySpecStomperAlley = 'Stomper Alley'
SellbotLegFactorySpecLavaRoomFoyer = 'Lava Room Foyer'
SellbotLegFactorySpecLavaRoom = 'Lava Room'
SellbotLegFactorySpecLavaStorageRoom = 'Lava Room Storage'
SellbotLegFactorySpecWestCatwalk = 'West Catwalk'
SellbotLegFactorySpecOilRoom = 'Oil Room'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'Oil Room Hallway'
SellbotLegFactorySpecEastSiloControlRoom = 'East Silo Control Room'
SellbotLegFactorySpecWestSiloControlRoom = 'West Silo Control Room'
SellbotLegFactorySpecCenterSiloControlRoom = 'Center Silo Control Room'
SellbotLegFactorySpecEastSilo = 'East Silo'
SellbotLegFactorySpecWestSilo = 'West Silo'
SellbotLegFactorySpecCenterSilo = 'Center Silo'
SellbotLegFactorySpecWestSiloCatwalk = 'West Silo Catwalk'
SellbotLegFactorySpecEastSiloCatwalk = 'East Silo Catwalk'
SellbotLegFactorySpecWestElevatorShaft = 'West Silo Elevator'
SellbotLegFactorySpecEastElevatorShaft = 'East Silo Elevator'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
FishBingoStart = "It's time for Fish Bingo!  Go to any available pier to play!"
FishBingoOngoing = 'Welcome! Fish Bingo is currently in progress.'
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo!  Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card.  Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card.  Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way.  Mark both diagonals and the middle row to win.  This one isn't easy!"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Blockout!  Mark the entire card to win.  You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
FishBingoJackpotWin = 'Win %s jellybeans!'
ResistanceToonupMenu = 'Toon-Up'
ResistanceToonupItem = '%s Toon-Up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons of the World, Toon-Up!'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Toons of the World, Gag-up!'
ResistanceMoneyMenu = 'Jellybeans'
ResistanceMoneyItem = '%s jellybeans'
ResistanceMoneyChat = 'Toons of the World, Spend Wisely!'
ResistanceEmote1 = 'Whispering Willow: Welcome to the Resistance!'
ResistanceEmote2 = 'Whispering Willow: Use your new emote to identify yourself to other members.'
ResistanceEmote3 = 'Whispering Willow: Good luck!'
KartUIExit = 'Leave Kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Buy Kart'
KartShop_BuyAccessories = 'Buy Accessories'
KartShop_BuyAccessory = 'Buy Accessory'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'No available accessories of this type'
KartShop_FullTrunk = 'Your trunk is full.'
KartShop_ConfirmReturnKart = 'Are you sure you want to return your current Kart?'
KartShop_ConfirmBoughtTitle = 'Congratulations!'
KartShop_NotEnoughTickets = 'Not Enough Tickets!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "You don't have enough tickets! Try a practice race instead."
StartingBlock_NoBoard = 'Boarding has ended for this race. Please wait for the next race to begin.'
StartingBlock_NoKart = 'You need a kart first! Try asking one of the clerks in the Kart Shop.'
StartingBlock_Occupied = 'This block is currently occupied! Please try another spot.'
StartingBlock_TrackClosed = 'Sorry, this track is closed for remodeling.'
StartingBlock_EnterPractice = 'Would you like to enter a practice race?'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'Would you like to park your car here?'
StartingBlock_KickSoloRacer = 'Toon Battle and Grand Prix races require two or more racers.'
StartingBlock_Loading = 'Going to the Race!'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Racer Name'
LeaderBoard_Daily = 'Daily Scores'
LeaderBoard_Weekly = 'Weekly Scores'
LeaderBoard_AllTime = 'All Time Best Scores'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Screwball Stadium',
 RaceGlobals.RT_Speedway_1_rev: 'Screwball Stadium' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'Rustic Raceway',
 RaceGlobals.RT_Rural_1_rev: 'Rustic Raceway' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'City Circuit',
 RaceGlobals.RT_Urban_1_rev: 'City Circuit' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'Corkscrew Coliseum',
 RaceGlobals.RT_Speedway_2_rev: 'Corkscrew Coliseum' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'Airborne Acres',
 RaceGlobals.RT_Rural_2_rev: 'Airborne Acres' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Blizzard Boulevard',
 RaceGlobals.RT_Urban_2_rev: 'Blizzard Boulevard' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Toon Utility Vehicle'}
KartDNA_AccNames = {1000: 'Air Cleaner',
 1001: 'Four Barrel',
 1002: 'Flying Eagle',
 1003: 'Steer Horns',
 1004: 'Straight Six',
 1005: 'Small Scoop',
 1006: 'Single Overhead',
 1007: 'Medium Scoop',
 1008: 'Single Barrel',
 1009: 'Flugle Horn',
 1010: 'Striped Scoop',
 2000: 'Space Wing',
 2001: 'Patched Spare',
 2002: 'Roll Cage',
 2003: 'Single Fin',
 2004: 'Double-decker Wing',
 2005: 'Single Wing',
 2006: 'Standard Spare',
 2007: 'Single Fin',
 2008: 'sp9',
 2009: 'sp10',
 3000: 'Dueling Horns',
 3001: "Freddie's Fenders",
 3002: 'Cobalt Running Boards',
 3003: 'Cobra Sidepipes',
 3004: 'Straight Sidepipes',
 3005: 'Scalloped Fenders',
 3006: 'Carbon Running Boards',
 3007: 'Wood Running Boards',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Curly Tailpipes',
 4001: 'Splash Fenders',
 4002: 'Dual Exhaust',
 4003: 'Plain Dual Fins',
 4004: 'Plain Mudflaps',
 4005: 'Quad Exhaust',
 4006: 'Dual Flares',
 4007: 'Mega Exhaust',
 4008: 'Striped Dual Fins',
 4009: 'Bubble Duals Fins',
 4010: 'Striped Mudflaps',
 4011: 'Mickey Mudflaps',
 4012: 'Scalloped Mudflaps',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Three Spoke',
 5004: 'Paint Lid',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'Five Bolt',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Five Spoke',
 5014: 'Knockoff',
 6000: 'Number Five',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Bright Red',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Sea Green',
 7015: 'Green',
 7016: 'Light Blue',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Royal Blue',
 7021: 'Slate Blue',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Grand Touring'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 2) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 3) + ' Kart Racing trophies won! Laff point boost!']
KartRace_TitleInfo = 'Get Ready to Race'
KartRace_SSInfo = 'Welcome to Screwball Stadium!\nPut the pedal to the metal and hang on tight!\n'
KartRace_CoCoInfo = 'Welcome to Corkscrew Coliseum!\nUse the banked turns to keep your speed up!\n'
KartRace_RRInfo = 'Welcome to Rustic Raceway!\nPlease be kind to the fauna and stay on the track!\n'
KartRace_AAInfo = 'Welcome to Airborne Acres!\nHold onto your hats! It looks bumpy up ahead...\n'
KartRace_CCInfo = 'Welcome to City Circuit!\nWatch out for pedestrians as you speed through downtown!\n'
KartRace_BBInfo = 'Welcome to Blizzard Boulevard!\nWatch your speed. There might be ice out there.\n'
KartRace_GeneralInfo = 'Use Control to throw gags you pick up on the track, and the arrow keys to control your kart.'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'all time'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'Final Lap!'
KartRace_Exit = 'Exit Race'
KartRace_NextRace = 'Next Race'
KartRace_Leave = 'Leave Race'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Race Total'
KartRace_CircuitTotal = 'Circuit Total'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'You timed out of that race.  Your tickets have been refunded.  Keep trying!'
KartRace_RaceTimeoutNoRefund = 'You timed out of that race.  Your tickets have not been refunded because the Grand Prix had already started.  Keep trying!'
KartRace_RacerTooSlow = 'You took too long to finish the race.  Your tickets have not been refunded.  Keep trying!'
KartRace_PhotoFinish = 'Photo Finish!'
KartRace_CircuitPoints = 'Circuit Points'
CircuitRaceStart = 'The Toontown Grand Prix at Goofy Speedway is about to begin!  To win, collect the most points in three consecutive races!'
CircuitRaceOngoing = 'Welcome! The Toontown Grand Prix is currently in progress.'
CircuitRaceEnd = "That's all for today's Toontown Grand Prix at Goofy Speedway.  See you next week!"
TrickOrTreatMsg = 'You have already\nfound this treat!'
WinterCarolingMsg = 'You have already been caroling here!'
LawbotBossTempIntro0 = "Hmmm... What's on the docket today?"
LawbotBossTempIntro1 = 'Aha, we have a Toon on trial!'
LawbotBossTempIntro2 = "The prosecution's case is strong."
LawbotBossTempIntro3 = 'And here are the public defenders.'
LawbotBossTempIntro4 = "Wait a minute... You're Toons!"
LawbotBossTempJury1 = 'Jury selection will now commence.'
LawbotBossHowToGetEvidence = 'Touch the witness stand to get evidence.'
LawbotBossTrialChat1 = 'Court is now in session.'
LawbotBossHowToThrowPies = 'Press the Delete key to throw the evidence\n at the lawyers or into the scale!'
LawbotBossNeedMoreEvidence = 'You need to get more evidence!'
LawbotBossDefenseWins1 = 'Impossible! The defense won?'
LawbotBossDefenseWins2 = 'No. I declare a mistrial! A new one will be scheduled.'
LawbotBossDefenseWins3 = "Hrrmpphh. I'll be in my chambers."
LawbotBossProsecutionWins = 'And so the defendant is guilty.'
LawbotBossReward = 'I award a promotion and the ability to summon Cogs'
LawbotBossLeaveCannon = 'Leave cannon'
LawbotBossPassExam = 'Bah, so you passed the bar exam.'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Objection sustained!',
 'Strike that from the record.',
 'Your appeal has been rejected. I sentence you to sadness!',
 'Order in the court!']
LawbotBossAreaAttackTaunt = "You're all in contempt of court!"
WitnessToonName = 'Bumpy Bumblebehr'
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Oh no, there are no Toon jurors. This will be a tough trial.'
WitnessToonOneJuror = 'Cool! There is 1 Toon in the jury!'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'Awesome! All the jurors are Toons!'
WitnessToonPrepareBattleThree = 'Hurry, touch the witness stand to get evidence.\x07Press the Delete key to throw the evidence at the lawyers, or at the defense pan.'
WitnessToonCongratulations = "You did it!  Thank you for a spectacular defense!\x07Here, take these papers the Chief Justice left behind.\x07With it you'll be able to summon Cogs from your Cog Gallery page."
WitnessToonLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
WitnessToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
WitnessToonMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'Issue a Cog Summon'
SummonDlgButton1 = 'Summon a Cog'
SummonDlgButton2 = 'Summon a Cog Building'
SummonDlgButton3 = 'Summon a Cog Invasion'
SummonDlgSingleConf = 'Would you like to issue a summons to a %s?'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Delivering Summons...'
SummonDlgSingleSuccess = 'You have successfully summoned the Cog.'
SummonDlgSingleBadLoc = "Sorry, Cogs aren't allowed here.  Try somewhere else."
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'You have successfully summoned the Cogs. A Shopkeeper has agreed to let them temporarily take over their building!'
SummonDlgBldgBadLoc = 'Sorry, there are no Toon buildings nearby for the Cogs to take over.'
SummonDlgInvasionSuccess = "You have successfully summoned the Cogs. It's an invasion!"
SummonDlgInvasionBusy = 'A %s cannot be found now.  Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Sorry, the Cog invasion has failed.'
SummonDlgShopkeeper = 'The Shopkeeper '
PolarPlaceEffect1 = 'Paula Behr: Welcome to Hibernation Vacations!'
PolarPlaceEffect2 = 'Paula Behr: Try this on for size.'
PolarPlaceEffect3 = 'Paula Behr: Your new look will only work in the Brrrgh.'
GreenToonEffectMsg = 'Eugene: You look Toontastic in green!'
LaserGameMine = 'Skull Sweeper!'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'Avoid the Skulls'
LaserGameDrag = 'Drag three of a color in a row'
LaserGameDefault = 'Unknown Game'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Your Best Score:\n'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Feather Gag Tree'
GagTreeJugglingBalls = 'Juggling Cubes Gag Tree'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Donald Statue'
StatuaryMinnie = 'Minnie Statue'
StatuaryMickey1 = 'Mickey Statue'
StatuaryMickey2 = 'Mickey Fountain'
StatuaryToon = 'Toon Statue'
StatuaryToonWave = 'Toon Wave Statue'
StatuaryToonVictory = 'Toon Victory Statue'
StatuaryToonCrossedArms = 'Toon Authority Statue'
StatuaryToonThinking = 'Toon Embrace Statue'
StatuaryMeltingSnowman = 'Melting Snowman'
StatuaryMeltingSnowDoodle = 'Melting SnowDoodle'
StatuaryGardenAccelerator = 'Insta-Grow Fertilizer'
AnimatedStatuaryFlappyCog = 'Flappy Cog'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('School Daisy',
      'Lazy Daisy',
      'Midsummer Daisy',
      'Freshasa Daisy',
      'Whoopsie Daisy',
      'Upsy Daisy',
      'Crazy Daisy',
      'Hazy Dazy'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('What-in Carnation',
      'Instant Carnation',
      'Hybrid Carnation',
      'Side Carnation',
      'Model Carnation'),
 52: ('Lily-of-the-Alley',
      'Lily Pad',
      'Tiger Lily',
      'Livered Lily',
      'Chili Lily',
      'Silly Lily',
      'Indubitab Lily',
      'Dilly Lilly'),
 53: ('Laff-o-dil',
      'Daffy Dill',
      'Giraff-o-dil',
      'Time and a half-o-dil'),
 54: ('Dandy Pansy',
      'Chim Pansy',
      'Potsen Pansy',
      'Marzi Pansy',
      'Smarty Pansy'),
 55: ('Car Petunia', 'Platoonia'),
 56: ("Summer's Last Rose",
      'Corn Rose',
      'Tinted Rose',
      'Stinking Rose',
      'Istilla Rose')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'New Entry'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'Water Skill'
GardeningShovelSkill = 'Shovel Skill'
GardeningNoSkill = 'No Skill Up'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'Choose the jellybeans you want to plant.'
GardeningChooseBeansItem = 'Choose the jellybeans / item you want to plant.'
GardeningChooseToonStatue = 'Choose the toon you want to create a statue of.'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Amazing! You've maxed out your shovel skill!"
GardenWateringCanLevelUp = "Congratulations you've earned a new watering can!"
GardenMiniGameWon = "Congratulations you've watered the plant!"
ShovelTin = 'Tin Shovel'
ShovelSteel = 'Bronze Shovel'
ShovelSilver = 'Silver Shovel'
ShovelGold = 'Gold Shovel'
WateringCanSmall = 'Small Watering Can'
WateringCanMedium = 'Medium Watering Can'
WateringCanLarge = 'Large Watering Can'
WateringCanHuge = 'Huge Watering Can'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = ' Make sure all your plants are watered first.'
UseFromSpecialsTab = ' Use from the specials tab of the garden page.'
UseSpecial = 'Use Special'
UseSpecialBadLocation = 'You can only use that in your garden.'
UseSpecialSuccess = 'Success! Your watered plants just grew.'
ConfirmWiltedFlower = '%(plant)s is wilted.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'Your flower basket is full. Sell some flowers first.'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = " If you remove this tree, you won't be able to harvest gags from the higher level trees."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "That didn't work.  Please try a different combination of jellybeans."
GardenGagTree = ' Gag Tree'
GardenUberGag = 'Uber Gag'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in xrange(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in xrange(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Magic Beans'
GardenTextMagicBeansB = 'Some Other Beans'
GardenSpecialDiscription = 'This text should explain how to use a certain garden special'
GardenSpecialDiscriptionB = 'This text should explain how to use a certain garden special, in yo face foo!'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Watering Can',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
SkillTooLow = 'Skill\nToo Low'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval


TravelGameTitle = 'Trolley Tracks'
TravelGameInstructions = 'Click up or down to set your number of votes.  Click the vote button to cast it. Reach your secret goal to get bonus beans. Earn more votes by doing well in the other games.'
TravelGameRemainingVotes = 'Remaining Votes:'
TravelGameUse = 'Use'
TravelGameVotesWithPeriod = 'votes.'
TravelGameVotesToGo = 'votes to go'
TravelGameVoteToGo = 'vote to go'
TravelGameUp = 'UP.'
TravelGameDown = 'DOWN.'
TravelGameVoteWithExclamation = 'Vote!'
TravelGameWaitingChoices = 'Waiting for other players to vote...'
TravelGameDirections = ['UP', 'DOWN']
TravelGameTotals = 'Totals '
TravelGameReasonVotes = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesPlural = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesSingular = 'The trolley is moving %(dir)s, winning by %(numVotes)d vote.'
TravelGameReasonPlace = '%(name)s breaks the tie. The trolley is moving %(dir)s.'
TravelGameReasonRandom = 'The trolley is randomly moving %(dir)s.'
TravelGameOneToonVote = '%(name)s used %(numVotes)s votes to go %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)d Beans'
TravelGamePlaying = 'Up next, the %(game)s trolley game.'
TravelGameGotBonus = '%(name)s got a bonus of %(numBeans)s jellybeans!'
TravelGameNoOneGotBonus = 'No one reached their secret goal.  Everyone gets 1 jellybean.'
TravelGameConvertingVotesToBeans = 'Converting some votes to jellybeans...'
TravelGameGoingBackToShop = "Only 1 player left. Going to Goofy's Gag Shop."
PairingGameTitle = 'Toon Memory Game'
PairingGameInstructions = 'Press Delete to open a card. Match 2 cards to score a point.  Make a match with the bonus glow and earn an extra point.  Earn more points by keeping the flips low.'
PairingGameInstructionsMulti = 'Press Delete to open a card. Press Control to signal another player to open a card. Match 2 cards to score a point.  Make a match with the bonus glow and earn an extra point.  Earn more points by keeping the flips low.'
PairingGamePerfect = 'PERFECT!!'
PairingGameFlips = 'Flips:'
PairingGamePoints = 'Points:'
TrolleyHolidayStart = 'Trolley Tracks is about to begin!  Board any trolley with 2 or more toons to play.'
TrolleyHolidayOngoing = 'Welcome! Trolley Tracks is currently in progress.'
TrolleyHolidayEnd = "That's all for today's Trolley Tracks.  See you next week!"
TrolleyWeekendStart = 'Trolley Tracks Weekend is about to begin!  Board any trolley with 2 or more toons to play.'
TrolleyWeekendEnd = "That's all for Trolley Tracks Weekend."
VineGameTitle = 'Jungle Vines'
VineGameInstructions = 'Get to the rightmost vine in time. Press Up or Down to climb the vine.  Press Left or Right to change facing and jump.  The lower you are on the vine, the faster you jump off.  Collect the bananas if you can, but avoid the bats and spiders.'
ValentinesDayStart = "Happy ValenToon's Day!"
ValentinesDayEnd = "That's all for ValenToon's Day!"
GolfCourseNames = {0: 'Walk In The Par',
 1: 'Hole Some Fun',
 2: 'The Hole Kit And Caboodle'}
GolfHoleNames = {0: 'Whole In Won',
 1: 'No Putts About It',
 2: 'Down The Hatch',
 3: 'Seeing Green',
 4: 'Hot Links',
 5: 'Peanut Putter',
 6: 'Swing-A-Long',
 7: 'Afternoon Tee',
 8: 'Hole In Fun',
 9: 'Rock And Roll In',
 10: 'Bogey Nights',
 11: 'Tea Off Time',
 12: 'Holey Mackerel!',
 13: 'One Little Birdie',
 14: 'At The Drive In',
 15: 'Swing Time',
 16: 'Hole On The Range',
 17: 'Second Wind',
 18: 'Whole In Won-2',
 19: 'No Putts About It-2',
 20: 'Down The Hatch-2',
 21: 'Seeing Green-2',
 22: 'Hot Links-2',
 23: 'Peanut Putter-2',
 24: 'Swing-A-Long-2',
 25: 'Afternoon Tee-2',
 26: 'Hole In Fun-2',
 27: 'Rock And Roll In-2',
 28: 'Bogey Nights-2',
 29: 'Tea Off Time-2',
 30: 'Holey Mackerel!-2',
 31: 'One Little Birdie-2',
 32: 'At The Drive In-2',
 33: 'Swing Time-2',
 34: 'Hole On The Range-2',
 35: 'Second Wind-2'}
GolfHoleInOne = 'Hole In One'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Double Bogey'
GolfTripleBogey = 'Triple Bogey'
GolfShotDesc = {-4: GolfCondor,
 -3: GolfAlbatross,
 -2: GolfEagle,
 -1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'Courses Completed'
CoursesUnderPar = 'Courses Under Par'
HoleInOneShots = 'Hole In One Shots'
EagleOrBetterShots = 'Eagle Or Better Shots'
BirdieOrBetterShots = 'Birdie Or Better Shots'
ParOrBetterShots = 'Par Or Better Shots'
MultiPlayerCoursesCompleted = 'Multiplayer Courses Completed'
TwoPlayerWins = 'Two Player Wins'
ThreePlayerWins = 'Three Player Wins'
FourPlayerWins = 'Four Player Wins'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 2) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 3) + ' Trophies won']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!!  Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Ranking: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Press Left or Right to change tee spot.\nPress Control to select.'
GolfWarningMustSwing = 'Warning: You must press Control on your next swing.'
GolfAimInstructions = 'Press Left or Right to aim.\nPress and hold Control to swing.'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'Hold Down Control Longer to\nHit the Ball Further'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Exit Course'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Golf Customizer'
GolfPageTitleRecords = 'Personal Best Records'
GolfPageTitleTrophy = 'Golfing Trophies'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'Tickets : '
GolfPageConfirmDelete = 'Delete Accessory?'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = ' -  %(time).2f seconds'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
RoamingTrialerWeekendStart = 'Tour Toontown is starting! Free players may now enter any neighborhood!'
RoamingTrialerWeekendOngoing = 'Welcome to Tour Toontown! Free players may now enter any neighborhood!'
RoamingTrialerWeekendEnd = "That's all for Tour Toontown."
MoreXpHolidayStart = 'Good news! Exclusive Test Toon double gag experience time has started.'
MoreXpHolidayOngoing = 'Welcome! Exclusive Test Toon double gag experience time is currently ongoing.'
MoreXpHolidayEnd = 'Exclusive Test Toon double gag experience time has ended. Thanks for helping us Test things!'
JellybeanDayHolidayStart = "It's Jellybean Day! Get Double Jellybean rewards at Parties!"
JellybeanDayHolidayEnd = "That's all for Jellybean Day. See you next year."
PartyRewardDoubledJellybean = 'Double Jellybeans!'
GrandPrixWeekendHolidayStart = "It's Grand Prix Weekend at Goofy Speedway! Free and paid players collect the most points in three consecutive races."
GrandPrixWeekendHolidayEnd = "That's all for Grand Prix Weekend. See you next year."
KartRace_DoubleTickets = 'Double Tickets'
SellbotNerfHolidayStart = 'Operation: Storm Sellbot is happening now! Battle the V.P. today!'
SellbotNerfHolidayEnd = 'Operation: Storm Sellbot has ended. Great work, Toons!'
JellybeanTrolleyHolidayStart = 'Double Bean Days for Trolley Games have begun!'
JellybeanTrolleyHolidayEnd = 'Double Bean Days for Trolley Games have ended!'
JellybeanFishingHolidayStart = 'Double Bean Days for Fishing have begun!'
JellybeanFishingHolidayEnd = 'Double Bean Days for Fishing have ended!'
JellybeanPartiesHolidayStart = "It's Jellybean Week! Get Double Jellybean rewards!"
JellybeanPartiesHolidayEnd = "That's all for Jellybean Week. See you next year."
JellybeanMonthHolidayStart = 'Celebrate Toontown with double beans, Cattlelog items and silly surprises!'
BankUpgradeHolidayStart = 'Something Toontastic happened to your Jellybean Bank!'
HalloweenPropsHolidayStart = "It's Halloween in Toontown!"
HalloweenPropsHolidayEnd = 'Halloween has ended. Boo!'
SpookyPropsHolidayStart = 'Silly Meter spins Toontown into spooky mode!'
BlackCatHolidayStart = 'Create a Black Cat - Today only!'
BlackCatHolidayEnd = 'Black Cat day has ended!'
SpookyBlackCatHolidayStart = 'Friday 13th means a Black Cat blast!'
TopToonsMarathonStart = "The Top Toons New Year's Day Marathon has begun!"
TopToonsMarathonEnd = "The Top Toons New Year's Day Marathon has ended."
WinterDecorationsStart = "It's Winter Holiday time in Toontown!"
WinterDecorationsEnd = 'Winter Holiday is over - Happy New Year!'
WackyWinterDecorationsStart = 'Brrr! Silly Meter goes from silly to chilly!'
WinterCarolingStart = 'Caroling has come to Toontown. Sing for your Snowman Head - see the Blog for details!'
ExpandedClosetsStart = 'Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 jellybeans!'
KartingTicketsHolidayStart = 'Get double tickets from Practice races at Goofy Speedway today!'
IdesOfMarchStart = 'Toons go GREEN!'
LogoutForced = 'You have done something wrong\n and are being logged out automatically,\n additionally your account may be frozen.\n Try going on a walk outside, it is fun.'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'All challenges must be defeated first.'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'Mole Stomp!\nJump on the red moles!'
MolesFinished = 'Mole Stomp successful!'
MolesPityWin = 'Stomp Failed! But the moles left.'
MolesRestarted = 'Stomp Failed! Restarting...'
BustACogInstruction = 'Remove the cog ball!'
BustACogExit = 'Exit for Now'
BustACogHowto = 'How to Play'
BustACogFailure = 'Out of Time!'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Shoot balls using the the mouse\n\n\nMatching three of a color causes the balls to fall\n\n\nRemove all Cog balls from the board'
enterHedgeMaze = 'Race through the Hedge Maze\n for a laff bonus!'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Maze Race!'
BoardingPartyReadme = 'Boarding Group?'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Show Boarding Group'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Boarding Group'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'Are you sure you want to quit this Boarding Group?'
BoardcodeMissing = 'Something went wrong; try again later.'
BoardcodeMinLaffLeader = 'Your group cannot board because you have less than %s laff points.'
BoardcodeMinLaffNonLeaderSingular = 'Your group cannot board because %s has less than %s laff points.'
BoardcodeMinLaffNonLeaderPlural = 'Your group cannot board because %s have less than %s laff points.'
BoardcodePromotionLeader = 'Your group cannot board because you do not have enough promotion merits.'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Your group cannot board because there is not enough space.'
BoardcodeBattleLeader = 'Your group cannot board because you are in battle.'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInviteMinLaffInviter = 'You need %s Laff Points before being a member of this Boarding Group.'
BoardingInviteMinLaffInvitee = '%s needs %s Laff Points before being a member of this Boarding Group.'
BoardingInvitePromotionInviter = 'You need to earn a promotion before being a member of this Boarding Group.'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteNotPaidInvitee = '%s needs to be a paid Member to be a part of your Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Your Boarding Group is already full.'
BoardingAlreadyInGroup = 'You cannot accept this invitation because you are part of another Boarding Group.'
BoardingGroupAlreadyFull = 'You cannot accept this invitation because the group is already full.'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'You need to deal with the\n pending invitation first.'
BoardingCannotLeaveZone = 'You cannot leave this area because you are part of a Boarding Group.'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'You have been removed from the Boarding Group.'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Your Boarding Group was disbanded by the group leader.'
BoardingMessageGroupDisbandedGeneric = 'Your Boarding Group was disbanded.'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Click Again to\nCancel Go'
And = 'and'
BoardingGoingTo = 'Going To:'
BoardingTimeWarning = 'Boarding the elevator in '
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming...'
BossbotBossName = 'Chief Executive Officer'
BossbotRTWelcome = 'You Toons will need different disguises.'
BossbotRTRemoveSuit = 'First take off your Cog suits...'
BossbotRTFightWaiter = 'and then fight these waiters.'
BossbotRTWearWaiter = "Good Job! Now put on the waiters' clothes."
BossbotBossPreTwo1 = "What's taking so long?"
BossbotBossPreTwo2 = 'Get cracking and serve my banquet!'
BossbotRTServeFood1 = 'Hehe, serve the food I place on these conveyor belts.'
BossbotRTServeFood2 = 'If you serve a cog three times in a row it will explode.'
BossbotResistanceToonName = "Good ol' Gil Giggles"
BossbotPhase3Speech1 = "What's happening here?!"
BossbotPhase3Speech2 = 'These waiters are toons!'
BossbotPhase3Speech3 = 'Get them!!!'
BossbotRTPhase4Speech1 = 'Good Job! Now squirt the C.E.O. with the water on the tables...'
BossbotRTPhase4Speech2 = 'or use golf balls to slow him down.'
BossbotPhase4Speech1 = 'Hrrmmpph. When I need a job done right...'
BossbotPhase4Speech2 = "I'll do it myself."
BossbotPitcherLeave = 'Leave Bottle'
BossbotPitcherLeaving = 'Leaving Bottle'
BossbotPitcherAdvice = 'Use the left and right keys to rotate.\nHold down Ctrl increase power.\nRelease Ctrl to fire.'
BossbotGolfSpotLeave = 'Leave Golf Ball'
BossbotGolfSpotLeaving = 'Leaving Golf Ball'
BossbotGolfSpotAdvice = 'Use the left and right keys to rotate.\nCtrl to fire.'
BossbotRewardSpeech1 = "No! The Chairman won't like this."
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = "You did it!  You've demoted the C.E.O.!\x07Here, take these pink slips the C.E.O. left behind.\x07With it you'll be able to fire Cogs in a battle."
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
BossbotRTHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
BossbotRTMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
GolfAreaAttackTaunt = 'Fore!'
OvertimeAttackTaunts = ["It's time to reorganize.", "Now let's downsize."]
ElevatorBossBotBoss = 'C.E.O. Battle'
ElevatorBossBotCourse0 = 'The Front Three'
ElevatorBossBotCourse1 = 'The Middle Six'
ElevatorBossBotCourse2 = 'The Back Nine'
ElevatorCashBotBoss = 'Cashbot Vault'
ElevatorCashBotMint0 = 'Coin Mint'
ElevatorCashBotMint1 = 'Dollar Mint'
ElevatorCashBotMint2 = 'Bullion Mint'
ElevatorSellBotBoss = 'Sellbot Towers'
ElevatorSellBotFactory0 = 'Front Entrance'
ElevatorSellBotFactory1 = 'Side Entrance'
ElevatorLawBotBoss = 'Lawbot Courthouse'
ElevatorLawBotCourse0 = 'Office A'
ElevatorLawBotCourse1 = 'Office B'
ElevatorLawBotCourse2 = 'Office C'
ElevatorLawBotCourse3 = 'Office D'
DaysToGo = 'Wait\n%s Days'
IceGameTitle = 'Ice Slide'
IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points and avoid the TNT!'
IceGameInstructionsNoTnt = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points.'
IceGameWaitingForPlayersToFinishMove = 'Waiting for other players...'
IceGameWaitingForAISync = 'Waiting for other players...'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Remember to press the Ctrl key!'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'How To Play'
PicnicTableMenuTutorial = 'What game do you want to learn?'
PicnicTableMenuSelect = 'What game do you want to play?'
ChineseCheckersGetUpButton = 'Get Up'
ChineseCheckersStartButton = 'Start Game'
ChineseCheckersQuitButton = 'Quit Game'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Your Turn'
ChineseCheckersGreenTurn = "Green's Turn"
ChineseCheckersYellowTurn = "Yellow's Turn"
ChineseCheckersPurpleTurn = "Purple's Turn"
ChineseCheckersBlueTurn = "Blue's Turn"
ChineseCheckersPinkTurn = "Pink's Turn"
ChineseCheckersRedTurn = "Red's Turn"
ChineseCheckersColorG = 'You are Green'
ChineseCheckersColorY = 'You are Yellow'
ChineseCheckersColorP = 'You are Purple'
ChineseCheckersColorB = 'You are Blue'
ChineseCheckersColorPink = 'You are Pink'
ChineseCheckersColorR = 'You are Red'
ChineseCheckersColorO = 'You are Observing'
ChineseCheckersYouWon = 'You just won a game of Chinese Checkers!'
ChineseCheckers = 'Chinese Checkers.'
ChineseCheckersGameOf = ' has just won a game of '
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'How to Play'
ChineseTutorialPrev = 'Previous Page'
ChineseTutorialNext = 'Next Page'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'The goal of Chinese Checkers is to be the first  player to move all of your marbles from the bottom triangle across the board and into the triangle at the top. The first player to do so wins!'
ChinesePage2 = 'Players take turns moving any marble of their own color.  A marble can move into an adjacent hole or it can hop over other marbles. Hops must go over a marble and end in an empty hole. It is possible to chain hops together for longer moves!'
CheckersPage1 = 'The goal of Checkers is to leave the opponent without any possible moves. To do this you can either capture all of his peices or block them in such that he has no available moves.'
CheckersPage2 = 'Players take turns moving any peice of their own color. A peice can move one square diagonal and forward. A peice can only move into a square that is not occupied by another peice. Kings follow the same rules but are allowed to move backwards.'
CheckersPage3 = 'To capture an opponents peice your peice must jump over it diagonally into the vacant square beyond it. If you have any jump moves during a turn, you must do one of them. You can chain jump moves together as long as it is with the same peice.'
CheckersPage4 = 'A piece becomes a king when it reaches the last row on the board. A peice that has just become a king cannot continue jumping until the next turn. Additionally, kings are allowed to move all directions and are allowed to change directions while jumping.'
CheckersGetUpButton = 'Get Up'
CheckersStartButton = 'Start Game'
CheckersQuitButton = 'Quit Game'
CheckersIts = "It's "
CheckersYourTurn = 'Your Turn'
CheckersWhiteTurn = "White's Turn"
CheckersBlackTurn = "Black's Turn"
CheckersColorWhite = 'You are White'
CheckersColorBlack = 'You are Black'
CheckersObserver = 'You are Observing'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = ' has just won a game of '
RegularCheckersYouWon = 'You just won a game of Checkers!'
MailNotifyNewItems = "You've got mail!"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'You have a new award in your mailbox!'
AwardNotifyOldItems = 'There are still awards waiting in your mailbox for you to pick up!'
InviteInvitation = 'the invitation'
InviteAcceptInvalidError = 'The invitation is no longer valid.'
InviteAcceptPartyInvalid = 'That party has been cancelled.'
InviteAcceptAllOk = 'The host has been informed of your reply.'
InviteRejectAllOk = 'The host has been informed that you declined the invitation.'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
HolidayNamesInCalendar = {1: ('Summer Fireworks', 'Celebrate Summer with a fireworks show every hour in each playground!'),
 2: ('New Year Fireworks', 'Happy New Year! Enjoy a fireworks show every hour in each playground!'),
 3: ('Bloodsucker Invasion', 'Help defend Toontown from the Bloodsucker invasion!'),
 4: ('Winter Holiday', 'Celebrate the Winter Holiday with Toontastic decorations, party and Cattlelog items, and more!'),
 5: ('Skelecog Invasion', 'Stop the Skelecogs from invading Toontown!'),
 6: ('Mr. Hollywood Invasion', 'Stop the Mr. Hollywood Cogs from invading Toontown!'),
 7: ('Fish Bingo', 'Fish Bingo Wednesday! Everyone at the pond works together to complete the card before time runs out.'),
 8: ('Toon Species Election', 'Vote on the new Toon species! Will it be Goat? Will it be Pig?'),
 9: ('Black Cat Day', 'Happy Halloween! Create a Toontastic Black Cat Toon - Today Only!'),
 13: ('Trick or Treat', 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'),
 14: ('Grand Prix', 'Grand Prix Monday at Goofy Speedway! To win, collect the most points in three consecutive races!'),
 16: ('Grand Prix Weekend', 'Free and Paid players compete in circuit races at Goofy Speedway!'),
 17: ('Trolley Tracks', 'Trolley Tracks Thursday! Board any Trolley with two or more Toons to play.'),
 19: ('Silly Saturdays', 'Saturdays are silly with Fish Bingo and Grand Prix throughout the day!'),
 24: ('Ides of March', 'Beware the Ides of March! Stop the Back Stabber Cogs from invading Toontown!'),
 26: ('Halloween Decor', 'Celebrate Halloween as spooky trees and streetlights transform Toontown!'),
 28: ('Winter Invasion', 'The Sellbots are on the loose spreading their cold sales tactics!'),
 29: ("April Toons' Week", "Celebrate April Toons' Week - a holiday built by Toons for Toons!"),
 33: ('Sellbot Surprise 1', 'Sellbot Surprise! Stop the Cold Caller Cogs from invading Toontown!'),
 34: ('Sellbot Surprise 2', 'Sellbot Surprise! Stop the Name Dropper Cogs from invading Toontown!'),
 35: ('Sellbot Surprise 3', 'Sellbot Surprise! Stop the Glad Hander Cogs from invading Toontown!'),
 36: ('Sellbot Surprise 4', 'Sellbot Surprise! Stop the Mover & Shaker Cogs from invading Toontown!'),
 37: ('A Cashbot Conundrum 1', 'A Cashbot Conundrum. Stop the Short Change Cogs from invading Toontown!'),
 38: ('A Cashbot Conundrum 2', 'A Cashbot Conundrum. Stop the Penny Pincher Cogs from invading Toontown!'),
 39: ('A Cashbot Conundrum 3', 'A Cashbot Conundrum. Stop the Bean Counter Cogs from invading Toontown!'),
 40: ('A Cashbot Conundrum 4', 'A Cashbot Conundrum. Stop the Number Cruncher Cogs from invading Toontown!'),
 41: ('The Lawbot Gambit 1', 'The Lawbot Gambit. Stop the Bottom Feeder Cogs from invading Toontown!'),
 42: ('The Lawbot Gambit 2', 'The Lawbot Gambit. Stop the Double Talker Cogs from invading Toontown!'),
 43: ('The Lawbot Gambit 3', 'The Lawbot Gambit. Stop the Ambulance Chaser Cogs from invading Toontown!'),
 44: ('The Lawbot Gambit 4', 'The Lawbot Gambit. Stop the Back Stabber Cogs from invading Toontown!'),
 45: ('The Trouble With Bossbots 1', 'The Trouble with Bossbots. Stop the Flunky Cogs from invading Toontown!'),
 46: ('The Trouble With Bossbots 2', 'The Trouble with Bossbots. Stop the Pencil Pusher Cogs from invading Toontown!'),
 47: ('The Trouble With Bossbots 3', 'The Trouble with Bossbots. Stop the Micromanager Cogs from invading Toontown!'),
 48: ('The Trouble With Bossbots 4', 'The Trouble with Bossbots. Stop the Downsizer Cogs from invading Toontown!'),
 49: ('Jellybean Day', 'Celebrate Jellybean Day with double Jellybean rewards at parties!'),
 53: ('Cold Caller Invasion', 'Stop the Cold Caller Cogs from invading Toontown!'),
 54: ('Bean Counter Invasion', 'Stop the Bean Counter Cogs from invading Toontown!'),
 55: ('Double Talker Invasion', 'Stop the Double Talker Cogs from invading Toontown!'),
 56: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 57: ('Caroling', 'Sing for your Snowman Head! See the Blog for details!'),
 59: ("ValenToon's Day", "Celebrate ValenToon's Day from Feb 09 to Feb 16!"),
 72: ('Yesman Invasion', 'Stop the Yesman Cogs from invading Toontown!'),
 73: ('Tightwad Invasion', 'Stop the Tightwad Cogs from invading Toontown!'),
 74: ('Telemarketers Invasion', 'Stop the Telemarketer Cogs from invading Toontown!'),
 75: ('Head Hunter Invasion', 'Stop the Head Hunter Cogs from invading Toontown!'),
 76: ('Spin Doctor Invasion', 'Stop the Spin Doctor Cogs from invading Toontown!'),
 77: ('Moneybags Invasion', 'Stop the Money Bags from invading Toontown!'),
 78: ('Two-Face Invasion', 'Stop the Two-\x04Faces from invading Toontown!'),
 79: ('Mingler Invasion', 'Stop the Mingler Cogs from invading Toontown!'),
 80: ('Loan Shark Invasion', 'Stop the Loan Shark Cogs from invading Toontown!'),
 81: ('Corporate Raider Invasion', 'Stop the Corporate Raider Cogs from invading Toontown!'),
 82: ('Robber Baron Invasion', 'Stop the Robber Baron Cogs from invading Toontown!'),
 83: ('Legal Eagle Invasion', 'Stop the Legal Eagle Cogs from invading Toontown!'),
 84: ('Big Wig Invasion', 'Stop the Big Wig Cogs from invading Toontown!'),
 85: ('Big Cheese Invasion', 'Stop the Big Cheese Cogs from invading Toontown!'),
 86: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 87: ('Mover And Shaker Invasion', 'Stop the Mover & Shaker Cogs from invading Toontown!'),
 88: ('Double Talker Invasion', 'Stop the Double Talkers Cogs from invading Toontown!'),
 89: ('Penny Pincher Invasion', 'Stop the Penny Pinchers Cogs from invading Toontown!'),
 90: ('Name Dropper Invasion', 'Stop the Name Dropper Cogs from invading Toontown!'),
 91: ('Ambulance Chaser Invasion', 'Stop the Ambulance Chaser Cogs from invading Toontown!'),
 92: ('Micro Manager Invasion', 'Stop the Micro Manager Cogs from invading Toontown!'),
 93: ('Number Cruncher Invasion', 'Stop the Number Cruncher Cogs from invading Toontown!'),
 95: ('Victory Parties', 'Celebrate our historic triumph against the Cogs!'),
 96: ('Operation: Storm Sellbot', "Sellbot HQ is open to everyone. Let's go fight the V.P.!"),
 97: ('Double Bean Days - Trolley Games', ''),
 98: ('Double Bean Days - Fishing', ''),
 99: ('Jellybean Week', 'Celebrate Jellybean Week with double Jellybean rewards!'),
 101: ("Top Toons New Year's Day Marathon", "Chances to win every hour! See the What's New Blog for details!"),
 105: ('Toons go GREEN!', 'Toons make a green scene at Green Bean Jeans on Oak Street in Daisy Gardens!')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
TimeZone = 'US/Pacific'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-\x04O-\x04Matic'
CogdoBarrelRoomTitle = 'Stomper Room'
CogdoBarrelIntroMovieDialogue = 'Good work! You\'ve halted the Stomp-\x04O-\x04Matic and are now able to collect some of the stolen Laff Barrels, but make sure to hurry before the Cogs come!'
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The COGS are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The COGS are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoMazeGameTitle = 'Mover & Shaker\nField Office'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers have our Jokes, and they've locked the exit!", 'Come in, Toons!  Mover & Shaker COGS have taken our jokes and have locked the exit!'), ('Fill water balloons at coolers, and throw them at Cogs!  Small Cogs drop Jokes; BIG COGS drop the pass code to open the exit.', "You'll need to fill water balloons at water coolers and throw them at Cogs.  Small Cogs drop jokes while BIG COGS have the pass code."), ('The more Jokes you rescue, the bigger your Toon-\x04Up at the end. Good luck!', "You'll get a bigger Toon-\x04Up if you pick up more Jokes.  Have fun!"))
CogdoMazeGameDoorOpens = 'THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER TOON-UP'
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG COGS!"
CogdoMazeGameWaitingForToons = 'Waiting for other Toons...'
CogdoMazeGameTimeOut = 'Oh no, time ran out! You lost your jokes.'
CogdoMazeGameTimeAlert = 'Hurry up! 60 seconds to go!'
CogdoMazeGameBossGuiTitle = 'BIG COGS:'
CogdoMazeFindHint = 'Find a Water Cooler'
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon"
CogdoMazeSquashHint = 'Falling objects pop your balloon'
CogdoMazeBossHint = 'BIG COGS take two hits to defeat'
CogdoMazeMinionHint = 'Smaller Cogs drop jokes'
CogdoFlyingGameTitle = 'Legal Eagle Offices'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and Cogs along the way, and don't forget to refuel your propeller!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our Stomp-\x04O-\x04Matic, and there's nothing you can do about it!", "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameWaiting = 'Waiting for other Toons%s'
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressCtrlToFly = "Press 'Ctrl' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'You made it on time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The Legal Eagles took all your memos!'
CogdoElevatorRewardLaff = 'Great job, Toons!\nYou get a Toon-Up from the jokes you saved!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s.'
CogdoExecutiveSuiteToonThankYouLawbot = 'Thanks for the rescue!\nThe Lawbots have left behind some sprocket awards that you can use to buy new things in your cattlelog!'
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = {1: 'Amusing Ascent!',
 2: 'Silly Surge!',
 3: 'Ridiculous Rise!',
 4: 'Giggle Growth!',
 5: 'Funny Fueling!',
 6: 'Batty Boost!',
 7: 'Crazy Climb!',
 8: 'Jolly Jump!',
 9: 'Loony Lift!',
 10: 'Hilarity Hike!',
 11: 'Insanity Increase!',
 12: 'Cracked-Uptick!'}
InteractivePropTrackBonusTerms = {0: 'Terrific Toon-Up!',
 1: '',
 2: '',
 3: 'Splendid Sound!',
 4: 'Thrilling Throw!',
 5: 'Super Squirt!',
 6: ''}
PlayingCardUnknown = 'Card Name is unknown'
SpellbookPageTitle = 'Spellbook'
WordPageTabTitle = 'Spellbook'
WordPageHelp = 'This page contains a list of all of the Magic Words that can be used in-game.'
WordPageSearch = 'Search'
WordPageActivator = 'Activator: '
WordPageTotal = 'Total Words: '
WordPageCurrent = 'Selected: '
WordPageNA = 'N/A'
WordPageCopyToChat = 'Copy To Chat'
WordPageMoreInfo = 'More Info'
WordPageDescription = 'Description: '
WordPageExample = 'Example: '
WordPageAliases = 'Aliases: '
WordPageAccessLevel = 'Required Access Level: '
ClothingPageTitle = 'Clothing'
ClothingPageShirt = 'Shirt IDs'
ClothingPageSleeve = 'Sleeve IDs'
ClothingPageShort = 'Shorts IDs'
AccessoriesPageHeadTab = 'Head\nAccessories'
AccessoriesPageBodyTab = 'Body\nAccessories'
AccessoriesPageHead = 'Head Accessories'
AccessoriesPageBody = 'Body Accessories'
AccessoriesPageHat = 'Hat IDs'
AccessoriesPageGlasses = 'Glasses IDs'
AccessoriesPageBackpack = 'Backpack IDs'
AccessoriesPageShoes = 'Shoes IDs'
TeleportGUITitle = 'Teleport'
TeleportGUITeleport = 'Go!'