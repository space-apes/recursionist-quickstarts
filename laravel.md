## Laravel Quickstart 

In this quickstart output guide, we will run through all of the fundamentals of Laravel, a php backend framework that focuses on simplicity and natural-language (english) like syntax. Laravel provides all of the fundamental backend web server needs. This includes routes, registration/login, templating, security, validation, model-view-controllers, database and storage drivers, unit testing, scheduling, and websockets. This way developers can focus on designing their software, creating models and solving their problem scope rather than using their time resources on boilerplate code. Note this guide will use official documentation as the main source of input, and then provide a set of projects for you to output. Use this as a step-by-step roadmap to learning Laravel. 

Before you begin, make sure you have a strong foundation of CS and Object Oriented Programming. It is strongly preferred that you know about creational patterns, dependency injection, and the MvC model. It is also a good to know relational algebra as Laravel's Eloquent ORM system is based on relational databases. You should be very comfortable using the unix command line and installing CLI programs, examples include npm, git, docker, mysql, ffmpeg, brew, and docker. Lastly, this guide assumes you are comfortable with the PHP language and static typing. While php is a dynamic language, you will use PHP 7.4 and above which has type declarations. We recommend you to use type declarations while you develop in Laravel.

Since Laravel is used for web applications and provides its own front-end rendering engine called blade, you will also need to know the front-end web development stack (html/css/javascript and optionally a web front-end framework like react, vue.js and/or angular). 

## Installation and setup

This guide assumes you are working with Laravel version 8.

Read the installation guide - https://laravel.com/docs/8.x/installation

For those that prefer video format, watch Section 1 of Laracast which is endorsed by Laravel. https://laracasts.com/series/laravel-8-from-scratch

While you can use Laravel's docker package, which bundles all the prerequisites together into its own self-contained development environment to get started, this guide assumes you have all the requirements installed locally and that you installed Laravel through composer. The Laravel requirements for a local environment are: php 7.4+, MySQL, and Composer. As for production or staging deployment, see https://laravel.com/docs/8.x/deployment for full details on server requirements.

If installed through docker rather than composer, the `sail` command is used rather than `php`. 

Example:

- `sail make:migration MyNewMigration` rather than `php make:migration MyNewMigration`
- `sail artisan serve` rather than `php artisan serve`.

Once Laravel is installed, run `laravel new hello-world `to create a new project named `hello-world` and run `php artisan serve` to run the Laravel project on your localhost which should appear on the url 127.0.0.1:8000.

## Routing and Views

