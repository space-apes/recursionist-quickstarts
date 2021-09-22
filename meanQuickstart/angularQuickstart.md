# Angular Quickstart
This quickstart will cover all the necessary knowledge to build web applications in [Angular](https://angular.io/) by guiding you through official documentation and incremental output steps. 

#### What is Angular?
- Angular is a sophisticated front-end design and development framework backed by Google with an emphasis on creating single-page apps
- The core goal for the Angular framework is to take static HTML and CSS pages and make them dynamic by combining them with javascript into packages called 'components'. Components can be composed to make applications
- Development in Angular is done in Typescript, a statically-typed superset of Javascript, then is transpiled to Javascript
- Ultimately, the product of Angular is HTML, CSS, and Javascript that is run on a web browser
- Angular has many features to support design, development, and testing, and is built from the ground up with dependency injection in mind 
- Angular is a non-compatible rewrite of the older framework 'Angular.js' which is being phased out

#### What You Will Need To Know For This Quickstart
- How to execute and run programs from a CLI
- HTML, CSS, Javascript fundamentals
- Object oriented design principles
- [Typescript](https://www.typescriptlang.org/) fundamentals (if you are comfortable with Javascript you will only need a short review to begin using Typescript)

#### Installation 
You have two options for setting up a development environment for running Angular programs. This quickstart will use the local CLI option, but you could easily follow along with either option. 
- [Web Based](https://stackblitz.com/fork/angular-ivy)
- [Local](https://angular.io/guide/setup-local)

#### Angular Element Hierarchy
*Application*: all angular files for project. composed of modules. always includes at least _root module_
- [Modules](https://angular.io/guide/architecture-modules): cohesive block of code towards some purpose. can import data or export data to other modules. composed of components, services providers, and other related code.
    - [Components](https://angular.io/guide/architecture-components): HTML, CSS, and TS that define a visible patch of website called a 'view'  
    - [Service Providers](https://angular.io/guide/architecture-services): 

#### Angular File Hierarchy
*Application*: `/rootDir/` 
- Modules: `/rootDir/src/app/<moduleName>.module.ts`
    - Components: `/rootDir/src/app/<componentName>/`
        - `/rootDir/src/app/<componentName>/<componentName>.component.ts` 
        - `/rootDir/src/app/<componentName>/<componentName>.component.html`
        - `/rootDir/src/app/<componentName>/<componentName>.component.css`
        - other files to support this component, like interfaces/class definitions
    - Services: `/rootDir/src/app/<serviceName>.service.ts`


#### Official Tutorial
Before continuing this quickstart, run through the [official tutorial](https://angular.io/tutorial) to get a broad understanding of Angular. 

#### Angular Element Hierarchy
- application: all relevant angular files built towards some common purpose
    - modules: 
            - components
            - services
   


# Stepping Stone 1: Components / Basic Templates
The first stepping stone will be concerned with concepts surrounding the building block of Angular apps: components ([overview](https://angular.io/guide/component-overview), [reference](https://angular.io/guide/architecture-components)). Each component in your program defines a patch of visible website.  

- components vs views
- command line 
- decorator / metadata 
    - template file
    - css file

# Project 1A: Golf Score Keeper


# Project 2B: Cafe Menu 
- (data model idea) menu item interface
    - string: itemName
    - number: itemPrice
    - string: itemImageUrl
    - string: customerName
- can select different items to display just 1 at a time

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
