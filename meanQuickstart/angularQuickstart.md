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
**Application**: all angular files for project. composed of modules. always includes at least _root module_
- [Modules](https://angular.io/guide/architecture-modules): cohesive block of code towards some purpose. can import data or export data to other modules. composed of components, services providers, and other related code.
    - [Components](https://angular.io/guide/architecture-components): HTML, CSS, and TS that define a visible patch of website called a 'view'  
    - [Service Providers](https://angular.io/guide/architecture-services): A class with a well defined purpose that is not directly associated with a visible part of the application.

#### Angular File Hierarchy ####FOR SHINYA: TURN THIS INTO A PICTURE / DIAGRAM
**Application**: `/rootDir/` 
- Modules: `/rootDir/src/app/<moduleName>.module.ts`
    - Components: `/rootDir/src/app/<componentName>/`
        - `/rootDir/src/app/<componentName>/<componentName>.component.ts` 
        - `/rootDir/src/app/<componentName>/<componentName>.component.html`
        - `/rootDir/src/app/<componentName>/<componentName>.component.css`
        - other files to support this component, like interfaces/class definitions
    - Services: `/rootDir/src/app/<serviceName>.service.ts`

#### Official Tutorial
Before continuing this quickstart, run through the [official tutorial](https://angular.io/tutorial) to get an initial understanding of Angular. 

# Stepping Stone 1: Components / Basic Templates / Basic Binding
The first stepping stone will focus on the building block of Angular apps: components and will touch lightly upon templates and binding. Make sure to read up on the concept of components [here](https://angular.io/guide/component-overview), and understand the architectural reference [here](https://angular.io/guide/architecture-components). 

Components are composed of templates, css files, and at least one typescript file that defines the component class. After creating a component using the command-line options, take note of the decorator above the component's class definition in the typescript file. This will map the component to each of its files. 

Each component defines a 'view' which is a portion of visible website. While the typescript file performs processing and is a source of dynamic data, this data can be inserted into your html through [templates](https://angular.io/guide/template-syntax) through various types of binding. You can use [structural directives](https://angular.io/guide/built-in-directives#built-in-structural-directives) within templates to programatically affect the html structure of your components.

Finally, while each component has it's own scope, you are able to [bind values between components](https://angular.io/guide/property-binding#bind-values-between-components) as well. 


# Project 1A: Number Guesser Basic
In this first project you will create a guessing game where player 1 submits a number between 1-100, and player 2 enters numbers, attempting to match the correct number submitted by player 1. After each guess, some visual feedback is given to player 2 to indicate how close their guess was to the correct number. Once player 2 enters the correct number, a message displays how many attempts it took. 

## Components
### Root Component ("app-component") 
- Game Component
### Game Component
- shows heading with welcome message 
- dynamic message using [text interpolation binding](https://angular.io/guide/interpolation) to direct the players at each step of the game
- input type text to enter all numeric values. 
    - use [event binding](https://angular.io/guide/event-binding) to call some update function whenever the user presses the 'enter' key. the event `(keyup.enter)` can be used. 
    - make sure to do some basic input validation to receive only integers between 1-100. add error text if they did not. 
    - if you want to hide the text when player 1 is submitting the correct number you can style the input field with `color: transparent` during that time.  
- if correct number has been submitted, show Guess Component. Use binding to pass information from Game component to Guess Component. 
- if guessed number matches correct number, show a reset button that returns the game to it's initial state 
### Guess Component
- a heading that shows whatever the last guess was
- a message that describes how close the last guess was to the correct number using the following ranges: 0, 1-2, 3-4, 5-9, 10-24, 25-49, 50+
- some visual indication that maps distance between last guess and correct number to some visual feedback (like colors or images)
    - EX: (0)-> blue, (1-2)-> green, (3-4)-> yellow-green, (5-9)->yellow, (10-24) -> yellow-orange, (25-49)->orange, (50+)->red    

## Application State Flow
1. game loads into initial state. 

# Project 1B: Number Guesser 
Next, you will add some complexity, 
- an 'update' function that allows up to 5 guesses
- directive to repeat component
- good data model to back each "guess" component

# Project 1A: Golf Score Keeper
In this first project you will create a dynamic score-keeping application for a game of golf that updates as data is entered into it. 

Golf is played over a series of 'holes' where the player attempts to hit the ball into a hole with the fewest amount of swings or 'strokes'. The number of strokes for each hole is recorded and added up for the final total. At each hole, a sign is typically posted that shows how many strokes a skilled golfer typically requires for that hole. This is a way to give a benchmark to players on a per-hole basis and a course-wide basis. A golfer who took 6 stokes on a 'par 4' hole would be considered 'two over par'. Also, a golfer that took 66 strokes across all holes compared to a par 70 course would be 'six under par' and would be considered very competent

SHINYA: if this explanation is not enough, explain deeper or add a link to some resource that explains golf scoring

Your single-page application should be made with at least 2 components and can be thought of as having 5 states: 

1. initial state(when page first loads): 
    - heading with a title like "golf score keeper"
    - text inputField for course name
    - text input field for player's name
    - dropdown or number input for number of holes in the course
![Golf Score Keeper Initial](images/golfScoreProjectInitialView.png)

2. entering the course name
    - all previous elements
    - use [event binding](https://angular.io/guide/event-binding) and [text interpolation](https://angular.io/guide/interpolation) to update the heading when the user enters a course name 
![Golf Score Keeper Initial](images/golfScoreProject/golfScoreProjectInitialViewWithCourseName.png)

3. scoring grid state(only visible when both name and number of holes have been set by input elements)
    - all previous elements
    - should generate a grid with enough columns for number of holes selected, as well as 'total' and 'under/over par'. you may need to [bind values between components](golfScoreProjectIShowScoreGridView.png)
        - generate one row for the table heading. include column headers for "Hole Number", a column for each hole by enumerating from 1 to the last hole, "total", and "under/over par"
        - generate one row for 'par for hole' with empty row cells for each hole, 'total', and 'under/over par' 
        - generate one row for the player, inserting their name in the first cell, with empty row cells for each hole, 'total', and 'under/over par' 
    - player's name in grid should be updated when the input field for player name is changed. You may use [two-way binding](https://angular.io/guide/two-way-binding)
![Golf Score Keeper Load Grid](images/golfScoreProject/golfScoreProjectIShowScoreGridView.png)

4. game in progress state
    - PAR ROW: as game progresses, users will enter values for each hole in the par row by clicking on the associated cell and typing a number
        - total column for par row will be dynamically updated when user enters a new par value for a hole. 
        - 'under/over par' column for par row is always 0
    - PLAYER ROW: users should also be able to enter their strokes for each hole for each cell in this row by clicking the cell and typing a number
        - the value in the total column for the player row will be updated every time a user enters a new stroke value by finding the sum of all strokes so far 
        - the value in the 'under/over par' column for the player row will be dynamically updated when player enters a new stroke value. This value will be sum of player strokes so far subtracted by sum of par strokes so far.
    - for each player number of strokes, the cell background color should be dynamically updated. You may use [style binding](https://angular.io/guide/attribute-binding#binding-to-a-single-style)
        - if the number of strokes is above par, that cell background should be red. 
        - if it is under par it should be green. 
        - if it is par it should be neutral. 
    - the par and player 'total and under/over par' columns should also be dynamically updated whenever a new number of player strokes and par strokes is entered for a hole. player's total follows same color scheme to individual strokes compared to overall par. 
![Golf Score Keeper In Progress](images/golfScoreProject/golfScoreProjectGameInProgressView.png)

5. game completed state(when all par and user stroke cells have had values entered)
    - no more cells left to enter data. User quickly closes application if their total is red or shows it to opponent if their total is green. 
    - a message alerts the user that the course has been completed
    - a button appears allowing the user to reset all values back to the initial state
![Golf Score Keeper In Progress](images/golfScoreProject/golfScoreProjectGameInCompleteView.png)


As an extra challenge, try adding more players whose scores can be tracked. 

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

# Stepping Stone 2: Binding maybe blend with Services? advanced component stuff?

# Stepping Stone 3: Services and Routes
    - queue
        - add messages to queue on events
    - application wide service
    - application wide and fetching from external source

# Stepping Stone 4: Asynchronous Requests

# Stepping Stone 5: Modules and Dependency Injection ?????
