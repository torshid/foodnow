from flask import render_template, redirect, abort, request
from flask.helpers import url_for
from common import *

from tables import restos, employees, users

page = Blueprint(__name__)

@page.route('/<string:resto_pseudo>/panel/employees', methods = ['GET', 'POST'])
def main(resto_pseudo):
    permission = hasPanelAccess('entities.manageemployees.main', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    employments = employees.getRestoEmployees(resto[0])
    index = 0

    for employment in employments:
        employments[index] += (users.getUserFromId(employments[index][2]),)
        index += 1

    return render_template('panel/employees.html', resto = resto, employees = employments)

@page.route('/<string:resto_pseudo>/panel/employees/add', methods = ['GET', 'POST'])
def add(resto_pseudo):
    permission = hasPanelAccess('entities.manageemployees.add', resto_pseudo = resto_pseudo)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    mail = ''
    role = roleworker
    errors = []

    if anydata():
        if exist('mail') and exist('role'):
            mail = request.form['mail']
            role = request.form['role']
            if not validMail(mail):
                errors.append('Please enter a correct mail address')
            else:
                user = users.getUserFromMail(mail)
                if not user:
                    errors.append('The mail address was not recognized')
                else:
                    employment = employees.getUserRestoEmployment(resto[0], user[0])
                    if employment:
                        errors.append('This person is already an employee')
            if not validRole(role):
                errors.append('You must select a valid role option')
            if len(errors) == 0:
                employees.addEmployee(resto[0], user[0], role)
                return redirectPanelJS('entities.manageemployees.main', '<br/>' + bsalert('You successfully added ' + user[1] + ' as an employee', 'success'), resto_pseudo = resto_pseudo)

    return render_template('panel/addemployee.html', resto = resto, mail = mail, role = role, errors = errors)

@page.route('/<string:resto_pseudo>/panel/employees/<int:employee_id>/remove', methods = ['GET', 'POST'])
def remove(resto_pseudo, employee_id):
    permission = hasPanelAccess('entities.manageemployees.remove', resto_pseudo = resto_pseudo, employee_id = employee_id)
    if not isinstance(permission, tuple):
        return permission
    resto, employment = permission

    employee = employees.getEmployee(employee_id)
    if not employee:
        abort(404)

    if employee[1] != resto[0]:
        abort(403)

    if employee[2] == getUser()[0]:
        return redirectPanelJS('entities.manageemployees.main', '<br/>' + bsalert('You can not remove yourself', 'danger'), resto_pseudo = resto_pseudo)

    employees.deleteEmployee(employee[0])
    employee = users.getUserFromId(employee[2])

    return redirectPanelJS('entities.manageemployees.main', '<br/>' + bsalert('You successfully removed employee ' + employee[1], 'info'), resto_pseudo = resto_pseudo)

def reset():
    menus.reset()
    return