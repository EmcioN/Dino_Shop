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

Newsletter:

* Possibility to subscribe to the newsletter using your email address.

![newsletter](/doc/images/newsletterform.png)

![newsletter](/doc/images/btnc.png)

![newsletter](/doc/images/btnf.png)

* Facebook page:

  I created a Facebook page dedicated to this store. It contains basic information, contact details, a link to the website and the opportunity to leave your opinion. This will definitely help in the development of the store.

  ![facebook](/doc/images/facebook1.png)

  ![facebook](/doc/images/facebook2.png)

  ![facebook](/doc/images/facebook3.png)

### Future Plans

I planned to do more with the project. Due to the deadline, not everything was completed as I would have liked. Login with Google has not been added yet, but is planned to be added. Same with Google Pay. I use Stripe as a payment method, but I would like to add Google Pay as a fallback method. The design lacks a polisher that would give the design a more professional look. I didn't have enough time to add webhooks to stripe. I plan to expand the project and add other products, such as raw materials. A lot of work has to be put into such a project. Unfortunately, I work long shifts and don't have enough time to devote to the project. I did as much as I could and I'm partially satisfied with it.

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

I had the least problems with html. The only thing we forget about is setting the appropriate hrefs. I really like using Django with Bootstrap because it simplifies things a lot.

![css](/doc/images/csserr.png)

#### I tested each page one by one using source code and html validator:

* Home

![home](/doc/images/hometest.png)

* Product view 

![product](/doc/images/producttest.png)

* Product detail

![product](/doc/images/producttest2.png)

* Login

![Login](/doc/images/logintest.png)

* Contact

![contact](/doc/images/contacttest.png)

* Profile

![profile](/doc/images/profiletest.png)

* Profile edit

![profile](/doc/images/editprofiletest.png)

* Newsletter

![newsletter](/doc/images/newslettertest.png)

* Basket

![basket](/doc/images/baskettest.png)

* Payment

![payment](/doc/images/paytest.png)

* Logout 

![logout](/doc/images/logouttest.png)

* Success Page

![Success](/doc/images/successtest.png)

* News

![news](/doc/images/newstest.png)


#### Css Validator

While testing CSS, I encountered several problems. After taking advice on stackoverflow, I decided to move on, because these are not serious errors. The page looks as intended, so it shouldn't be a problem

![css](/doc/images/csserr.png)

#### CI python Linter

I had some fun with python. You can still probably find some bugs because everything was tested quickly due to lack of time. The command "python3 -m flake8" turned out to be a lot of help. At the beginning I had a lot of problems there, but I cleaned up some code and it looks much better. When creating the code, I relied on a tutorial from Code Institute Boutique Ado. I tried to follow along with him. Thanks to it, I managed to set up the databases correctly this time without any major problems. There are a few things that don't work, but due to the deadline I won't be able to fix them in time. The most important thing for me is that the store is operational.

![clean](/doc/images/clean1.png)

![clean](/doc/images/clean2.png)

To be sure, I used CI python linter to make sure the code I wrote was correct

![basket](/doc/images/basketp.png)

![checkout](/doc/images/checkoutp.png)

![home](/doc/images/homep.png)

![product](/doc/images/productp.png)

![settings](/doc/images/settingsp.png)

![user](/doc/images/userp.png)

#### Manual Testing
I tested the project continuously during production. Most things were done by trial and error. I don't consider the project finished due to the lack of tests. There are two known errors in the project. I ran out of time. I didn't encounter any huge problems, but some of them took a lot of time. When switching to production I had a problem with static files. Back then I was using whitenoise and AWS S3. It was confusing for me so I decided to give up whitenoise. Due to my lack of attention, I had a few errors related to the wrong path. This time, I changed the database for production purposes with a tutorial from Code Institute and it went without any major problems. I plan to continue working on this project so that I can open this store someday.

