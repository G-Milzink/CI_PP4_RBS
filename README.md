# Wine & Vinegar | Restaurant

![Am I Responsive](docs/am-i-responsive.webp)

**Developer: Gustaaf Milzink**

[Visit live website](https://wine-vinegar-0533cc22e633.herokuapp.com/)


## Table of Contents
- [About](#about)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
    - [User Story testing](#user-story-testing)
    - [Browser compatibility](#browser-compatibility)
    - [Real-World devices](#real-world--devices)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Wine & Vinegar is a fictional restaurant. The website provides users the abillity to view the menu, read a blog, view the menu and book a table.

### User Goals

- The abillity to book a table.
- The abillity to view edit and cancel bookings.
- The abillity to view the menu, contact info and blog.

### Site Owner Goals

- Provide a website with an intuitive responnsive design.
- Facillitate communication with customers through a blog and contact form.
- Allow users to book a table.
- Attract additional business with an aestheticly pleasing website.

## User Experience

### Target Audience

- People looking for a place to have a meal.
- People who wish to book a table for a meal.
- Potential customers who want to get a sense of the atmosphere in the restautrant.
- Returning customers who want to know the current menu
- New and Returning customers who want to know more about what's happening in the restaurant.

### User Requirements and Expectations

- A welcoming design
- Accessibility
- Full responsiveness
- Contact information

## User Stories

### Site Owner 

1. As site owner I want the site to be fully responsive so that I can provide a good user experience. (Must Have)
2. As site owner I want to provide a contact page so that users can find/contact the restaurant easily. (Must Have)
3. As site owner I want users to be able to view the menu so that they can easily ddecide wether or not to book with us.(Must Have)
4. As site owner I want users to be able to book a table online. (Must Have)
5. as site owner I want to be able to maintain a blog so that users can be informed about the goings on in the restaureant. (Must Have)

### Admin

6. As site admin I want to be able to login so that I can acces the backend of the site. (Must Have)
7. As site admin I want to be able to view/make changes to the menus so that I can keep it up to date. (Must Have)
8. As site admin I want to be able confirm or reject a booking so that I can avoid double bookings. (Must Have)
9. As site admin I want to be able to manually enter a booking so that I can book a table in response to a user's phonecall or email. (Must Have)
10. As site admin I want to be able to post articles to the blog so that I can maintain customer communication. (Must Have)
11. As site admin I want to be able to approve blog-comments so that I can make sure nothing innaprorpiate is displayed. (Must Have)
12. As site admin I want to be able to filter bookings by date so that I can see wich bookings we have for a particular day. (Must Have)
13. As site admin I want to be able to add a registered user to "staff" so they can acces the site's backend.  (Must Have)

### Users

14. As site user I want to be able to easily navigate the site to find the information I am looking for. (Must Have)
15. As site user I want to be able to view the menu. (Must Have)
16. As site user I want to be able to easily contact the restaurant. (Must Have)
17. As site user I want to be able to be able to see the restaurants opening times and location. (Must Have)
18. As site user I want to be able to get a sense of the atmosphere in the restaurant. (Must Have)
19. As site user I want to be able to login so that I can book a table. (Must Have)
20. As site user I want to be able to view previous bookings. (Should Have)
21. As site user I want to be able to edit an unconfirmed booking.  (Should Have)
22. As site user I want to be able to cancel a booking. (Should Have)
23. As site user I want to be able to comment on/like a blogpost so that I can communicate what I think of the content. (Should Have)
24. As site user I want to be able to get confirmation of any action I take so that I know it was successfull. (Should Have)

### Epics

<hr>

##### Back to [top](#table-of-contents)

## Design
- GitHub issues was used to track all open user stories
- Epics were created using the milestones feature.
<details>
<img src="docs/agile/user_stories.png">
img src="docs/agile/milestones.png">
</details>

### Colours

For the colour scheme I have selected a set of light colours to represent the open and informal atmosphere of the restaurant.
This also helps distuingish the site from many other sites that often use a darker theme these days.

<details><summary>Original colour palette:</summary>
<img src="docs/colour-scheme.png">
</details>

### Fonts

 Two Google fonts where used across the site:
 1. "Dancing Script" with cursive as fallback.
 2. "Domine" with sans-serif as fallback.

 The fonts where chosen to complement each other and generate a sense of style/class across the site.

 ### Structure

 #### Website pages

 The site was designed to utilize a familiar navigational structure consisting of a navigation bar along the top of the screen
 wich collapses into a "hamburger menu" on smaller screen sizes. These are present across all pages.

 - The site contains the following pages:
    - Homepage with image carousel and image0-links to the menu, booking and blog pages for easy navigation.
    - Food menu listing all currently available starters, mains and desserts.
    - Drinks menu listing all currently available drinks.
    - Bites menu listing all currently available snacks/bites.
    - Blog page listing all published blogs on a single page.
    - Blog detail shows a single blogpost for reading.
    - Booking page allowing users to make a booking and provides a link to a list of all the users previous bookings.
    - Booking list allows users to view bookings.
    - Edit booking allows users to edit any unconfirmed bookings.
    - Cancel booking allows user to cancel a booking and removes it from the database.
    - Contact allows a user to easily send a message to the restauant staff.
    - Sign Up allows the user to create an acount so they can use all the sites features.
    - Login allows users to log in to their acount so they can utilize the sites features.
    - 404 error page to display in the event a 404 error is raised, provides quick link back to homepage.

#### Database

Built using Python and the Django framework, using ElephantSQL for the deployed version.

<details><summary>Database diagram</summary>
<img src="docs/db_models/db_model_overview.png">
</details>

##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

##### FoodItem Model
The FoodItem Model contains the following:
- item_id
- item_name
- item_description
- item_price
- item_category
- item_available

##### DrinkItem Model
The DrinkItem Model contains the following:
- item_id
- item_name
- item_description
- item_price
- item_category
- item_available

##### BitesItem Model
TheBitesItem Model contains the following:
- item_id
- item_name
- item_description
- item_price
- item_category
- item_available

##### Blogpost Model
The Blogpost Model contains the following:
- post_id
- title
- slug
- author
- content
- image
- created_on
- updated-on
- status
- likes

##### Comment Model
The Comment Model contains the following:
- post
- name
- email
- body
- created_on
- approved

##### Booking Model
The Booking Model contains the following:
- booking_id
- created_on
- booking_date
- booking_time
- user
- name
- email
- phone
- booking_status
- nr_of_seats
- nr_of_guests

##### Contact Model
The Contact Model contains the following:
- message_id
- created_on
- user
- name
- email

### Wireframes
The wireframes were created using Balsamiq
<details><summary>Home</summary>
<img src="docs/wireframes/wf_home.png">
</details>
<details><summary>Menu</summary>
<img src="docs/wireframes/wf_menu.png">
</details>
<details><summary>Blog</summary>
<img src="docs/wireframes/wf_blog.png">
</details>
<details><summary>Blog Detail</summary>
<img src="docs/wireframes/wf_blog_detail.png">
</details>
<details><summary>Booking</summary>
<img src="docs/wireframes/wf_booking.png">
</details>
<details><summary>Contact</summary>
<img src="docs/wireframes/wf_contact.png">
</details>
<details><summary>SignUp</summary>
<img src="docs/wireframes/wf_signup.png">
</details>
<details><summary>LogIn</summary>
<img src="docs/wireframes/wf_login.png">
</details>
<br>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [GitPod](https://gitpod.io/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [ElephantSQL](https://www.elephantsql.com/)
- [Summernote](https://summernote.org/)
- [Whitenoise](https://pypi.org/project/whitenoise/)

- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

<hr>

##### Back to [top](#table-of-contents)

## Features

### Logo & Navigation
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- displayed across all pages

<details><summary>images</summary>
<img src="docs/features/navbar/navbar_logged_out.png">
<img src="docs/features/navbar/navbar_logged_in.png">
<img src="docs/features/navbar/navbar_collapsed.png">
</details>
<br>

### Home page
- Includes image carousel, welcome text and image links to: Food menu, Table Booking and Blog.
<details><summary>images</summary>
<img src="docs/features/home/home_carousel.png">
<img src="docs/features/home/home_image_links.png">
</details>
<br>

### Sign up
- Allow users to register an acoount
- Username and password are required
- email is optional
<details><summary>images</summary>
<img src="docs/features/signup/signup.png">
</details>
<br>

### Log In
- User can login to make use of the sites features.(make a booking, edit/cancel a booking, send message, comment/like blogposts)
<details><summary>images</summary>
<img src="docs/features/login_logout/login.png">
</details>
<br>

### Log Out
- User can logout to prevent others from utilizing their account
<details><summary>images</summary>
<img src="docs/features/login_logout/logout.png">
</details>
<br>

### Blog
- Displays all posts made by staff members.
<details><summary>images</summary>
<img src="docs/features/blog/blog_list.png">
</details>
<br>

### Blog Detail
- Displays specific blogpost as selected by user.
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Users that have signed up/logged in can comment on/like the post.
<details><summary>images</summary>
<img src="docs/features/blog/blog_detail.png">
<img src="docs/features/blog/blog_comments.png">
</details>
<br>

### Booking
- Allows registered users to book a table by way of the booking form.
- Form will only submit if all fields are filled out and are valid.
- A message will alert users to incorrectly filled out/empty fields.
- Provides a link to the users booking overview.
- Booking status is displayed.
- If a booking is rejected a message is displayed to the user and link to the contact page is provided.
- Unconfirmed bookings can be edited/cannceled.
- Confirmed bookings can not be edited only canceled.
<details><summary>images</summary>
<img src="docs/features/booking/booking_log_in.png">
<img src="docs/features/booking/booking_new_booking.png">
<img src="docs/features/booking/booking_received.png">
<img src="docs/features/booking/booking_all_my_bookings.png">
<img src="docs/features/booking/booking_edit.png">
<img src="docs/features/booking/booking_cancel.png">
</details>
<br>

### Contact Us
- Registered users can send a message to restaurant staff
- Adress and contact information is displayed.
- Google map is provided
<details><summary>images</summary>
<img src="docs/features/contact/contact_logged_out.png">
<img src="docs/features/contact/contact_new_message.png">
<img src="docs/features/contact/contact_message_sent.png">
<img src="docs/features/contact/contact_info.png">
</details>
<br>

### Food Menu
- Displays all currently available food menu items.
- Menu items can be added by staff via the site's backend.
- Menu item availability can be set via the sites backend.
- Menu items are seperated into "Starters", "Mains" and "Desserts".
<details><summary>images</summary>
<img src="docs/features/menu/food_starters.png">
<img src="docs/features/menu/food_mains.png">
<img src="docs/features/menu/food_desserts.png">
</details>
<br>

### Drinks Menu
- Displays all currently available drink menu items.
- Menu items can be added by staff via the site's backend.
- Menu item availability can be set via the sites backend.
- Menu items are seperated into "Beers", "Wines" and "Non Alchoholic".
<details><summary>images</summary>
<img src="docs/features/menu/drinks_beers.png">
<img src="docs/features/menu/drinks_wines.png">
<img src="docs/features/menu/drinks_nonalc.png">
</details>
<br>

### Bites Menu
- Displays all currently available bites menu items.
- Menu items can be added by staff via the site's backend.
- Menu item availability can be set via the sites backend.
- Menu items are seperated into "Beers", "Wines" and "Non Alchoholic".
<details><summary>images</summary>
<img src="docs/features/menu/bites_veggie.png">
<img src="docs/features/menu/bites_assorted.png">
</details>
<br>

## Validation

The pages files were validated using W3C Markup Validation Service. All pages passed with no errors.

<details><summary>Home</summary>
<img src="docs/validation/html/w3_home.png">
</details>

<details><summary>Food Menu</summary>
<img src="docs/validation/html/w3_food_menu.png">
</details>

<details><summary>Drinks Menu</summary>
<img src="docs/validation/html/w3_drinks_menu.png">
</details>

<details><summary>Bites Menu</summary>
<img src="docs/validation/html/w3_bites_menu.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/html/w3_blog.png">
</details>

<details><summary>Blog Detail</summary>
<img src="docs/validation/html/w3_blog_detail.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/html/w3_booking.png">
</details>

<details><summary>My Bookings</summary>
<img src="docs/validation/html/w3_my_bookings.png">
</details>

<details><summary>Edit Booking</summary>
<img src="docs/validation/html/w3_edit_booking.png">
</details>

<details><summary>Cancel Booking</summary>
<img src="docs/validation/html/w3_cancel_booking.png">
</details>

<details><summary>Contact</summary>
<img src="docs/validation/html/w3_contact.png">
</details>

<details><summary>Message Sent</summary>
<img src="docs/validation/html/w3_contact.png">
</details>

<details><summary>Sign Up</summary>
<img src="docs/validation/html/w3_signup.png">
</details>

<details><summary>Log In</summary>
<img src="docs/validation/html/w3_login.png">
</details>

<details><summary>Log Out</summary>
<img src="docs/validation/html/w3_logout.png">
</details>

### CSS Validation
CSS was validated using the W3C Jigsaw CSS Validation Service. No errors reported.

<details><summary>style.css</summary>
<img src="docs/validation/css/w3_style.png">
</details>

### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle. No errors were reported.

<hr><summary>Home</summary><hr>
<details><summary>admin.py</summary>
<img src="docs/validation/pep8/home/home_admin.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/home/home_urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8/home/home_views.png">
</details>

<hr><summary>Menu</summary><hr>
<details><summary>admin.py</summary>
<img src="docs/validation/pep8/menu/menu_admin.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/menu/menu_urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8/menu/menu_views.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8/menu/menu_models.png">
</details>

<hr><summary>Blog</summary><hr>
<details><summary>admin.py</summary>
<img src="docs/validation/pep8/blog/blog_admin.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/blog/blog_urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8/blog/blog_views.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8/blog/blog_models.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8/blog/blog_forms.png">
</details>

<hr><summary>Booking</summary><hr>
<details><summary>admin.py</summary>
<img src="docs/validation/pep8/booking/booking_admin.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/booking/booking_urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8/booking/booking_views.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8/booking/booking_models.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8/booking/booking_forms.png">
</details>

<hr><summary>Contact</summary><hr>
<details><summary>admin.py</summary>
<img src="docs/validation/pep8/contact/contact_admin.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/contact/contact_urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8/contact/contact_views.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8/contact/contact_models.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8/contact/contact_forms.png">
</details>

<hr><summary>Project</summary><hr>
<details><summary>manage.py</summary>
<img src="docs/validation/pep8/project/project_manage.png">
</details>
<details><summary>settings.py</summary>
<img src="docs/validation/pep8/project/project_settings.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8/project/project_urls.png">
</details>

### WAVE TESTING
The following pages were tested with WAVE
No errors were reported.

<details><summary>Home</summary>
<img src="docs/validation/wave/wave_home.png">
</details>
<br>
<details><summary>Food Menu</summary>
<img src="docs/validation/wave/wave_food_menu.png">
</details>
<details><summary>Drinks Menu</summary>
<img src="docs/validation/wave/wave_drinks_menu.png">
</details>
<details><summary>Bites Menu</summary>
<img src="docs/validation/wave/wave_bites_menu.png">
</details>
<br>
<details><summary>Blog</summary>
<img src="docs/validation/wave/wave_blog.png">
</details>
<details><summary>Blog Detail</summary>
<img src="docs/validation/wave/wave_blog_detail.png">
</details>
<br>
<details><summary>Booking Login</summary>
<img src="docs/validation/wave/wave_booking_login.png">
</details>
<details><summary>Booking New</summary>
<img src="docs/validation/wave/wave_booking_new.png">
</details>
<details><summary>Booking List</summary>
<img src="docs/validation/wave/wave_booking_list.png">
</details>
<details><summary>Booking Edit</summary>
<img src="docs/validation/wave/wave_booking_edit.png">
</details>
<details><summary>Booking Cancel</summary>
<img src="docs/validation/wave/wave_booking_cancel.png">
</details>
<br>
<details><summary>Contact Login</summary>
<img src="docs/validation/wave/wave_contact_login.png">
</details>
<details><summary>Contact</summary>
<img src="docs/validation/wave/wave_contact.png">
</details>
<details><summary>Contact Sent</summary>
<img src="docs/validation/wave/wave_contact_sent.png">
</details>
<br>
<details><summary>SignUp</summary>
<img src="docs/validation/wave/wave_signup.png">
</details>
<details><summary>Login</summary>
<img src="docs/validation/wave/wave_login.png">
</details>
<details><summary>Login</summary>
<img src="docs/validation/wave/wave_logout.png">
</details>
<br>

### LIGHTHOUSE TESTING

The following pages performance was tested with Lighthouse

<details><summary>Home</summary>
<img src="docs/validation/lighthouse/lighthouse_home.png">
</details>
<details><summary>Menu</summary>
<img src="docs/validation/lighthouse/lighthouse_menu.png">
</details>
<details><summary>Blog</summary>
<img src="docs/validation/lighthouse/lighthouse_blog.png">
</details>
<details><summary>Blog Detail</summary>
<img src="docs/validation/lighthouse/lighthouse_blog_detail.png">
</details>
<details><summary>Booking</summary>
<img src="docs/validation/lighthouse/lighthouse_booking.png">
</details>
<details><summary>Booking List</summary>
<img src="docs/validation/lighthouse/lighthouse_booking_list.png">
</details>
<details><summary>Contact</summary>
<img src="docs/validation/lighthouse/lighthouse_contact.png">
</details>
<details><summary>SignUp</summary>
<img src="docs/validation/lighthouse/lighthouse_signup.png">
</details>
<details><summary>LogIn</summary>
<img src="docs/validation/lighthouse/lighthouse_login.png">
</details>
<details><summary>LogOut</summary>
<img src="docs/validation/lighthouse/lighthouse_logout.png">
</details>

<br>

##### Back to [top](#table-of-contents)<hr>

## Testing

### user story testing

1. As site owner I want the site to be fully responsive so that I can provide a good user experience.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|All pages|view site on various screens|site adapts|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_1a.png">
<img src="docs/user_stories/user_story_1b.png">
<img src="docs/user_stories/user_story_1c.png">
</details>

2. As site owner I want to provide a contact page so that users can find/contact the restaurant easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Contact Page|click contact link|find contact page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_2.png">
</details>

3. As site owner I want users to be able to view the menu so that they can easily decide wether or not to book with us.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Menu Page|click menu link|find menu page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_3.png">
</details>

4. As site owner I want users to be able to book a table online.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Booking Page|click booking link|find booking page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_4.png">
</details>

4. As site owner I want users to be able to book a table online.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Booking Page|click booking link|find booking page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_4.png">
</details>

5. as site owner I want to be able to maintain a blog so that users can be informed about the goings on in the restaurant.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Blog Page|click blog link|find booking page|Works as expected|
|Admin Panel|navigate to admin panel|find blog entry section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_5a.png">
<img src="docs/user_stories/user_story_5b.png">
</details>

6. As site admin I want to be able to login so that I can acces the backend of the site.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find login page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_6.png">
<img src="docs/user_stories/acces_admin.png">
</details>

7. As site admin I want to be able to view/make changes to the menus so that I can keep it up to date.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find menu sections|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_7.png">
</details>

8. As site admin I want to be able confirm or reject a booking so that I can avoid double bookings.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find bookings section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_8a.png">
<img src="docs/user_stories/user_story_8b.png">
</details>

9. As site admin I want to be able to manually enter a booking so that I can book a table in response to a user's phonecall or email.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find bookings section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_9.png">
</details>

10. As site admin I want to be able to post articles to the blog so that I can maintain customer communication.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find blog section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_10a.png">
<img src="docs/user_stories/user_story_10b.png">
</details>

11. As site admin I want to be able to approve blog-comments so that I can make sure nothing innaprorpiate is displayed.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find comments section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_11a.png">
<img src="docs/user_stories/user_story_11b.png">
</details>

12. As site admin I want to be able to filter bookings by date so that I can see wich bookings we have for a particular day.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find bookings section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_12.png">
</details>

13. As site admin I want to be able to add a registered user to "staff" so they can acces the site's backend.  (Must Have)
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Admin Panel|navigate to admin panel|find Users Section section|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/change_user_role_a.png">
<img src="docs/user_stories/change_user_role_b.png">
<img src="docs/user_stories/change_user_role_c.png">
</details>


14. As site user I want to be able to easily navigate the site to find the information I am looking for.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Navigation Bar|Click apropriate link|find expected page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_13a.png">
<img src="docs/user_stories/user_story_13b.png">
<img src="docs/user_stories/user_story_13c.png">
<img src="docs/user_stories/user_story_13d.png">
<img src="docs/user_stories/user_story_13e.png">
<img src="docs/user_stories/user_story_13f.png">
<img src="docs/user_stories/user_story_13g.png">
</details>

15. As site user I want to be able to view the menu.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Navigation Bar|Click apropriate link|find menu page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_13b.png">
</details>

16. As site user I want to be able to easily contact the restaurant.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Navigation Bar|Click apropriate link|find contact page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_13e.png">
</details>

17. As site user I want to be able to be able to see the restaurants opening times and location.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Contact Page|Scroll down|find adress & info|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_16.png">
</details>

18. As site user I want to be able to get a sense of the atmosphere in the restaurant.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Home Page|Open Site|see carousel|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_17a.png">
<img src="docs/user_stories/user_story_17b.png">
<img src="docs/user_stories/user_story_17c.png">
</details>

19. As site user I want to be able to login so that I can book a table.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Login Page|Navigate to login|Find login page|Works as expected|
|Booking Page|Navigate to booking|Find booking page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_13f.png">
<img src="docs/user_stories/user_story_13d.png">
</details>

20. As site user I want to be able to view previous bookings. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Booking Page|Navigate to booking|Find my bookings link|Works as expected|
|My Bookings Page|click my bookings link|Find my bookings list|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_19a.png">
<img src="docs/user_stories/user_story_19b.png">
</details>

21. As site user I want to be able to edit an unconfirmed booking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|My Bookings Page|click edit button|Find edit form|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_20.png">
</details>

22. As site user I want to be able to cancel a booking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|My Bookings Page|click cancel button|Find cancel page|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_21.png">
</details>

23. As site user I want to be able to comment on/like a blogpost so that I can communicate what I think of the content.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Blog Detail Page|click heart|post is liked|Works as expected|
|Blog Detail Page|post comment|comment is submitted for approval|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_22a.png">
<img src="docs/user_stories/user_story_22b.png">
</details>

24. As site user I want to be able to get confirmation of any action I take so that I know it was successfull.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Popup message|take perform user action|message is displayed|Works as expected|

<details><summary>images</summary>
<img src="docs/user_stories/user_story_23.png">
</details>

### Browser compatibility

The website was tested for functionality in the following browsers:

|**Browser**|**Result**|
|-----------|----------|
|Edge | working|
|Internet Explorer | working|
|FireFox | working|
|Opera|working|
|Safari|working|

### Real World Devices

The Site has been tested on the following real world devices:

|**Browser**|**Result**|
|-----------|----------|
|Samsung Galaxy A01|working|
|Standard Windows 10 Desktop PC|working|
|Asus Laptop|working|

##### Back to [top](#table-of-contents)<hr>

### Heroku Deployment

This application has been deployed from Github using Heroku using the following steps.

1. Create an acount at heroku.com.
<details>
<img src="docs/deployment/heroku_signup.png">
</details>
<br>

2. Create a new app, give it an apropriate name and select your region.
<details>
<img src="docs/deployment/heroku_new_app_a.png">
<img src="docs/deployment/heroku_new_app_b.png">
</details>
<br>

3. Create an acount at elephantSQL.com and login.
<details>
<img src="docs/deployment/elephant_login.png">
</details>
<br>

4. Click "Create New Instance".
<details>
<img src="docs/deployment/elephant_new_instance.png">
</details>
<br>

5. Select a plan, set your region, review your settings and confirm.
<details>
<img src="docs/deployment/elephant_select_plan.png">
<img src="docs/deployment/elephant_region.png">
<img src="docs/deployment/elephant_review.png">
</details>
<br>

5. Open your new instance and in the details section copy the database url.
<details>
<img src="docs/deployment/elephant_open.png">
<img src="docs/deployment/elephant_details.png">
</details>
<br>

6. Return to your heroku app. Under the "settings" click "reveal config vars".
<details>
<img src="docs/deployment/heroku_show_configvars.png">
</details>
<br>

7. Add a new CONFIG VAR with thew following content:
- KEY: DATABASE_URL
- VALUE: "paste the database url you just copied here."
<details>
<img src="docs/deployment/heroku_empty_var.png">
<img src="docs/deployment/heroku_add_elephant.png">
</details>
<br>

8. Create an acount at cloudinary.com and navigate to the dashboard.
<br>
9. From the dashboard copy the cloudinary-url.
<details>
<img src="docs/deployment/cloudinary_dashboard.png">
</details>
<br>

10. Go back to your heroku app and add a new CONFIG VAR with thew following content:
- KEY: CLOUDINARY_URL
- VALUE: "paste the database url you just copied here."
<details>
<img src="docs/deployment/heroku_add_cloudinary.png">
</details>
<br>

11. Add the following KEY/VALUE pairs to your heroku apps "config vars":
- KEY: PORT
- VALUE: 8000
<br>
- KEY: SECRET_KEY
- VALUE: any_string_you_want
<details>
<img src="docs/deployment/heroku_final_vars.png">
</details>
<br>

13. Navigate to your heroku app's deploy tab and select GitHub as your deployment method.
    Then search for your repository.
<details>
<img src="docs/deployment/heroku_deploy_method.png">
</details>
<br>

14. Scroll down to the bottom of the page and click "deploy branch".
<details>
<img src="docs/deployment/heroku_deploy.png">
</details>
<br>

15. Once the build is complete click "view".
<details>
<img src="docs/deployment/heroku_open_app.png">
</details>
<br>

### Fork Repository
You can fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

### Credits

### Images

Images used were sourced from Unsplash.com.
Blog articles used were sourced from "Resell Rights Weekly"

### Code

Bootstrap navbar, carousel and classes were used.

### Acknowledgements

## Acknowledgements
I would like to take the opportunity to thank:
- My mentor Mo Shami for his feedback, advice, guidance and support.
- My partner Geertje van der Zalm for her support, inspiration and patience.
- My mother Anne Rijsdijk and her husband Mickel Pereira for helping me persue this dream.
- Anyone who spends time on the internet making tutorials, awnsering questions or otherwise helping others to learn.

[Back to Table Of Contents](#table-of-contents)