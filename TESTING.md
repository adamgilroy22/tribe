# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

As my project uses Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}`
it will not validate properly if I copy and paste into the HTML validator straight from my source files.

Usually in order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, nearly all of the pages on this site require a user to be logged-in and authenticated,
and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to the pages.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2F) | ![screenshot](documentation/testing/html-validation-home.png) | Pass: No Errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/html-validation-sign-up.png) | Pass: No Errors |
| Log In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/html-validation-sign-in.png) | Pass: No Errors |
| Forgot Password | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F) | ![screenshot](documentation/testing/html-validation-forgot-password.png) | Pass: No Errors |
| Following Feed | n/a | ![screenshot](documentation/testing/html-validation-feed.png) | Pass: No Errors |
| All Posts Feed | n/a | ![screenshot](documentation/testing/html-validation-all-posts-feed.png) | Pass: No Errors |
| Messaging Inbox | n/a | ![screenshot](documentation/testing/html-validation-inbox.png) | Pass: No Errors |
| Messaging Thread | n/a | ![screenshot](documentation/testing/html-validation-message-thread.png) | Pass: No Errors |
| Create Thread | n/a | ![screenshot](documentation/testing/html-validation-create-thread.png) | Pass: No Errors |
| User Profile | n/a | ![screenshot](documentation/testing/html-validation-user-profile.png) | Pass: No Errors |
| Other Profile | n/a | ![screenshot](documentation/testing/html-validation-other-profile.png) | Pass: No Errors |
| Edit Profile | n/a | ![screenshot](documentation/testing/html-validation-edit-profile.png) | Pass: No Errors |
| Followers List | n/a | ![screenshot](documentation/testing/html-validation-followers-list.png) | Pass: No Errors |
| Individual Post | n/a | ![screenshot](documentation/testing/html-validation-individual-post.png) | Pass: No Errors |
| Delete Post | n/a | ![screenshot](documentation/testing/html-validation-delete-post.png) | Pass: No Errors |
| Edit Comment | n/a | ![screenshot](documentation/testing/html-validation-edit-comment.png) | Pass: No Errors |
| Delete Comment | n/a | ![screenshot](documentation/testing/html-validation-delete-comment.png) | Pass: No Errors |
| Admin Panel | n/a | ![screenshot](documentation/testing/html-validation-admin-panel.png) | Pass: No Errors |
| Search | n/a | ![screenshot](documentation/testing/html-validation-search.png) | Pass: No Errors |
| Sign Out | n/a | ![screenshot](documentation/testing/html-validation-sign-out.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file. On the first test, the validator threw an issue on line 231 of my CSS file saying that 0.3s is not a transform value. This alerted me to a typo in my CSS where I should have put transition instead of transform. I fixed this error and on my second validation test, no errors were thrown.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftribe.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/css-validation-1.png) | Fail: 0.3s is not a transform value |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftribe.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/css-validation-2.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| message.js | ![screenshot](documentation/testing/js-validation-messages.png) | Undefined variable Bootstrap |
| notifications.js | ![screenshot](documentation/testing/js-validation-notifications.png) | Unused variables showNotification removeNotification (Used in notifications.html) |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/tribe/settings.py) | ![screenshot](documentation/testing/py-validation-settings.png) | Pass: No Errors |
| urls.py (main) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/tribe/urls.py) | ![screenshot](documentation/testing/py-validation-main-urls.png) | Pass: No Errors |
| forms.py (comments) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/comments/forms.py) | ![screenshot](documentation/testing/py-validation-comments-forms.png) | Pass: No Errors |
| models.py (comments) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/comments/models.py) | ![screenshot](documentation/testing/py-validation-comments-models.png) | Pass: No Errors |
| urls.py (home) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/home/urls.py) | ![screenshot](documentation/testing/py-validation-home-urls.png) | Pass: No Errors |
| views.py (home) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/home/views.py) | ![screenshot](documentation/testing/py-validation-home-views.png) | Pass: No Errors |
| forms.py (messaging) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/messaging/forms.py) | ![screenshot](documentation/testing/py-validation-messaging-forms.png) | Pass: No Errors |
| models.py (messaging) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/messaging/models.py) | ![screenshot](documentation/testing/py-validation-messaging-models.png) | Pass: No Errors |
| urls.py (messaging) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/messaging/urls.py) | ![screenshot](documentation/testing/py-validation-messaging-urls.png) | Pass: No Errors |
| views.py (messaging) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/messaging/views.py) | ![screenshot](documentation/testing/py-validation-messaging-views.png) | Pass: No Errors |
| models.py (notifications) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/notifications/models.py) | ![screenshot](documentation/testing/py-validation-notifications-models.png) | Pass: No Errors |
| urls.py (notifications) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/notifications/urls.py) | ![screenshot](documentation/testing/py-validation-notifications-urls.png) | Pass: No Errors |
| views.py (notifications) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/notifications/views.py) | ![screenshot](documentation/testing/py-validation-notifications-views.png) | Pass: No Errors |
| forms.py (posts) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/posts/forms.py) | ![screenshot](documentation/testing/py-validation-posts-forms.png) | Pass: No Errors |
| models.py (posts) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/posts/models.py) | ![screenshot](documentation/testing/py-validation-posts-models.png) | Pass: No Errors |
| urls.py (posts) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/posts/urls.py) | ![screenshot](documentation/testing/py-validation-posts-urls.png) | Pass: No Errors |
| views.py (posts) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/posts/views.py) | ![screenshot](documentation/testing/py-validation-posts-views.png) | Pass: No Errors |
| models.py (profiles) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/profiles/models.py) | ![screenshot](documentation/testing/py-validation-profiles-models.png) | Pass: No Errors |
| urls.py (profiles) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/profiles/urls.py) | ![screenshot](documentation/testing/py-validation-profiles-urls.png) | Pass: No Errors |
| views.py (profiles) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/profiles/views.py) | ![screenshot](documentation/testing/py-validation-profiles-views.png) | Pass: No Errors |
| urls.py (search) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/search/urls.py) | ![screenshot](documentation/testing/py-validation-search-urls.png) | Pass: No Errors |
| views.py (search) | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/adamgilroy22/tribe/main/search/views.py) | ![screenshot](documentation/testing/py-validation-search-views.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsive-mobile.png) ![screenshot](documentation/testing/responsive-mobile-menu.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsive-tablet.png) ![screenshot](documentation/testing/responsive-tablet-menu.png) | Works as expected |
| Laptop | ![screenshot](documentation/testing/responsive-laptop.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/responsive-desktop.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/testing/lighthouse-home-desktop.png) | No major warnings |
| Home | Mobile | ![screenshot](documentation/testing/lighthouse-home-mobile.png) | Some minor warnings |
| Sign Up | Desktop | ![screenshot](documentation/testing/lighthouse-sign-up-desktop.png) | No major warnings |
| Sign Up | Mobile | ![screenshot](documentation/testing/lighthouse-sign-up-mobile.png) | Some minor warnings |
| Sign In | Desktop | ![screenshot](documentation/testing/lighthouse-sign-in-desktop.png) | No major warnings |
| Sign In | Mobile | ![screenshot](documentation/testing/lighthouse-sign-in-mobile.png) | Some minor warnings |
| Forgot Password | Desktop | ![screenshot](documentation/testing/lighthouse-forgot-password-desktop.png) | No major warnings |
| Forgot Password | Mobile | ![screenshot](documentation/testing/lighthouse-forgot-password-mobile.png) | Some minor warnings |
| Following Feed | Desktop | ![screenshot](documentation/testing/lighthouse-following-feed-desktop.png) | No major warnings |
| Following Feed | Mobile | ![screenshot](documentation/testing/lighthouse-following-feed-mobile.png) | No major warnings |
| All Posts Feed | Desktop | ![screenshot](documentation/testing/lighthouse-all-posts-feed-desktop.png) | No major warnings |
| All Posts Feed | Mobile | ![screenshot](documentation/testing/lighthouse-all-posts-feed-mobile.png) | Some minor warnings |
| Messages Inbox | Desktop | ![screenshot](documentation/testing/lighthouse-inbox-desktop.png) | No major warnings |
| Messages Inbox | Mobile | ![screenshot](documentation/testing/lighthouse-inbox-mobile.png) | No major warnings |
| Messages Thread | Desktop | ![screenshot](documentation/testing/lighthouse-message-desktop.png) | No major warnings |
| Messages Thread | Mobile | ![screenshot](documentation/testing/lighthouse-message-mobile.png) | Some minor warnings |
| Create Thread | Desktop | ![screenshot](documentation/testing/lighthouse-create-message-desktop.png) | No major warnings |
| Create Thread | Mobile | ![screenshot](documentation/testing/lighthouse-create-message-mobile.png) | No major warnings |
| User Profile | Desktop | ![screenshot](documentation/testing/lighthouse-profile-desktop.png) | Some warnings - image sizes |
| User Profile | Mobile | ![screenshot](documentation/testing/lighthouse-profile-mobile.png) | No major warnings |
| Other Profile | Desktop | ![screenshot](documentation/testing/lighthouse-other-profile-desktop.png) | No major warnings |
| Other Profile | Mobile | ![screenshot](documentation/testing/lighthouse-other-profile-mobile.png) | Some warnings - image sizes |
| Admin Panel | Desktop | ![screenshot](documentation/testing/lighthouse-admin-panel-desktop.png) | No major warnings |
| Admin Panel | Mobile | ![screenshot](documentation/testing/lighthouse-admin-panel-mobile.png) | No major warnings |
| Search | Desktop | ![screenshot](documentation/testing/lighthouse-search-desktop.png) | No major warnings |
| Search | Mobile | ![screenshot](documentation/testing/lighthouse-search-mobile.png) | No major warnings |
| Sign Out | Desktop | ![screenshot](documentation/testing/lighthouse-sign-out-desktop.png) | No major warnings |
| Sign Out | Mobile | ![screenshot](documentation/testing/lighthouse-sign-out-mobile.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| **Home Page** | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| **Sign Up** | | | | |
| | Click on Sign Up button on home page | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Sign Up button on sign up page | Redirects user to feed | Pass | |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| **Log In** | | | | |
| | Click on the Login button on home page | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button on login page | Redirects user to feed | Pass | |
| | Click Forgot Password | Redirects user to password reset page | Pass | |
| **Password Reset** | | | | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Click Reset Password button | Sends email with instructions to reset password | Pass | |
| **Log Out** | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| **Own Profile** | | | | |
| | Click on Profile button in nav | User will be redirected to their Profile page | Pass | |
| | Click on the Edit icon | User will be redirected to the edit profile page | Pass | |
| | Click on the Back To Feed button | User will be redirected to their feed | Pass | |
| | Click on followers | User will be redirected to followers list page | Pass | |
| | Click on a post | User will be redirected to the individual post page | Pass | |
| | Click delete icon on own post | User is redirected to post delete confirmation page | Pass | |
| | Type text into the add a post form and click send | New post is created by the user | Pass | |
| | Click send on new post form without adding content | User is prompted to enter something into the field before sending | Pass | |
| **Other Profile** | | | | |
| | Click on the follow button | User will follow current profile they're on and button will change to say unfollow | Pass | Profile owner receives a notification letting them know someone has followed them and followers count will increase by 1 |
| | Click on the unfollow button | User will unfollow current profile they're on and button will change to say follow | Pass | Followers count will decrease by 1 |
| | Click on the Back To Feed button | User will be redirected to their feed | Pass | |
| | Click on followers | User will be redirected to followers list page | Pass | |
| | Brute forcing the URL to edit another user's profile | User should be given an error | Pass | Redirects user to error page |
| | Click on a post | User will be redirected to the individual post page | Pass | |
| **Following Feed** | | | | |
| | Click on a post | User will be redirected to the individual post page | Pass | |
| | Click on the username on a post | User will be redirected to the post author's profile | Pass | |
| | Click the like button on a post | Like button will fill with colour and the like count will increase by 1 | Pass | Post author receives a notification letting them know someone has liked their post |
| | Click the like button on a post already liked by the user | Like button will become clear in the middle like count will decrease by 1 | Pass | |
| | Click flag button | Message appears telling the user the post has been reported | Pass | Post is added to the Admin Panel page for admins to review |
| | Type text into the add a post form and click send | New post is created by the user | Pass | |
| | Click send on new post form without adding content | User is prompted to enter something into the field before sending | Pass | |
| | Click delete icon on own post | User is redirected to post delete confirmation page | Pass | |
| | Brute forcing the URL to delete another user's post | User should be given an error | Pass | Redirects user to error page |
| | Click All Posts button | User is redirected to feed containing all posts from every user on the website | Pass | |
| **All Posts Feed** | | | | |
| | Click on a post | User will be redirected to the individual post page | Pass | |
| | Click on the username on a post | User will be redirected to the post author's profile | Pass | |
| | Click the like button on a post | Like button will fill with colour and the like count will increase by 1 | Pass | Post author receives a notification letting them know someone has liked their post |
| | Click the like button on a post already liked by the user | Like button will become clear in the middle like count will decrease by 1 | Pass | |
| | Click flag button | Message appears telling the user the post has been reported | Pass | Post is added to the Admin Panel page for admins to review |
| | Type text into the add a post form and click send | New post is created by the user | Pass | |
| | Click send on new post form without adding content | User is prompted to enter something into the field before sending | Pass | |
| | Click delete icon on own post | User is redirected to post delete confirmation page | Pass | |
| | Brute forcing the URL to delete another user's post | User should be given an error | Pass | Redirects user to error page |
| | Click Following button | User is redirected to feed containing posts only from users they have followed | Pass | |
| **Individual Post Page** | | | | |
| | Click on the username on the post | User will be redirected to the post author's profile | Pass | |
| | Click on the Back To Feed button | User will be redirected to their feed | Pass | |
| | Click the like button on the post | Like button will fill with colour and the like count will increase by 1 | Pass | Post author receives a notification letting them know someone has liked their post |
| | Click the like button on the post if already liked by the user | Like button will become clear in the middle like count will decrease by 1 | Pass | |
| | Click flag button | Message appears telling the user the post has been reported | Pass | Post is added to the Admin Panel page for admins to review |
| | Click delete icon on own post | User is redirected to post delete confirmation page | Pass | |
| | Brute forcing the URL to delete another user's post | User should be given an error | Pass | Redirects user to error page |
| | Type text into Leave Your Reply form and click Send | Comment is created under current post | Pass | Post author will receive a notification to tell them they have a new comment on their post |
| **Delete Post Page** | | | | |
| | Click on the Delete button | Post will be permanently deleted | Pass | |
| | Click on the Back To Post button | User will be redirected to the original post | Pass | |
| **Comments** | | | | |
| | Click on the username on a comment | User will be redirected to the comment author's profile | Pass | |
| | Click the like button on a comment | Like button will fill with colour and the like count will increase by 1 | Pass | Comment author receives a notification letting them know someone has liked their comment |
| | Click the like button on the comment if already liked by the user | Like button will become clear in the middle like count will decrease by 1 | Pass | |
| | Click delete icon on own comment or comment on own post | User is redirected to comment delete confirmation page | Pass | |
| | Brute forcing the URL to delete another user's comment if not on your post | User should be given an error | Pass | Redirects user to error page |
| | Click edit icon on own comment | User is redirected to comment edit page | Pass | |
| | Brute forcing the URL to edit another user's comment | User should be given an error | Pass | Redirects user to error page |
| **Delete Comment Page** | | | | |
| | Click on the Delete button | Comment will be permanently deleted | Pass | |
| | Click on the Back To Post button | User will be redirected to the original post | Pass | |
| **Edit Comment Page** | | | | |
| | Fill in comment form and click submit | Original comment will be edited | Pass | |
| | Click on the Back To Post button | User will be redirected to the original post | Pass | |
| **Error Page** | | | | |
| | Click on Back To Your Tribe button | User will be redirected to their feed | Pass | |
| **Inbox** | | | | |
| | Click on Messages button in nav | User will be redirected to their inbox | Pass | |
| | Click on New Conversation button | User will be redirected to the create message thread page | Pass | |
| | Click on any previos message threads | User will be redirected to relevant thread | Pass | |
| **Create Thread** | | | | |
| | Type valid username into form and click continue | User will be redirected message thread with username they typed | Pass | If a thread already exists, they will be brought to that and if not a new thread will be created between the two users |
| | Type an invalid username into form and click continue | Message will appear letting user know that username doesn't exist | Pass | |
| | Click continue without entering anything into form | User will be asked to enter something into the form before continuing | Pass | |
| | Click Back to Inbox button | User will be redirected to their inbox | Pass | |
| **Message Thread** | | | | |
| | Type text into form and click Send Message | Content in form will be sent to the other user as a message | Pass | Other user will receive a notification to tell them they have a new message |
| | Click on other user's name | User will be redirected to other user's profile | Pass | |
| **Search Page** | | | | |
| | Type text into search form into nav and click the search icon | User is directed to a page with a list of both users and posts containing their search query | Pass | If there are no users and/or posts containing the query the page will let the user know there was no results in either or both for their query |
| | Click on user's name in either user or post list | User will be redirected to other user's profile | Pass | |
| **Admin Panel** | | | | |
| | Click on Admin Panel button in nav | User will be redirected to the Admin Panel page with a list of flagged posts | Pass | Admin Panel button only appears on the nav if the logged in user is an admin |
| | Brute forcing the URL to access Admin Panel as a regular user | User should be given an error | Pass | Redirects user to error page |
| | Click delete icon on post in list | User is redirected to post delete confirmation page | Pass | Admin's are able to delete any post on the site regardless of if they are the author or not |
| | Click flag button | Message appears telling the user the post has been unflagged and the post is removed from the admin panel page | Pass | Only admins can unflag a post, if a regular user clicks the flag on an already reported post they will get the post flagged message but nothing else will happen as the post will already be in the admin panel |
| | Click on user's name on post | User will be redirected to other user's profile | Pass | |

## User Story Testing

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Coverage | Screenshot |
| --- | --- | --- | --- |
| 1 passed | 16 passed | 55% | ![screenshot](documentation/js-test-coverage.png) |
| x | x | x | repeat for all remaining tests |

#### Jest Test Issues

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

## Bugs

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/adamgilroy22/tribe/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/adamgilroy22/tribe/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/adamgilroy22/tribe/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/adamgilroy22/tribe/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/adamgilroy22/tribe/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/adamgilroy22/tribe/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/adamgilroy22/tribe/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/adamgilroy22/tribe/issues/5) | Open |

## Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

There are no remaining bugs that I am aware of.