# Angular.js Quickstart
This quickstart output guide will cover all the necessary knowledge to begin building web applications in ![Angular.js](https://angularjs.org/), a sophisticated front-end design and development framework with an emphasis on creating single-page apps that is backed by Google. The core goal for the Angular framework is to take static HTML and CSS pages and make them dynamic by combining them with javascript into packages called 'components'. The power of Angular comes from the ability to create whole applications by composing components, which can be reused, nested, and can share data between each other. Angular ha

- what is angular
    - front-end framework for developing flexible GUIs and following the general "one-page app" form
    - essentially 100% client side js loaded from web browser and included in HTML
    - is actually transpiled from typescript
    - gives ability to: reuse elements, dependency injection, 
    - collection of common functionality: client/server, forms 
    - try it link
- what you will need to know
    - html, css
    - object oriented concepts
    - typescript fundamentals 

- conceptual hierarchy
    - application
        - modules
            - components (views)
            - services
    
- installation
    - https://angular.io/guide/setup-local 
    - basic file hierarchy
    - root module

- official tutorial: https://angular.io/tutorial

# Stepping Stone 1: Components / Basic Templates
- components vs views
- command line 
- decorator / metadata 
    - template file
    - css file

# Project 1A: Coffeeshop Menu Item (OR SPORT SCORE KEEPER)
- (data model idea) menu item interface
    - string: itemName
    - number: itemPrice
    - string: itemImageUrl
    - string: customerName
- can select different items to display just 1 at a time

# Project 1B: Cafe Menu 
- uses hierarchical quality of components
- can select multiple Coffeeshop Menu Items to create an Order
- displays all menuItems, total price, customer name
- can store multiple orders, expand/collapse view of orders, 'finish' to remove orders

# Stepping Stone 2: Binding

# Stepping Stone 3: Services and Routes
    - queue
        - add messages to queue on events
    - application wide service
    - application wide and fetching from external source
