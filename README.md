![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

The user can explore the website by clicking on the post links, which will direct them to either the reviews/comments page or the genre list page. On the genre list page, the user can select their preferred genre and view a list of movie directors. Both of these pages are readily accessible from the navigation bar, allowing the user to easily move back and forth as needed.

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

# Future features

# Testing

## Validation

### Html Validation

### Css Validation

### JS Validation

### Python Validation

## Lighthouse

## Manual testing

## Bugs & Fixes

# Deployment

## Deployment to Heroku 

### Django project creation

### Heroku app creation

### Enviroment Variables 

### Settings.py

### Final Deployment

## Github

# Technologies Used

# Credits 

# Acknowledgements