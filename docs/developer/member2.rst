Parts Implemented by Member Name
================================
My responsability was to implement a part of the social network part of the project. I worked on many entities
and tables

Entities
--------
These are the main entities I worked on

user
____
This entity represents a user and all the his properties
- :code:`main()` returns the user page

- :code:`settings()` returns the settings page

- :code:`updateProfile()` updates the profile settings

- :code:`likeResto()` add a restaurant to the favorites list

- :code:`likeDish()` add a dish to the favorites list

reviews
_______
- :code:`addReview()` add a review on a restaurant or dish

- :code:`deleteReview()` delete a given review on a restaurant or dish

recommendations
_______________
- :code:`main()` returns the recommendations page


Tables
------

restolikes
__________
.. code-block:: sql
   CREATE TABLE restolikes (user_id INTEGER, resto_id INTEGER)

- :code:`likeResto(userId, restoId)`   add a like relationship between a user and a restaurant

- :code:`getLikedRestos(userId)`  get the list of restaurants a user likes

- :code:`getLikedRestoDetails(restoId)`  get information about restaurant

- :code:`reset()`  resets the table to the initial state



dishlikes
_________
.. code-block:: sql
   CREATE TABLE dishlikes (user_id INTEGER, dish_id INTEGER)

- :code:`likeDish(userId, dishId)`   add a like relationship between a user and a dish

- :code:`getLikedDishess(userId)`  get the list of dishes a user likes

- :code:`getDishDetails(dishId)`  get information about a dish

- :code:`reset()`  resets the table to the initial state

reviews
_______
.. code-block:: sql
   CREATE TABLE reviews (id SERIAL PRIMARY KEY, user_id INTEGER ,
                resto_id INTEGER, dish_id INTEGER, content VARCHAR)

- :code:`addReview()` add a review about given resto, dish or general

- :code:`deleteReview()` delete a given review

- :code:`getUserReviews(userId)` get reviews list of a user


Jinja module
____________
These are the methods I wrote in the jinja module to facilitate use in templates

- :code:`getAllReviews(userId)`

- :code:`addReview(userId, restoId, dishId, content)`

- :code:`getLikedRestos(userId)`

- :code:`getLikedDishes(userId)`

