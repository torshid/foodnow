from flask import render_template
from common import *

import datetime
import psycopg2 as dbapi2

page = Blueprint(__name__)

@page.route('/recommendations/')
def main():
    return render_template('recommendations.html')

def recommendResto(restoId):

    return

def recommendMeal(restoId, mealId):

    return

def getRecommendations():
    statement = ""
    try:
        connection = dbapi2.connect(dsn)
        cursor = connection.cursor()
        cursor.execute(statement)
        connection.commit()
        cursor.close()
    except dbapi2.DatabaseError:
        connection.rollback()
    finally:
        connection.close()
    return