## Links
- Django official docs: https://docs.djangoproject.com/en/3.2/
    - see tutorial 
    - see topic list
    - see advanced topics
- geeksforgeeks django: https://www.geeksforgeeks.org/django-tutorial/
- readthedocs.io free book: https://django-book.readthedocs.io/en/latest/
- learn django from scratch youtube: https://www.youtube.com/watch?v=t7DrJqcUviA

## Potential Core Stepping Stones
- requests, urls, views, static sites
    - slugs
- templates
- models
    - local vs persisted vs 'instanced'!!!
    - CRUD operations
    - field types
- queries / querysets
    - chaining
    - querysets are lazy.. do not touch DB
- migrations
- forms
    -cross site navigation!
- djangoadmin site

- Task/Project ideas
    - amazon clone (models, querysets, templates)
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

    - Food Survey / recommender
        - FoodItem Model



## Bird's Eye Structure
- Django Quickstart
    - version
    - what is django
- Installation
    - installing libraries / venv
    - installing DB
    - creating new project
        - projects vs apps
        - location of files on server
    - file structure 
    - running test server / difference between full server
- Concept1: Static Site: linking routes to views
    - project-wide urls vs 
    - hello world with single route that returns HttpResponse
    - link up hello world to simple view
- Challenge 1
- Concept 2
- Challenge 2
- Concept 3
- Challenge 3
- Concept 4
- Challenge 4
- Concept 5
- Challenge 5


