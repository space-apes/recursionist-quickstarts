## Django Quickstart
This quickstart output guide will cover all of the necessary knowledge to begin building applications in Django, a Python-based back-end web framework that emphasizes ease of  development but is also powerful enough to be the basis of large projects like Instagram and the Mozilla website. In its most common use-case, Django would be used to create web applications that are driven by Python logic to interact with data from persistent storage (like a database), then insert that data as dynamic content into the web pages that your user sees. However, Django can do much more than that. On top of the ability to pull in any existing Python libraries, Django follows a “batteries included” philosophy and comes packaged with many of the features and functionality that a developer would commonly use in their projects such as testing, authentication, multi-site support and middlewares.

To make the best use of this quickstart, it is suggested you feel comfortable with the following topics:
- Command line activities such as installation, execution with flags
- MVC application architecture
- Python3 Syntax, Python modules
- OOP principles and design
- HTTP protocol 
- Relational database basics
- Getting information from Web API
- HTML, CSS, JS basics

## Django High-Level Overview

Before we begin with installing Django on your system, let’s take a high-level view of Django’s MVT architecture and compare it to the serving of a static web page from a web-server in order to see how all the components of Django fit together. 

![Basic Static Website Overview](images/StaticPageDiagram.png "Basic Static Website Overview")
Almost every website interaction will involve the basic flow of having a client browser make an HTTP request from a server, requesting some resource, and the server sending back an HTTP response with the contents of the requested resource. In the most basic case, the resource requested is stored on the server computer as one or more static files that may be stored on the hard drive.

