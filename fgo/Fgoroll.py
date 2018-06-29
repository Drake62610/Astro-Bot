import json
import random
import os
import traceback


class Error(Exception):
    pass


class NotFoundError(Exception):
    def __init__(self, not_found_id):
        super().__init__("Something was not found in the database : "+not_found_id)


class Fgodb:
    class __Fgodb:
        servantsDB = os.getcwd() + os.sep + 'fgo' + os.sep + 'fgoScrap' + os.sep + 'servants.json'
        essencesDB = os.getcwd() + os.sep + 'fgo' + os.sep + 'fgoScrap' + os.sep + 'essences.json'
        #servantsDB = os.getcwd() + os.sep + 'fgoScrap' + os.sep + 'servants.json'
        #essencesDB = os.getcwd() + os.sep + 'fgoScrap' + os.sep + 'essences.json'

        servantList = ''
        essenceList = ''

        def __init__(self):
            self.load_servants()
            self.load_essences()

        def load_servants(self):
            self.servantList = json.loads(open(self.servantsDB).read())

        def load_essences(self):
            self.essenceList = json.loads(open(self.essencesDB).read())

        def get_servant(self, serv_name):
            for row in self.servantList:
                if 'name' in serv_name:
                    if serv_name['name'] in row['name'] and serv_name['sclass'] in row['sclass']:
                        return Servant(row)
                else:
                    if serv_name in row['name']:
                        return Servant(row)
            raise NotFoundError(serv_name)

        def get_essence(self, ess_name):
            for row in self.essenceList:
                if ess_name in row['name']:
                    return Essence(row)
            raise NotFoundError(ess_name)

    instance = None

    def __init__(self):
        if not Fgodb.instance:
            Fgodb.instance = Fgodb.__Fgodb()

    def __getattr__(self, item):
        return getattr(self.instance, item)


class Servant:
    name, stars, sclass, image_url = '', '', '', ''

    def __init__(self, serv_dict=None, name=None):
        if serv_dict is None:
            serv_dict = {'name': "notfound", 'stars': 0, 'sclass': 'none', 'image_url': ''}
        self.name = serv_dict['name']
        self.stars = serv_dict['stars']
        self.sclass = serv_dict['sclass']
        self.image_url = serv_dict['image_url']
        if name is not None:
            self.name = name

    def __str__(self):
        return str(self.name) + "   (" + str(self.sclass) + ")   " + str(self.stars) + "⭐\n"


class Essence:
    name, stars, image_url = '', '', ''

    def __init__(self, serv_dict=None, name=None):
        if serv_dict is None:
            serv_dict = {'name': "notfound", 'stars': 0, 'image_url': ''}
        self.name = serv_dict['name']
        self.stars = serv_dict['stars']
        self.image_url = serv_dict['image_url']
        if name is not None:
            self.name = name

    def __str__(self):
        return str(self.name) + "   " + str(self.stars) + "⭐\n"


