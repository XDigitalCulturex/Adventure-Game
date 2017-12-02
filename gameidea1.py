# -*- coding: utf8 -*-
from __future__ import print_function

import csv
import os
import random
import urllib
import json

##print os.listdir(r"/sdcard")
import sys

## must be downloaded
##import PyQt4
import openpyxl
from xlrd import open_workbook

creatureTemplates = [{"creature":"WereCroc", "stories":[{"NONE":"A tormented man asks you to kill him. If he isn't, he will return later as a werecroc."}, {"NONE":"A panicked villager vears for his life after nearly all his people have been eaten. Few remain, he believes one of them is a traitor."}], "clues":[{"Debris": ["Scales", "Digested Carcasses"]}], "hit locations":["Long Tail","Soft Belly","Feet","Clawed Hands","Upper Jaw", "Lower Jaw","Rigged Back", "Between the eyes"], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Giant Snake", "stories":[{"NONE": "Come across a servant who has lost his Master's precious jewel. It occurred when a giant pet escaped."}, {"HUNTER":"A Ranger shares with you that a snake with a very valuable hide stalks the nearby area."}], "clues":[{"Debris": ["Scales"]}], "hit locations":["Long Tail","Head", "Soft Belly"], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Ogre Shaman", "stories":[{"SHAMAN":"Seeking ritual components, the spirt speaks and asks for your help"}, {"NONE":"You come across a middle aged woman, weeping. She reports that her youngest child was kidnapped."}], "clues":[{"Debris": ["Burnt Herbs"]}], "hit locations":["Horns","Face","Belly", "Loin Cloth", "Slender Legs","Arms","Muscular Back", "Arm Bands"], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Rune Dwarf", "stories":[{"NONE":"He has a greed for runic knowledge. He is twisted, seeing such knowledge in many things"}, {"DWARF":"His wife is enclosed in an eternal magical prison. He must learn of hte Runes to unlock the prison."}], "clues":[], "hit locations":["Head", "Arm","Leg","Groin","Chest","Stomach","Back","Neck","Foot","Hand","Knee"], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Elven Sword Master", "stories":[{"NONE":"A boastful champion will challenge any MARTIAL character to a test of skill."}, {"MALE":"She seeks a potential mate to join her in ruling her village and providing her with children. The suitor must prove himself by a quest."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Flouring Bandit Captain", "stories":[{"BANDIT":"Seeks your aid in dealing with some mercenaries that were hired to remove her band."}, {"NONE":"There is a knonw bounty on her head for burning a small village."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Preaching Cleric", "stories":[{"RELIGIOUS":"Seeks apostles to spread the word of the gods and acquire new followers."}, {"NONE":"Years of fanatical worship have turned him into an extremist who seeks to destroy all but the RIGHTEOUS"}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Golem Swordsman", "stories":[{"LIEGE":"Devoted to finding a noble master to guide him."}, {"NONE":"His creator seeks out to destroy those of a certain blood heritage."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Noble Sorceress", "stories":[{"NOBLE":"Invites the nobles to a courtly dinner nearby"}, {"VASSAL":"Seeks those without a Liege to work for her or she will subjugate them."}, {"NONE":"Familiar was captured while she was using it to explore and she needs help rescuing it."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Screaming Dwarf Champion", "stories":[{"SOLDIER":"Wishes to join forces in fighting to gain honor."}, {"NONE":"His whole family was killed and now he only wishes to die in battle."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Bow Ranger", "stories":[{"NONE":"Offers to take the people to a hidden refuge away from danger."}, {"NONE":"Paranoid and entrapped, tries to elude contact or fights."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Male Bow Bandit", "stories":[{"NONE":"If he has allies, he strikes victims from the shadows, otherwise, he likes to remain non-chalant."}, {"BANDIT":"He offers to keep an eye out for you after you help him sneak past patrols."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Lightbringer", "stories":[{"NONE":"In a selfless act of purity, she offers to cure curses and sickness."}, {"ZEALOT":"Asks for holy crusaders to bring light to the area and purge otherworldly entities."}, {"EVIL":"Screams out that she will purge the darkness and attacks."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Spear Border Guard", "stories":[{"NONE":"Suspiciously looks over passersby and if she accepts, she'll offer entry to areas she guards."}, {"NONE":"Raiders snuck by and then got away. She can't leave her post, but they must be found."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Ogre Clobberer", "stories":[{"NONE":"Can't swim, but he needs a precious item of his mother's that was thrown into a pool."}, {"NONE":"Bellows out his hunger for man flesh and attacks the meatiest target."}, {"GIANT":"Offers beer to the winner of an arm wrestling match."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Batwinged Helm Chaos Warrior", "stories":[{"FEMALE":"Requires a sacrifice upon his altar for a dark ritual."}, {"NONE":"Seeks an altar where he can perform a communion with his gods."}, {"RELIGIOUS":"Wishes to promote the power of all the old gods both 'Good' and 'Evil'."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Wereboar", "stories":[{"NONE":"A raging lunatic charges at you and quickly transforms into a man boar."}, {"NONE":"The figure barrels down another hallway, sniffing aggressively, obviously searching. At the end are rare herbs."}, {"LUNAR":"The mad ramblings of htis person end in volunteering to join your pack."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Robed Cultist", "stories":[{"NONE":"Seeks out tomes of forbidden knowledge and will attack if such things are spotted."}, {"DOOMED":"An ancient temple possesses a book that would bring forgotten rituals. He wants it."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Grave Vulture", "stories":[{"NONE":"The dead can speak through this vulture, this dead can only rest once its kiler is dead."}, {"ZEALOT":"This creature disturbs the resting dead adn must be vanquished."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Old Wizard", "stories":[{"NONE":"Seeks worthy adventurers for a future cause. Has placed an artifact behind danger for others to prve themselves and gain WORTHY"}, {"WORTHY":"He senses that you are of value and offers to travel with you to ehlp with a task of his later."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Yeti Men", "stories":[{"NONE":"Can't speak, only communicate through grunts and gestures. They are aggressive and will take what they want if it isn't offered."}, {"PRIMAL":"You can glean that these creatures need help with rebuilding a broken totem."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Hobgoblin Brothers", "stories":[{"SOLDIER":"Demand that you join their command and follow the superiors orders."}, {"NONE":"Are the vanguard of a regiment that seek to dominate the region. They won't fight if you run or submit."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Gorilla Chief", "stories":[{"PRIMAL":"Seeks to fight for Alpha, serving if lost, control if won."}, {"NONE":"Tries to scare off interlopers, but if they don't run, he will fight to the death to protect young."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Bluehaired Paladin", "stories":[{"NONE":"Seeks help to remove a faerie curse that has hampered her at completing her duties."}, {"NONE":"Adamantly demands that your turn back as a sacred site lies beyond, one dangerous to most."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Maritime Explorer", "stories":[{"NONE":"Needs a map of the local area while he nurses a leg injury."}, {"SURVIVAL":"Seeks to join travelling companions to get out far from here."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Dwarf Rogue", "stories":[{"NONE":"Evasive and dishonest, trying to evade authority types after stealing jewels."}, {"NONE":"Tries to be kind and interested all in an attempt to pick pocket someone."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Female Dwarf Blacksmith", "stories":[{"NONE":"Seeks a rare ingredient for a wine, sacred in nature."}, {"NONE":"There is a cave nearby with a rare metal, too dangerous for her to get on her own."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Shaolin Spear Lady", "stories":[{"NONE":"Needs someone to take her beer to a nearby customer."}, {"NONE":"Seeks a student, one of great patience to take as a pupil, and teach spear skills and CHI."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Bug Ranger", "stories":[{"NONE":"Xenophobic explorer that typically attacks on site unless extreme attempts at diplomacy are made."}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Bug Ninja", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Red Clan Lizards", "stories":[{"NONE":"As a group, screech a bloody war cry before throwing themselves at the enemy."}, {"SURVIVAL":"The nearby territory is marked by this clan. The only way to pacify them is to find their chief."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Starving Troll", "stories":[{"ARCANE":"A cursed item spotted on the troll gives the wearer an uncontrollable, unending hunger."}, {"NONE":"Anyone emitting a fire source will keep the troll at bay, all others are food."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Half-Orc War Veteran", "stories":[{"NONE":"Drunkenly tries to pick fights or strength contests."}, {"NONE":"Sober as a stone, so seriously asks for help in setting banners to mark claimed and defended territories."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Trash Goblins", "stories":[{"NONE":"Wish to follow ans scavenge remains in teh wake of adventurers."}, {"NONE":"Tell people how superior they are to ease them, ask for help and lure them into a trap."}], "clues":[], "hit locations":[], "size":"Small", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Manticore", "stories":[{"NONE":"Seeking out to recover a meal for its young."}, {"NONE":"A mad alchemist created this bastard creature. Evidence of magic tampering leads to seeking out the creator."}], "clues":[], "hit locations":[], "size":"Huge", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Fomorian", "stories":[{"NONE":"It must fight intruders, but it will even say that if its masters are properly tricked (fae), it will join them."}, {"HEALER":"This creature is evidence of a hideous mystical disease, the source of which must be nearby."}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Monk Temple Guards", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Skull Bearing Necromancer", "stories":[{"NONE":"An aura of death energy surrounds this man and works to empower and protect him."}, {"NOBLE":"He has stoeln the power of an ancient king and now found someone of the bloodline to steal."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Carrion Centipedes", "stories":[{"NONE":"Sense dead possessions and meat and will attack to get at them unless placated."}, {"NONE":"Under a nearby large piece of Debris, the nest of thsee things stinks of death. Disturbing it will cause them to lash out."}], "clues":[], "hit locations":[], "size":"Small", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Dark Beetles", "stories":[{"NATURE":"The glands of tehse beetles has a mystical use. Generally, they are non-hostile."}, {"NONE":"The beetles are subdued, moving about their tasks. Seems almost as if they are being domesticated."}], "clues":[], "hit locations":[], "size":"Small", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Kitsune", "stories":[{"ARTS":"Seek to share an exchange of creative endeavors, joining the worthy or giving a gift."}, {"NONE":"Believe that any they come across seek to outdo their cunning, attacking those not relingquishing."}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Raven Men", "stories":[{"NONE":"The are protectors of a tree village and admit any that seem trusting but watching from nearby."}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Lady Wanderer", "stories":[{"WISE":""}, {"NOMAD":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Giant Bat", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"WereBear", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Large", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"Great Horned Dark Paladin", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"Medium", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"", "picture_id":"", "keywords":[], "resources":[] } ,{"creature":"", "stories":[{"NONE":""}, {"NONE":""}], "clues":[], "hit locations":[], "size":"", "picture_id":"", "keywords":[], "resources":[] } ]

def powers():
  if os.path.exists(r"/sdcard/Download/powers.xlsx"):
    return r"/sdcard/Download/powers.xlsx"
  else:
    return r"./Gameidea/powers.xlsx"
monsterPics = r"https://drive.google.com/open?id=0B2hVzlUGJ_AMcnFZUm0tUDM1LXc"

def monsterBuild(attrs):
  wb = open_workbook(powers())
  for s in wb.sheets():
    values = []
    for row in range(s.nrows):
      col_value = []
      for col in range(s.ncols):
        value = (s.cell(row,col).value)
        try:
          value = str(int(value))
        except:
          pass
        col_value.append(value)
        values.append(col_value)
  var = list()
  maybe = list()
  while len(var)<6:
    for row in values:
      if row[0] in attrs:
        maybe.append(row)
    num = random.randint(1,len(maybe))
    var.append(maybe[num])
    maybe.remove(maybe[num])
  return var
  
attributes = ["Ranged","Armored","Divine", "Arcane", "Monstrous", "Bandit","Zealot"]

def numPlay():
  ans =raw_input("How many players do you have?")
  return int(ans)
  
class monster(object):
  def __init__(self):
    self.powers = monsterBuild(attributes)
    self.size = {"Small":2,"Medium":5,"Large":10,"Huge":20}
    self.setSize()
    self.monStar = {"Size":self.monSize,"Name":" ","HP":self.HP,"Powers":self.powers, "Picture":" "}
    self.monPic = ""
  def setSize(self):
    self.monSize = random.choice(self.size.keys())
    print (self.monSize)
    self.HP = numPlayers * self.size[self.monSize]
    print (self.HP)
  def resetMonster(self):
    self.powers = monsterBuild(attributes)
  def showStats(self):
    print (self.monStar.items())
  def getImage(self):
    test = urllib.urlopen(monsterPics + r"/files").read()
    print (test)
numPlayers = 3
curMonst = monster()
curMonst.showStats()
curMonst.getImage()


#############################################
##Start of the google drive code

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
  import argparse
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
  flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
  """Gets valid user credentials from storage.

  If nothing has been stored, or if the stored credentials are invalid,
  the OAuth2 flow is completed to obtain the new credentials.

  Returns:
    Credentials, the obtained credential.
  """
  home_dir = os.path.expanduser('~')
  credential_dir = os.path.join(home_dir, '.credentials')
  if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
  credential_path = os.path.join(credential_dir,
                  'drive-python-quickstart.json')

  store = Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
      credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
      credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
  return credentials

def main():
  """Shows basic usage of the Google Drive API.

  Creates a Google Drive API service object and outputs the names and IDs
  for up to 10 files.
  """
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('drive', 'v3', http=http)

  results = service.files().list(
    pageSize=10,fields="nextPageToken, files(id, name)").execute()
  items = results.get('files', [])
  if not items:
    print('No files found.')
  else:
    print('Files:')
    for item in items:
      print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
  main()

​monsterX = ​[{"creature":"WereCroc",
  "stories":[{"NONE":"A tormented man asks you to kill him. If he isn't, he will return later as a werecroc."},
             {"NONE":"A panicked villager vears for his life after nearly all his people have been eaten. Few remain, he believes one of them is a traitor."}],
           "clues":["Debris": ["Scales", "Digested Carcasses"]],
   "hit locations":["Long Tail","Soft Belly","Feet","Clawed Hands","Upper Jaw", "Lower Jaw","Rigged Back", "Between the eyes"],
  "size":"Large",
  "picture_id":"", "keywords":[], "resources":[]
  }
 ,{"creature":"Giant Snake",
   "stories":[{"NONE": "Come across a servant who has lost his Master's precious jewel. It occurred when a giant pet escaped."},
              {"HUNTER":"A Ranger shares with you that a snake with a very valuable hide stalks the nearby area."}],
         "clues":["Debris": ["Scales"],
   "hit locations":["Long Tail","Head", "Soft Belly"],
  "size":"Large",  
  "picture_id":"", "keywords":[], "resources":[]   
   }
 ,{"creature":"Ogre Shaman",
   "stories":[{"SHAMAN":"Seeking ritual components, the spirt speaks and asks for your help"},
              {"NONE":"You come across a middle aged woman, weeping. She reports that her youngest child was kidnapped."}],
      "clues":["Debris": ["Burnt Herbs"]],
   "hit locations":["Horns","Face","Belly", "Loin Cloth", "Slender Legs","Arms","Muscular Back", "Arm Bands"],
  "size":"Large",  
  "picture_id":"", "keywords":[], "resources":[]   
   }
 ,{"creature":"Rune Dwarf",
   "stories":[{"NONE":"He has a greed for runic knowledge. He is twisted, seeing such knowledge in many things"},
              {"DWARF":"His wife is enclosed in an eternal magical prison. He must learn of hte Runes to unlock the prison."}],
   "clues":[],
   "hit locations":["Head", "Arm","Leg","Groin","Chest","Stomach","Back","Neck","Foot","Hand","Knee"],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
  ,{"creature":"Female Elven Sword Master",
   "stories":[{"NONE":"A boastful champion will challenge any MARTIAL character to a test of skill."},
              {"MALE":"She seeks a potential mate to join her in ruling her village and providing her with children. The suitor must prove himself by a quest."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Flouring Bandit Captain",
   "stories":[{"BANDIT":"Seeks your aid in dealing with some mercenaries that were hired to remove her band."},
              {"NONE":"There is a knonw bounty on her head for burning a small village."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Preaching Cleric",
   "stories":[{"RELIGIOUS":"Seeks apostles to spread the word of the gods and acquire new followers."},
              {"NONE":"Years of fanatical worship have turned him into an extremist who seeks to destroy all but the RIGHTEOUS"}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Golem Swordsman",
   "stories":[{"LIEGE":"Devoted to finding a noble master to guide him."},
              {"NONE":"His creator seeks out to destroy those of a certain blood heritage."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Noble Sorceress",
   "stories":[{"NOBLE":"Invites the nobles to a courtly dinner nearby"},
              {"VASSAL":"Seeks those without a Liege to work for her or she will subjugate them."}
              {"NONE":"Familiar was captured while she was using it to explore and she needs help rescuing it."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Screaming Dwarf Champion",
   "stories":[{"SOLDIER":"Wishes to join forces in fighting to gain honor."},
              {"NONE":"His whole family was killed and now he only wishes to die in battle."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Bow Ranger",
   "stories":[{"NONE":"Offers to take the people to a hidden refuge away from danger."},
              {"NONE":"Paranoid and entrapped, tries to elude contact or fights."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Male Bow Bandit",
   "stories":[{"NONE":"If he has allies, he strikes victims from the shadows, otherwise, he likes to remain non-chalant."},
              {"BANDIT":"He offers to keep an eye out for you after you help him sneak past patrols."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Lightbringer",
   "stories":[{"NONE":"In a selfless act of purity, she offers to cure curses and sickness."},
              {"ZEALOT":"Asks for holy crusaders to bring light to the area and purge otherworldly entities."},
              {"EVIL":"Screams out that she will purge the darkness and attacks."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Spear Border Guard",
   "stories":[{"NONE":"Suspiciously looks over passersby and if she accepts, she'll offer entry to areas she guards."},
              {"NONE":"Raiders snuck by and then got away. She can't leave her post, but they must be found."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Ogre Clobberer",
   "stories":[{"NONE":"Can't swim, but he needs a precious item of his mother's that was thrown into a pool."},
              {"NONE":"Bellows out his hunger for man flesh and attacks the meatiest target."},
              {"GIANT":"Offers beer to the winner of an arm wrestling match."}],
   "clues":[],
   "hit locations":[],
  "size":"Large", 
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Batwinged Helm Chaos Warrior",
   "stories":[{"FEMALE":"Requires a sacrifice upon his altar for a dark ritual."},
              {"NONE":"Seeks an altar where he can perform a communion with his gods."},
              {"RELIGIOUS":"Wishes to promote the power of all the old gods both 'Good' and 'Evil'."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Wereboar",
   "stories":[{"NONE":"A raging lunatic charges at you and quickly transforms into a man boar."},
              {"NONE":"The figure barrels down another hallway, sniffing aggressively, obviously searching. At the end are rare herbs."},
              {"LUNAR":"The mad ramblings of htis person end in volunteering to join your pack."}],
   "clues":[],
   "hit locations":[],
  "size":"Large",
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Robed Cultist",
   "stories":[{"NONE":"Seeks out tomes of forbidden knowledge and will attack if such things are spotted."},
              {"DOOMED":"An ancient temple possesses a book that would bring forgotten rituals. He wants it."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Grave Vulture",
   "stories":[{"NONE":"The dead can speak through this vulture, this dead can only rest once its kiler is dead."},
              {"ZEALOT":"This creature disturbs the resting dead adn must be vanquished."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Old Wizard",
   "stories":[{"NONE":"Seeks worthy adventurers for a future cause. Has placed an artifact behind danger for others to prve themselves and gain WORTHY"},
              {"WORTHY":"He senses that you are of value and offers to travel with you to ehlp with a task of his later."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Yeti Men",
   "stories":[{"NONE":"Can't speak, only communicate through grunts and gestures. They are aggressive and will take what they want if it isn't offered."},
              {"PRIMAL":"You can glean that these creatures need help with rebuilding a broken totem."}],
   "clues":[],
   "hit locations":[],
  "size":"Large",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Hobgoblin Brothers",
   "stories":[{"SOLDIER":"Demand that you join their command and follow the superiors orders."},
              {"NONE":"Are the vanguard of a regiment that seek to dominate the region. They won't fight if you run or submit."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Gorilla Chief",
   "stories":[{"PRIMAL":"Seeks to fight for Alpha, serving if lost, control if won."},
              {"NONE":"Tries to scare off interlopers, but if they don't run, he will fight to the death to protect young."}],
   "clues":[],
   "hit locations":[],
  "size":"Large", 
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Bluehaired Paladin",
   "stories":[{"NONE":"Seeks help to remove a faerie curse that has hampered her at completing her duties."},
              {"NONE":"Adamantly demands that your turn back as a sacred site lies beyond, one dangerous to most."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Maritime Explorer",
   "stories":[{"NONE":"Needs a map of the local area while he nurses a leg injury."},
              {"SURVIVAL":"Seeks to join travelling companions to get out far from here."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Dwarf Rogue",
   "stories":[{"NONE":"Evasive and dishonest, trying to evade authority types after stealing jewels."},
              {"NONE":"Tries to be kind and interested all in an attempt to pick pocket someone."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Female Dwarf Blacksmith",
   "stories":[{"NONE":"Seeks a rare ingredient for a wine, sacred in nature."},
              {"NONE":"There is a cave nearby with a rare metal, too dangerous for her to get on her own."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Shaolin Spear Lady",
   "stories":[{"NONE":"Needs someone to take her beer to a nearby customer."},
              {"NONE":"Seeks a student, one of great patience to take as a pupil, and teach spear skills and CHI."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Bug Ranger",
   "stories":[{"NONE":"Xenophobic explorer that typically attacks on site unless extreme attempts at diplomacy are made."},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Bug Ninja",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Red Clan Lizards",
   "stories":[{"NONE":"As a group, screech a bloody war cry before throwing themselves at the enemy."},
              {"SURVIVAL":"The nearby territory is marked by this clan. The only way to pacify them is to find their chief."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Starving Troll",
   "stories":[{"ARCANE":"A cursed item spotted on the troll gives the wearer an uncontrollable, unending hunger."},
              {"NONE":"Anyone emitting a fire source will keep the troll at bay, all others are food."}],
   "clues":[],
   "hit locations":[],
  "size":"Large",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Half-Orc War Veteran",
   "stories":[{"NONE":"Drunkenly tries to pick fights or strength contests."},
              {"NONE":"Sober as a stone, so seriously asks for help in setting banners to mark claimed and defended territories."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Trash Goblins",
   "stories":[{"NONE":"Wish to follow ans scavenge remains in teh wake of adventurers."},
              {"NONE":"Tell people how superior they are to ease them, ask for help and lure them into a trap."}],
   "clues":[],
   "hit locations":[],
  "size":"Small",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Manticore",
   "stories":[{"NONE":"Seeking out to recover a meal for its young."},
              {"NONE":"A mad alchemist created this bastard creature. Evidence of magic tampering leads to seeking out the creator."}],
   "clues":[],
   "hit locations":[],
  "size":"Huge",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Fomorian",
   "stories":[{"NONE":"It must fight intruders, but it will even say that if its masters are properly tricked (fae), it will join them."},
              {"HEALER":"This creature is evidence of a hideous mystical disease, the source of which must be nearby."}],
   "clues":[],
   "hit locations":[],
  "size":"Large",  
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Monk Temple Guards",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Skull Bearing Necromancer",
   "stories":[{"NONE":"An aura of death energy surrounds this man and works to empower and protect him."},
              {"NOBLE":"He has stoeln the power of an ancient king and now found someone of the bloodline to steal."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Carrion Centipedes",
   "stories":[{"NONE":"Sense dead possessions and meat and will attack to get at them unless placated."},
              {"NONE":"Under a nearby large piece of Debris, the nest of thsee things stinks of death. Disturbing it will cause them to lash out."}],
   "clues":[],
   "hit locations":[],
  "size":"Small",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Dark Beetles",
   "stories":[{"NATURE":"The glands of tehse beetles has a mystical use. Generally, they are non-hostile."},
              {"NONE":"The beetles are subdued, moving about their tasks. Seems almost as if they are being domesticated."}],
   "clues":[],
   "hit locations":[],
  "size":"Small",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Kitsune",
   "stories":[{"ARTS":"Seek to share an exchange of creative endeavors, joining the worthy or giving a gift."},
              {"NONE":"Believe that any they come across seek to outdo their cunning, attacking those not relingquishing."}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Raven Men",
   "stories":[{"NONE":"The are protectors of a tree village and admit any that seem trusting but watching from nearby."},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Lady Wanderer",
   "stories":[{"WISE":""},
              {"NOMAD":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Giant Bat",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Large",  
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"WereBear",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Large",
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"Great Horned Dark Paladin",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"Medium",   
 "picture_id":"", "keywords":[], "resources":[]
   }
 ,{"creature":"",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"",   
 "picture_id":"", "keywords":[], "resources":[]
   }


 ,{"creature":"",
   "stories":[{"NONE":""},
              {"NONE":""}],
   "clues":[],
   "hit locations":[],
  "size":"",   
 "picture_id":"", "keywords":[], "resources":[]
   }

 ]
