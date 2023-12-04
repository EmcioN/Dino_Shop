![logo](/doc/images/herotrex.jpeg)
# Dino Shop
## Table of Contents
[UX](#ux)
  * [Goal for the Project](#goal-for-the-project)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Site owner Goals](#site-owner-goals)
  * [Design Choices](#design-choices)
    * [Font](#font)
    * [Icons](#icons)
    * [Colours](#colours)
    * [Structure](#structure)
  * [Features](#features)    
  * [Future Plans](#future-plans)      
  * [Tehnologies used](#tehnologies-used)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
## UX
## Goal for the Project
  Create a user-friendly online shop for selling virtual dinosaurs from Ark: Survival Evolved, providing an enjoyable shopping experience for gamers and a profitable venture for the site owner.
### User Goals 
  * Find and purchase virtual dinosaurs for use in Ark: Survival Evolved.
  * Easily navigate the website to browse available dinosaurs.
  * Create an account for personalized shopping and easy order tracking.
  * Receive prompt and secure transactions when buying dinosaurs.
  * Access information about each dinosaur's attributes, level, and price.
  * Contact customer support for assistance with any issues.
  * Receive email notifications for order confirmation
### User Stories  
  * As a user who plays Ark: Survival Evolved, I want to see detailed information about each dinosaur, including its level, attributes, and any special abilities it may have.
  * As a user, I want to create an account with my personal details, email, and password so that I can track my orders and have a personalized experience.
  * As a user and buyer, I want a straightforward and secure checkout process to make my purchases without any complications.
  * As a user and customer, I want to receive email notifications confirming my orders and providing tracking information once my dinosaurs have been delivered.
  * As a user and gamer, I want the website to provide a responsive and user-friendly design that works well on both desktop and mobile devices.
  * As a user and shopper, I want to have access to customer support through email in case I have questions or encounter any issues while browsing or making a purchase.
### Site owner Goals
  * Build a visually appealing and user-friendly website that showcases the available dinosaurs effectively.
  * Offer a secure payment system to protect customer data and transactions.
  * Provide detailed information about each dinosaur, including its level, attributes, and price.
  * Implement a customer account system for order tracking and a personalized shopping experience.
  * Offer responsive customer support to address user inquiries and issues promptly.
  * Ensure a smooth and efficient order processing and delivery system.
  * Advertise the online shop to the Ark: Survival Evolved gaming community to attract potential buyers.
### Design Choices
#### Font
  [Open Sans](https://fonts.google.com/specimen/Open+Sans) is a clean and modern font that's perfect for any website. It's easy to read on screens of all sizes, making it ideal for web and mobile use.
#### Icons
  I use [Font Awesome](https://fontawesome.com) icons because they're easy to use and look great. After adding them to the site, it became livelier and more attractive. Thanks to them, the website is easier to read. They are easy to understand, so they replace some descriptions.
#### Colours
My project utilizes a dark-themed color scheme inspired by Bootstrap's dark color palette.

![colors](/doc/images/colors.png)
#### Structure

Wireframes:

* Home page

![home](/doc/images/fhome.png)

* Login page

![login](/doc/images/flogin.png)

* Profile page

![profile](/doc/images/fprofile.png)

* Dinosuar listing

![dinolist](/doc/images/fdinolist.png)

* Basket

![basket](/doc/images/fbasket.png)

* Checkout

![checkout](/doc/images/fcheckout.png)

* Contact

![contact](/doc/images/fcontact.png)

The project is structured into the following main components:

Home Page:
*  User welcome page. You can see the most popular dinosaur there
![home1](/doc/images/homep1.png)
![home2](/doc/images/homep2.png)

User Accounts:

*  Users can create accounts, log in, and personalize their profiles. Profiles include a profile picture, bio, and transaction history

![profile](/doc/images/profile.png)

Dinosaurs Listing

* : Here the user can select the dinosaur he wants to buy. If you are a superuser you can add new products

![dinolist](/doc/images/dinolist.png)

Contact Page:

*  If you have any questions, feel free to fill out the form and you will receive an answer as quickly as possible

![contact](/doc/images/contact.png)

Basket:

* The user can add and remove items from the cart. There will be a shopping cart icon with the number of items on the navbar. If we go to it we will get more information.

![basket](/doc/images/basket.png)

### Features
Navbar:

* It is adapted to both large and small screens. Clean and easy to use

![navbar](/doc/images/navbar.png)

![navbar](/doc/images/navsmall.png)

Login:

* Login page provides a gateway to access the platform.

![login](/doc/images/login.png)

Create account:

* For new users, we've built a streamlined account creation process. This feature enables anyone to join our community with ease. Simply fill in the required details, and you're all set to explore!

![register](/doc/images/signup.png)

Edit Profile:

* Understand the importance of personalization. Once logged in, users can navigate to their profile settings and make modifications. From updating profile pictures to changing personal information.

![edit](/doc/images/editprofile.png)

Add/Edit Dinosaur:

* If you are logged in as masteruser, you can add, delete and edit dinosaurs. You can give them a short description and information that will interest the user, such as statistics or price. You can also add a link to a video that will show the dinosaur in action

![edit](/doc/images/editdelete.png)

![add](/doc/images/adddino.png)

![editdino](/doc/images/editdino.png)

* If you are a regular user, you can see exactly all the information about the dinosaur by clicking see more

![info](/doc/images/infop1.png)

![info](/doc/images/infop2.png)

Checkout:

* Here the user can see his order. After providing your in-game username, server, email address and card details, you can proceed to payment

![checkout](/doc/images/checkout.png)

Transaction history:

* The user can see their purchase history on their profile

![thistory](/doc/images/thistory.png)

Footer:

* At the base of our platform lies the footer, a space where users can find additional information and quick links.

![footer](/doc/images/footer.png)

### Future Plans

I planned to do more with the project. Due to the deadline, not everything was implemented as I would have liked. Login with Google has not been added yet, but it is planned to be added. Same with Google Pay. I use Stripe as a payment method but I would like to add Google Pay as a replacement method. The project lacks a polisher that would make the project look more professional.

### Tehnologies used
#### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
#### Frameworks and Libraries
* [Font Awesome](https://fontawesome.com) - Used for icons on the website.
* [Google fonts](https://fonts.google.com) - Used for text font on page.
* [Django](https://www.djangoproject.com/) - Python-based web framework
* [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) - HTTP server interface.
* [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.
* [Bootstrap](https://getbootstrap.com/) Bootstrap  was used in this project.
* [balsamiq](https://balsamiq.com/) Balsamiq used to create wireframes
#### Tools
* [Gitpod](https://gitpod.io/workspaces) - Used for building the website.
* [Github](https://github.com/) - Used to deploy the project. 
* [W3C HTML Validation Service](https://validator.w3.org/) - Used to test HTML.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to test CSS.
* [Devtools](https://developer.chrome.com/docs/devtools/#:~:text=Chrome%20DevTools%20is%20a%20set,you%20can%20open%20Chrome%20DevTools.) - I checked all the time how my code works and if there are any errors in console
* [CI Python](https://pep8ci.herokuapp.com/) - Used to test my python code if there is any mistakes.
* [Heroku](https://www.heroku.com) - Deployment of website.
* [Stripe](https://stripe.com/) - Payment method 
### Testing
#### Html Validator
#### Css Validator
#### CI python Linter
#### Manual Testing
### Deployment

Local Development

* Go to Github repo [here](https://github.com/EmcioN/Dino_Shop) 
press **< CODE >**, and press COPY.
or **FORK** my repo

![clone](/doc/images/clonefork.png)

* Go to your github repositories and create new repo, call it whatever you like. Press Create Repository it will lead you to another page, and press Gitpod it should open workspace for you
* Now you need to download all libraries and frameworks used in this project. Use command : 
```
pip3 install -r requirements.txt
```
* Log in to Heroku or create a new account.
* Click the New button in the top right corner and select Create New App.

![step](/doc/images/step1.png)

* Choose a unique name for your app and select the region you want it to run in, then click Create App.

![step](/doc/images/step2.png)

* Go to the Deploy tab and click on the Settings tab.

![step](/doc/images/step3.png)

* Scroll down to the Buildpack section and click Add Buildpack.

![step](/doc/images/step4.png)

* Select "python" and click Save Changes.

![step](/doc/images/step5.png)

* Go back to the top of the page and select the Deploy tab again.

![step](/doc/images/step6.png)

* Choose Github as the deployment method and confirm that you want to connect to your Github account.

![step](/doc/images/step7.png)

* Search for your repository name and click the connect button.
* Scroll to the bottom of the deploy page and select your preferred deployment type.
* You can choose to enable automatic deploys for automatic deployment when you push updates to Github.

![step](/doc/images/step8.png)

* That's it, your site should now be deployed!

### Credits
[Code Institute](https://codeinstitute.net/ie/): A special acknowledgment to the Code Institute. Revisiting lessons there proved invaluable, reinforcing core concepts and strengthening my foundation.

[YouTube Tutorials](https://www.youtube.com/): Many thanks to the numerous educators and developers on YouTube. Their shared knowledge and step-by-step tutorials provided clarity and depth to my understanding.

[Stack Overflow](https://stackoverflow.co/): An essential resource during this journey. The community's expertise and shared experiences on Stack Overflow were immensely beneficial in navigating challenges and troubleshooting issues.

Gratitude to all these resources for guiding me through this coding journey and for being reliable pillars of support.
#### For help, advice and insperation
I would like to thank my mentor for helping me with the YouTube link processing function. Of course, this is not the only thing I am grateful for. Many other small problems were solved by him explaining it to me so that I could understand.
[Simen Daehlin](https://github.com/Eventyret)