class Campaign:
    title = ''
    featured_servants, featured_essences = [], []
    base_ce_override_3, base_ce_override_4, base_ce_override_5 = [], [], []
    base_servant_override_3, base_servant_override_4, base_servant_override_5 = [], [], []

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
    imagesLocation = "fgo" + os.sep + "card_images"

    fiveStarBase, fiveStarStory, fourStarBase, fourStarStory, threeStarBase, threeStarStory = [], [], [], [], [], []
    fiveStarEss, fourStarEss, threeStarEss = [], [], []

    campaigns = []

    featured5sChance, featured4sChance, featured3sChance = 0, 0, 0
    featured5eChance, featured4eChance, featured3eChance = 0, 0, 0

    five_ess_chance, four_ess_chance, three_ess_chance = 0, 0, 0
    five_serv_chance, four_serv_chance, three_serv_chance = 0, 0, 0

    fgodb = ''

    def init_base_servants(self):
        # Amai : This needs to be updated manually for now

        self.fiveStarBase = ["Altria Pendragon", "Altera", "Zhuge Liang (El-Melloi II)", "Vlad III", "Jeanne d'Arc",
                             "Orion", "Francis Drake", "Tamamo-no-Mae", "Jack the Ripper", "Mordred", "Nightingale",
                             "Xuanzang Sanzang", "Karna", "Arjuna"]

        self.fourStarBase = ["Siegfried", "Chevalier d'Eon", "Emiya", "Atalante", "Elisabeth Bathory",
                             "Anne Bonny & Mary Read", "Marie Antoinette", "Martha", "Stheno", "Carmilla",
                             "Heracles", "Lancelot", "Tamamo Cat", "Nursery Rhyme", "Frankenstein",
                             "Ibaraki-Douji", "Emiya (Assassin)", "Fionn mac Cumhail", "Beowulf",
                             "Astolfo", "Helena Blavatsky", "Rama"]

        self.threeStarBase = ["Gaius Julius Caesar", {'name': "Gilles de Rais", 'sclass': "Saber"}, "Robin Hood",
                              "David", "Euryale", {'name': "Cu Chulainn", 'sclass': "Lancer"},
                              "Cu Chulainn (Prototype)", "Romulus", "Hektor", "Medusa", "Boudica", "Ushiwakamaru",
                              "Alexander", "Medea", "Mephistopheles", "Jing Ke", "Lu Bu Fengxian", "Darius III",
                              "Kiyohime", "Diarmuid Ua Duibhne", "Fergus mac Roich", "Paracelsus von Hohenheim",
                              "Charles Babbage", "Henry Jekyll & Hyde", 'Fuuma "Evil-wind" Kotarou', "Billy the Kid",
                              "Geronimo", "Gilgamesh (Child)", "Hassan of the Hundred Persona"]

    def init_base_essences(self):
        # Amai : This needs to be updated manually for now

        self.fiveStarEss = ["Formal Craft", "Imaginary Around", "Limited/Zero Over", "Kaleidoscope", "Heaven's Feel",
                            "Prisma Cosmos", "The Black Grail", "Victor of the Moon", "Another Ending",
                            "A Fragment of 2030", "500-Year Obsession"]

        self.fourStarEss = ["Iron-Willed Training", "Primeval Curse", "Projection", "Gandr",
                            "Verdant Sound of Destruction", "Gem Magecraft: Antumbra", "Be Elegant",
                            "The Imaginary Element", "Divine Banquet", "Angel's Song", "Seal Designation Enforcer",
                            "Holy Shroud of Magdalene", "With One Strike", "Code Cast", "Knight's Dignity",
                            "Awakened Will", "Necromancy", "Golden Millennium Tree"]

        # self.threeStarEss = ["Azoth Blade", "False Attendant's Writings", "The Azure Black Keys",
        #                       "The Verdant Black Keys", "The Crimson Black Keys", "Rin's Pendant", "Spell Tome",
        #       OLD             "Dragon's Meridian", "Sorcery Ore", "Dragonkin", "Mooncell Automaton", "Runestones",
        #                       "Anchors Aweigh", "Demon Boar", "Clock Tower"]

        # self.threeStarEss = ["Mooncell Automaton", "Runestone", "Anchors Aweigh", "Demon Boar", "Clock Tower",
        #      OLD             "Ryudoji Temple", "Mana Gauge", "Elixir of Love", "Storch Ritter", "Hermitage",
        #                      "Motored Cuirassier", "Stuffed Lion", "Lugh's Halo"]

        self.threeStarEss = ["Bronze-Link Manipulator", "Ath nGabla", "Bygone Dream", "Extremely Spicy Mapo Tofu",
                             "Jeweled Sword Zelretch", "Clock Tower",
                             "Ryudoji Temple", "Mana Gauge", "Elixir of Love", "Storch Ritter", "Hermitage",
                             "Motored Cuirassier", "Stuffed Lion", "Lugh's Halo"]

    def init_story_servants(self):
        # Amai : This needs to be updated manually for now

        self.fiveStarStory = ["Nikola Tesla", "Queen Medb", "Cu Chulainn (Alter)"]

        self.fourStarStory = ["Medea (Lily)", "Nero Claudius", {'name': "Altria Pendragon (Alter)", 'sclass': "Saber"},
                              {'name': "Altria Pendragon (Alter)", 'sclass': "Lancer"}, "Li Shuwen", "Thomas Edison"]

        self.threeStarStory = [{'name': "Gilles de Rais", 'sclass': "Caster"},
                               {'name': "Cu Chulainn", 'sclass': "Caster"}]

    def check_mode(self, mode):
        if mode != "Story":
            mode_exist = False
            for i in range(0, len(self.campaigns)):
                if mode == self.campaigns[i].title:
                    mode_exist = True
            return mode_exist
        else:
            return True

    def init_campaigns(self):
        # Amai : This needs to be updated manually for now

        title = "Camelot"
        featured_servants = ["Ozymandias", "Nitocris", {'name': "Lancelot", 'sclass': "Saber"}, "Hassan of the Serenity", "Tawara Touta"]
        featured_essences = ["Origin Bullet", "Covering Fire", "Battle of Camlann"]
        self.campaigns.append(Campaign(title, featured_servants, featured_essences))

    def init_luck(self):
        self.featured5sChance, self.featured4sChance, self.featured3sChance = 0.67, 0.67, 0.20
        self.featured5eChance, self.featured4eChance, self.featured3eChance = 0.45, 0.33, 0.20

        self.five_ess_chance, self.four_ess_chance, self.three_ess_chance = 0.04, 0.12, 0.4
        self.five_serv_chance, self.four_serv_chance, self.three_serv_chance = 0.01, 0.03, 0.4

    def __init__(self, fgodb):
        self.init_base_servants()
        self.init_story_servants()
        self.init_base_essences()
        self.init_campaigns()
        self.init_luck()
        self.fgodb = fgodb


