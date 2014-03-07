IFDTCDjangoServer
=================

The Django backend for the IFDTC app

Install dependencies:
---------------------
Install Python 3.3+

Install pip

Make sure python33 and python33/scripts are in your path

	pip install django
	pip install djangorestframework
	pip install TwitterAPI

Setting up the server
---------------------
To set up the server, you need to define various settings in ifdtc/settings.py
Django has a good set of documentation on setting up your settings.py file for your needs
https://docs.djangoproject.com/en/dev/topics/settings/

There's also a reference for any command available in the settings.py:
https://docs.djangoproject.com/en/dev/ref/settings/

I would also recommend running the following command, and then replacing the ifdtc/settings.py that comes in this git with the new ifdtc/settings.py

	python startproject ifdtc
	
This will allow you to start with a fresh settings.py, since I had to remove a bunch of varaibles from this code.

Once you have your database setup, sync the database to your Django model from the app's root directory (manage.py)

	python manage.py syncdb

You can also define the verbosity by adding --verbosity num at the end, where num is 0-3, 3 being most verbose

When you syncdb without changing any settings, it will default to a SQLite database, which comes with python.

Setting up twitter
------------------
Twitter runs as a passthrough from the mobile app, where the mobile app defines the twitter query.  You need to setup the twitter API here though
To do that:

* Open twitter/views.api

Set the following variables with the values you get from Twitter's API v2 on a twitter dev account:

    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''
	

How to run a development server
-------------------------------
Open the directory with manage.py
	python manage.py runserver [hostname:port]
	
For the most part, configuration of different "apps" is done through the mobile app, this only stores & processes data or acts as a passthrough in the case of Twitter
This also isn't how you should handle production, this uploaded version has also had various values removed.

How to access parts of the server
---------------------------------
At any time, you can look at a module's urls.py to see where http traffic is directed.  Here's a quick rundown though:

	[domain]/admin - admin interface
	[domain]/feedback - takes POST requests from the overall conference feedback
	[domain]/sessionfeedback - takes POST requests from session feedback, ties response to session in one-to-many relationship
	[domain]/activites - returns a JSON list of activities
	[domain]/activitysubmit - takes POST request from activity submission
	[domain]/agenda - shows overall agenda in JSON
	[domain]/agenda/[date] - shows the agenda for that specifc date in JSON
	[domain]/attendees/all - shows all the attendees in JSON
	[domain]/attendees/[letter] - shows all attendees that start with [letter] in JSON
	[domain]/twitter/[search] - searches twitter for [search], returns JSON
	
	
Things that need to be done still
---------------------------------
* User auth is only there for admin interface, adding auth for users might be a good idea
* Serialization of data to JSON is very static, should be rebuilt to be more restful
* More fields may need to be added to various models to store data that may not be used on mobile
* Build tests for the views/models.  This was written on a very tight schedule and I didn't have time to make these

Any questions, feel free to email me at rfenton@umich.edu
