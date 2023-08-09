# User Stories

## Users

### Sign Up

* As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
  * When I'm on the `/signup` page:
    * I would like to be able to enter my email, username, and preferred password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the sign-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
    * So that I can try again without needing to refill forms I entered valid data into.

### Log in

* As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
  * When I'm on the `/login` page:
    * I would like to be able to enter my email and password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the lob-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the log-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
      * So that I can try again without needing to refill forms I entered valid data into.

### Demo User

* As an unregistered and unauthorized user, I would like an easy to find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
  * When I'm on either the `/signup` or `/login` pages:
    * I can click on a Demo User button to log me in and allow me access as a normal user.
      * So that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out

* As a logged in user, I want to log out via an easy to find log out button on the navigation bar.
  * While on any page of the site:
    * I can log out of my account and be redirected to a page displaying the home page.
      * So that I can easily log out to keep my information secure.

## Films
* As a logged in _or_ logged out user, I want to be able to view a selection of the most recent films.
  * When I'm on the `/films` page:
    * I can view recently added films.
      * So that I can discover and read about films.

* As a logged in _or_ logged out user, I want to be able to view a specific film and its associated people.
  * When I'm on the `/films/:id` page:
    * I can view the content of the film, as well as the associated cast and crew.
      * So that I can read about films.

### Updating films

* As a logged in user, I want to be able to edit my films by clicking an Edit button associated with the film on the profile page.
  * When I'm on the `/profile` pages:
    * I can click "Edit" to make permanent changes to the films I have created.
      * So that I can fix any errors I make in my films.

### Deleting films

* As a logged in user, I want to be able to delete my films by clicking a Delete button associated with the film on the profile page.
  * When I'm on the `/profile` pages:
    * I can click "Delete" to permanently delete an film I have posted.
      * So that when I realize I have an error in my film, I can easily remove it.

## people

### Create people
** As a logged in user, I want to be able to add new people.
  * When I'm on the `/people/add` page:
    * I can create and submit a new person.
      * So that users can learn about cast and crewmembers.

### Viewing people

* As a logged in _or_ logged out user, I want to be able to view a details about a person.
  * When I'm on the `/people:id` page:
    * I can view details about a person.
      * So that users can learn about cast and crewmembers.

### Updating people

* As a logged in user, I want to be able to edit my people by clicking an Edit button associated with the person on the profile page.
  * When I'm on the `/profile` page:
    * I can click "Edit" to make permanent changes to the people I have created.
      * So that I can fix any errors I make in my person.


### Deleting people

* As a logged in user, I want to be able to delete my people by clicking a Delete button associated with the person on the user profile page.
  * When I'm on the `/profile` page:
    * I can click "Delete" to permanently delete a person I have posted.
      * So that when I realize I have an error in my person, I can easily remove it.

## Seen

### Mark a film as seen
** As a logged in user, I want to be able to mark a film as seen, anywhere films are displayed.
  * When I'm on the `/films`, `/films/:id`, and home page:
    * I can mark a film as seen
      * So that I can catalogue which films I've seen.


### Viewing Likes

* As a logged in _or_ logged out user, I want to be able to view the number of likes for any film.
  * When I'm on the `/films` page:
    * I can view the number of likes.

* As a logged in user, I want to be able to view if I have liked a film.
  * When I'm on the `/films`, `/films/:id`, and home page:
