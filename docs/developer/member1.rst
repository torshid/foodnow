Parts implemented by Yusuf Aksoy
================================
I was responsible of the project architecture, I implemented several entities along with multiple functions in the common and jinja modules.

Common module
-------------
Below is a partial list of the methods I implemented in the common module.

- :code:`db()` Returns a new database connection.

- :code:`anydata()` Returns true if there is any http post variable sent.

- :code:`exist(key)` Checks if a http post variable was sent.

- :code:`validLength(value, min, max)` Checks if the given string's length is between the given bounds

- There are many :code:`valid[...]()` functions, mainly based on the :code:`validLength` function, which checks if a given string matches some category. These functions are called to verify user input. For example, :code:`validMail(mail)` checks if a given string is a valid mail address.

- :code:`isbool(s)` Checks if a given variable is a bool.

- :code:`isint(s)` Checks if a given variable is of type int.

- :code:`isfloat(s)` Checks if a given variable is of type float.

- :code:`md5(value)` Generates the md5 hash of a given string

- :code:`md5Password(password)` Generates a password's md5 hash (salted).

- :code:`hasPanelAccess(entity, onlypost = True, **data)` Checks if the logged user can access a restaurant's panel, if not: he is redirected, if yes, the restaurant tuple and employment tuple are returned.

- :code:`redirectLogin(entity, **data)` Redirects to the login page and generates the redirect url (called when successful login) depending on the given entity.

- :code:`redirectPanel(entity, **data)` Makes a panel redirection.

- :code:`redirectPanelJS(entity, message = None, **data)` Makes a panel javascript redirection.

- :code:`bsalert(message, type = None)` Generates a bootstrap alert.

- :code:`allowedFile(extensions, filename)` Checks if the given file name has a valid extension depending on the given extensions.

- :code:`checkUpload(extensions, path)` Checks if an uploaded file is valid, if so; saved.

- :code:`resizePicture(source, destination, size)` Resizes a picture file.

- :code:`selectone(table, dict = None, extra = None)` Makes an sql select and returns the first result.

- :code:`selectall(table, dict = None, extra = None)` Makes an sql select and returns all the results.

- :code:`count(table, field, dict = None)` Makes an sql count.

- :code:`delete(table, dict)` Makes an sql delete.

- :code:`insert(table, dict, simple = None)` Makes an sql insert.

- :code:`update(table, dict, extra = None)` Makes an sql update.

Jinja module
------------
Below are functions I implemented callable by templates.

- :code:`foodnow()` Returns the project name..

- :code:`isMobile()` Checks if the visitor uses a mobile..

- :code:`checkSessions()` Updates user session variables (called in the beginning of layouts)..

- :code:`isLogged()` Checks if the visitor is logged.

- :code:`getUser()` Returns the user tuple.

- :code:`fileExists(name)` Checks if a given file name exists..

- :code:`dishImageExists(dishid)` Checks if dish's picture exists.

- :code:`nl2br(value)` Replaces *\\n* with *<br/>*.

- :code:`random(min, max)` Generates a random int.

- :code:`istrue(s)` Checks if a given string is *true*, ('1', 1, ...).

- :code:`isfalse(s)` Checks if a given string is *false* ('0', 0, ...).

- :code:`getUserEmployments()` Returns the user's employments.

- :code:`getRoles()` Returns the list of roles (id, title).

- :code:`getRoleTitle(role)` Returns the title of a given role.

- :code:`isManager(employee)` Checks if a given employment's role is manager.

- :code:`isWorker(employee)` Checks if a given employment's role is worker.

- :code:`isDriver(employee)` Checks if a given employment's role is manager.

- :code:`getMenuDishes(menuid)` Returns the dishes of a given menu.

- :code:`getResto(id = None, pseudo = None)` Returns a restaurant's tuple.

- :code:`panel_for(entity, **data)` Generates a url for panel entities.

Tables
------
Below are table modules I implemented (with their sql definitions and functions).

Users
_____
.. code-block:: sql

   CREATE TABLE users (id SERIAL, name VARCHAR, mail VARCHAR UNIQUE, password VARCHAR)

- :code:`addUser(name, mail, password)` Creates a new user.

- :code:`getUser(mail, password)` Returns a user with given mail and password combination.

