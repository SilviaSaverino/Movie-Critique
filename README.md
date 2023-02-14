# Movie Critique

Welcome to Movie Critique, the ultimate destination for movie lovers everywhere! This website is designed to help users make informed decisions about what to watch, with a comprehensive search feature and user-generated reviews

Where everyone is welcomed in joining the conversation with other passionate cinephiles and prompt to leave their own reviews to help guide others in their movie-watching journey.

# User Experience

## Website goals:

- To provide a platform for users to share their opinions and reviews on movies. 
- To provide users with the ability to rate movies and leave written reviews. 
- To enable users to easily find reviews for movies they are interested in viewing. 
- To provide a user-friendly interface for users to navigate and interact with the website. 
- To ensure that the website is regularly updated with the latest movie releases and reviews. 
- To provide a secure platform for users to share their personal information while leaving reviews.
- To provide a clear and appropriate response to any user inputs or actions.

## User Stories:

As a Site User I want to be able to:
- register an account so that I can comment and like
- select a specific movie and view its reviews so that I can decide whether or not to watch it.
- write and submit a review for a movie so that I can share my thoughts with others.
- edit and correct my own reviews so that I can ensure the accuracy of my feedbacks.
- delete my reviews so that I can remove any inaccuracies or irrelevant content.
- like and unlike posts so that I can indicate my appreciation or lack thereof for the post in question.
- request a director so that i can later find some of his/her movies on the website.
- filter director per genre, so that i can have a better idea of what to expect from a movie of a certain director.

## Admin stories:

As a site Admin, I want to be able to: 
- create draft posts so that I can finish writing the content later.
- update posts so that movie description are up to date.
- read and moderate reviews to ensure that they are appropriate and do not contain any offensive content.
- delete spam or fake reviews that are submitted to the site.
- review user requests of a director so that i can approve them and grow my site content.

# Agile

This project was planned utilizing the Agile Methodology. The implementation of this approach was carried out through the utilization of Github and the Project Board, which can be viewed here below:

![screenshot of kanban board](/MovieCritique/docs/userstoriesgit.png)

The project was divided into various segments through the utilization of the Kanban board found in the projects view on Github:
1 - To do
2 - In progress
3 - Done

Additionally, Github issues were employed to generate User Stories and any other necessary repairs or updates for the project. This is where the project users were assigned and labels were added to provide a quick visualization of task importance and assist in task prioritization. The User Story was incorporated into the relevant Iteration and the project as a whole.

# Database Schema
![screenshot of database schema diagram](/MovieCritique/docs/proj4models.jpeg)

•	The Post model has a one-to-many relationship with the Comment model, meaning that a single post can have multiple comments. The relationship is defined by a ForeignKey in the Comment model to the Post model.

•	The Post model also has a many-to-many relationship with the User model, meaning that a single post can be liked by multiple users, and a single user can like multiple posts. The relationship is defined by a ManyToManyField in the Post model to the User model.

•	The UserRequest model has a many-to-many relationship with the MovieGenre model, meaning that a single request can be associated with multiple genres and a single genre can be associated with multiple requests. The relationship is defined by a ManyToManyField in the UserRequest model to the MovieGenre model.

•	The MovieGenre model has a many-to-many relationship with the Director model, meaning that a single genre can be associated with multiple directors and a single director can be associated with multiple genres. The relationship is defined by a ManyToManyField in the Director model to the MovieGenre model.

# Design wireframes

# Website Structure

Upon initial access of the website, the user is greeted with a clear and intuitive layout that allows for quick and easy navigation. The homepage is immediately visible and both the sign-in and log-in options are readily available on the navigation bar. In the event that the user chooses to register, they will then have the ability to log in, and the "Your Request" page link will replace the "Sign Up" page one.

The user can explore the website by clicking on the post links, which will direct them to either the reviews/comments page or the genre list page. On the genre list page, the user can select their preferred genre and view a list of movie directors.  Additionally, users have access to the "Your Request" page where they can check the status of their director request and edit or cancel their request. Both of these pages are readily accessible from the navigation bar, allowing the user to easily move back and forth as needed.

At all time the users will be able to log out if they wish to do so.

# Design & Color scheme

The website features a distinctive color scheme, utilizing a rich dark yellow/orange shade complemented by bright white and eye-catching green accents. The selection of these colors was deliberate, aimed at creating a visually impactful design while highlighting the images on the site.

Throughout the website, a visually striking dark background is paired with an elegant antique white color for the content to clearly convey information to the user. This color scheme is applied consistently for the display of introductions, posts, and administrative messages.

# Features

## Navigation

The navigation of the website is achieved through the top navigation bar on each page, which remains consistent in appearance as the user navigates throughout the site. 

The tabs displayed on the navigation bar are dependent on the user's login status and page visited.

![screenshot of navigation bar](/MovieCritique/docs/navigation.png)

## Home page

The main page of the website, the Home Page, is the first thing that is displayed upon site loading. 

Its design makes it clear what the purpose of the website is, with a striking hero image, an introduction of what Movie Critique is about; the site name, and a call to action featuring log in and sign up buttons. 

