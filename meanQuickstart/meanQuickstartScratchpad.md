# LINKS

## The MEAN stack overview (replacing mongodb with mysql)
- tutorials
    - https://www.youtube.com/watch?v=1tRLveSyNz8
    - https://www.youtube.com/watch?v=5NER79OFmTY 
## Typescript 
- tutorials
    - https://www.youtube.com/watch?v=-w1i-gARuJs 
    - https://www.typescriptlang.org/docs/handbook/dom-manipulation.html (DOM manipulation with types)
- quick references
    - http://hoomanb.com/cs/quickref/typescript_cheatsheet.pdf
    - https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html 
    - https://www.typescriptlang.org/play?#code/PTAEHUFMBsGMHsC2lQBd5oBYoCoE8AHSAZVgCcBLA1UABWgEM8BzM+AVwDsATAGiwoBnUENANQAd0gAjQRVSQAUCEmYKsTKGYUAbpGF4OY0BoadYKdJMoL+gzAzIoz3UNEiPOofEVKVqAHSKymAAmkYI7NCuqGqcANag8ABmIjQUXrFOKBJMggBcISGgoAC0oACCoASMFmgY7p7ehCTkVOle4jUMdRLYTqCc8LEZzCZmoNJODPHFZZXVtZYYkAAeRJTInDQS8po+rf40gnjbDKv8LqD2jpbYoACqAEoAMsK7sUmxkGSCc+VVQQuaTwVb1UBrDYULY7PagbgUZLJH6QbYmJAECjuMigZEMVDsJzCFLNXxtajBBCcQQ0MwAUVWDEQNUgADVHBQGNJ3KAALygABEAAkYNAMOB4GRogLFFTBPB3AExcwABT0xnM9zsyhc9wASmCKhwDQ8ZC8iElzhB7Bo3zcZmY7AYzEg-Fg0HUiS58D0Ii8AoZTJZggFSRxAvADlQAHJhAA5SASAVBFQAeW+ZF2gldWkgx1QjgUrmkeFATgtOlGWH0KAQiBhwiudokkuiIgMHBx3RYbC43CCJSAA
## Node.js
- guides / tutorials
    - https://blog.bitsrc.io/javascript-require-vs-import-47827a361b77 
    - https://www.youtube.com/watch?v=2LUdnb-mls0
    - https://nodejs.dev/learn 
    - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/deployment
- quick references
    - https://nodejs.org/en/docs/guides/getting-started-guide/ 
    - https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
    - 
## Angular 
- tutorials
    - https://www.youtube.com/watch?v=3dHNOWTI7H8
    - https://www.youtube.com/watch?v=k5E2AVpwsko
    - https://docs.angularjs.org/tutorial
- quick references
    - https://angular.io/guide/cheatsheet 
## Express 
- tutorials
    - https://expressjs.com/en/advanced/best-practice-performance.html  
- projects
- quick references
    - https://expressjs.com/en/4x/api.html 
    - https://www.guru99.com/node-js-express.html
    - https://expressjs.com/en/guide/database-integration.html#mysql

# Typescript notes
## What is it
- superset of javascript
- includes typing
- ts can not be executed on its own (ts sourcecode transpiles to javascript)
## Tooling
1. `npm install -g typescript`
2. `touch example.ts`
3. `tsc example.ts` (creates js file)
## Typing
- valid primitive types
    - number
    - string
    - bigint
    - boolean
    - symbol: create unique entity. can never equal another symbol.
    - null
    - undefined
    - object
- non-primitive types
    - any: wildcard type. used to avoid typechecking errors
    - unknown
    - never
    - object literal
    - void: subtype of undefined. for use as return type
    - T[]: mutable arrays. also written as `Array<T>`
    - [T, T]: tupes. fixed length but mutable
    - (t: T)=> U: functions  
- type annotation in declaration: 
    - `let message : string = "Hello World"` 
- type annotation in function/method definition
```
    function greeter(message : string, age : number) : string {
    return "asdasd"
    }
```
- type annotation for object types list attributes and types of attributes: `function printCoord(pt: { x: number; y: number }`
- classes
    - defining class: `class blah {}`
    - constructors: `constructor()`  
    - inheritance: `class Derived extends Base {....` 
    - defining methods: `scale(n: number): void `
    - overloading: can define diff functions w same name but diff signature including constructors
- interfaces vs types
- interfaces 
```
interface ArtistForEdit {
  id: number;
  name?: string;
  bio?: string;
}
``` 
- unions vs generic types
- unions: type can match multiple other types: `function printId(id: number | string) {`
- generic types

# Node.js Notes
- What is it?
    - local runtime environment for javascript
    - server side runtime
    - includes package manager NPM
    - automatic package dependency 
- what can it do
    - listen for HTTP requests, send back responses
    - execute server side logic
    - interact with files, databases
- Tooling
    - https://nodejs.org/en/download/
    - execute js with `node example.js` 

# Express Notes
- what is it?
    - basic web framework package for NPM 
    - includes web server, routes, hooks to interact with DB, middleware, controller
- what can and can't express js do?
    - simplifies node.js's web framework capabilities
    - funnels requests through chain of functions (middlewares)
    - routing
    - view-rendering  (but we will use Angular) 