- :code:`getUserFromId(id)` Returns a user with given id.

- :code:`getUserFromMail(mail)` Returns a user with given mail address.

Restos
______
.. code-block:: sql

   CREATE TABLE restos (
      id SERIAL, name VARCHAR, pseudo VARCHAR UNIQUE, mail VARCHAR, phone VARCHAR,
      accessible BOOLEAN DEFAULT false, warnmsg VARCHAR DEFAULT 'Our restaurant page is under construction, see you soon!',
      currency VARCHAR, description VARCHAR)

- :code:`addResto(name, pseudo, mail, phone, currency, description, accessible = None)` Creates a new restaurant.

- :code:`getResto(pseudo)` Returns a restaurant with given pseudo (string identifier).

- :code:`getRestoFromId(id)` Returns a restaurant with given id.

- :code:`updateResto(id, name, pseudo, mail, phone, accessible, warnmsg, currency, description)` Updates a restaurant.

- :code:`getLastRestos()` Returns the last created restaurants.

Employees
_________
.. code-block:: sql

   CREATE TABLE employees (id SERIAL, restoid INTEGER, userid INTEGER, role SMALLINT, deleted BOOLEAN DEFAULT false)

- :code:`addEmployee(restoid, userid, role)` Adds an employee to a restaurant.

- :code:`getEmployee(id)` Returns an employment with given id.

- :code:`deleteEmployee(id)` Deletes an employment.

- :code:`getRestoEmployees(restoid)` Returns a restaurant's employees.

- :code:`getUserEmployments(userid)` Returns a user's employments.

- :code:`getUserRestoEmployment(restoid, userid)` Returns an employment.

- :code:`isManager(employee)` Checks if an employment's role is manager.

- :code:`isWorker(employee)` Checks if an employment's role is worker.

- :code:`isDriver(employee)` Checks if an employment's role is driver.

- :code:`countRestoEmployees(restoid)` Returns the number of a restaurant's employees.

Menus
_____
.. code-block:: sql

   CREATE TABLE menus (id SERIAL, restoid INTEGER, name VARCHAR, disposition SMALLINT, visible BOOLEAN)

- :code:`addMenu(restoid, name, disposition, visible)` Creates a menu in a restaurant.

- :code:`getRestoMenus(restoid)`  Returns menus of a restaurant.

- :code:`getMenu(id)` Returns the menu with given id.

- :code:`getRestoMenuHighestDisposition(restoid)` Returns the menu with the highest disposition in a restaurant.

- :code:`updateMenu(id, name, disposition, visible)`  Updates a menu.

- :code:`deleteMenu(id)` Deletes a menu.

- :code:`countRestoMenus(restoid)` Returns the number of menus in a restaurant.

Dishes
______
.. code-block:: sql

   CREATE TABLE dishes (id SERIAL, menuid INTEGER, name VARCHAR, price REAL, disposition SMALLINT, visible BOOLEAN, deleted BOOLEAN DEFAULT false, description VARCHAR DEFAULT '')

- :code:`addDish(menuid, name, price, disposition, visible, description)` Creates a dish in a menu.

- :code:`getDish(id)` Returns the dish with given id.

- :code:`getMenuDishesHighestDisposition(menuid)` Returns the dish with the highest disposition in a menu.

- :code:`deleteDish(id)` Deletes a dish.

- :code:`getMenuDishes(menuid)` Returns the dishes of a menu.

- :code:`updateDish(id, menuid, name, price, disposition, visible, description)` Updates a dish.

- :code:`countMenuDishes(menuid)` Returns the number of dishes in a menu.

Entities
--------

Home
____
+-----------+----------------+--------------------------+
| Route     | Function       | Description              |
+===========+================+==========================+
| :code:`/` | :code:`main()` | Home page of the website |
+-----------+----------------+--------------------------+

Login/signup
____________
+------------------------------------+-----------------------------+---------------------------------------------------+
| Route                              | Function                    | Description                                       |
+====================================+=============================+===================================================+
| :code:`/signup`                    | :code:`signup()`            | Signup page                                       |
+------------------------------------+-----------------------------+---------------------------------------------------+
| :code:`/login/<path:redirect_url>` | :code:`login(redirect_url)` | Login page with redirection upon successful login |
+------------------------------------+-----------------------------+---------------------------------------------------+
| :code:`/logout`                    | :code:`logout()`            | Logout page                                       |
+------------------------------------+-----------------------------+---------------------------------------------------+

