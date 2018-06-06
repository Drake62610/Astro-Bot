import csv
import math
import random

servantsDB = 'servantsDB.csv'
essencesDB = 'essencesDB.csv'

def get_servant(servName):
    with open(servantsDB) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] == servName:
                csvfile.close
                return Servant(line[0], line[2], line[1])
    csvfile.close
    print("NOT FOUND: " + servName)
    return Servant()


def get_essence(essName):
    with open(essencesDB) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[1] == essName:
                csvfile.close
                return Essence(line[1], line[0])
    csvfile.close
    print("NOT FOUND: "+essName)
    return Essence()

class Servant:
    name, stars, sclass = '', '', ''

    def __init__(self, name="notfound", stars=0, sclass="unknown"):
        self.name = name
        self.stars = stars
        self.sclass = sclass


class Essence:
    name, stars = '', ''

    def __init__(self, name="notfound", stars=0):
        self.name = name
        self.stars = stars


class Campaign:
    title=''
    featured_servants,featured_essences=[],[]
    base_ce_override_3,base_ce_override_4,base_ce_override_5=[],[],[]
    base_servant_override_3,base_servant_override_4,base_servant_override_5=[],[],[]

    def __init__(self, title, featured_servants, featured_essences, base_ce_override_3="", base_ce_override_4="",
                 base_ce_override_5="", base_servant_override_3="", base_servant_override_4="",
                 base_servant_override_5=""):
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
    fiveStarBase, fiveStarStory, fourStarBase, fourStarStory, threeStarBase, threeStarStory = [], [], [], [], [], []
    fiveStarEss, fourStarEss, threeStarEss = [], [], []
    campaigns=[]
    currFiveStars, currFourStars, currThreeStars = [], [], []
    currFiveStarEss, currFourStarEss, currThreeStarEss = [], [], []

    currFeatured3S, currFeatured4S, currFeatured5S = [], [], []
    currFeatured3E, currFeatured4E, currFeatured5E = [], [], []

    featured5sChance, featured4sChance, featured3sChance = [], [], []
    featured5eChance, featured4eChance, featured3eChance = [], [], []

    def raw_init(self):
        # Amai : This needs to be updated manually for now
        self.fiveStarBase = ["Altria Pendragon", "Altera", "Zhuge Liang (El-Melloi II)", "Vlad III", "Jeanne d'Arc",
                             "Orion", "Francis Drake", "Tamamo no Mae", "Jack the Ripper", "Mordred", "Nightingale"]
        self.fiveStarStory = ["Nikola Tesla", "Queen Medb", "Cu Chulainn (Alter)"]

        self.fourStarBase = ["Siegfried", "Chevalier d'Eon", "EMIYA", "Atalante", "Elisabeth Bathory",
                             "Anne Bonny & Mary Read", "Marie Antoinette", "Saint Martha", "Stheno", "Carmilla",
                             "Heracles", "Lancelot", "Tamamo Cat", "Nursery Rhyme", "Frankenstein"]
        self.fourStarStory = ["Medea (Lily)", "Nero Claudius", "Altria Pendragon (Alter)",
                              "Altria Pendragon (Lancer Alter)", "Li Shuwen", "Thomas Edison"]

        self.threeStarBase = ["Gaius Julius Caesar", "Gilles de Rais", "Robin Hood", "David", "Euryale", "Cu Chulainn",
                              "Cu Chulainn (Prototype)", "Romulus", "Hektor", "Medusa", "Boudica", "Ushiwakamaru",
                              "Alexander", "Medea", "Mephistopheles", "Jing Ke", "Lu Bu Fengxian", "Darius III",
                              "Kiyohime", "Diarmuid ua Duibhne", "Fergus mac Roich", "Paracelsus von Hohenheim",
                              "Charles Babbage", "Henry Jekyll & Hyde"]
        self.threeStarStory = ["Cu Chulainn (Caster)", "Gilles de Rais (Caster)"]

        self.fiveStarEss = ["Formal Craft", "Imaginary Around", "Limited/Zero Over", "Kaleidoscope", "Heaven's Feel",
                            "Prisma Cosmos", "The Black Grail", "Victor of the Moon", "Another Ending",
                            "A Fragment of 2030", "500-Year Obsession"]

        self.fourStarEss = ["Iron-Willed Training", "Primeval Curse", "Projection", "Gandr",
                            "Verdant Sound of Destruction", "Gem Magecraft: Antumbra", "Be Elegant",
                            "The Imaginary Element", "Divine Banquet", "Angel's Song", "Seal Designation Enforcer",
                            "Holy Shroud of Magdalene", "With One Strike", "Code Cast", "Knight's Dignity",
                            "Awakened Will", "Necromancy", "Golden Millennium Tree"]

        # OLD ONES: var threeStarEss = ["Azoth Blade", "False Attendant's Writings", "The Azure Black Keys", "The Verdant Black Keys", "The Crimson Black Keys", "Rin's Pendant", "Spell Tome", "Dragon's Meridian", "Sorcery Ore", "Dragonkin", "Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower"]
        # TODO need to add these ce's first

        self.threeStarEss = ["Mooncell Automaton", "Runestones", "Anchors Aweigh", "Demonic Boar", "Clock Tower",
                             "Ryudoji Temple", "Mana Gauge", "Elixir of Love", "Storch Ritter", "Hermitage",
                             "Motored Cuirassier", "Stuffed Lion", "Lugh's Halo"]

    def check_mode(self,mode):
        if mode != "Story":
            mode_exist = False
            for i in range(0,len(self.campaigns)):
                if mode == self.campaigns[i].title:
                    mode_exist = True
            return mode_exist
        else:
            return True

    def init_campaigns(self):
        # Amai : This needs to be updated manually for now
        title = "Sanzang Coming To The West"
        featured_servants = ["Xuanzang Sanzang", "Li Shuwen", "David", "Lu Bu Fengxian"]
        featured_essences = ["GO WEST!!", "True Samadhi Fire", "All Three Together"]
        self.campaigns.append(Campaign(title, featured_servants, featured_essences))

    def init_gacha(self):
        self.currFiveStars = []
        self.currFourStars = []
        self.currThreeStars = []

        self.currFiveStars = self.fiveStarBase
        self.currFourStars = self.fourStarBase
        self.currThreeStars = self.threeStarBase
        self.currFiveStarEss = self.fiveStarEss
        self.currFourStarEss = self.fourStarEss
        self.currThreeStarEss = self.threeStarEss

        # servantsPulled = [], essencesPulled = [] Amai : not using these for now

        # featured rates estimated from excel spreadsheet
        self.featured5sChance, self.featured4sChance, self.featured3sChance = 67, 67, 20
        self.featured5eChance, self.featured4eChance, self.featured3eChance = 45, 33, 20

    def __init__(self):
        self.raw_init()
        self.init_gacha()
        self.init_campaigns()

    def change_mode(self, mode):

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

            for i in range(0, len(self.campaigns)):
                if mode == self.campaigns[i].title:
                    featured_servants = self.campaigns[i].featured_servants
                    featured_essences = self.campaigns[i].featured_essences

                    if self.campaigns[i].base_servant_override_5:
                        self.currFiveStars = self.campaigns[i].base_servant_override_5
                    if self.campaigns[i].base_servant_override_4:
                        self.currFourStars = self.campaigns[i].base_servant_override_4
                    if self.campaigns[i].base_servant_override_3:
                        self.currThreeStars = self.campaigns[i].base_servant_override_3
                    if self.campaigns[i].base_ce_override_5:
                        self.currFiveStarEss = self.campaigns[i].base_ce_override_5
                    if self.campaigns[i].base_ce_override_4:
                        self.currFourStarEss = self.campaigns[i].base_ce_override_4
                    if self.campaigns[i].base_ce_override_3:
                        self.currThreeStarEss = self.campaigns[i].base_ce_override_3

                    for j in range(0, len(featured_servants)):
                        curr_servant = featured_servants[j]
                        servant_obj = get_servant(curr_servant)
                        stars = servant_obj.stars
                        if stars == 3:
                            self.currFeatured3S.append(curr_servant)
                        elif stars == 4:
                            self.currFeatured4S.append(curr_servant)
                        elif stars == 5:
                            self.currFeatured5S.append(curr_servant)

                    for j in range(0, len(featured_essences)):
                        curr_essence = featured_essences[j]
                        ess_obj = get_essence(curr_essence)
                        stars = ess_obj.stars
                        if stars == 3:
                            self.currFeatured3E.append(curr_essence)
                        elif stars == 4:
                            self.currFeatured4E.append(curr_essence)
                        elif stars == 5:
                            self.currFeatured5E.append(curr_essence)

    def pull_essence(self, stars):
        featured_chance = math.floor(random.random() * 100)

        if stars == 3:
            pull_featured = featured_chance < self.featured3eChance
            essence = self.pull_featured_obj(pull_featured, self.currFeatured3E, self.currThreeStarEss)

        elif stars == 4:
            pull_featured = featured_chance < self.featured4eChance
            essence = self.pull_featured_obj(pull_featured, self.currFeatured4E, self.currFourStarEss)

        else:
            pull_featured = featured_chance < self.featured5eChance
            essence = self.pull_featured_obj(pull_featured, self.currFeatured5E, self.currFiveStarEss)

        essence_obj = get_essence(essence)
        return essence_obj

    def pull_servant(self, stars):
        featured_chance = math.floor(random.random() * 100)
        # 50% chance that it pulls from the featured list

        if stars == 3:
            pull_featured = featured_chance < self.featured3sChance
            servant = self.pull_featured_obj(pull_featured, self.currFeatured3S, self.currThreeStars)

        elif stars == 4:
            pull_featured = featured_chance < self.featured4sChance
            servant = self.pull_featured_obj(pull_featured, self.currFeatured4S, self.currFourStars)

        else:
            pull_featured = featured_chance < self.featured5sChance
            servant = self.pull_featured_obj(pull_featured, self.currFeatured5S, self.currFiveStars)

        servant_obj = get_servant(servant)
        #print("SERVANT PULLED: "+servant+" - NAME: "+servant_obj.name+" STARS: "+servant_obj.stars)
        return servant_obj

    def pull_featured_obj(self, featured, curr_featured, currs):
        if featured and len(curr_featured) > 0:
            idx = math.floor(random.random() * len(curr_featured))
            return curr_featured[idx]

        else:
            idx = math.floor(random.random() * len(currs))
            return currs[idx]

    def simulate(self, num, is_ticket):
        num = int(num)
        pulled_servant = False
        pulled_high = False
        result = []
        for i in range(0, num):
            if i == 9 and not pulled_servant and not is_ticket:
                self.pull_servant(3)
                continue

            if i == 8 and not pulled_high and not is_ticket:
                # 4x higher chance to pull essence than servant
                rand = math.floor(random.random() * 100) + 1
                if rand <= 80:
                    self.pull_essence(4)
                else:
                    pulled_servant = True
                    self.pull_servant(4)
                continue

            rarityNum = math.floor(random.random() * 100) + 1

            # pulled 3* servant
            if rarityNum < 40:
                pulled_servant = True
                result.append(self.pull_servant(3))

            # pulled 4* essence
            elif rarityNum < 52:
                pulled_high = True
                result.append(self.pull_essence(4))

            # pulled 4* servant
            elif rarityNum < 55:
                pulled_servant = True
                pulled_high = True
                result.append(self.pull_servant(4))

            # pulled 5* servant
            elif rarityNum < 56:
                pulled_servant = True
                pulled_high = True
                result.append(self.pull_servant(5))

            # pulled 3* essence
            elif rarityNum < 96:
                result.append(self.pull_essence(3))

            # pulled 5* essence
            else:
                pulled_high = True
                result.append(self.pull_essence(5))

        return result

gacha = Gacha()
mode="Sanzang Coming To The West"
if gacha.check_mode(mode):
    gacha.change_mode(mode)
    result = gacha.simulate(10,False)
    msg="Resultat : "
    for pulled in result:
          msg = msg + str(pulled.name) + "   " + str(pulled.stars) + "*\n"
    print(msg)
else:
    print("Mode inexistant")