# Wine & Vinegar | Restaurant

![Am I Responsive](docs/am-i-responsive.webp)

**Developer: Gustaaf Milzink**

[Visit live website](https://ci-pp4-rbs.herokuapp.com/)


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

1. As site owner I want the site to be fully responsive so that I can provide a good user experience.
2. As site owner I want to provide a contact page so that users can find/contact the restaurant easily.
3. As site owner I want users to be able to view the menu so that they can easily ddecide wether or not to book with us.
4. As site owner I want users to be able to book a table online.
5. as site owner I want to be able to maintain a blog so that users can be informed about the goings on in the restaureant.

### Admin

6. As site admin I want to be able to login so that I can acces the backend of the site.
7. As site admin I want to be able to view/make changes to the menus so that I can keep it up to date.
8. As site admin I want to be able confirm or reject a booking so that I can avoid double bookings.
9. As site admin I want to be able to manually enter a booking so that I can book a table in response to a user's phonecall or email.
10. As site admin I want to be able to post articles to the blog so that I can maintain customer communication.
11. As site admin I want to be able to approve blog-comments so that I can make sure nothing innaprorpiate is displayed.
12. As site admin I want to be able to filter bookings by date so that I can see wich bookings we have for a partivular day.

### Users

13. As site user I want to be able to easily navigate the site to find the information I am looking for.
14. As site user I want to be able to view the menu.
15. As site user I want to be able to easily contact the restaurant.
16. As site user I want to be able to be able to see the restaurants opening times and location.
17. As site user I want to be able to get a sense of the atmosphere in the restaurant.
18. As site user I want to be able to login so that I can book a table.
19. As site user I want to be able to view previous bookings. 
20. As site user I want to be able to edit an unconfirmed booking.
21. As site user I want to be able to cancel an unconfirmed booking.
22. As site user I want to be able to comment on/like a blogpost so that I can communicate what I think of the content.
23. As site user I want to be able to get confirmation of any action I take so that I know it was successfull.

### Epics

<hr>

##### Back to [top](#table-of-contents)

## Design

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