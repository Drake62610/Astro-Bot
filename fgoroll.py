import csv
import math
import random

servantsDB = 'servantsDB.csv'
essencesDB = 'essencesDB.csv'

def getServant(servName):
	with open(servantsDB,'rb') as data:
		file = csv.reader(servantsDB)
		for line in data:
			if line[0]==servName:
				data.close
				return Servant(line[0],line[2],line[1])
	data.close
	return Servant()

def getEssence(essName):
	with open(essencesDB,'rb') as data:
		file = csv.reader(essencesDB)
		for line in data:
			if line[0]==essName:
				data.close
				return Essence(line[0],line[1])
	data.close
	return Essence

class Servant:
	name,stars,sclass = '','',''
	def __init__(self,name="notfound",stars=0,sclass="unknown"):
		self.name = name
		self.stars = stars
		self.sclass = sclass

class Essence:
	name,stars='',''
	def __init__(self,name="notfound",stars=0):
		self.name = name
		self.stars = stars

class Campaign:
	def __init__(self,title,featured_servants,featured_essences,base_ce_override_3="",base_ce_override_4="",base_ce_override_5="",base_servant_override_3="",base_servant_override_4="",base_servant_override_5=""):
		self.title = title
		self.featured_servants = featured_servants
		self.featured_essences = featured_essences
		self.base_ce_override_3 = base_ce_override_3
		self.base_ce_override_4 = base_ce_override_4
		self.base_ce_override_5 = base_ce_override_5
		self.base_servant_override_3 = base_servant_override_3
		self.base_servant_override_4 = base_servant_override_4
		self.base_servant_override_5 = base_servant_override_5

