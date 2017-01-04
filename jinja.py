def foodnow():
    return "Food — Now !"

def fileExists(name):
    import os
    if name[:1] == '/':
        name = name[1:]
    return os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/' + name)

def checkSessions():
    from flask import request, session
    if 'mail' in request.cookies and 'password' in request.cookies:
        session['mail'] = request.cookies['mail']
        session['password'] = request.cookies['password']
    if 'mail' in session and 'password' in session:
        from tables import users
        user = users.getUser(session['mail'], session['password'])
        if user:
            session['user'] = user
        else :
            if 'mail' in session: del session['mail']
            if 'password' in session: del session['password']
            if 'user' in session: del session['user']
    return

def istrue(s):
    return s == '1' or s == 1

def isfalse(s):
    return not istrue(s)

def isLogged():
    from flask import session
    return 'user' in session

def getUser():
    from flask import session
    return session['user']

def getUserEmployments():
    from tables import employees
    return employees.getUserEmployments(getUser()[0])

def isManager(employee):
    from tables import employees
    return employees.isManager(employee)

def isWorker(employee):
    from tables import employees
    return employees.isWorker(employee)

def isDriver(employee):
    from tables import employees
    return employees.isDriver(employee)

def getRoles():
    from common import roles
    return roles

def getRoleTitle(role):
    from common import roles
    for rol in roles:
        if rol[0] == role:
            return rol[1]
    return 'Unknown'

def panel_for(entity, **data):
    from flask.helpers import url_for
    return '/'.join(url_for(entity, **data).split('/')[3:]).replace('/', '-')

def getResto(id = None, pseudo = None):
    from tables import restos
    if id:
        return restos.getRestoFromId(id)
    else:
        return restos.getResto(pseudo)

def getLikedRestos(userId):
    from tables import restolikes
    return restolikes.getLikedRestos(userId)

def updateProfile(userId, name = None, email = None, password = None):
    from entities import user
    user.updateProfile(name, email, password)
    return

def getMostLikedRestos():
    from tables import restos
    return restos.getMostLikedRestos()

def getMostLikedDishes():
    from tables import dishes
    return dishes.getMostLikedDishes()
