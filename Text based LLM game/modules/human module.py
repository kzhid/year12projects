class HumanRankingSystem:
    def __init__(self):
        self.ranks = {
            "1": {
                "rank": "Novice",
                "location": "Any human settlement.",
                "rarity": "Common.",
                "power_level": "Basic, minimal impact.",
                "abilities": "Simple, instinctive (enhanced senses, minor telekinesis).",
                "average_stats": "Comparable to an untrained human (around 5 in each category)."
            },
            "2": {
                "rank": "Awakened",
                "location": "Urban areas, larger towns.",
                "rarity": "Common.",
                "power_level": "Slightly enhanced, localized feats.",
                "abilities": "Enhanced physical abilities, basic energy manipulation.",
                "average_stats": "Enhanced (20 to 75)."
            },
            "3": {
                "rank": "Master",
                "location": "Cities, less densely populated than Rank 2.",
                "rarity": "Uncommon.",
                "power_level": "Significant strength, strategic abilities.",
                "abilities": "Advanced combat skills, limited energy manipulation, enhanced senses.",
                "average_stats": "Noticeably improved, averaging between 75 and 200.",
            },
            "4": {
                "rank": "Expert",
                "location": "Sporadic in large towns, smaller cities.",
                "rarity": "Rare.",
                "power_level": "Markedly stronger, substantial feats.",
                "abilities": "Enhanced physical attributes, advanced combat techniques, minor energy manipulation.",
                "average_stats": "Considerably stronger (200 to 600)."
            },
            "5": {
                "rank": "Sovereign",
                "location": "Scattered across regions.",
                "rarity": "Very Rare.",
                "power_level": "Considerable strength, high regional impact.",
                "abilities": "Mastery of combat arts, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Formidable (600 to 1,200)."
            },
            "6": {
                "rank": "Grandmaster",
                "location": "Rare, once per country or large part of a continent.",
                "rarity": "Extremely Rare.",
                "power_level": "Formidable strength, significant continental impact.",
                "abilities": "Mastered combat techniques, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Powerful (1,200 to 6,000)."
            },
            "7": {
                "rank": "Archmage",
                "location": "Highly limited, state or regional level.",
                "rarity": "Exceptionally Rare.",
                "power_level": "Considerable strength, potential regional destructive capabilities.",
                "abilities": "Exceptional mastery of combat arts, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Monstrous (6,000 to 12,000)." 
            },
            "8": {
                "rank": "Ascendant",
                "location": "Continental scale, sightings spanning multiple countries.",
                "rarity": "Incredibly Rare.",
                "power_level": "Extraordinary, capped at high continental level impact.",
                "abilities": "Unmatched mastery of combat arts, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Exceptional (12,000 to 25,000)."
            },
            "9": {
                "rank": "Worldshaper",
                "location": "Rarely on a global scale, sightings covering continents.",
                "rarity": "Almost Mythical.",
                "power_level": "Monstrously potent, capped at high continental level impact.",
                "abilities": "Unparalleled mastery of combat arts, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Phenomenal (stats surpassing 25,000)."
            },
            "10": {
                "rank": "Exalted",
                "location": "Extremely rare on a global scale.",
                "rarity": "Legendary, almost unheard of, handful known worldwide.",
                "power_level": "Pinnacle, capped at high continental level impact.",
                "abilities": "Unprecedented mastery of combat arts, advanced energy manipulation, heightened senses, minor elemental control.",
                "average_stats": "Godlike, reaching the absolute peak, often exceeding 50,000."
            }
        }

    def get_rank_info(self, rank):
        return self.ranks.get(rank)


ranking_system = HumanRankingSystem()
rank_info = ranking_system.get_rank_info("3")
print(rank_info)