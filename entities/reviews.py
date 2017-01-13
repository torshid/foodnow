from flask import render_template
from common import *

import datetime

from tables import users

page = Blueprint(__name__)



def reset():
    from tables import reviews
    reviews.reset()
    return

@page.route('/reviews/add/')
def addReview(userId, restoId, dishId, content):
    inserted = insert('reviews', {'user_id': userId, 'resto_id': restoId, 'dish_id': dishId, 'content': content})
    return inserted

@page.route('/reviews/delete/<int:id>')
def deleteReview(id):
    deleted = delete('reviews', {'id': id})
    return redirect(request.args.get('next') or request.referrer or  url_for(default))

