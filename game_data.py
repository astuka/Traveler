
universal_stats = {
    "strength": 0,
    "endurance":0,
    "mechanics": 0, 
}

universal_equipment = {
    "head": "",
    "torso": "",
    "legs": ""
}

universal_resources = {
    "fuel": 0,
    "metal": 0,
}


class Faction:
    def __init__(self, name, resources, army, territory, focus):
        self.name = name
        self.resources = resources
        self.army = army
        self.territory = territory
        self.focus = focus

class NPC:
    def __init__(self, appearance, race, job, faction, money):
        self.appearance = appearance
        self.equipment = universal_equipment #changed later
        self.race = race
        self.job = job
        self.faction = faction
        self.stats = universal_stats 
        self.stats[race.focus] += 1
        self.stats[job.focus] += 1
        self.stats[faction.focus] += 1
        self.money = money
        self.hp = 100 #changed later
        self.hp_max = 100 #changed later
        self.attack = 5 #changed later
        self.defense = 5 #changed later

class Race:
    def __init__(self, name, focus):
        self.name = name
        self.focus = focus

class Job:
    def __init__(self, name, focus):
        self.name = name
        self.focus = focus

class Planet:
    def __init__(self, name, id, type, size, capital, nodes):
        self.name = name
        self.id = id
        self.type = type
        self.size = size
        self.capital = capital
        self.nodes = nodes

class City:
    def __init__(self, name, population, nodes):
        self.name = name
        self.population = population
        self.nodes = nodes

class Ship:
    def __init__(self, name, pop_capacity, cargo_capacity, attack, defense):
        self.name = name
        self.pop_capacity = pop_capacity
        self.cargo_capacity = cargo_capacity
        self.attack = attack
        self.defense = defense

class Mech:
    def __init__(self) -> None:
        pass

class Satellite:
    def __init__(self, name, pop_capacity, cargo_capacity, attack, defense, faction):
        self.name = name
        self.pop_capacity = pop_capacity
        self.cargo_capacity = cargo_capacity
        self.attack = attack
        self.defense = defense
        self.faction = faction

class Creature:
    def __init__(self, name, appearance, attack, defense):
        self.name = name
        self.appearance = appearance
        self.attack = attack
        self.defense = defense

class Item_Salvage:
    def __init__(self, name, sell_amount, resource):
        self.name = name
        self.sell_amount = sell_amount
        self.resource = resource


class Item_Food:
    def __init__(self, name, sell_amount, heal):
        self.name = name
        self.sell_amount = sell_amount
        self.heal = heal


class Equipment:
    def __init__(self, name, type, attribute, bonus):
        self.name = name
        self.type = type
        self.attribute = attribute
        self.bonus = bonus

class Weapon:
    def __init__(self, name, type, element, damage):
        self.name = name
        self.type = type
        self.element = element
        self.damage = damage



#FACTIONS - The Imperium, Free Planets of Astoria, The Corruption, New Earth Association, The Convocation, 

#RACES - Orks, Kobolds, Humans, Light Elves, Dark Elves, Ascended, Shark race, Frogfolk, Elder Gods, 

#JOBS - skill trainer, smuggler, popstar, space pirate, slaver, trader, bounty hunter, dancer, psion, archaeologist, farmer, slave, doctor, noble, cultist, cosmic inquisitor, cosmic paladin, soldier, diplomat, corporate executive

#SHIPS - cargoship, gunship, starfighter, cruiser, destroyer, dreadnought

#MECHS - reaper class, wasp class, 

#CREATURES - Corruption Parasite, Slime, Minotaur, Gryphon

#ITEM, SALVAGE - Asteroid Debris, 

#ITEM, FOOD - 

#EQUIPMENT, HEAD - 

#EQUIPMENT, TORSO - plain t-shirt, studded leather corset, leather coat, 

#EQUIPMENT, LEGS - 

#WEAPON, PISTOL - 

#WEAPON, RIFLE - scoped sniper rifle, Gatling Gun, 

#WEAPON, EXPLOSIVE - 

#WEAPON, BLADE - axe, 

#WEAPON, BLUNT - 

#Tuya, Gojiko, Rue, Olivier, Katrina, Rowenda, Nintamo, Kiri, Runar, Kiba, Xathan, Bannister, Rhiki, Ambelina
npc_names = ["Castillo", "Fatima", "Deidranna", "Maya", "Enroth", "Jade", "Rondo", "Phaidon", "Xaphura", "Sigmar", "Nagash", "Orok", "Caradura", "Meanne", "Bolas", "Seymour", "Karn", "Chalm", "Tartan", "Goyd", "Strolk", "Baal","Gamon", "Nataranja", "Khaine", "Shrike", "Commissar","Slaanesh", "Lizer", "Kensai", "Tanya", "Reesus", "Kane", "Erika", "Gonk", "Gomesh", "Charly", "Tichon", "Quinn", "Lei", "Fitz", "Virginia", "Olgrim", "Yung", "Menphala", "Strife", "Tevorian", "Quellis", "Dagon", "Alp", "Salvo Kar", "Gupa", "Adraan", "Aelric", "Krigi", "Ophelia", "Flynn", "Therani", "Velvet", "Senrae", "Luka", "Brico"]

planet_names = ["Septerra", "Alpharius", "Primaris", "Archaon", "Caledor", "Coda", "Hereticus", "Fatalis", "Anbennar", "Nobilis", "Polaris", "Earth", "Ishtar", "Data", "Leviathan", "Aldanis", "Scylla", "Volytis", "Destiny", "Dei", "Goerica", "Sumeria", "Mako", "Numera"]
planet_types = ["volcanic", "acidic", "oceanic", "tropical", "desert", "gas", "astral", "umbral"]
planet_sizes = ["small", "medium", "large"]


city_names = ["Drassen", "Omerta", "White Cap", "Sorpigal", "Britannia", "Hal Kuron", "Bala Ged", "Irvine", "Catalan", "Lustria", "Habsburg", "Ostermalm", "Blackfire Pass", "Necropolis", "Ravenloft", "Nibelheim", "Magnus", "Ur-Turuk", "Mythros", "Toan", "Shangri-La", "Verden", "Scion"]

satellite_names = ["Sal Mona", "Anachronox", "Seraphim", "Delta Green", "Anima Prime", "Heliotrope", "Ymir", "Battlestar"]

ship_names = ["Armageddon", "Saint Kansas", "Mandate of Heaven", "Vindictus", "Starbrand", "Deathwing", "The Whirlwind", "Fear Incarnate", "The Tempest", "The Black Sun", "The Astral God", "Death on High"]