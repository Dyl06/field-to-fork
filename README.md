# Field to Fork

### Site Purpose
- Our farm is dedicated to providing local consumers with the highest quality, ethically produced meats. With a deep commitment to transparency and traceability, we offer discerning consumers a delightful and guilt-free option, promoting a healthier lifestyle and supporting the local community.

### Site Owner goals
- As a farmer I would like to sell the meat that I produce on my farm to people in my area. 
To do this I would like to set up an online store, called FieldToFork.
The store needs to display the meat I have available for purchase and allows users to scroll through the different products.
The Users will then be able order the products and come and collect those products from the farm. 

### Site Design
- The design of the website I have created revolves around a user-centric approach, prioritizing good user experience (UX) and user interface (UI). Key aspects of the design focus on simplicity and ease of navigation. The website features a streamlined and intuitive navigation system, ensuring that users can effortlessly explore various sections. With a minimal number of clicks, users can quickly find and purchase desired products, thanks to the strategically placed "buy now" option. Consistency in styling and layout has been maintained throughout the pages, creating a familiar and seamless experience for users. Navigating the website becomes an enjoyable and hassle-free journey, ensuring that users can focus on their needs and goals with utmost convenience.

### Existing Features
#### -Navigation Bar
- Hamburger menu is common to many sites and stays consitent across all screen sizes giving users a familiar feel to the site.
- Field to Fork Heading displayed in the top right corner accross all sites gives users a good UX, while being a subtle reminder of the brand and what site they are part of.
#### -Landing Page
- Has a big background image of a wide open countryside that provides users with a good feeling and UX about the farm and the products that they are about to buy and recieve from it.
- About the Farm - A short description sharing with users the values upheld by the farm. Giving users a sense of trust and understand about what they are possible about to buy.
- Products Shows a picture of each of the three product categories and a linkto view each specific category.
#### - Footer
- Social Media links to facebook twitter and instagram.
- They display across all pages of the site for good uniformity and UX
    
#### -Products
- Templates with all products avvailable for purchase.
- Each product has a Name, Description, Weight and Price with a add to basket button below.
- Three different product categories, - Beef, Lamb and Chicken.
- Each category has three products within it namely:
- BEEF: steak, mince, roast
- LAMB: chops, leg steak, roast
- CHICKEN: pieces, whole, fillet

#### - Basket
- Users must be registered and logged in
- Basket is a simple form that allows users to manipulate their current selections of products before it is commited to an order. 
- Users can Add Subtract or Delete items and they have the ability to add multiple different products to the basket in one session.
- Basket remains available until logout then it is lost unless user clicks buy now in which case it is a secured order.
#### - Login
- login form is a simple username and password from previous registarion for quick and easy logging in to site. 
- Users are then redirected to the home page and can browse the site without any restriction
- registration option is available under the login form incase users haven't yet registered
#### - Register
- Register form has a user name and password with password confirmation and email address.
- Hints are found next to each field for easy user registartion.
- login link is found under the form for users who have previously registered to then login.
#### - Logout
- Logout button is easily accesible in the menu and redirects users back to the home page with a succes message saying you have been logged out.
#### - My Orders
- Provides users with a detailed breakdown of their order history. 
- Orders are from newest to oldest with a box around each order for easy readability and good UX
## Features left to implement
- Order collection date, users could selet a collection date from a datepicker for collection
- Delivery, users could get products delivered to them.
- Likes, Users could like different products that they had tried.
- Review, users could leave a review on products
- Newsleter, userss could signup to a newsletter to stay up to date or recieve special offers etc
## Testing 
During the creation of this site multiple manual tests were conducted to test the proper running and function of the site.
User Validation was tested accross the site to ensure username and passwords were entered correctly and in the right format. Django built-in validation and crispy_forms were used to ensure extra validation. 
-Test to see if user could buy products without being logged in. Login_required functionality was implemented and worked correctly.
Site navigation was tested and and all buttons clicked in order to make sure the flow of the site worked and that all the templates rendered correctly and the url paths directed to the correct places. 
MVC (Model, View, Controller) was tested across the site to make sure all UI was implemented and view and controller logic was achieved and maintained throughout site. 
Login was tested with new user and existing users. Different information was put in to login form to validate that it was working as expected and that all incorrect usernames or passwords or combinations of the two would create expected errors and validation was working. 
Tried multiple logins on different devices at the same time to make sure the site could handle more then one verified user at the same time, all these tests were passed and site ran as expected 
Tested to see thay ony logged in users could view a basket and orders page and that they could only view their own baskets or orders pages and not those of other users.
-Ensure logout functionality would empty the basket so that users would have extra safety and couldn't be charged if someone accessed their devices without them knowing. 
-Registration was tested to see if invaalid documentation could be added or invallid user inputs. All passed 
 -Testing to see if you could register with already registered details. Error messaged recieved and didn't allow registration
 -Tried to register same username with different password or email or combinations of all three. Error messaged apperead and prevented registration.
 -Email fields in registration and login wanted a combination of @ and . in the correct format for an email.
 -Passwords need to match and new users need to insert password twice to make sure it works.
