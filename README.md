# Recipe
#### Video Demo: 
#### Description:
Recipe is a web application built with flask that allows users to input a list
of food ingredients and get in return a list of ingredients which uses said ingredients 
extensively. Using the Python requests library, an API request is sent to the spoonacular
food API. The API request is formed by obtaining user input via HTML form. 
upon receiving the list of recipes from ingredients, a second API request
is formed and sent, which returns a link to the page the recipe is found
from. Displayed in the link embedded to the recipes name along with a picture
of the recipe to provide a visual component. The application
has register and log in pages. User information is saved in a SQL database using SQLite.
The frontend of the website contains images stored in the project hierarchy under the
/static/images directory along with a css stylesheet.Elements from Bootstrap have been
utilized as well.

This project was developed in Jetbrain's Pycharm, an initial challenge I faced was setting
up a new IDE for development with flask as I used CS50's codespace exclusively in the past.
Along with learning to set up development in a new IDE, I sharpened my skills with git,
I worked on this project on two machines, my desktop and laptop, and used git to merge
changes I made on the seperate machines. I settled on using python flask bootstrap and
SQLite becuase these were the technologies we learned throughout the class. I built
the application as a solo project.

In the future I plan to make the login feature more useful. I plan on adding the ability
to save ingredients to your account so that all ingredients do not need to be 
inputted for each use. Another feature I plan on looking in to implementing is creating
a downloadable mobile app. The app will have the same functionality but will include the
ability to add ingredients using a camera. The camera will rely on Natural Language Processing
technology to read labels and add them to the users saved ingredients.

The app is simple to use, from the homepage either register for an account, log in, or skip this
step entirely, then navigate to the pantry page. Enter the ingredients you want to use seperated
by commas and click submit.You will be presented with a list of recipes with images and
links to the instructions.