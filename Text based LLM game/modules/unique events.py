class UniqueEvent:
    def __init__(self, name, description, details):
        self.name = name
        self.description = description
        self.details = details

unique_events = {
    "1": UniqueEvent(
        "Scavenger Camps",
        "Groups of survivors form makeshift camps in urban ruins.",
        "Camps scavenge for resources, forming alliances or rivalries."
    ),
    "2": UniqueEvent(
        "Resource Scarcity",
        "Essential resources like clean water, food, and medical supplies are in short supply.",
        "Characters may need to compete for these resources or find alternatives."
    ),
    "3": UniqueEvent(
        "Power Struggles",
        "Breakdown of societal structures leads to power struggles.",
        "Charismatic leaders emerge to establish new orders or enforce rules."
    ),
    "4": UniqueEvent(
        "Abandoned Military Bases",
        "Former military bases become critical locations for survivors.",
        "These places are often dangerous and contested."
    ),
    "5": UniqueEvent(
        "Roving Bands of Raiders",
        "Lawlessness prevails with roving bands of raiders.",
        "Characters must navigate encounters with hostile groups."
    ),
    "6": UniqueEvent(
        "Wildlife Encroachment",
        "Nature reclaims urban areas; wildlife poses threats to survivors.",
        "A new and deadly disease spreads rapidly among survivors."
    ),
    "7": UniqueEvent(
        "Radioactive Zones",
        "Areas contaminated by radiation present significant risks and valuable resources.",
        "Characters may come across old computers, databases, or experimental facilities."
    ),
    "8": UniqueEvent(
        "Nomadic Tribes",
        "Groups of survivors embrace a nomadic lifestyle.",
        "They move across the desolate landscape in search of habitable areas."
    ),
    "9": UniqueEvent(
        "Urban Decay",
        "Once vibrant cities stand as haunting reminders of the past.",
        "Dilapidated skyscrapers, crumbling infrastructure, and overgrown streets create a surreal environment."
    ),
    "10": UniqueEvent(
        "Mysterious Illness",
        "A new and deadly disease spreads rapidly among survivors.",
        "Finding a cure or preventing further outbreaks becomes a critical priority."
    ),
    "11": UniqueEvent(
        "Technological Relics",
        "Abandoned technology from the old world holds potential dangers and valuable information.",
        "Characters may come across old computers, databases, or experimental facilities."
    ),
    "12": UniqueEvent(
        "Cults and Belief Systems",
        "Chaos has given rise to cults and extreme belief systems.",
        "Some survivors turn to radical ideologies as a means of coping."
    ),
    "13": UniqueEvent(
        "Environmental Changes",
        "The world's climate has shifted dramatically.",
        "Extreme weather conditions such as frequent storms, acid rain, or temperature fluctuations."
    ),
    "14": UniqueEvent(
        "Lack of Communication",
        "Collapse of communication networks isolates survivors.",
        "Characters must rely on physical messages, rumors, or long-distance travel to connect with other communities."
    ),
    "15": UniqueEvent(
        "Mental Health Struggles",
        "Traumatic events take a toll on survivors' mental well-being.",
        "Characters may encounter individuals grappling with anxiety, depression, or PTSD."
    ),
    "16": UniqueEvent(
        "Mutant Outbreaks",
        "Radiation and environmental contamination lead to the emergence of mutated creatures.",
        "Survivors must contend with new, often hostile, species that have evolved in the aftermath of the apocalypse."
    ),
    "17": UniqueEvent(
        "Scarcity of Fuel",
        "Shortage of fuel and energy sources disrupts transportation and power generation.",
        "Characters must seek alternative means of travel and energy generation, leading to resourceful adaptations and technological innovation."
    ),
    "18": UniqueEvent(
        "The Rise of Mercenary Groups",
        "The breakdown of law and order results in the proliferation of mercenary groups and hired guns.",
        "Survivors may encounter professional mercenaries offering their services for protection, trade, or other purposes."
    ),
    "19": UniqueEvent(
        "Factional Warfare",
        "Fractured survivor communities engage in territorial disputes and conflicts over resources.",
        "Characters must navigate complex allegiances and rivalries while avoiding getting caught in the crossfire of factional warfare."
    ),
    "20": UniqueEvent(
        "Cultural Resurgence",
        "Amid the ruins of the old world, new cultural movements, art forms, and belief systems emerge.",
        "Survivors witness the birth of unique cultural expressions, traditions, and philosophies in the post-apocalyptic landscape."
    )
}

def get_event_by_id(event_id):
    return unique_events.get(event_id)
