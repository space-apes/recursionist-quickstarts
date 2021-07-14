## Links
- Django official docs: [link](https://docs.djangoproject.com/en/3.2/)
    - see tutorial 
    - see topic list
    - see advanced topics
- geeksforgeeks django: [link](https://www.geeksforgeeks.org/django-tutorial/)
- readthedocs.io free book: [link](https://django-book.readthedocs.io/en/latest/)
- learn django from scratch youtube: [link](https://www.youtube.com/watch?v=t7DrJqcUviA)

## Potential Core Stepping Stones
### requests, urls, views, static sites
- static resources / filestructure
- http requests
- HttpRequest, HttpResponse
- slugs
- urls.py, project wide vs app-widea
- urlconf has urlpatterns list of paths
    - path: 
        - string: route
        - function/method reference: view
        - string: name
        - kwargs: optional dictionary of values to pass in to view
        - (dont forget passes httprequest in to view
- "When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so"

    - https://docs.djangoproject.com/en/3.2/topics/http/urls/
    - using name instead of hardcoded urls
        - if multiple apps with same url names, can namespace 
            - add 'app_name = <name>' in urlsconf
            - when referencing the url, <app_name>:<urlName>
- views
    - "A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template."
    - 'pages' vs 'actions'?
    - goal of view is to either return an HttpResponse or raise an exception(EX: 404)
    - passing context into httpresponse
    - redirecting after handling POST data
    - using reverse to pass control to different view from view name, and pass arguments to view
        - uses view name to determine urlconf url. returns url string after domain name with inserted variable parts
        - 'args' parameter must be iterable
    - using generic views: commonm case of getting data from DB from URL, loading template, returning rendered templatea
        - https://docs.djangoproject.com/en/3.2/topics/class-based-views/
        - types: listView, detailView
        - adjust urlconf (variable part must use int:pk), view goes views.functionname to views.FunctionName.as_view()
        - each view is now class that subclasses (generic.ListView) or DetailView
            - member variable string: template_name 
                - (if not specified, defaults to <appname>/<model_name>_<genericTypeName>.html (detail or list)
            - member variable context_object_name
                - this also overrides default context variable. in detail, it is the queried mode object, in list, it is <modelName>_list
            - member variable Class : model
            - method get_queryset(self) -> queryset (default method for querying db in listview only)

    - why class-based views? to use power of OOP mixins and inheritance

### templates
- subtle diff between mvc and mvt: https://www.tutorialspoint.com/django/django_overview.htm
- https://docs.djangoproject.com/en/3.2/topics/templates/
- maybe cover static resources
- evaluation in templates / limiting logic to views(separation of concerns)
- namespacing templates for modularity
- loading and rendering templates in views, using django.shortcuts.render
- error handling / 404s
- removing hardcoded URLS. using 'name' of a path instead. modularity. dont need to change url in each template, only need to update urlsconf

### models / DB (or models / DB / migrations)
- "DRY" philosophy: models are absolute truth about data. define them in one place, derive all else from that definition.
- adjust settings.py ('default', 'user', 'password', 'host')
- defining models
    - fields may have optional or mandatory parameters
- each model is a table "appName-modelName"
- each member variable that instantiates models.Xfield is a column in table (underscore convention)

- activate models by adding to settings.py, makemigrations, migrate (adds schema and API!), DO THIS EVERY TIME ADJUST data fields of models
- why creating migrations separate from applying them: schema version control
- using the shell
    - import model first
    - instantiate local object
    - CRUD operations
    - persist
        - use F() to avoid race conditions
        - https://docs.djangoproject.com/en/3.2/ref/models/expressions/#avoiding-race-conditions-using-f
    - retrieve
        - all()
        - filter(): for multiple items. no matches gives empty queryset
        - get(): for single items. no matches throws error
    - access member values
    - why to use 'shell_plus' and how to install
        - install django-extensions
        - install ipython
        - 'ipython profile create'
        - update config file
        - may need to downgrade jedi 
- local vs persisted vs 'instanced'!!!
- field types
- relationships
    - https://docs.djangoproject.com/en/3.2/ref/models/relations/
    - double underscores to refer to model object that belongs to another mode object
    - one to many 
        - api access of many from one <ModelName>.<relModelName>_set.all()
    - one to one 
    - many to many
- underscoreunderscore str underscoreunderscore method of model definitionsa
- django.shortcuts.get_object_or_404
    - use helper function to maintain loose coupling: do not want to couple view and model layers
    - also django.shortcuts.get_list_or_404() that uses filter instead of get() and raises Http404 if list is empty
### queries / querysets
- https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro
- querysets are lazy.. do not touch DB
- ordering
- chaining
### migrations
- 'makemigrations' to make new migration after changing models
    - look in file to see migration
- 'sqlmigrate' to view sql code generated for migration
- 'migrate' to execute migration
- 'check' to look for problems in current migration before touching db
- forms
- cross site navigation!
- http method review
- 'name/value' http attributes when posting
- request.post[<name>], use try and except on KeyError
    - request.post is a dictionary like object with key value pairs. value is always a string!
    - always redirect when posting to avoid user hitting 'back' button and submitting multiple times

### building RESTful API
- https://docs.djangoproject.com/en/3.2/ref/request-response/

### djangoadmin site
- admin/0ligarch33
- purpose of admin site
- added by default (check apps)
- manage.py createsuperuser
- change admin.py to add certain models to admin site
    - (web interface generated from models.py!)
- configuring
- using
### multi-app projects, reusable apps, virtual environments
### configuring external DB server
### security issues in Django apps
### testing in django, "Test Driven Development"
- work is done in <appName>/tests.py
- import django.test.TestCase
- class of tests for each model(for example) QuestionModelTests(TestCase), subclasses TestCase
    - define function for each test whose name starts with 'test' and whose body ends with ends with self.assertIs(arg1, value) 
- run test with manage.py test <appName>a
- testing http responses using shell
    - django.test.Client()
        -response = client.get('url')
        - can now observer response.status_code, response.content, response.context
-testing views 
    

## Task/Project ideas
- amazon clone (views, routes, models, querysets, templates)
    - Possible Educational Sequence
        - views/routes/templates
            - create basic HttpResponse views and urlpatterns for Login, Register, Search, ItemDetail, Cart,
            - create models for User, Item, use shell, learn about migrations, the Model API, relationships
            - create querysets for different varieties of searching for items(filter, order_by, chaining)
            - create templates for each type of page
                - form template for registering 
                - template for when search is blank vs search has search termaa
            - integrate some visualization librarys to see how much of each item category has been purchased


    - MODELS
        - User model
            - string: address
            - string: name
            - [string] : common search terms (maybe recommended?)
            - [Product]: previous purchases
            - [Product]: current cart
        - Product Model
            - string: description
            - real: price
            - [real]: dimensions, weight
            - [string]: urls of images
            - [Review] : list of reviews for this product
        - Review Model
            - string: review contents
            - integer: rating
            - User: user who did review
    -PAGES
        -home
        -register
        -login
        -search result
        -product
        -cart
        -checkout

- Food Survey / food recommender (admin?, libraries?)
    - MODELS
        - FoodItem
            - string: name
            - string: description
            - string: image
            - int: index
        -User
            - string: ID
            - [(integer, integer)]: foodItem index, personal rating
    - NOTES
        - maybe make this one based on sessions instead of username/password?
        - allow users to enter in new food Items
        - use admin to remove offensive/incorrect food items
        - users may not have rated all foods, but can still iterate through all foods that are in DB to find recommendations
        - recommendation ideas:
            - top 5 foodItem ratings of k nearest User neighbors
            - can make it a social media site where you browse other users
            - OR choose your own reccomendation algorithms

## Bird's Eye Structure
- Django Quickstart
    - version
    - what is django
        - great short explanation: https://www.youtube.com/watch?v=GGkFg52Ot5o
    - requirements
        - OOP
        - 'coupling' 
        - helps to understand python modules, html, css, db basics
        - model view controller architecture
    - a note on content: some concepts fall across earlier stepping stones and will appear in multiple places.. something like this...
    - a note on workflow: it may help to have many windows open at same time...(image of example workflow)
        - MVC: 'create model', 'add controller views and routes to access them from urls', 'write templatea
        - https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/
- Installation
    - installing libraries / venv
        - https://docs.python.org/3/library/venv.html
    - installing DB
    - creating new project
        - projects vs apps
        - location of files on servera
        - default apps
    - file structure
    - manage.py -h  
    - running test server / difference between full server
    - running remotely
    - settings.py, 'disallowed host', timezone 
    - creating app, adding app to project apps in settings
- Concept1: Requests, Routes, Views, static site
    - project-wide urlsconf vs app specific
    - greedy match on urlpattern route
    - hello world with single route that returns HttpResponse
    - link up hello world to simple view
- Challenge 1
- Concept 2 Models / DB / Dynamic content
    - 'model is definitive truth about data': fields, behavior, db schema, API calls on models
- Challenge 2
- Concept 3
- Challenge 3
- Concept 4
- Challenge 4
- Concept 5
- Challenge 5


