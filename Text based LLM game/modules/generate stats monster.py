import mysql.connector
from random import randint

class MonsterStatsGenerator:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def generate_random_stats(self, tier):
        # Generate random stats for each tier
        if tier == "1":
            # Tier 1 stats range from 5 to 10
            return {
                "Strength": randint(3, 8),
                "Agility": randint(5, 10),
                "Defense": randint(5, 10),
                "Intelligence": randint(1, 4)
            }
        elif tier == "2":
            # Tier 2 stats range from 20 to 75
            return {
                "Strength": randint(20, 75),
                "Agility": randint(20, 75),
                "Defense": randint(20, 75),
                "Intelligence": randint(20, 75)
            }
        elif tier == "3":
            # Tier 3 stats range from 20 to 75
            return {
                "Strength": randint(75, 200),
                "Agility": randint(75, 200),
                "Defense": randint(75, 200),
                "Intelligence": randint(75, 200),
            }
        elif tier == "4":
            # Tier 4 stats range from 5 to 10
            return {
                "Strength": randint(200, 600),
                "Agility": randint(200, 600),
                "Defense": randint(200, 600),
                "Intelligence": randint(200, 600),
            }
        elif tier == "5":
            return {
                "Strength": randint(600, 1200),
                "Agility": randint(600, 1200),
                "Defense": randint(600, 1200),
                "Intelligence": randint(600, 1200),
            }
        elif tier == "6":
            return {
                "Strength": randint(1200, 6000),
                "Agility": randint(1200, 6000),
                "Defense": randint(1200, 6000),
                "Intelligence": randint(1200, 6000),
            }
        elif tier == "7":
            return {
                "Strength": randint(6000, 12000),
                "Agility": randint(6000, 12000),
                "Defense": randint(6000, 12000),
                "Intelligence": randint(6000, 12000),
            }
        elif tier == "8":
            return {
                "Strength": randint(12000, 25000),
                "Agility": randint(12000, 25000),
                "Defense": randint(12000, 25000),
                "Intelligence": randint(12000, 25000),
            }
        elif tier == "9":
            return {
                "Strength": randint(25000, 50000),
                "Agility": randint(25000, 50000),
                "Defense": randint(25000, 50000),
                "Intelligence": randint(25000, 50000),
           }
        elif tier == "10":
            return {
                "Strength": randint(50000, 80000),
                "Agility": randint(50000, 80000),
                "Defense": randint(50000, 80000),
                "Intelligence": randint(50000, 80000),
            }

    def insert_monster_stats(self, monster_id, name, tier_id, tier_gem_id):
        # Get random stats based on the tier
        tier_stats = self.generate_random_stats(str(tier_id))

        # Insert the monster data into the database
        sql = "INSERT INTO Monster (monster_id, name, tier_id, tier_gem_id, strength, agility, defense, intelligence) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            monster_id, name, tier_id, tier_gem_id,
            tier_stats["Strength"], tier_stats["Agility"], tier_stats["Defense"], tier_stats["Intelligence"]
        )

        self.cursor.execute(sql, values)
        self.connection.commit()

        print(f"Monster '{name}' stats inserted successfully.")

if __name__ == "__main__":
    # Template login
    db_config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database'
    }

    # Create an instance of MonsterStatsGenerator
    monster_generator = MonsterStatsGenerator(db_config)

    # Example: Insert a monster into the database
    monster_generator.insert_monster_stats(31, 'New Monster', 6, 6)

    # Close the connection
    monster_generator.close_connection()

# Keep in mind we dont know rlly how to use SQL so we cant rlly use it yet