from random import randint

class Monster:
    def __init__(self, name, tier, location, rarity, power_level, abilities, average_stats, gem):
        self.name = name
        self.tier = tier
        self.location = location
        self.rarity = rarity
        self.power_level = power_level
        self.abilities = abilities
        self.average_stats = average_stats
        self.gem = gem

    def generate_random_stats(self):
        # Generate random stats for each tier
        if self.tier == "1":
            # Tier 1 stats range from 5 to 10
            return {
                "Strength": randint(3, 8),
                "Agility": randint(5, 10),
                "Defense": randint(5, 10),
                "Intelligence": randint(1, 4)
            }
        elif self.tier == "2":
            # Tier 2 stats range from 20 to 75
            return {
                "Strength": randint(20, 75),
                "Agility": randint(20, 75),
                "Defense": randint(20, 75),
                "Intelligence": randint(20, 75)
            }
        elif self.tier == "3":
            # Tier 3 stats range from 20 to 75
            return {
                "Strength": randint(75, 200),
                "Agility": randint(75, 200),
                "Defense": randint(75, 200),
                "Intelligence": randint(75, 200),
            }
        elif self.tier == "4":
            # Tier 4 stats range from 5 to 10
            return {
                "Strength": randint(200, 600),
                "Agility": randint(200, 600),
                "Defense": randint(200, 600),
                "Intelligence": randint(200, 600),
            }
        elif self.tier == "5":            return {
                "Strength": randint(600, 1200),
                "Agility": randint(600, 1200),
                "Defense": randint(600, 1200),
                "Intelligence": randint(600, 1200),
            }
        elif self.tier == "6":            return {
                "Strength": randint(1200, 6000),
                "Agility": randint(1200, 6000),
                "Defense": randint(1200, 6000),
                "Intelligence": randint(1200, 6000),
            }
        elif self.tier == "7":            return {
                "Strength": randint(6000, 12000),
                "Agility": randint(6000, 12000),
                "Defense": randint(6000, 12000),
                "Intelligence": randint(6000, 12000),
            }
        elif self.tier == "8":            return {
                "Strength": randint(12000, 25000),
                "Agility": randint(12000, 25000),
                "Defense": randint(12000, 25000),
                "Intelligence": randint(12000, 25000),
            }
        elif self.tier == "9":            return {
                "Strength": randint(25000, 50000),
                "Agility": randint(25000, 50000),
                "Defense": randint(25000, 50000),
                "Intelligence": randint(25000, 50000),
           }
        elif self.tier == "10":            return {
                "Strength": randint(50000, 80000),
                "Agility": randint(50000, 80000),
                "Defense": randint(50000, 80000),
                "Intelligence": randint(50000, 80000),
            }
