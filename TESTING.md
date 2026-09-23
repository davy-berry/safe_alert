# Testing

SafeAlert was thoroughly tested throughout development to ensure that the
application functions correctly, responds appropriately to user actions,
and provides a consistent experience across different screen sizes and
browsers.

Testing was carried out using both automated Django tests and manual
testing.

The testing process covered:

- Application functionality
- User authentication
- Report creation and management
- Administrator functionality
- Report status management
- Comments
- Status history
- Heatmap functionality
- Responsive design
- Browser compatibility
- Form validation
- Security and permissions
- Database interactions

---

## 1. Testing Introduction

Testing was performed throughout the development of SafeAlert rather than
only after the application was completed.

Individual features were tested as they were implemented, allowing issues
to be identified and resolved during development.

Testing included:

- Automated unit and integration testing using Django's testing framework.
- Manual testing of all major user and administrator functionality.
- Testing of form validation and error handling.
- Testing of authentication and access permissions.
- Testing of responsive layouts on different screen sizes.
- Testing across different browsers.
- Testing of the deployed application.
- HTML and CSS validation where applicable.

The results of the testing process are documented in this file.

## 2. Automated Testing

SafeAlert includes automated tests using Django's built-in testing
framework.

The automated tests were executed using bash command: python manage.py test

The test suite completed successfully with the following result:
![SafeAlert Tests Result](documentation\testing\auto-test\tests_results.png)