![screenshot of hero image](/MovieCritique/docs/hero.png)

![screenshot of movie critique intro](/MovieCritique/docs/mcintro.png)

Upon successful login, a notification alerts the user to confirm their login status.

By scrolling down, the user can view movie cards displaying the movies currently posted in the website.

![screenshot of post movie card](/MovieCritique/docs/post.png)

## Sign Up,Login and Logout 

The Log In page can be reached through the navigation bar and has a link to the Sign Up and it offers a link to the Sign Up page for users who may have accidentally clicked on the wrong option. The sign up page will instead offer a link to the login page for the same reason.

Should the user wish to logout this won't happen automatically, but  a confirmation will be required to proceed.

These three pages are designed with consistent styles and are fully responsive, using django-allauth for user authentication and for each option, the user will be receive a confirmation notified by a pop up message.

![screenshot of the log in page](/MovieCritique/docs/login.png)

![screenshot of the sign up page](/MovieCritique/docs/signup.png)

![screenshot of the log out page](/MovieCritique/docs/logout.png)

## Post Details

The card displayed on the homepage showcases a sleek design that presents the movie's poster, title, brief summary, and the author of the post. 

This layout offers the user two options - either to view the reviews or navigate to the director and genre section of the site.

![screenshot of a movie post](/MovieCritique/docs/post.png)

## Reviews

Upon clicking on a movie card, the user will be presented with the full details of the selected movie including its title, author, and post date, as well as a comprehensive description and movie image. 
![screenshot of movie post with description](/MovieCritique/docs/postdetailsrev.png)

The user will also have the following options at their disposal:

  -  View the number of reviews that have been posted
  -  Like the movie by clicking on the heart icon (available after login)
  -  Check the total number of likes the movie has received 
  
     ![screenshot of like buttons and reviews count](/MovieCritique/docs/likebutton.png)
  
  -  Write a review (available after login)

     ![screenshot of leave reviews section](/MovieCritique/docs/leavereviews.png)

  -  Edit their own review using the edit icon (only visible for their own reviews)
  -  Delete their own review using the trash bin icon (only visible for their own reviews)
     
     ![screenshot of edit and cancel buttons](/MovieCritique/docs/editcancelbutton.png)

Please note that users will not be able to edit or remove reviews written by other users. 

Additionally, all reviews will be subject to review by an administrator to ensure that they are appropriate and do not contain explicit language or offensive content. 

Upon submitting a review, the user will receive a notification indicating that the review is pending approval.

![screenshot of awaiting approval message](/MovieCritique/docs/awaitingapproval.png)

## Directors&Genre

Upon arriving at the Director & Genre page, the user will be greeted with a brief introduction followed by a scrollable list of movie genres. Each genre features the genre type, an age recommendation, and a concise description of the genre's content.

![screenshot of genrelist](/MovieCritique/docs/genrelist.png)

By choosing one of the listed genres, the user will be directed to the Directors page where they can explore further details and information about each director. The page will showcase a picture of the director alongside a concise biography, highlighting some of their notable works.

![screenshot of director bio](/MovieCritique/docs/directorbio.png)

For users who wish to discover new directors, a convenient link is provided for them to request the addition of a new director, along with suggested films to be added to the website.

![screenshot of director request link](/MovieCritique/docs/formlink.png)

## Director request

This page features a form that allows users to submit requests for new directors and suggest movies to be added to the website. 

![screenshot of director request form](/MovieCritique/docs/directorform.png)

Upon submitting their request, the user will be redirected to the "Your Request" page, where a pop-up message will confirm the successful submission of their request.

## Your Request page

On this page, the user can view all of their requests and the status of each, whether it's pending approval or currently being worked on. During the pending period, the user has the option to edit or cancel their requests.

![screenshot of user request](/MovieCritique/docs/pending.png)

![screenshot of approved request](/MovieCritique/docs/approved.png)


# Future features

## Login: 
- For convenience, users could log in using their social media credentials instead of creating another password to remember.

## User Page:
- In the future, I would like to enhance the user experience by adding a user page where they can personalize 
  their experience. This page would include:

   1) Avatar Selection: Users will have the option to choose an avatar that will represent them in their movie reviews.

   2) Personalized Movie Review Section: A section where users can view only their own movie reviews and categorize them into "Must Watch" or "Watch Again".

   3) Filter and Sort Functionality: Users will be able to filter and sort their movie reviews by genre and personal preference.

   4) Movie Recommendations: A personalized movie recommendation section based on the user's previously watched and reviewed movies.

This user page will provide a more personalized and organized experience for movie enthusiasts and will help users keep track of their favorite films and genres.

## Search Bar: 
- In the future, I would like to incorporate a search bar on the main screen to make it easier for users to find specific 
  movie  titles or directors. 


# Testing

## Validation

### Html Validation

### Css Validation

### JS Validation

### Python Validation

## Lighthouse

## Manual testing

As part of ensuring the quality and reliability of the website, manual testing was conducted to validate its functionality and user experience. The following is a screenshot of a list of the functionalities that were tested.

![screenshot of manual testing for user not logged in yet](/MovieCritique/docs/testingloggedout.png)