You can find a refreshed on general HTTP concepts including Requests and Responses here:
[https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

![Django Simplified Overview](images/DjangoBasicDiagram.png)
Django adds a layer to the basic flow, where the Django executable is able to send and retrieve data from a variety of other elements, process it, and assemble a dynamic response that will be understood by the web browser before sending a response. In the end, a Django app receives an HTTP request, and responds with an HTTP response. In this way, we can connect the idea of Django apps to Input->Output.

![Django MVT Elements Through Example](images/MVTBasicDiagram.png)
Let’s look a little deeper through an example. In order to maintain a separation of concerns, Django follows the MVT (Model, View, Template) architectural pattern. MVT is similar to the MVC (Model View Controller) pattern, but if you are familiar with MVC be careful about conflicts in the terminology between the two patterns.

### Model
These are descriptions of the types of data we will use in our application and arguably, serve as the core of our django projects. They are very similar to the concept of OOP classes, containing both data fields and also method definitions. Instances of models can be created and manipulated in code, but they are also represented in the database as records. In this example, we have GolfPlayers, but might also have Skiers, and WebsiteUsers.

### View
These are Python functions and methods that are executed when some url is requested. They take in an Http Request and return an Http Response. They are responsible for all of the business logic that must occur when a resource is requested, as well as the selection and assembly of the components in the final response. In this example, we have views that will be executed when users access the login page, golf page, or skiing page.

### Template
These are skeletons for the types of web pages we want to view as the final output. They are made up of HTML, CSS, and data that was retrieved and inserted by the View. Along with these, Django has a templating language to interact with data passed in as well as help structure the page to do things like create multiple tags in a loop. In this example there is a template for all pages that have to do with sports. We may reuse this template when users request Golf resources or Skiing resources, inserting different content but using the same structure. 

### Putting It All Together
![Django MVT Elements Through Example](images/MVTBasicDiagram.png)
1.  client browser requests ‘example.com/golf’
2.  server passes request on to django
3.  the url mapper matches the ‘/golf’ part of request and calls golfView()
4.  golfView() requests data from the database and uses the GolfPlayer model as a 
        guide
5.  golfView() uses data from the DB and GolfPlayer.calculateStats() from Model 
        definition to calculate statistics for given players
6.  golfView() inserts DB data and calculated data into sports template 
7.  golfView() returns assembled template with inserted dynamic data
8.  Django passes response back to server
9.  Server passes response back to client browser

Of course, this is an example showing a fraction of the potential of Django in order to illustrate the overall flow.

## Installation and Setup
Django is written in Python and installed as a python package through the pip python package manager. If your particular operating system supports Python, you will more than likely be able to install Django as well.

1. Install Python if it is not already installed. 
    - check which version of Python is needed for the newest version of Django:
    -  https://docs.djangoproject.com/en/3.2/faq/install/#faq-python-version-support
    - Official Beginner’s Guide for Python: 
    -  https://wiki.python.org/moin/BeginnersGuide/Download
    - make sure to click “add Python to PATH” during installation
    - Test your installation by running the python executable with no arguments. exit interactive mode with `quit()` 
    - because the python executable has different names in different operating systems, 
    it will be referred to by the name ‘python’ for the rest of this quickstart. 
2. Install Django pip package
    -  https://docs.djangoproject.com/en/3.2/intro/install/
    - `pip install django`
3. Start a test project 
    - `django-admin startproject testProject`
    - this should generate a folder containing a number of files
    - ![Django Project Files](images/djangoProjectFiles.png)
4. Run your test project on the development server
    - change directory to the testProject directory
    - `python manage.py runserver 8080`
    - open your web browser and enter this address: “127.0.0.1:8080”
    - you should see this:
    - ![Django Install Success](images/djangoInstallSuccess.png)
5. (optional) Create virtual environments to isolate each Django project
    - Windows: https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment  
    - Linux/MacOS(see section on venv): https://docs.djangoproject.com/en/3.2/intro/contributing/ 
7. (Optional) Install django-extensions pip package
    - this package includes some quality of life features like auto-loading all packages when 
        testing instead of loading them in manually
    - `pip install django-extensions`

## Official Tutorial: Poll Project
Follow the Django official tutorial to get an understanding of how all of the components work together:
https://docs.djangoproject.com/en/3.2/intro/tutorial01/

## Stepping Stone 1: Url Dispatcher, Views, Templates
The Django request cycle is:

1. Client Browser makes Http Request
2. Url Dispatcher matches the requested url, and calls associated view function
3. View function assembles an Http Response
4. Http Response is sent back to Client Browser

The url dispatcher is the first routine of our django app that is triggered by an incoming request and the url->view mappings are stored in one or more `urls.py` files within the `urlpatterns` list.

https://docs.djangoproject.com/en/3.2/ref/urls/

The next step in the sequence is to call the view functions that are defined in any django applications’s `views.py` file. View functions will do one of the following: redirect the request, raise an exception, or assemble and return an HttpResponse object. 

https://docs.djangoproject.com/en/3.2/topics/http/views/

You can learn about HttpResponse and HttpRequest objects including determining the Http Request method (GET, POST..) and accessing data posted from forms here:

https://docs.djangoproject.com/en/3.2/ref/request-response/

Views are used in conjunction with templates. As a view is assembling the HttpResponse, it needs a way to dynamically generate the HTML of the response. Templates are composed of static HTML and django-template syntax for inserting data from the view and basic flow-control abilities (FOREACH, IF) related to the construction of the HTML. They can be extended and reused and can be made to generate other formats like XML and CSV as well. 

https://docs.djangoproject.com/en/3.2/ref/templates/language/

## Challenge 1A: Sports/Game Fan Website
Your first project involves the creation of a website about your favorite sport (or video game if you like) meant to inform the audience about relevant details of the sport. It will rely on templates in order to give structure to the HttpResponses, and pre-written data from views that is passed into templates.

Your project will contain one Django application that has its own `urls.py` and `views.py`. 

Your website will have 5 types of pages, and for each you will need to add an entry into the Url Dispatcher, write a view function, and create an appropriate template that uses reverse url resolution for internal urls.
https://docs.djangoproject.com/en/3.2/topics/http/urls/#reverse-resolution-of-urls


#### ‘’->views.index
- _description:_
    - landing page
- _view:_
    - includes hard-coded list of strings of urls of images of scenes from the sport
    - randomly selects one of url strings from list and passes it into template 
- _template:_ 
    - includes named blocks “header” and “footer” from base.html
    - includes content describing purpose of page and image tag with random url from view

#### ‘rules/’->views.rules
- _description:_
    - page giving rules or description of sport
- _view:_
    - simply render template 
- _template:_ 
    - includes named blocks “header” and “footer” from base.html
    - includes content describing rules or description of sport

#### ‘notables/\<int:notablesIndex\>/’->views.notablesDetail
- _description:_
    - detailed view of a notable player or character including name, image, description, and stats
- _view:_
    - includes hard-coded list of dictionary elements representing players or characters (at least 3)
    - a single list element will be selected and passed to template
    - each dictionary element should have string values for name, imageUrl, description, and a list for stats
    - uses `notablesIndex` value from `path()` to access appropriate list element
    - should raise Http404(“player does not exist”) on IndexError exception https://docs.djangoproject.com/en/3.2/intro/tutorial03/#raising-a-404-error
- _template:_ 
    - includes named blocks “header” and “footer” from base.html
    - image tag and relevant information of selected player
    - link back to list of notables

#### ‘notables/’->views.notablesList
- _description:_
    - list of internal links to each of the notable players
- _view:_
    - simply pass the list of players into template 
- _template:_ 
    - generate anchor tags for each player, using thumbnail of their image and 
      their name as the content of html tag using `for` django-template tag
      https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatetag-for
    - anchor tags link to detailed view of player

#### ‘externalLinks/’->views.externalLinks
- _description:_
    - set of external links to learn more information about your sport / game
- _view:_
    - contains list of string urls to off-site resources
    -  passes list of urls to template
- _template:_ 
    - includes named blocks “header” and “footer” from base.html
    - iterates through each url and generates anchor tag for each

Finally create the base template `base.html` in the appropriate directory that will be extended for each of the pages in your site. It will contain the following named blocks:
- "header": has navbar with anchor tags to each of the pages within the site besides the detailed view of notable players
- "footer": has copyright information, year, webmaster email address

## Challenge 1B: Car Information Portal
Your employer runs a car warehouse that specializes in some subset of car makes (EX: "German Cars": Audi, BMW, Mercedes... OR  EX: "Sports Cars": Ferrari, McLaren, Bugatti...) They need to a user-friendly website for requesting and displaying information from the external API located at 

https://vpic.nhtsa.dot.gov/api/

JSON data must be retrieved and parsed from the API in order to display the results within a webpage. 
This is a good opportunity to incorporate python libraries into your django project. Python has a with a library for opening external URLs:

https://docs.python.org/3/library/urllib.request.html

But it is highly recommended to install and use the 'requests' library instead:

https://docs.python-requests.org/en/master/

You will most likely want to convert JSON data into a python dictionary. You use python's json library for that:

https://docs.python.org/3/library/json.html

Once you have installed the library and created a single-app Django project, use Django's shell to explore how to make these requests within the context of your Django program using  `python manage.py shell`.

Besides the data from the API, your employer wants the site to serve a lot of the media and scripts directly from the server. Determine the set of car makes you wish to use and find images of their logos to be used as static resources on your page. Any javascript files you create should be included as well. 

https://docs.djangoproject.com/en/3.2/howto/static-files/

The user will interact with the site primarily through forms. You can refresh your memory on creating forms in Django here:

https://docs.djangoproject.com/en/3.2/ref/forms/

This Django project will feel like a single-page app and will reuse a header on all pages that has these elements:
![Car Information Portal Header](images/carPortalHeader.png)
- MAKE: dropdown menu with options populated by the set of car makes you decided to use and defaults to the first choice from the set
- MODEL: dropdown menu with options populated by API call if a car make has been selected and submitted. it also includes an 'any' option which is default if no make is selected. You may also load these choices asynchronously using AJAX
https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started
- BEG DATE: input type number that has minimum of 1886, maximum of the current year and defaults to current year
- END DATE: input type number that has minimum of 1886, maximum of the current year and defaults to current year
- SUBMIT: button or anchor to submit form data

The project will have 3 types of pages: 

#### ‘’->views.index
- HTTP GET
    - header with default search values
    - display available makes including images of logos of each and links that lead to modelList/\<make\>/ of each make for current year to current year
    - ![Car Portal Landing Page](images/carPortalLandingPage.png)
- HTTP POST
    - header must maintain search values that were submitted
    - list items for all matching entries with at least 4 values (EX: year, model, engine power, top speed) from API entry
    List of available variables per entry: 
    https://vpic.nhtsa.dot.gov/api//vehicles/GetVehicleVariableList?format=json
    - view raises http404 if no matches
    - ![Car Portal Search Results](images/carPortalSearchResults.png)
#### 'modelList/\<make\>/'-> views.modelList
- search parameters in header should be set to make: given, model: any, beg date: current year, end date: current year
- main content contains list of all models for the current year of the given make
- each model in list should be clickable and send user to search results page with parameters make: given, model: given, beg year: minimum, end year: maximum
- should raise http404 if user enters url with make that is not in set of makes your employer chose
- ![Car Portal Model List](images/carPortalModelList.png)
    

## Stepping Stone 2: Models, DBs, Migrations
Django can use a wide range of choices for your persistent and ephemeral backend storage. Generally all that is required to hook your Django project up to storage is a few modifications of your project's `settings.py` file. You can choose from any of the available options but this quickstart will follow a MySQL route. 

### Install database
- “MySQL Community Edition” is the free version
- https://dev.mysql.com/downloads/
- you can skip any registration
- you can choose the ‘developer default’ installation options
- if you want to save space, do custom install and select the server, the shell, the python connector, the java connector
### Install Python DB API driver for mysql 
- https://pypi.org/project/mysqlclient/
### Install MySQL database explorer
- The suggested choice that is user-friendly is DBeaver: https://dbeaver.io/
- As long as your server is running, you can also access a shell-like interface from any commandline using `mysql -h localhost -p`
### Connect a new Django project to running database
- https://docs.djangoproject.com/en/3.2/ref/databases/#connecting-to-the-database

Models are one of the most powerful features in Django, giving developers an API for interacting programmatically with stored data regardless of the way it is stored. They are the "definitive source of information about your data" and each model defined in `models.py` files is used to derive DB schema, relationships between types of data, and  behavior. 
https://docs.djangoproject.com/en/3.2/topics/db/models/