Reset
_____
+---------------------------------+---------------------------+-----------------------------+
| Route                           | Function                  | Description                 |
+=================================+===========================+=============================+
| :code:`/reset`                  | :code:`main()`            | Resetting whole entities    |
+---------------------------------+---------------------------+-----------------------------+
| :code:`/reset/<string:modname>` | :code:`specific(modname)` | Resetting a specific entity |
+---------------------------------+---------------------------+-----------------------------+
| :code:`/pull`                   | :code:`pull()`            | Performing a git pull       |
+---------------------------------+---------------------------+-----------------------------+

Manage restos
_____________
+-------------------------+---------------+--------------------------------+
| Route                   | Function      | Description                    |
+=========================+===============+================================+
| :code:`/new-restaurant` | :code:`new()` | Creating a new restaurant page |
+-------------------------+---------------+--------------------------------+

Panel
_____
+-----------------------------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------+
| Route                                         | Function                       | Description                                                                                             |
+===============================================+================================+=========================================================================================================+
| :code:`/<string:resto_pseudo>/panel/`         | :code:`main(resto_pseudo)`     | Panel main page of a restaurant; sends the panel layout (the other pages are called with JS: no layout) |
+-----------------------------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :code:`/<string:resto_pseudo>/panel/overview` | :code:`overview(resto_pseudo)` | Overiew (summary of data)                                                                               |
+-----------------------------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :code:`/<string:resto_pseudo>/panel/settings` | :code:`settings(resto_pseudo)` | Editing settings                                                                                        |
+-----------------------------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------+

Manage employees
________________
+-------------------------------------------------------------------------+-------------------------------------------+------------------------------------------+
| Route                                                                   | Function                                  | Description                              |
+=========================================================================+===========================================+==========================================+
| :code:`/<string:resto_pseudo>/panel/employees`                          | :code:`main(resto_pseudo)`                | Listing of the employees of a restaurant |
+-------------------------------------------------------------------------+-------------------------------------------+------------------------------------------+
| :code:`/<string:resto_pseudo>/panel/employees/add`                      | :code:`add(resto_pseudo)`                 | Adding a new employee                    |
+-------------------------------------------------------------------------+-------------------------------------------+------------------------------------------+
| :code:`/<string:resto_pseudo>/panel/employees/<int:employee_id>/remove` | :code:`remove(resto_pseudo, employee_id)` | Removing an employee                     |
+-------------------------------------------------------------------------+-------------------------------------------+------------------------------------------+

Manage menus
____________
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+
| Route                                                           | Function                              | Description                          |
+=================================================================+=======================================+======================================+
| :code:`/<string:resto_pseudo>/panel/menus`                      | :code:`main(resto_pseudo)`            | Listing of the menus of a restaurant |
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/new`                  | :code:`new(resto_pseudo)`             | Creating a new menu                  |
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>`        | :code:`view(resto_pseudo, menu_id)`   | Viewing a menu (dish list)           |
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/edit`   | :code:`edit(resto_pseudo, menu_id)`   | Editing a menu                       |
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/delete` | :code:`delete(resto_pseudo, menu_id)` | Deleting a menu                      |
+-----------------------------------------------------------------+---------------------------------------+--------------------------------------+

Manage dishes
_____________
+--------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------+
| Route                                                                                | Function                                       | Description                   |
+======================================================================================+================================================+===============================+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/new`                  | :code:`new(resto_pseudo, menu_id)`             | Creating a new dish in a menu |
+--------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/delete` | :code:`delete(resto_pseudo, menu_id, dish_id)` | Deleting a dish               |
+--------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>`        | :code:`view(resto_pseudo, menu_id, dish_id)`   | Viewing a dish                |
+--------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------+
| :code:`/<string:resto_pseudo>/panel/menus/<int:menu_id>/dishes/<int:dish_id>/edit`   | :code:`edit(resto_pseudo, menu_id, dish_id)`   | Editing a dish                |
+--------------------------------------------------------------------------------------+------------------------------------------------+-------------------------------+