class Roll:

    currFiveStars, currFourStars, currThreeStars = [], [], []
    currFiveStarEss, currFourStarEss, currThreeStarEss = [], [], []

    currFeatured3S, currFeatured4S, currFeatured5S = [], [], []
    currFeatured3E, currFeatured4E, currFeatured5E = [], [], []

    gacha = ''

    result = []

    def __init__(self, gacha, mode, num, is_ticket):
        self.currFiveStars = []
        self.currFourStars = []
        self.currThreeStars = []

        self.currFiveStars = gacha.fiveStarBase
        self.currFourStars = gacha.fourStarBase
        self.currThreeStars = gacha.threeStarBase
        self.currFiveStarEss = gacha.fiveStarEss
        self.currFourStarEss = gacha.fourStarEss
        self.currThreeStarEss = gacha.threeStarEss

        self.gacha = gacha

        self.pulled_servant = False
        self.pulled_high = False

        self.set_mode(mode)
        self.simulate(num, is_ticket)

    # If the campaign needs to override the base content
    def override_base(self, campaign):
        if campaign.base_servant_override_5:
            self.currFiveStars = campaign.base_servant_override_5
        if campaign.base_servant_override_4:
            self.currFourStars = campaign.base_servant_override_4
        if campaign.base_servant_override_3:
            self.currThreeStars = campaign.base_servant_override_3
        if campaign.base_ce_override_5:
            self.currFiveStarEss = campaign.base_ce_override_5
        if campaign.base_ce_override_4:
            self.currFourStarEss = campaign.base_ce_override_4
        if campaign.base_ce_override_3:
            self.currThreeStarEss = campaign.base_ce_override_3

    def add_featured_servants(self, featured_servants):
        for j in range(0, len(featured_servants)):
            curr_servant = featured_servants[j]
            try:
                servant_obj = self.gacha.fgodb.get_servant(curr_servant)
                stars = servant_obj.stars
                if stars == 3:
                    self.currFeatured3S.append(curr_servant)
                elif stars == 4:
                    self.currFeatured4S.append(curr_servant)
                elif stars == 5:
                    self.currFeatured5S.append(curr_servant)
            except NotFoundError:
                traceback.print_exc()

    def add_featured_essences(self, featured_essences):
        for j in range(0, len(featured_essences)):
            curr_essence = featured_essences[j]
            try:
                ess_obj = self.gacha.fgodb.get_essence(curr_essence)
                stars = ess_obj.stars
                if stars == 3:
                    self.currFeatured3E.append(curr_essence)
                elif stars == 4:
                    self.currFeatured4E.append(curr_essence)
                elif stars == 5:
                    self.currFeatured5E.append(curr_essence)
            except NotFoundError:
                traceback.print_exc()

    def set_mode(self, mode):

        if mode == "Story":
            self.currFiveStars = self.currFiveStars + self.gacha.fiveStarStory
            self.currFourStars = self.currFourStars + self.gacha.fourStarStory
            self.currThreeStars = self.currThreeStars + self.gacha.threeStarStory

        else:
            for i in range(0, len(self.gacha.campaigns)):
                if mode == self.gacha.campaigns[i].title:
                    campaign = self.gacha.campaigns[i]

                    featured_servants = campaign.featured_servants
                    featured_essences = campaign.featured_essences

                    self.override_base(campaign)

                    self.add_featured_servants(featured_servants)

                    self.add_featured_essences(featured_essences)
                    break

    def pull_essence(self, stars):
        featured_chance = random.random()

        if stars == 3:
            pull_featured = featured_chance <= self.gacha.featured3eChance
            essence = self.pull_obj(pull_featured, self.currFeatured3E, self.currThreeStarEss)

        elif stars == 4:
            self.pulled_high = True
            pull_featured = featured_chance <= self.gacha.featured4eChance
            essence = self.pull_obj(pull_featured, self.currFeatured4E, self.currFourStarEss)

        else:
            self.pulled_high = True
            pull_featured = featured_chance <= self.gacha.featured5eChance
            essence = self.pull_obj(pull_featured, self.currFeatured5E, self.currFiveStarEss)

        try:
            essence_obj = self.gacha.fgodb.get_essence(essence)
            return essence_obj
        except NotFoundError:
            traceback.print_exc()
            return Essence(name=essence)

    def pull_servant(self, stars):
        self.pulled_servant = True

        featured_chance = random.random()
        # 50% chance that it pulls from the featured list

        if stars == 3:
            pull_featured = featured_chance < self.gacha.featured3sChance
            servant = self.pull_obj(pull_featured, self.currFeatured3S, self.currThreeStars)

        elif stars == 4:
            self.pulled_high = True
            pull_featured = featured_chance < self.gacha.featured4sChance
            servant = self.pull_obj(pull_featured, self.currFeatured4S, self.currFourStars)

        else:
            self.pulled_high = True
            pull_featured = featured_chance < self.gacha.featured5sChance
            servant = self.pull_obj(pull_featured, self.currFeatured5S, self.currFiveStars)

        try:
            servant_obj = self.gacha.fgodb.get_servant(servant)
            return servant_obj
        except NotFoundError:
            traceback.print_exc()
            return Servant(name=servant)

    def pull_obj(self, featured, curr_featured, currs):
        if featured and len(curr_featured) > 0:
            return random.choice(curr_featured)
        else:
            return random.choice(currs)

    def simulate(self, num, is_ticket):
        num = int(num)

        probs = [self.gacha.three_ess_chance, self.gacha.three_serv_chance, self.gacha.four_ess_chance, self.gacha.five_ess_chance,
                 self.gacha.four_serv_chance, self.gacha.five_serv_chance]
        cum_probs = [0.0]
        for p in probs:
            cum_probs.append(p + cum_probs[-1])
        call_dict = {0: lambda:self.pull_essence(3), 1: lambda:self.pull_servant(3), 2: lambda:self.pull_essence(4),
                     3: lambda:self.pull_essence(5), 4: lambda:self.pull_servant(4), 5: lambda:self.pull_servant(5)}

        for i in range(0, num):
            # 10th roll : 3* servant guaranteed
            if i == 9 and not self.pulled_servant and not is_ticket:
                self.result.append(self.pull_servant(3))
                continue

            # 9th roll : 4* guaranteed
            if i == 8 and not self.pulled_high and not is_ticket:
                # 4x higher chance to pull essence than servant
                rand = random.random()
                if rand <= 0.8:
                    self.result.append(self.pull_essence(4))
                else:
                    self.result.append(self.pull_servant(4))
                continue

            rarity_num = random.random()

            for i, poss in enumerate(cum_probs[1:]):
                if rarity_num < poss:
                    self.result.append(call_dict[i]())
                    break

    def pretty_print(self):
        msg_queue = []
        for pulled in self.result:
            if int(pulled.stars) == 0:
                color = "black"
            elif int(pulled.stars) < 3:
                color = "bronze"
            elif int(pulled.stars) == 3:
                color = "silver"
            else:
                color = "gold"

            msg_queue.append({'type': "upload", 'content': self.gacha.imagesLocation + os.sep + color + "_back.png"})

            if isinstance(pulled, Servant):
                sclass = str(pulled.sclass).lower()
                msg_queue.append({'type': "delete"})
                msg_queue.append(
                    {'type': "upload", 'content': self.gacha.imagesLocation + os.sep + color + "_" + sclass + ".png"})
                msg_queue.append({'type': "delete"})
                msg_queue.append({'type': "say", 'content': str(pulled.image_url)})
                msg_queue.append({'type': "say",
                                  'content': str(pulled.name) + "    (" + str(pulled.sclass) + ")   " + str(
                                      pulled.stars) + " ⭐"})

            else:
                msg_queue.append({'type': "delete"})
                msg_queue.append({'type': "say", 'content': str(pulled.image_url)})
                msg_queue.append({'type': "say", 'content': str(pulled.name) + "    " + str(pulled.stars) + " ⭐"})

        return msg_queue