All buttons have been tested and work as intended. Fields that are supposed to be displayed only for Superuser work as they should. Adding, removing or editing dinosaurs from the superuser level works without problems. The form on the contact page works correctly and sends a message to the provided email address. All links work as they should. In the dinosaur description, the video displays correctly, thanks to my mentor. Adding and removing items from your cart works as intended. Editing your profile works fine.

* Table with tested working pages as a guest, user and admin

| Test case            | Guest | User | Admin | Pass/failed |
|----------------------|-------|------|-------|-------------|
| Basket loop          | ❎     | ✅    | ✅     | Pass        |
| Profile Edit         | ❎     | ✅    | ✅     | Pass        |
| Profile login/Create | ✅     | ✅    | ✅     | Pass        |
| Product Edit         | ❎     | ❎    | ✅     | Pass        |
| Product View         | ✅     | ✅    | ✅     | Pass        |
| Contact              | ❎     | ✅    | ✅     | Pass        |
| Newsletter           | ✅     | ✅    | ✅     | Pass        |




* Payment testing:

  The payment method works. The transaction is saved in the transaction history on the user's profile. Everything seems to be properly connected to Stripe

  ![history](/doc/images/history.png)

  ![stripe](/doc/images/paymenttest.png)

  ![stripe](/doc/images/paymenttest1.png)

  ![stripe](/doc/images/adminpanel.png)

  ![stripe](/doc/images/webhooks.png)

  ![stripe](/doc/images/payments.png)

  ![stripe](/doc/images/striped.png)

  ![stripe](/doc/images/profilethistory.png)

* Newsletter Testing:

  I tested the newsletter and it seems to work properly. After entering the correct email address, we are redirected to the success page. It is saved in the database. If a given email is already subscribed to the newsletter, we receive a message that the email is already saved. If we enter an incorrect email address, we will also be informed.

  Incorrect Email

![emailcorrect](/doc/images/newscorrecte.png)

  Email exist

![emailexist](/doc/images/newsexist.png)

  Success page

![success](/doc/images/success.png)


#### User stories Test

* As a user who plays Ark: Survival Evolved, I want to see detailed information about each dinosaur, including its level, attributes, and any special abilities it may have.

  Each dino has a description, basic statistics, a photo and even a video of it in action

![dinos](/doc/images/users.png)

* As a user, I want to create an account with my personal details, email, and password so that I can track my orders and have a personalized experience.

  Everyone can create their own account. You can edit your profile by adding a short description about yourself, a photo or links to social media

![signup](/doc/images/usersignup.png)

![profile](/doc/images/userprofile.png)


* As a user and buyer, I want a straightforward and secure checkout process to make my purchases without any complications.

  The shopping cart is very easy to use with no hidden features. The same applies to the payment method. Everything seems clear and easy to use

![basket](/doc/images/userbasket.png)

![payment](/doc/images/userpay.png)


* As a user and gamer, I want the website to provide a responsive and user-friendly design that works well on both desktop and mobile devices.

  The website works well on small screens and on large screens. The initial idea was to create a store that would work on small screens

![small](/doc/images/usersmall.png)

![big](/doc/images/userbig.png)


* As a user and shopper, I want to have access to customer support through email in case I have questions or encounter any issues while browsing or making a purchase.

  Each user can contact support via email address. This can be done by filling out a simple form. You can also subscribe to the newsletter to stay up to date

![contact](/doc/images/usercontact.png)


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

[Ark Survival Evolved](https://en.wikipedia.org/wiki/Ark:_Survival_Evolved): Information about dinosaurs was taken from the wiki page. I was inspired by this game, which I am grateful for, because I had no specific idea for the project.

Gratitude to all these resources for guiding me through this coding journey and for being reliable pillars of support.
#### For help, advice and insperation
I would like to thank my mentor for helping me with the YouTube link processing function. Of course, this is not the only thing I am grateful for. Many other small problems were solved by him explaining it to me so that I could understand.
[Simen Daehlin](https://github.com/Eventyret)