![screenshot of manual testing for user logged in](/MovieCritique/docs/testingloggedin.png)

## Bugs & Fixes

While building the website, I encountered several bugs that required fixes. Of all the bugs, I believe that the following posed the greatest risk to the user experience:

   - Upon logging in, users were able to edit and cancel their own reviews or requests. However, due to a flaw in my code, others could easily manipulate the URL by changing the ID number and access the ability to edit or cancel other users' reviews or requests.

### Steps taken to fix this major issue:

The initial code wasn't properly considering the user's ability to edit a different review by simply manipulating the url id number.

![screenshot of urls reviews id/edit](/MovieCritique/docs/originalbug.png)  


![screenshot of urls reviews id/edit](/MovieCritique/docs/bughttpresponse.png) 

An HttpResponse was first used to prevent a user from editing a review by changing the id number in the URL, but it was discovered that the user name and the author of the review were matching, but their data types were different, which was causing the HttpResponse to be returned.

To resolve this issue, the code was updated to convert both the user name and the author of the review into strings.

![screenshot of urls reviews id/edit](/MovieCritique/docs/bugtype.png) 

However, after the HttpResponse was triggered, it was noted that the user wasn't being redirected back to the site. 

!![screenshot of urls reviews id/edit](/MovieCritique/docs/bugid403.png)  

To fix this, the HttpResponse was replaced with an error message indicating that the user can't edit other reviews or requests, and a redirect was added to take the user back to the previous page of comments/reviews or the director request.

![screenshot of urls reviews id/edit](/MovieCritique/docs/cannotedit.png)

# Deployment

## Deployment to Heroku 

### Django project creation

To get started with developing your Django web application, you'll need to perform the following steps:

1) - Install Django and Gunicorn using the following command: pip3 install django gunicorn. These are essential components for building a Django web application.
2) - Install supporting database libraries dj_database_url and psycopg2 using the command pip install dj_database_url psycopg2. These will allow you to connect your Django application to a PostgreSQL database.
3) - Install the Cloudinary library to manage your application's static files with the command pip install   dj-3-cloudinary-storage. This library will allow you to store your static files on the Cloudinary platform.
4) - Create a file for your application's dependencies using the command pip freeze --local > requirements.txt. This will generate a requirements.txt file that lists all the packages and libraries required to run your application.
5) - Create a Django project using the command django-admin startproject project_name .. Replace project_name with the name of your project.
6) - Create a Django app using the command python manage.py startapp app_name. Replace app_name with the name of your app.
7) - Add your app to the list of installed apps in the settings.py file by adding 'app_name' to the INSTALLED_APPS list.
8) - Migrate your database using the command python manage.py migrate. This will create the necessary database tables for your app.
9) - Test that your server is working locally using the command python manage.py runserver. This will start the Django development server on your local machine.

### Heroku app creation

To host your Django app on Heroku, you'll need to perform the following steps:

1) - Navigate to the Heroku website and create an account using your email address and a password. If you already have an account, log in to your account.
2) - Activate your account by following the authentication email that Heroku sends to your email account.
3) - Click the "New" button on the top right corner of the Heroku dashboard and select "Create new app" from the dropdown menu.
4) - Choose a unique name for your application and select the region where you want to deploy your app.
5) - Click the "Create app" button to create your new app.
6) - Go to the "Resources" tab on the Heroku dashboard and scroll down to the "Add-ons" section. Look for "Heroku Postgres" and add it to your app.
7) - In the "Settings" tab, scroll down to "Reveal Config Vars". You'll see a DATABASE_URL variable with a value. Copy the entire value, including postgres://, the username, the password, the host, the port, and the database name.

### Enviroment Variables 

### Settings.py

### Final Deployment

## Github

# Technologies Used
The development of this website utilized a range of technologies, including:

   - HTML - Used to structure all the templates on the site and create the basic layout.
   - CSS - Enhanced the overall appearance of the site with additional styling.
   - Python - Implemented the website's functionalities with the aid of packages listed in the requirements.txt file.
   - Django - A Python framework that was chosen to build the website.
   - Heroku - The platform used to deploy the site publicly, making it accessible to users worldwide.
   - Heroku ElephantSQL - The database solution used during both development and deployment phases.
   - JavaScript - A minimal amount of JavaScript was used to create user-friendly features such as fading out alerts 
     and a button that takes users back to the top of the screen.
   - Bootstrap 4 - Provided pre-designed layouts and styling options for the HTML templates.
   - Lucid Chart - To create database schema diagram
   - Cloudinary - Hosted all of the website's static files, ensuring efficient and fast loading times for users.

# Credits 

To complete this project, I relied on various sources of information, including videos from YouTube, articles found online, the W3School website, and Stack Overflow. 

# Acknowledgements

I would like to thank my mentor Spencer for his support and for taking the time to review this project.  
I am thankful for my dear friend Francesco for being a constant source of support, and for my family members Martina and Cosimo for their love and encouragement.
I would also like to acknowledge the creators and contributors of the online resources mentioned in the Credits section for providing valuable guidance and insights.