import sqlite3
from flask import Response
import json


def run_db_query(db_path, query, params={}, is_json=True, multilines=True):
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    if bool(params):
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    if multilines:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()

    if is_json:
        response = Response(json.dumps(result))
    else:
        response = Response(result)

    response.headers['Content-type'] = "application/json"

    return response