class Gacha:

	fiveStarBase,fiveStarStory,fourStarBase,fourStarStory,threeStarBase,threeStarStory,fiveStarEss,fourStarEss = '','','','','','','',''
	campaigns, currFiveStars, currFourStars, currThreeStars = [], [], [], []

	currFeatured3S, currFeatured4S, currFeatured5S = [], [], []
	currFeatured3E, currFeatured4E, currFeatured5E = [], [], []

	currFourStars = []
	currThreeStars = []
	def rawInit(self):
		#Amai : This needs to be updated manually for now
		self.fiveStarBase = ["Altria Pendragon", "Altera", "Zhuge Liang (El-Melloi II)", "Vlad III", "Jeanne d'Arc", "Orion", "Francis Drake", "Tamamo no Mae", "Jack the Ripper", "Mordred", "Nightingale"]
		self.fiveStarStory = ["Nikola Tesla", "Queen Medb", "Cu Chulainn (Alter)"]

		self.fourStarBase = ["Siegfried", "Chevalier d'Eon", "EMIYA", "Atalante", "Elisabeth Bathory", "Anne Bonny & Mary Read", "Marie Antoinette", "Saint Martha", "Stheno", "Carmilla", "Heracles", "Lancelot", "Tamamo Cat", "Nursery Rhyme", "Frankenstein"]
		self.fourStarStory = ["Medea (Lily)", "Nero Claudius", "Altria Pendragon (Alter)", "Altria Pendragon (Lancer Alter)", "Li Shuwen", "Thomas Edison"]

		self.threeStarBase = ["Gaius Julius Caesar", "Gilles de Rais", "Robin Hood", "David", "Euryale", "Cu Chulainn", "Cu Chulainn (Prototype)", "Romulus", "Hektor", "Medusa", "Boudica", "Ushiwakamaru", "Alexander", "Medea", "Mephistopheles", "Jing Ke", "Lu Bu Fengxian", "Darius III", "Kiyohime", "Diarmuid ua Duibhne", "Fergus mac Roich",  "Paracelsus von Hohenheim", "Charles Babbage", "Henry Jekyll & Hyde"]
		self.threeStarStory = ["Cu Chulainn (Caster)", "Gilles de Rais (Caster)"]

		self.fiveStarEss = ["Formal Craft", "Imaginary Around", "Limited/Zero Over", "Kaleidoscope", "Heaven's Feel", "Prisma Cosmos", "The Black Grail", "Victor of the Moon", "Another Ending", "A Fragment of 2030", "500-Year Obsession"]

		self.fourStarEss = ["Iron-Willed Training", "Primeval Curse", "Projection", "Gandr", "Verdant Sound of Destruction", "Gem Magecraft: Antumbra", "Be Elegant", "The Imaginary Element", "Divine Banquet", "Angel's Song", "Seal Designation Enforcer", "Holy Shroud of Magdalene", "With One Strike", "Code Cast", "Knight's Dignity", "Awakened Will", "Necromancy", "Golden Millennium Tree"]

		# OLD ONES: var threeStarEss = ["Azoth Blade", "False Attendant's Writings", "The Azure Black Keys", "The Verdant Black Keys", "The Crimson Black Keys", "Rin's Pendant", "Spell Tome", "Dragon's Meridian", "Sorcery Ore", "Dragonkin", "Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower"]
		# TODO need to add these ce's first

		self.threeStarEss = ["Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower", "Ryudoji Temple", "Mana Gauge", "Elixir of Love", "Storch Ritter", "Hermitage", "Motored Cuirassier", "Stuffed Lion", "Lugh's Halo"]

	def initCampaigns(self):
		#Amai : This needs to be updated manually for now
		title = "Sanzang Coming To The West"
		featured_servants = ["Xuanzang Sanzang","Li Shuwen","David","Lu Bu Fengxian"]
		featured_essences = ["GO WEST!!","True Samadhi Fire","All Three Together"]
		self.campaigns.append(Campaign(title,featured_servants,featured_essences))

	def initGacha(self):
		self.currFiveStars = []
		self.currFourStars = []
		self.currThreeStars = []

		self.currFiveStars = self.fiveStarBase
		self.currFourStars = self.fourStarBase
		self.currThreeStars = self.threeStarBase
		self.currFiveStarEss = self.fiveStarEss
		self.currFourStarEss = self.fourStarEss
		self.currThreeStarEss = self.threeStarEss




		#servantsPulled = [], essencesPulled = [] Amai : not using these for now

		#featured rates estimated from excel spreadsheet
		self.featured5sChance, self.featured4sChance, self.featured3sChance = 67, 67, 20
		self.featured5eChance, self.featured4eChance, self.featured3eChance = 45, 33, 20

	def __init__(self):
		self.rawInit()
		self.initGacha()
		self.initCampaigns()

	def changeMode(self,mode):
		self.currFeatured3S = []
		self.currFeatured4S = []
		self.currFeatured5S = []
		self.currFeatured3E = []
		self.currFeatured4E = []
		self.currFeatured5E = []

		if mode == "Story":
			self.currFiveStars = self.fiveStarBase + self.fiveStarStory
			self.currFourStars = self.fourStarBase + self.fourStarStory
			self.currThreeStars = self.threeStarBase + self.threeStarStory

		else:
			self.currFiveStars = self.fiveStarBase
			self.currFourStars = self.fourStarBase
			self.currThreeStars = self.threeStarBase

			for i in range (0,len(self.campaigns)):
				if mode == campaigns[i].title:
					featuredServants = self.campaigns[i].featured_servants
					featuresEssences = self.campaigns[i].featured_essences

					if campaigns[i].base_servant_override_5:
						self.currFiveStars = self.campaigns[i].base_servant_override_5
					if campaigns[i].base_servant_override_4:
						self.currFourStars = self.campaigns[i].base_servant_override_4
					if campaigns[i].base_servant_override_3:
						self.currThreeStars = self.campaigns[i].base_servant_override_3
					if campaigns[i].base_ce_override_5:
						self.currFiveStarEss = self.campaigns[i].base_ce_override_5
					if campaigns[i].base_ce_override_4:
						self.currFourStarEss = self.campaigns[i].base_ce_override_4
					if campaigns[i].base_ce_override_3:
						self.currThreeStarEss = self.campaigns[i].base_ce_override_3

					for j in range (0,len(self.featuredServants)):
						currServant = self.featuredServants[j]
						servantObj = getServant(currServant)
						stars = servantObj.stars
						if stars==3:
							self.currFeatured3S.append(currServant)
						elif stars==4:
							self.currFeatured4S.append(currServant)
						elif stars==5:
							self.currFeatured5S.append(currServant)

					for j in range (0,len(featuredEssences)):
						currEssence = featuredEssences[j]
						essObj = getServant(currServant)
						stars = essObj.stars
						if stars==3:
							self.currFeatured3E.append(currEssence)
						elif stars==4:
							self.currFeatured4E.append(currEssence)
						elif stars==5:
							self.currFeatured5E.append(currEssence)

	def checkFeatured(self,roll,chance):
		return roll < chance

	def pullEssence(self,stars):
		featuredChance = math.floor(random.random()*100)
		pullFeatured = False
		essence=""

		if stars==3:
			pullFeatured = self.checkFeatured(featuredChance,self.featured3eChance)
			essence = self.pullFeaturedObj(pullFeatured,self.currFeatured3E,self.currThreeStarEss)

		elif stars==4:
			pullFeatured = self.checkFeatured(featuredChance,self.featured4eChance)
			essence = self.pullFeaturedObj(pullFeatured,self.currFeatured4E,self.currFourStarEss)

		else:
			pullFeatured = self.checkFeatured(featuredChance,self.featured5eChance)
			essence = self.pullFeaturedObj(pullFeatured,self.currFeatured5E,self.currFiveStarEss)

		essenceObj = getEssence(essence)
		return essenceObj

	def pullServant(self,stars):
		featuredChance = math.floor(random.random()*100)
		#50% chance that it pulls from the featured list
		pullFeatured = False
		servant=""

		if stars==3:
			pullFeatured = self.checkFeatured(featuredChance,self.featured3sChance)
			servant = self.pullFeaturedObj(pullFeatured,self.currFeatured3S,self.currThreeStars)

		elif stars==4:
			pullFeatured = self.checkFeatured(featuredChance,self.featured4sChance)
			servant = self.pullFeaturedObj(pullFeatured,self.currFeatured4S,self.currFourStars)

		else:
			pullFeatured = self.checkFeatured(featuredChance,self.featured5sChance)
			servant = self.pullFeaturedObj(pullFeatured,self.currFeatured5S,self.currFiveStars)

		servantObj = getServant(servant)
		return servantObj

	def pullFeaturedObj(self,featured,currFeatured,currs):
		if featured and len(currFeatured)>0:
			idx = math.floor(random.random() * len(currFeatured))
			return currFeatured[idx]

		else:
			idx = math.floor(random.random() * len(currs))
			return currs[idx]

	def simulate(self,num, isTicket):
		num = int(num)
		pulledServant = False
		pulledHigh = False
		result = []
		for i in range(0,num):
			if i==9 and not pulledServant and not isTicket:
				self.pullServant(3,i)
				continue

			if i==8 and not pulledHigh and not isTicket:
				#4x higher chance to pull essence than servant
				rand = math.floor(random.random()*100)+1
				if rand <= 80:
					self.pullEssence(4)
				else:
					pullServant = True
					self.pullServant(4)
				continue

			rarityNum = math.floor(random.random()*100)+1
			#pulled 3* servant
			if rarityNum < 40:
				pulledServant = True
				result.append(self.pullServant(3))
			#pulled 4* essence
			elif rarityNum < 52:
				pulledHigh = True
				result.append(self.pullEssence(4))
			#pulled 4* servant
			elif rarityNum < 55:
				pulledServant = True
				pulledHigh = True
				result.append(self.pullServant(4))
			#pulled * servant
			elif rarityNum < 56:
				pulledServant = True
				pulledHigh = True
				result.append(self.pullServant(5))
			#pulled 3* essence
			elif rarityNum < 96:
				result.append(self.pullEssence(3))
			#pulled 5* essence
			else:
				pulledHigh = True
				result.append(self.pullEssence(5))

			return result

	def reset():
		servantsPulled = []
		essencesPulled = []
