Feature: Login Access
  As a user, I want to log in to the website to access jubelio account.

Scenario: Successful login
  Given Im at the sign-in page
  When I enter valid email and password
  And I click the login button
  Then I should be redirected to my jubelio home page

Scenario: Empty Credentials
  Given Im at the sign-in page
  When I leave the login credentials empty and click on the login button
  Then I should not be logged in and should receive an error message

