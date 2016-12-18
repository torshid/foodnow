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

def getResto(id = None, pseudo = None):
    from tables import restos
    if id:
        return restos.getRestoFromId(id)
    else:
        return restos.getResto(pseudo)