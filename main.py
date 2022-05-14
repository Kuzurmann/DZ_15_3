import sqlite3
import json
import query
from flask import Flask, request, jsonify
import logging

OLD_DATABASE = 'animal.db'
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_sqlite_query(query, base=OLD_DATABASE, is_script=False):
    """Читаем старую базу данных"""
    with sqlite3.connect(base) as connection:
        cursor = connection.cursor()
        if is_script:
            result = cursor.executescript(query)
        else:
            result = cursor.execute(query)
        return result.fetchall()


def get_all_by_id(id):
    query = f"""
    SELECT * 
    FROM animals.final
    WHERE id == {id}
    """

    raw = get_sqlite_query(query, is_script=False)
    result_dict = {'id': raw[0][0], 'age_upon_outcome': raw[0][1], 'animals_id': raw[0][2],
                   'name': raw[0][3], 'animals_type': raw[0][4], 'animals_breed': raw[0][5],
                   'color1': raw[0][6], 'color2': raw[0][7], 'date_of_birth': raw[0][8][0:10],
                   'outcome_subtype': raw[0][9], 'id_outcome_type': raw[0][10], 'outcome_month': raw[0][11],
                   'outcome_year': raw[0][12]}
    return result_dict


@app.route('/<id>/')
def get_by_id(id):
    """ Шаг 1. Поиск по названию самого свежего """
    logging.info(f'Ищем по ID: {id}')

    animal = get_all_by_id(id)  # Словарь с данными по ОДНОМУ посту
    logging.info(f'Функция поиска вернула: {animal}')

    return jsonify(animal)


if __name__ == '__main__':
    app.run()