After running `laravel new` you will see many directories and files automatically installed into that project folder. Check out the documentation regarding the directory structure of Laravel (https://laravel.com/docs/8.x/structure). If you take a look at your `hello-world` project folder you will see this exact same structure. You will also see an `.env` file which contains all of your configuration such as database drivers and login information, storage drivers, and mail SMTP information. Developers are free to add variables to this `.env` file, like adding API public/private key variables. For more information, read (https://laravel.com/docs/8.x/configuration). You will make use of this `.env` file and the config folder at a later point.

Read the documentation on routing (https://laravel.com/docs/8.x/routing). Routes allow you to create server url endpoints and run a function that takes in many different kinds of inputs thanks to Dependency Injection (DI) and return a response such as returning a view, a json, or a redirect. DI for routes are usually based on the URL, see route parameters https://laravel.com/docs/8.x/routing#route-parameters . 

Laravel follows an Model-View-Controller architecture, where views are completely separated from other modules. Read the documentation on views (https://laravel.com/docs/8.x/views).

Views use the *blade* templating engine, files ending in `.blade.php`. Read the documentation on blade templating here: (https://laravel.com/docs/8.x/blade)

Before moving on, attempt to practice what you have learned by defining some simple routes and creating some view files. Declare new routes in the `routes/web.php` that return a view you have created in `resources/views/...`. Run `php artisan serve` to see your routes respond with your views locally. If your route is /hello-world, then you would go to `127.0.0.1:8000/hello-world`.

## Cookie Bakery

You decided to tackle some website freelance work for a small bakery chain called "Dr.Sweet's factory ". They want you to create a *static* website of their bakery based on the following wireframes and designs. 

![alt-text](img/part1.png)

There will be 5 GET url routes available, all which render a view (an HTML page):

- /
  - The home page that is the main marketing page for the bakery. There is a section in the middle showing all current promotions.
  - route name: home
- /menu
  - A static page showing all the menu items such as cookies, chocolate, cakes, pudding and coffee. A section is also shown here with all current promotions, use the exact same code as the home page promotions.
  - route name: menu
- /locations
  - A static page showing a set of Dr. Sweet's Factory locations along their open hours, including the main branch.
  - route name: locations
- /history
  - A static page showing the history of the bakery chain and its founders.
  - route name: history
- /contact
  - A static page showing information about the main branch address, email address, contact business hours, and contact phone number. Show the location as well here with the exact same code used in the 'locations' route.
  - route name: contact

For this project, when creating these routes stick to using the default web.php route (`routes/web.php`) and pass in anonymous functions (called closure objects in PHP) to the route namespace's *get* function. Make sure to give your routes a unique name using method chaining (`Route::get('/menu', function() { ...... })->name('menu')`) as you will use the route helper function to generate the url of your routes (i.e `route('menu')`).

All of your routes will return a blade view, which you must create under `resources/views/....`. All of these route blade view pages will share the same navigation, footer, stylesheets, and javascript files. Some pages will share the same code, like locations and contact. You must make use of blade layouts and blade subviews to accomplish this. Don't worry about passing data into your views through the view helper function that is called in your route functions (i.e `return view('welcome', ['data' => 'hello world!!!'])`) since all of the views you will make for this project are static html web pages, and the next project will focus on dynamic web pages. However, if you do use subviews through blade do pass in data to your subviews (https://laravel.com/docs/8.x/blade#including-subviews), i.e `@include('menu-item', ['title' => 'Apple Pie Cookies'])`. 

Make sure to make a main blade layout page called bakery, and place it under layouts (`resources/views/layouts/bakery.blade.php`).  Add yields at any section you think the views that extend this layout will add custom code into. For example, you may want to yield at the main content and other pages will simply add to that section. You may want to yield for CSS and javascript as well, so other pages can insert css and js files.

Keep code reusability in mind and make use of subviews whenever you are writing the exact same piece of blade code again.  

All of your public files (stylesheets, js, images, audio, mp4 etc) must go in the public folder and must be well organized. For example, all css files should go under `public\css\...` , all images under `public/img/...` and all audio files under `public/audio/....` and so on. 

## Language Exchange Meetup Prototype

You are working on a startup company with a group of friends, and you need a prototype of your software to pitch to investors. You are making a language exchange web application where users can create a local meeting. Users whose native language is A who want to practice language B are paired with users whose native language is B who want to practice language A. A meeting will have at most x people, split in half by their native language. Instead of creating meetings, you can also simply search for and join meetings. 

The team has created the following wireframes and designs. 

**INSERT WIREFRAMES AND DESIGNS HERE**

Since this is just a prototype, you want to replicate these designs and generate random data to mock the feeling of using the application.  You will use the faker library (https://github.com/fzaninotto/Faker) to mock data. Laravel comes packaged with Faker as a composer dependency and you may import it through `use \Faker\Factory as FakerFactory`. Create a new factory through `$faker = FakerFactory::create()`.

Create the following classes, that represents the models which we will then generate randomly. All of these classes are Plain Old PHP Objects (POPO). They are simple classes that contain state and behaviors you will define for the purpose of this project. In this case, they only contain private instance variables, a constructor, and setter/getters to the instance variables. You are free to put these in a new folder, or create a `MyClasses` directory under app to store them (`app\MyClasses\...`). Don't forget to add a namespace to your class definition (https://www.php.net/manual/ja/language.namespaces.php) so you can import your classes from a different file using the `use` keyword.

Create the following classes:

|              User               |
| :-----------------------------: |
|       - username: string        |
|       - firstName: string       |
|       - lastName: string        |
|        - gender: string         |
|       - birthday: string        |
|    - nativeLanguage: string     |
|   - knownLanguages: string[]    |
|   - targetLanguages: string[]   |
| - currentMeetingList: Meeting[] |

On top of setter/getters, the user will have a getAge() function that calculates their birthday (i.e 12/25/1985) to an age. You may use the Carbon library to calculate this (https://carbon.nesbot.com/docs/). Carbon is also a dependency for Laravel, so you may import carbon through `use Illuminate\Support\Carbon` or `use Carbon\Carbon`. Lastly, a user's target language cannot be the nativeLanguage or be part of knownLanguages.

|        Meeting         |
| :--------------------: |
| - hostUsername: string |
|    - title: string     |
|   - meetDate: string   |
|   - location: string   |
|  - languageA: string   |
|  - languageB: string   |
| - participants: users  |
|       - min: int       |
|       - max: int       |
|                        |
|                        |

On top of setter/getters, create a function addParticipant(participant: user) that takes in a user, validates if it can add the user or not as a participant and if so, adds the user to the meeting. It returns a boolean that informs whether the user was added to the meeting or not. In order for a user to be a valid participant, the group must not be at max capacity, and all the participants must be split evenly (+/- 1) between languageA and languageB determined by each participant's nativeLanguage/knownLanguages. Note, the host is also a participant. As an example, if the meeting is to have a language exchange between English and Japanese with a maximum of 8, there must be 4 people whose native or known language is English, and 4 other whose native or known language is Japanese.

Now that you have these models at hand, create the following routes and views. This will be the prototype that will be shown to investors. Remember to use faker to generate/mock user or meetings objects within the route closure that returns a view. Pass all generated objects into the view using the view helper, i.e `return view('/meetings', ['meetings' => $myMeetings]`. Faker allows you to generate almost everything from numbers, users, addresses, dates to companies. It also supports different languages, such as Japanese (Hiragana/Katana/Kanji) or Korean (Hangul) names and sentences.

For your views, follow the provided wireframes and designs accordingly and use blade templating (layouts, subviews, yield/sections) effectively. Keep reusability in mind. If you feel like exploring, give blade components a try (https://laravel.com/docs/8.x/blade#components) and remember to pass variables to components using the `:` prefix.

Lastly, create a function that returns the logged in user to mock. You may hardcode the constructor inputs. Make this a public static function that is part of the User class, `User::createFakeSignedInUser()`. Pass this $loggedInUser to your views, and display this logged in user in the navigator.

- /
  - This is the homepage that shows a list of meetings currently occurring, and a list of users. Both meetings and users should show up as cards, so user subviews or components to accomplish this. Use blade foreach to loop through the array of meetings/users.
  - Both the meetings and users should be randomly generated, and they must match the currently logged in user's targetLanguage. It is a match if a logged in user's targetLanguage is part of the meeting. If the user is not able to join the meeting, show the meeting as greyed out. For users, its a match if a logged in user's targetLanguage is part of a user's native language or knownLanguage.
  - With that said, generate meetings/users based on the logged in user's targetLanguage.
- /users/{language}
  - This page shows a list of users whose nativeLanguage or knownLanguages matches the `language` provided by the url. Use url parameters on your routes to get the actual language (https://laravel.com/docs/8.x/routing#route-parameters).
  - All users you generate for this page will have the specified language url parameter in their nativeLanguage or knownLanguage state.
- /meetings
  - This page returns a list of meetings. Note this page will accept get parameters, i.e /meetings?languageA=spanish. If no parameters are specified, return a list of meetings that match the logged in user's targetLanguage just like the home page. 
  - There may be many different kinds of available get parameters, and multiple parameters may be passed in. The generated meeting must abide by those parameters. i.e /meetings?languageA=spanish&languageB=portuguese&max=6 will return meetings where languageA is spansih, languageB is portugues and there is a max of 6 participants. 
  - Get parameters are injected through dependency injection. Through the route closure function, simply *type hint* the Request class as a parameter input, and Laravel will retrieve the dependency from its internal *service container*. Inside the route's closure function, you are free to access this request variable and retrieve get parameters. See https://laravel.com/docs/8.x/routing#parameters-and-dependency-injection for more details, and https://laravel.com/docs/8.x/requests for full API details about the Request class.
    - As you will see, many objects whose structure come packaged with Laravel, such as Eloquent ORM objects you will learn, are able to be injected into functions by just type hinting. 



