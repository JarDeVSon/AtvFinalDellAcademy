
Feature: My Courses
@mycourses
Scenario: My Courses
	Given the user accesses the Dell Accessible Learning platform #2.
	When the user selects the My Courses on the left menu.
	Then the platform returns to the user his courses in progress and completed.