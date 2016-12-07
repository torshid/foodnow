from flask import render_template, redirect, url_for

from common import *

import datetime

page = Blueprint(__name__)

@page.route('/reset')
def main():
    with db() as connection:
        for name in os.listdir("entities"):
            if name.endswith(".py"):
                modname = name[:-3]
                module = __import__('entities.' + modname, fromlist = ['reset'])
                if (hasattr(module, 'reset')):
                    func = getattr(module, 'reset')
                    if callable(func):
                        func()
    return redirect(url_for('entities.home.main'))