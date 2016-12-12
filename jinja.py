def fileExists(name):
    import os
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
    return session['user']