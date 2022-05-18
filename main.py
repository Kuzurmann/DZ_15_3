from utils import connect
import sqlite3

query_1 = """
CREATE TABLE colors (
id INTEGER PRIMARY KEY AUTOINCREMENT,
color VARCHAR(30)
    )
"""
# print(connect(query_1))
query_2 = """
          CREATE TABLE animals_colors (
          animal_id INTEGER,
          color_id INTEGER,
          FOREIGN KEY (animal_id) REFERENCES animal_finally(id)
          FOREIGN KEY (color_id) REFERENCES colors(id)

)
"""
# print(connect(query_2))
query_3 = """
          INSERT INTO colors (color)
          SELECT DISTINCT * FROM (
            SELECT DISTINCT color1 as color 
            FROM animals
          UNION ALL
            SELECT DISTINCT color2 as color
            FROM animals
          )
"""
# print(connect(query_3))
query_4 = """
          INSERT INTO animals_colors (animal_id, color_id)
          SELECT DISTINCT animals."index", colors.id
          FROM animals
          JOIN colors
              ON colors.color = animals.color1
          UNION ALL
          SELECT DISTINCT animals."index", colors.id
          FROM animals
          JOIN colors ON colors.color = animals.color2
"""
# print(connect(query_4))

query_5 = """
          CREATE TABLE outcome (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          subtype varchar(50),
          "type" varchar(50),
          "month" integer,
          "year" integer
)
"""
# print(connect(query_5))
query_6 = """
          INSERT INTO outcome (subtype, "type", "month", "year")
          SELECT DISTINCT animals.outcome_subtype, animals.outcome_type, animals.outcome_month, animals.outcome_year
          FROM animals
"""
# print(connect(query_6))
query_7 = """
          CREATE TABLE breed (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          breed varchar(50)
        )
"""
# print(connect(query_7))
query_8 = """
          CREATE TABLE animals_breed (
          animal_id integer,
          breed_id integer,
          FOREIGN KEY (animal_id) REFERENCES animals("index")
          FOREIGN KEY (breed_id) REFERENCES breed(id)
)
"""
# print(connect(query_8))
query_infinity = """
                 CREATE TABLE types (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 types varchar(100)
        )
"""

query_infinity_3 = """
                   INSERT INTO types (types)
                   SELECT DISTINCT animals.animal_type as types
                   FROM animals

"""

query_9 = """
          INSERT INTO animals_breed (animal_id, breed_id)
          SELECT DISTINCT animals."index" as animal_id, breed.id as breed_id
          FROM animals
          JOIN breed ON breed.breed = animals.breed

"""
# print(connect(query_9))
query_10 = """
          INSERT INTO breed (breed)
          SELECT DISTINCT animals.breed
          FROM animals
"""
# print(connect(query_10))

query_13 = """
           CREATE TABLE animals_finally (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           age_upon_outcome VARCHAR(50),
           animal_id INTEGER,
           "name" VARCHAR(50),
           date_of_birth varchar(50),
           outcome_id integer,
           breed_id integer,
           type_id integer,
           FOREIGN KEY (outcome_id) REFERENCES outcome(id)
           FOREIGN KEY (breed_id) REFERENCES breed(id)
           FOREIGN KEY (type_id) REFERENCES types(id)
           )
"""
# print(connect(query_13))
query_14 = """
           INSERT INTO animals_finally (age_upon_outcome, animal_id, "name", 
           date_of_birth, outcome_id, breed_id, type_id)
           SELECT DISTINCT animals.age_upon_outcome, animals.animal_id, animals."name", 
           animals.date_of_birth, outcome.id, breed.id, types.id
           FROM animals
           LEFT JOIN outcome ON outcome.subtype = animals.outcome_subtype
           AND outcome.type = animals.outcome_type
           AND outcome.month = animals.outcome_month
           AND outcome.year = animals.outcome_year
           JOIN breed ON breed.breed = animals.breed
           JOIN types ON types.types = animals.animal_type
    """
# print(connect(query_14))


if __name__ == '__main__':
    print(connect(query_14))