```
var express=require('express'); //include express module 
var app=express(); // store express as an object
app.get('/',function(req,res){ res.send('Hello World!');}); // add a route: app.METHOD(PATH, HANDLER)
var server=app.listen(3000,function() {}); // start web server
```

# Angular Notes
- what is it?
    - 100% TS->JS, 100% client-side framework for building UIs
    - focus on single-page-apps
    - similar to mobile app UI
- what can angular do?
    - update UI with dynamic whenever there are changes to data
    - communicate with node/express
- installation
    1. https://angular.io/guide/setup-local
        - install npm
        - install angular cli `npm install -g @angular/cli`
        - if have version errors
            - update node.js with 'n'
                - `npm install -g n`
                -   
        - start new project `ng new new-app-name`
        - start test server
            - `cd new-app-name`
            - `ng serve --open` serves at port 4200 
    2. file structure?
    3. html file includes script tag with src = to angular framework js
    4. html file includes  script tag with our angular code


## FILE STRUCTURE
- package.json: node.js project meta-data (dependencies etc)
- main.ts: ???
- /src/
    - styles.css: application-wide css 
    - app/: highest level component?
        - app.module.ts: module definition for this app. opt in high level modules like FormsModule here 
        - app.component.ts: root component class file. 
        - app.component.spec.ts: unit tests for root component class file
        - app.component.html: root component template
        - app.component.css: root component specific styles
     
        - heroes/: non-app component directory
            - hero.ts : example, can define interface/classes for data
            - heroes.component.ts: non-root component class file
            - heroes.component.html: non-root component template
            - heroes.component.css: non-root component styles
            - heroes.component.spec.ts: unit tests for non-root component class file
    
## DECORATORS / CLASSES
- all modules, components, services, are _classes_ that use _decorators_.
    - make type and provide metadata
- metadata for component class associates it with a template that defines view\
- metadata for service class allows service to be available through dependency injection

## APPLICATION
- set of modules towards some goal?
- has root module AppModule, launches application  
- APP SHELL:
    -  Application shell is a way to render a portion of your application using a route at build time. It can improve the user experience by quickly launching a static rendered page (a skeleton common to all pages) while the browser downloads the full client version and switches to it automatically after the code loads.
    -  This gives users a meaningful first paint of your application that appears quickly because the browser can render the HTML and CSS without the need to initialize any JavaScript.
## MODULES
- declares compilation context for set of related components
- can import/allow export functionality from other modules
- can load modules on demand ("lazy loading") 
## COMPONENTS
- generate with `ng generate component NAMEHERE`
- define views. sets of screen elements can choose from / modify
- must be declared in exactly 1 NgModule `declarations: in modulefile`
- use services. (specific functionality not directly related to views)
- includes
    -  An HTML template that declares what renders on the page
    - A Typescript class that defines behavior
    - A CSS selector that defines how the component is used in a template
    - Optionally, CSS styles applied to the template
- `selector` meta data is name of tag that can be used in _parent_ templates and will insert entire component. ex: selector: `app-root` can be used as \<app-root\> \</app-root\>
- always import Component and decorate classes with @component
- always export classes defined in ts file so can be imported by... parent components
- constructor(): initialize class members, set up DI
- ngOnInit() method called after constructor. 

- `@Component()` class decorator
```
// in x.component.ts

//decorator for new component
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

//actual component class definition
export class AppComponent {
  title = 'Tour Of Tutorials!!!';
}

```
## TEMPLATES
- syntax: https://angular.io/guide/template-syntax
- component views are defined through component templates
- combines ordinary HTML with Angular directives and binding markup that allow Angular to modify the HTML before rendering it for display. 
- modifies html elements before they are displayed
- "directives" provide program data and logic: 
    - `<input id="name" [(ngModel)]="hero.name" placeholder="name">`
    - `<li *ngFor="let hero of heroes">` for x in y repeat li tag 
    - `<div *ngIf="selectedHero">` displays div only if value is set
- "binding markup" connects application data and DOM
- `{{ varName }}` interpolation from app data
- templates / views are though of as hierarchical 
- BINDING: coordinate app data and dom data
    1. event binding: lets your application respond to user input by updating application data
        - `<li *ngFor="let hero of heroes" (click)="onSelect(hero)">` 
    2. property binding: interpolate values that are computed from application into HTML
        - `@Input() hero?: Hero` in class file and `<app-hero-detail [hero]="selectedHero"></app-hero-detail>` in template
        - It's a one way data binding from the selectedHero property of the HeroesComponent to the hero property of the target element, which maps to the hero property of the HeroDetailComponent. 
        - "two way binding": changes to DOM also are reflected in program data: "hero.name property to the textbox, and from the textbox back to the hero.name."
        - "pipes" tranforming values to display (locale, currency etc): `{{ hero.name | uppercase }}`
    - two way binding syntax in input tag in template: `[(ngModel)]="hero.name"`
    - class binding: Add `[class.some-css-class]="some-condition"` to the element you want to style. 
    - class binding ex: `[class.selected] = "hero === selectedHero"`
## SERVICES
- data/logic isn't associated with specific view 
- data/logic shared across components
- instead of directly, use services to do things like
    - fetch data from server
    - valdiate user input
    - log directly into console
- `@Injectable()` class decorator

