Developer guide
===============

Database design
---------------

**explain the database design of your project**

**include the E/R diagram(s)**

Code
----
The project uses a precisely defined architecture which should be respected, in order to be maintained easily, prevent git collisions, and more.

Config module
_____________
The config module is a configuration file, which defines database credentials, and many other parameters such as the min and max length of a user's email address.

Jinja module
____________
The jinja module regroups python methods callable by templates.

There are many methods in it, but main ones are: *checkSessions*, which is called at the beginning of each layout to manage the user state (if connected or not, by the use of cookies and sessions).
Another important method is *isLogged* to check whether the current user is logged in.
With this module, it is possible to check easily in any page if the visistor uses a mobile, generate a random number, check if a file exists, and many other necessary things.

Template example::

      <!-- some html -->
      Welcome
      {% if isLogged() %}
         {{ getUser()[1] }}
      {% else %}
         visitor
      {% endif %}

Common module
_____________
The common module regroups methods which are often used by entities to avoid redundancy.

Some examples are *md5* (generate md5 hash), *validPhone* (checks wether input is a valid phone number), *redirectLogin* (redirects to the login page with optionally a link called in case of a successful login)..
The method to be used for creating a new connection to the database is *db*.
There are also important methods to build basic queries easily such as *selectone*, *insert*, *count* or *delete*.
These functions basically convert a given dictionary to an SQL query, execute it, and return desired results::

      selectone('users', { 'id' : 1 }) # SELECT * FROM users WHERE id = 1
      insert('employees', { 'restoid' : 5, 'userid' : 8, 'role' : 1 }) # INSERT INTO employees (restoid, userid, role) VALUES (5, 8, 1)

Entities
________
Entities are distinct parts of the project, an entity depends on other entities very minimally.

They must be in the folder */entities* of the project.
They are automatically loaded. It is sufficient to create a module without the need of special setup in the project.
Each entity should have a main variable called page of type Blueprint.
An entity can have a method called *reset*. All the reset methods are called when the website should be reset.
A reset can be anything, but in general, it drops and recreates the tables the entity works on, and add some dummy data.
An entity can have its own css and js files beside the main ones (called *style.css* and *common.js*), which should be in the */static/(styles|scripts)* folder and have the names *[entity].(css|js)*.

Example of a basic entity accessible with the links */example* and */hello*::

      from flask import render_template
      import datetime

      from common import *
      from tables import restos, menus

      page = Blueprint(__name__)

      @page.route('/example')
      def main():
          now = datetime.datetime.now()
          return render_template('example.html', current_time = now.ctime())

      @page.route('/hello')
      def main():
          return 'hello'

      def reset():
          restos.reset()
          menus.reset()
          restos.add('My new restaurant', )
          return

Tables
______
Tables is a folder which contains modules dealing with database operations.
These must be imported to entities when needed.
For example, the module users (referring to the table of the same name) has methods for creating a new user, loading a user from credentials (mail, password) or by id.

.. toctree::

   member1
   member2