monsters = {
    "1": Monster(
        "Zombie", "1", "Widespread, appearing anywhere.", "Common, numerous sightings.",
        "Basic, minimal destructive capabilities.", "Simple, instinctive behavior; might exhibit enhanced strength or speed.",
        "Comparable to an average human, around 5 in each category.",
        {
            "Type": "Tier 1 Gem",
            "Effect": "1/10th increase in strength, agility, or defense based on the monster's stats. Single use.",
            "Ability Chance": "0%"
        }
    ),
    "2": Monster(
        "Goblin", "2", "Widespread, appearing anywhere.", "Common, numerous sightings.",
        "Basic, minimal destructive capabilities.", "Simple, instinctive behavior; might exhibit enhanced strength or speed.",
        "Slightly enhanced, averages ranging from 20 to 75.",
        {
            "Type": "Tier 1 Gem",
            "Effect": "1/10th increase in strength, agility, or defense based on the monster's stats. Single use.",
            "Ability Chance": "0%"
        }
    ),
    "3": Monster(
        "Werewolf", "3", "Found in urban areas and larger towns.", "Common, multiple sightings in urban centers.",
        "Slightly stronger, able to cause localized damage.", "Improved coordination and agility.",
        "Slightly enhanced, averages ranging from 20 to 75.",
        {
            "Type": "Tier 2 Gem",
            "Effect": "1/10th boost in strength, agility, or defense, reflecting the monster's capabilities. Can be applied independently to each stat.",
            "Ability Chance": "0%"
        }
    ),
    "4": Monster(
        "Ogre", "4", "Sporadic in large towns and smaller cities.", "Rare, only a few in a county.",
        "Markedly stronger, capable of causing substantial damage.", "Enhanced physical attributes and rudimentary elemental control.",
        "Considerably stronger, averages ranging from 200 to 600.",
        {
            "Type": "Tier 4 Gem",
            "Effect": "1/10th increase in strength, agility, or defense. Allows for profound intelligence enhancement. Selective use.",
            "Ability Chance": "10%"
        }
    ),
    "5": Monster(
        "Dragonling", "5", "Scattered across regions.", "Very Rare, one or two spanning a part of the country.",
        "Considerable strength with potential regional impact.", "Advanced skills, like elemental manipulation and heightened intelligence.",
        "Formidable, average stats around 600 to 1,200.",
        {
            "Type": "Tier 5 Gem",
            "Effect": "1/10th escalation in strength, agility, or defense. Facilitates a substantial boost in intelligence. Strategic application.",
            "Ability Chance": "6%"
        }
    ),
    "6": Monster(
        "Kraken", "6", "Rare, appearing once per country or a large part of a continent.", "Extremely Rare, sightings across larger geographic areas.",
        "Formidable strength with potential regional devastation.", "Advanced elemental control, telepathy, or other impactful powers.",
        "Powerful, stats reaching from 1,200 to 6,000.",
        {
            "Type": "Tier 6 Gem",
            "Effect": "1/10th augmentation in strength, agility, or defense. Allows for advanced intelligence enhancement, insights into cosmic nature. Precision use.",
            "Ability Chance": "4%"
        }
    ),
    "7": Monster(
        "Leviathan", "7", "Highly limited presence, sightings at a state or regional level.", "Exceptionally Rare, 1 or 2 monsters across a state or region.",
        "Considerable strength, potential for regional destructive capabilities.", "Sophisticated abilities like energy manipulation, enhanced regeneration, or limited control over elements.",
        "Monstrous, averages around 6,000 to 12,000.",
        {
            "Type": "Tier 7 Gem",
            "Effect": "1/10th increase in strength, agility, or defense. Enables a profound boost in intelligence. Strategic utilization.",
            "Ability Chance": "2%."
        }
    ),
    "8": Monster(
        "Ancient Dragon", "8", "Found on a continental scale, sightings spanning multiple countries.", "Incredibly Rare, appearing once every few countries or over a significant continental area.",
        "Extraordinary, capable of causing widespread continental impact.", "Advanced elemental control, powerful telepathy, or manipulation of large-scale natural phenomena.",
        "Exceptional, stats in the range of 12,000 to the continental level.",
        {
            "Type": "Tier 8 Gem",
            "Effect": "1/10th escalation in strength, agility, or defense. Allows for advanced intelligence enhancement, insights into nature and cosmic forces. Finesse application.",
            "Ability Chance": "1%."
        }
    ),
    "9": Monster(
        "Dimensional Horror", "9", "Rare on a global scale, sightings covering continents.", "Almost Mythical, appearing once every few continents or over large portions of the world.",
        "Monstrously potent, potential global-scale devastation abilities.", "Could include reality manipulation, mind-bending powers, or control over fundamental forces.",
        "Phenomenal, average stats surpassing 25,000, capped at the continental level.",
        {
            "Type": "Tier 9 Gem",
            "Effect": "1/10th augmentation in strength, agility, or defense. Enables an unparalleled boost in intelligence, grasping the intricacies of reality manipulation. Precision use.",
            "Ability Chance": "0.6%"
        }
    ),
    "10": Monster(
        "Cosmic Entity", "10", "Extremely rare, known to exist on a global scale.", "Legendary, almost unheard of, only a handful known worldwide.",
        "At the pinnacle, potential for continental-level annihilation.", "Might encompass reality-warping, control over time and space, or manipulation of cosmic forces.",
        "Godlike, reaching the absolute peak, capped at the continental level, often exceeding 50,000.",
        {
            "Type": "Tier 10 Gem",
            "Effect": "1/10th increase in strength, agility, or defense. Allows for the most advanced intelligence enhancement, profound insights into cosmic forces. Unparalleled finesse.",
            "Ability Chance": "0.2%"
        }
    ),
 
    "11": {
        "name": "Humanities 5 Greatest Calamities",
        "creatures": [
            {
                "name": "???",
                "description": "This enigmatic entity is shrouded in mystery, its true form and motivations unknown. It forces humans with 100,000 stats or above to duel each other to the death, seemingly for its own inscrutable purposes. Its influence spans the globe, and its actions have sparked fear and uncertainty among the populace.",
                "location": "Global scale",
                "rarity": "Nearly everyone knows about it. Only one",
                "power_level": "Unknown, but presumed to be cataclysmic.",
                "abilities": "Unpredictable and potentially reality-altering powers.",
                "average_stats": "Undefined, exceeding any known benchmarks.",
                "gem": {
                    "Type": "Unknown",
                    "Effect": "Unknown",
                    "Ability Chance": "Unknown"
                }
            },
            {
                "name": "Void Eater",
                "description": "The Void Eater is a malevolent force that mercilessly wipes out areas with more than 50,000 people. Its methods are varied and insidious, capable of causing widespread devastation through illness, mass killings, or inducing mass madness. The true nature and origin of the Void Eater remain a chilling enigma, leaving those in its wake to grapple with fear and despair.",
                "location": "Global scale",
                "rarity": "Nearly everyone knows about it. Only one"
            },
            {
                "name": "The Moon",
                "description": "Unbeknownst to humanity, the Moon harbors a sinister power that extends beyond mere celestial influence. It is responsible for slowly rising sea levels and causing mutations among fish and monsters in the water. The gradual, ominous transformation of the aquatic ecosystem has sparked concern and speculation about the Moon's cryptic agenda. If you're outside with no cover in the night when the moon is out, it slowly saps your stat points and can cause your desires to be more profound.",
                "location": "Global scale",
                "rarity": "Nearly everyone knows about it. Only one"
            },
            {
                "name": "World Tree",
                "description": "A foreboding presence that emerged in Russia, the World Tree exerts a slow, insidious influence on the earth's vitality and farmland. Those who venture near the World Tree experience haunting hallucinations and an inexplicable urge to pledge loyalty to it. The World Tree's eerie aura casts a shadow of unease over the land, leaving humanity to grapple with its unsettling effects.",
                "location": "Global scale",
                "rarity": "Nearly everyone knows about it. Only one"
            },
            {
                "name": "The Devil",
                "description": "Taking on the guise of a human in any shape, The Devil materializes in response to the whims of mortals. Whether invoked through jest or genuine despair, speaking of the desire for death summons this malevolent entity, which swiftly ends the life of the unfortunate individual within a minute. The mere mention of The Devil's name sends shivers down the spines of those aware of its dread presence.",
                "location": "Global scale",
                "rarity": "Nearly everyone knows about it. Only one"
            },
        ],
    }
}

# Define the get_monster_by_tier function
def get_monster_by_tier(tier):
    return [monster for monster in monsters.values() if monster.tier == tier]

# Define the get_monster_by_name function
def get_monster_by_name(name):
    return next((creature for monster in monsters.values() if monster.name == "Humanities 5 Greatest Threats" for creature in monster.creatures if creature.name.lower() == name.lower()), None)


# Example usage of get_monster_by_tier
tier_3_monsters = get_monster_by_tier("3")
for monster in tier_3_monsters:
    print(f"{monster.name} (Tier {monster.tier}) Stats: {monster.generate_random_stats()}")

# Example usage of get_monster_by_name
monster_name = "Kraken"
specific_monster = get_monster_by_name(monster_name)
if specific_monster:
    print(f"{specific_monster.name} Stats: {specific_monster.generate_random_stats()}")
else:
    print(f"No monster found with the name {monster_name}")
    
    # Stuck, have to check this later