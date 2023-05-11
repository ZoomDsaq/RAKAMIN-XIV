Feature: Manage a goods stock.
  As a user, I want to manage my goods stock.

Scenario: Adding stocks
  Given Im at the home page
  When Im at the homepage, I click the Akunting menu and the Penyesuaian button
  And I click the tambah baru button to increase my goods stocks
  Then Successfully added the number of items