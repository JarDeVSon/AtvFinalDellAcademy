Feature: Login
@login
Scenario: Login
	Given the user accesses the Dell Accessible Learning platform.
	When the user authenticates with valid credentials.
	Then the platform returns the home page to the user.