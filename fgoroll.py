import csv
import math

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
	def __init__(self,name="notfound",stars=0,sclass="unknown"):
		self.name = name
		self.stars = stars
		self.sclass = sclass
		
class Essence:
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
	def __init__(self):
		rawInit()
		initGacha()
		initCampaigns()

	def rawInit():
		#Amai : This needs to be updated manually for now
		fiveStarBase = ["Altria Pendragon", "Altera", "Zhuge Liang (El-Melloi II)", "Vlad III", "Jeanne d'Arc", "Orion", "Francis Drake", "Tamamo no Mae", "Jack the Ripper", "Mordred", "Nightingale"]
		fiveStarStory = ["Nikola Tesla", "Queen Medb", "Cu Chulainn (Alter)"]

		fourStarBase = ["Siegfried", "Chevalier d'Eon", "EMIYA", "Atalante", "Elisabeth Bathory", "Anne Bonny & Mary Read", "Marie Antoinette", "Saint Martha", "Stheno", "Carmilla", "Heracles", "Lancelot", "Tamamo Cat", "Nursery Rhyme", "Frankenstein"]
		fourStarStory = ["Medea (Lily)", "Nero Claudius", "Altria Pendragon (Alter)", "Altria Pendragon (Lancer Alter)", "Li Shuwen", "Thomas Edison"]

		threeStarBase = ["Gaius Julius Caesar", "Gilles de Rais", "Robin Hood", "David", "Euryale", "Cu Chulainn", "Cu Chulainn (Prototype)", "Romulus", "Hektor", "Medusa", "Boudica", "Ushiwakamaru", "Alexander", "Medea", "Mephistopheles", "Jing Ke", "Lu Bu Fengxian", "Darius III", "Kiyohime", "Diarmuid ua Duibhne", "Fergus mac Roich",  "Paracelsus von Hohenheim", "Charles Babbage", "Henry Jekyll & Hyde"]
		threeStarStory = ["Cu Chulainn (Caster)", "Gilles de Rais (Caster)"]

		fiveStarEss = ["Formal Craft", "Imaginary Around", "Limited/Zero Over", "Kaleidoscope", "Heaven's Feel", "Prisma Cosmos", "The Black Grail", "Victor of the Moon", "Another Ending", "A Fragment of 2030", "500-Year Obsession"]
			
		fourStarEss = ["Iron-Willed Training", "Primeval Curse", "Projection", "Gandr", "Verdant Sound of Destruction", "Gem Magecraft: Antumbra", "Be Elegant", "The Imaginary Element", "Divine Banquet", "Angel's Song", "Seal Designation Enforcer", "Holy Shroud of Magdalene", "With One Strike", "Code Cast", "Knight's Dignity", "Awakened Will", "Necromancy", "Golden Millennium Tree"]
			
		# OLD ONES: var threeStarEss = ["Azoth Blade", "False Attendant's Writings", "The Azure Black Keys", "The Verdant Black Keys", "The Crimson Black Keys", "Rin's Pendant", "Spell Tome", "Dragon's Meridian", "Sorcery Ore", "Dragonkin", "Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower"]
		# TODO need to add these ce's first
			
		threeStarEss = ["Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower", "Ryudoji Temple", "Mana Gauge", "Elixir of Love", "Storch Ritter", "Hermitage", "Motored Cuirassier", "Stuffed Lion", "Lugh's Halo"]

	def initCampaigns():
		#Amai : This needs to be updated manually for now
		title = "Sanzang Coming To The West"
		featured_servants = ["Xuanzang Sanzang","Li Shuwen","David","Lu Bu Fengxian"]
		featured_essences = ["GO WEST!!","True Samadhi Fire","All Three Together"]
		campaigns.append(Campaign(title,featured_servants,featured_essences))
		
	def initGacha():
		currFiveStars = []
		currFourStars = []
		currThreeStars = []

		currFiveStars = fiveStarBase;
		currFourStars = fourStarBase;
		currThreeStars = threeStarBase;
		currFiveStarEss = fiveStarEss;
		currFourStarEss = fourStarEss;
		currThreeStarEss = threeStarEss;

		currFeatured3S = [], currFeatured4S = [], currFeatured5S = []
		currFeatured3E = [], currFeatured4E = [], currFeatured5E = []

		campaigns = []
		#servantsPulled = [], essencesPulled = [] Amai : not using these for now

		#featured rates estimated from excel spreadsheet
		featured5sChance = 67, featured4sChance = 67, featured3sChance = 20;
		featured5eChance = 45, featured4eChance = 33, featured3eChance = 20;
		
	def changeMode(mode):
		currFeatured3S = []
		currFeatured4S = []
		currFeatured5S = []
		currFeatured3E = []
		currFeatured4E = []
		currFeatured5E = []
		
		if mode == "Story":
			currFiveStars = fiveStarBase + fiveStarStory
			currFourStars = fourStarBase + fourStarStory
			currThreeStars = threeStarBase + threeStarStory
			
		else:
			currFiveStars = fiveStarBase
			currFourStars = fourStarBase
			currThreeStars = threeStarBase
			
			for i in range (0,len(campaigns)):
				if mode == campaigns[i].title:
					featuredServants = campaigns[i].featured_servants
					featuresEssences = campaigns[i].featured_essences
					
					if campaigns[i].base_servant_override_5:
						currFiveStars = campaigns[i].base_servant_override_5
					if campaigns[i].base_servant_override_4:
						currFourStars = campaigns[i].base_servant_override_4
					if campaigns[i].base_servant_override_3:
						currThreeStars = campaigns[i].base_servant_override_3
					if campaigns[i].base_ce_override_5:
						currFiveStarEss = campaigns[i].base_ce_override_5
					if campaigns[i].base_ce_override_4:
						currFourStarEss = campaigns[i].base_ce_override_4
					if campaigns[i].base_ce_override_3:
						currThreeStarEss = campaigns[i].base_ce_override_3
						
					for j in range (0,len(featuredServants)):
						currServant = featuredServants[j]
						servantObj = getServant(currServant)
						stars = servantObj.stars
						if stars==3:
							currFeatured3S.append(currServant)
						elif stars==4:
							currFeatured4S.append(currServant)
						elif stars==5:
							currFeatured5S.append(currServant)
					
					for j in range (0,len(featuredEssences)):
						currEssence = featuredEssences[j]
						essObj = getServant(currServant)
						stars = essObj.stars
						if stars==3:
							currFeatured3E.append(currEssence)
						elif stars==4:
							currFeatured4E.append(currEssence)
						elif stars==5:
							currFeatured5E.append(currEssence)
							
	def simulate(num, isTicket):
		pulledServant = False
		pulledHigh = False
		result = []
		for i in range(0,num):
			if i==9 and not pulledServant and not isTicket:
				pullServant(3,i)
				continue
				
			if i==8 and not pulledHigh and not isTicket:
				#4x higher chance to pull essence than servant
				rand = math.floor(random()*100)+1
				if rand <= 80:
					pullEssence(4)
				else:
					pullServant = True
					pullServant(4)
				continue
				
			rarityNum = math.floor(random()*100)+1
			#pulled 3* servant
			if rarityNum < 40:
				pulledServant = True
				result.append(pullServant(3))
			#pulled 4* essence
			elif rarityNum < 52:
				pulledHigh = True
				result.append(pullEssence(4))
			#pulled 4* servant
			elif rarityNum < 55:
				pulledServant = True
				pulledHigh = True
				result.append(pullServant(4))
			#pulled * servant
			elif rarityNum < 56:
				pulledServant = True
				pulledHigh = True
				result.append(pullServant(5))
			#pulled 3* essence
			elif rarityNum < 96:
				result.append(pullEssence(3))
			#pulled 5* essence
			else:
				pulledHigh = True
				result.append(pullEssence(5))
							
			return result
			
	def pullEssence(stars):
		featuredChance = math.floor(random()*100)
		pullFeatured = False
		essence=""
		
		if stars==3:
			pullFeatured = checkFeatured(featuredChance,featured3eChance)
			essence = pullFeaturedObj(pullFeatured,currFeatured3E,currThreeStarEss)
		
		elif stars==4:
			pullFeatured = checkFeatured(featuredChance,featured4eChance)
			essence = pullFeaturedObj(pullFeatured,currFeatured4E,currFourStarEss)
			
		else:
			pullFeatured = checkFeatured(featuredChance,featured5eChance)
			essence = pullFeaturedObj(pullFeatured,currFeatured5E,currFiveStarEss)
			
		essenceObj = getEssence(essence)
		return essenceObj
		
	def pullServant(stars):
		featuredChance = math.floor(random()*100)
		#50% chance that it pulls from the featured list
		pullFeatured = False
		servant=""
		
		if stars==3:
			pullFeatured = checkFeatured(featuredChance,featured3sChance)
			servant = pullFeaturedObj(pullFeatured,currFeatured3S,currThreeStars)
			
		elif stars==4:
			pullFeatured = checkFeatured(featuredChance,featured4sChance)
			servant = pullFeaturedObj(pullFeatured,currFeatured4S,currFourStars)
			
		else:
			pullFeatured = checkFeatured(featuredChance,featured5sChance)
			servant = pullFeaturedObj(pullFeatured,currFeatured5S,currFiveStars)
			
		servantObj = getServant(servant)
		return servantObj
		
	def checkFeatured(roll,chance):
		return roll < chance
		
	def pullFeaturedObj(featured,currFeatured,currs):
		if featured and len(currFeatured)>0:
			idx = math.floor(random() * len(currFeatured))
			return currFeatured[idx]
			
		else:
			idx = math.floor(random() * len(currs))
			return currs[idx]
			
	def reset():
		servantsPulled = []
		essencesPulled = []
		
@bot.command()
async def roll(number,mode,isTicket):
	gacha = Gacha()
	gacha.changeMode(mode)
	result = gacha.simulate(number,isTicket)
	msg=""
	for pulled in result:
		msg = msg + pulled.name + "   " + pulled.stars + "*\n"
	
	await bot.send_message(bot.get_channel('178532977901305857'), msg)
		