-Javascript was tested manually on the site to see if the function could be broken or manipulated. This included trying to input incorrect data types and trying to reduce order quantity below zero. Code was then corrected if needed and all javascript runs as expected and prevent errors. 
-Site was tested accross multiple devices and operating systems. 
-Testing was done by family and friends to make sure they could navigate the site without any issues and utilize all functionality

#### - Validator testing
        -No errors found when passing through W3c Validator. https://jigsaw.w3.org/css-validator/validator
        
#### - Automatic testing
        - Ran tests in test.py all tests returned without errors.
        -Ran JLint tests on code in the terminal window.
        
#### - Unfixed Bugs
-If a new user registers to the site and tries to navigate to Orders page they get a 404 error. In future deployments I would like to fix this with a better javascript error message and a redirect.
-Login redirect goes to the home page rather than the previous add to basket page the user was on before the were forced to login. Would prefer to update this in future deployments to allow for better site navigation.
-If a user tries to login with an existing username even with different password and email, validation won't allow it but doesn't display reason for error. Just that it is invalid registration. 

## Deployment
The code is written in Github.
The site was deployed to Heroku.
ElephantSQL has been used to host the database.
    -The code was created in github and then deployed to Heroku and I used ElephantSQL to host the database.
    -The site uses the Django Framework which was installed and linked to heroku and ElephantSQL.

The live link to the site can be  found here - 
    
## Credits
#### -Django Helper Documentation
    -https://www.w3schools.com/html/html_forms.asp
    -https://docs.djangoproject.com/en/4.2/howto/csrf/
    -https://docs.djangoproject.com/en/4.2/topics/http/urls/
    -https://stackoverflow.com/questions/11336548/django-taking-values-from-post-request
    -https://docs.djangoproject.com/en/4.2/topics/db/queries/#creating-objects
    -https://realpython.com/django-redirects/
    -https://www.w3schools.com/django/django_queryset_filter.php
    -https://docs.djangoproject.com/en/4.2/topics/db/queries/#deleting-objects
    -https://www.w3schools.com/django/django_queryset_orderby.php orders item in a page.

####  -Register/Login/Logout
        -https://ordinarycoders.com/blog/article/django-user-register-login-logout

#### -Basket Tutorial
        -https://www.youtube.com/watch?v=yC5YvGDnhDw

#### -Login Required
        -http://www.learningaboutelectronics.com/Articles/How-to-specify-the-URL-for-the-login_required-decorator-in-Django.php#:~:text=The%20login_required%20decorator%20is%20a,a%20user%20to%20log%20in.
        -https://www.fullstackpython.com/django-contrib-auth-decorators-login-required-examples.html
#### - Hamburger Menu
        -https://codepen.io/erikterwan/pen/EVzeRP
        -I used this site to get my hamburger menu and coppied the code into my project with a few minor styling tweaks to make it fit better.
#### -Font Awesome Icons
        -https://fontawesome.com/v5/search?q=cart&o=r
        
#### - CSS 
        -https://css-tricks.com/snippets/css/a-guide-to-flexbox/
        -https://www.w3schools.com/css/css_display_visibility.asp 
        -setting display to none to hide a button.
        
#### - Javascript 
        -https://stackoverflow.com/questions/30313314/django-how-to-include-javascript-in-template
        -https://stackoverflow.com/questions/9186346/javascript-onclick-increment-number
        -https://launchschool.com/books/javascript/read/loops_iterating
        -https://www.geeksforgeeks.org/how-to-force-input-field-to-enter-numbers-only-using-javascript/

#### - Image Convertor 
        -https://cloudconvert.com/jpeg-to-webp
        -https://convertio.co/jpeg-webp/





