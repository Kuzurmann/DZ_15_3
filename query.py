import sqlite3


def connect(query):
    connection = sqlite3.connect('animal.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    return result


def main():
    query_1 = """
        CREATE TABLE IF NOT EXISTS colors (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , color VARCHAR(50)
        )
    """

    query_2 = """
        CREATE TABLE IF NOT EXISTS animals_colors (
            animals_id INTEGER
            , colors_id INTEGER
            , FOREIGN KEY (animals_id) REFERENCES animals("index")
            , FOREIGN KEY (colors_id) REFERENCES colors(id)
        )
    """

    query_3 = """
            CREATE TABLE IF NOT EXISTS animals_type, animals_breed (
                type_id INTEGER
                , colors_id INTEGER
                , FOREIGN KEY (type_id) REFERENCES animals("index")
                , FOREIGN KEY (breed_id) REFERENCES breeds(id)
            )
        """

    query_4 = """
        INSERT INTO colors (colors)
        SELECT DISTINCT * FROM (
            SELECT DISTINCT
                color1 AS color
            FROM animals
            UNION ALL 
            SELECT DISTINCT
                color2 AS color
            FROM animals
        )
    """

    query_5 = """
        INSERT INTO animals_colors (animals_id, colors_id)
        SELECT DISTINCT
            animal."index", colors.id
        FROM animals
        JOIN colors 
            ON colors.color = animals.color1
        UNION ALL
        SELECT DISTINCT animals."index", colors.id
        FROM animals
        JOIN colors ON colors.color = animals.color2
    """

    query_6 = """
        INSERT INTO animals_colors (animals_id, colors_id)
        SELECT DISTINCT
            animals.final_id, colors.id
        FROM animals
        JOIN colors 
            ON colors.color = animals.color1
        JOIN animals.final
            ON animals.final.animal_id = animals.animal_id
        UNION ALL
        SELECT DISTINCT animals.final.id, colors.id
        FROM animals
        JOIN colors ON colors.color = animals.color2
        JOIN animals.final
            ON animals_final.animal_id = animals.animal_id
    """

    query_7 = """
        CREATE TABLE IF NOT EXISTS outcome (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , subtype VARCHAR(50)
            , "type" VARCHAR(50)
            , "month" INTEGER
            , "year" INTEGER 
        )
    """

    query_8 = """
        INSERT INTO outcome (subtype, "type", "month", "year")
        SELECT DISTINCT
            animals.outcome_subtype
            , animals.outcome_type
            , animals.outcome_month
            , animals.outcome_year
        FROM animals
    """

    query_9 = """
        CREATE TABLE IF NOT EXISTS animals.final (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , age_upon_outcome VARCHAR(50)
            , animal_id VARCHAR(50)
            , animal_type VARCHAR(50)
            , name VARCHAR(50)
            , breed VARCHAR(50)
            , date_of_birth VARCHAR(50)
            , outcome_id INTEGER
            , FOREIGN KEY (outcome_id) REFERENCES outcome(id)
        )
    """

    query_10 = """
        INSERT INTO animals_final (age_upon_outcome, animal_id, animal_type, name, breed, date_of_birth, outcome_id)
        SELECT
            animals.age_upon_outcome
            , animals.animal_id
            , animals.animal_type
            , animals.name
            , animals.breed
            , animals.date_of_birth
            , animals.outcome_id
        FROM animals
        JOIN outcome
            ON outcome.subtype = animals.outcome_subtype
            AND outcome."type" = animals.outcome_type
            AND outcome."month" = animals.outcome_month
            AND outcome."year" = animals.outcome_year
        )
    """

    query_11 = """
        INSERT INTO breeds (breed)
        SELECT DISTINCT animals.breed
        FROM animals
        LEFT JOIN breeds ON breeds.breed = animals.breed
        )
    """

    query_12 = """
        INSERT INTO types (type)
        SELECT DISTINCT animals.animal_type
        FROM animals
        LEFT JOIN types ON types.type = animals.animal_type
        )
    """

    query_final = """
        INSERT INTO animals_colors (animals_id, colors_id)
        SELECT DISTINCT
            animals_final.id, colors_id
        FROM animals
        JOIN COLORS
            ON colors.color = animals.color1
        JOIN animals_final
            ON animals_final.animal_id = animals.animal_id
        UNION ALL
        SELECT DISTINCT animals_final.id, colors_id
        FROM animals
        JOIN colors ON colors.color = animals.color2
        JOIN animal_final
            ON animals_final.animal_id = animals.animal_id
        SELECT * FROM animals_colors
        DELETE FROM colors WHERE color IS NULL
    """


if __name__ == '__main__':
    main()
