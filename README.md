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

## Home page

## Sign Up,Login and Logout 

## Post Details

## Reviews

## Directors&Genre

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