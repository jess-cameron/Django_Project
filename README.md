# Jessica Cameron - She Codes News Project

## About This Project
My project is a news website. There is a main news page, the option to add articles to your favourites (when signed in), the option to add new users and the option to write and add new articles.

## How To Run This Code

Clone the repo to your local machine and rename as you wish. Create a virtual environment using these commands: `python -m venv venv`, `.venv/Scripts/activate`, `python -m pip install -r requirements.txt`. 
Open the file in VS Code, or similar.
Migrate the database by navigating to the shecodesnews file and running these commands: `python manage.py migrate`, `python manage.py runserver`. 
The application should now be live.

## Database Schema
Not included - I didn't do an ERD. I must have missed that class. Apologies.

## Project Features
- [x] Order stories by date
![ Stories are ordered by date. ]( ./images/orderstoriesbydate.png )

- [x] Styled "new story" form
![ New story form was created. Limited css styling. ]( ./images/stylednewstoryform.png )

- [x] Story images
![ Functionality added to add an image when creating a new story. I missed this class but added it later. ]( ./images/storyimages.png  )

- [x] Log-in
![ {{ Log in and Log out functionality }} ]( ./images/login.png )

- [x] log-out
![ {{ Log in and Log out functionality }} ]( ./images/logout.png )

- [ ] "Account view" page
![ Did not create. ]

- [x] "Create Account" page
![ Functionality to create a new user account ]( ./images/createaccount.png )

- [ ] View stories by author
![ Did not create. ]

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" button
only visible when a user *is* logged in
![ Did not create. ]

- [ ] "Create Story" functionality only available when user is logged in
![ Did not create. ]

## Additional Features:

- [x] Add the ability to “favourite” stories and see a page with your favourite stories.
![ Created the ability to favourite and un-favourite stories. Added a page to the nav bar but did not get time to complete it, to display a summary of favourited stories. ]( ./images/addtofavourites.png ) 
![  ]( ./images/removefromfavourites.png )