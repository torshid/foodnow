Parts implemented by Yusuf Aksoy
================================

Home page
---------
The home page displays a welcoming message with a random background image. If the visitor is not connected, he is invited to sign up.
The last created created restaurants are also displayed with their descriptions.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/home.png

Signup page
-----------
The visitor should enter his full name, mail address (which will be used as the login), and a password.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/register.png

Login page
----------
In order to log in, users should enter their mail address and relevant password.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/login.png

Create restaurant page
----------------------
On this page, a connected user can create his own restaurant by defining it with some properties. Important ones to note are:
   - @name: which we can say will be the identifier of the restaurant, used to access it.
   - currency: this is what will be shown after each price in the menus.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/newresto.png

Restaurant page
---------------
Users can access this page to interact with a restaurant. See all the informations, social data, and most importantly: see the menus.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/restoo.png

Panel pages
-----------
The pages listed below are all related to the panel.
The panel is what we call the group of pages with the purpose of managing a restaurant.
We should note that the panel is accessible for the employees having the status of manager.
*Some pages with no special rendering are not listed.*

Overview
--------
This page is a quick summary of the restaurant data.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/overview.png

Settings
--------
Here, a manager can modify the properties of the restaurant.
It is also possible to disable the restaurant page to the public and write a warning message, for maintenance purposes or to be able to manage the menus calmly for example.
The restaurant page is then visible only by employees.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/settings.png

Menus management
----------------
A menu is what is used to divide dishes. Examples can be: breakfast, dinner, beverages.
The manager should give a menu a name, a disposition (order of appearence), and can specify if it is visible.
It is afterwards possible to edit it, add dishes to it, or delete it (if it contains no dishes).

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/menus.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/newmenu.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/editmenu.png

Dishes management
-----------------
After having selected a menu, a dish can be added.
A dish has several properties such as a name, price, and a picture.
It is also possible to edit and delete dishes.

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/menu.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/newdish.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/dish.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/editdish.png

Employees management
--------------------
It is possible here for a manager to add employees with their mail addresses. The employees should therefore have an account too.
There are three employee roles: manager, worker (able to manage incoming orders), driver (can be assigned as the delivery man for an order).

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/employees.png

.. figure:: https://github.com/torshid/foodnow-screens/raw/master/panel/addemployee.png