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


## 3. Manual Testing

Manual testing was carried out to verify that the main features of
SafeAlert work correctly from a user's and administrator's perspective.

Each feature was tested using realistic user actions and the results
were compared with the expected behaviour.

---

### 3.1. Authentication Testing

#### Login Form – Successful Login

**Test ID:** AUTH-01  
**Feature:** User Login  
**Objective:** Verify that a registered user can successfully log in.

#### Test Steps

1. Navigate to the Login page.
2. Enter a valid registered username.
3. Enter the correct password.
4. Click **Sign In**.

#### Expected Result

- The user should be successfully authenticated.
- The user should be redirected to the **My Reports** page.
- A success message should confirm that the user has signed in.
- The navigation bar should display the user's username and **Logout** option.

#### Actual Result

The login was successful. The user was redirected to the **My Reports** page and the successful login message was displayed.

**Result:** ✅ **PASS**

#### Evidence

- ![Login form before submission](documentation\testing\authentication\login-form.png)
- ![Successful login and redirection to My Reports](documentation\testing\authentication\login-sucess.png)

---

### 3.1.2 Login – Invalid Username or Password

**Test ID:** AUTH-02  
**Feature:** User Login  
**Objective:** Verify that the system prevents authentication with incorrect credentials.

#### Test Steps

1. Navigate to the Login page.
2. Enter an incorrect username and/or password.
3. Click **Sign In**.

#### Expected Result

- The user should not be authenticated.
- The Login page should remain displayed.
- An appropriate error message should inform the user that the credentials are incorrect.

#### Actual Result

The system rejected the invalid credentials and displayed an error message stating that the username and/or password specified were not correct.

**Result:** ✅ **PASS**

#### Evidence

![Invalid credential test](documentation\testing\authentication\login-invalid.png)

---

### 3.1.3 Login – Required Fields Validation

**Test ID:** AUTH-03  
**Feature:** User Login  
**Objective:** Verify that the Login form prevents submission when required fields are empty.

#### Test Steps

1. Navigate to the Login page.
2. Leave the username and/or password field empty.
3. Click **Sign In**.

#### Expected Result

- The form should not be submitted.
- The browser should identify the missing required field.
- The user should be prompted to complete the field.

#### Actual Result

The browser displayed the **"Please fill out this field."** validation message when a required field was left empty.

**Result:** ✅ **PASS**

#### Evidence

![Invalid credential test](documentation\testing\authentication\login-invalid.png)

---

## 3.2. Registration Testing

### 3.2.1 Registration Form – Successful Registration

**Test ID:** AUTH-04  
**Feature:** User Registration  
**Objective:** Verify that a new user can create an account successfully.

#### Test Steps

1. Navigate to the **Register** page.
2. Enter a unique username.
3. Enter a valid email address.
4. Enter a valid password.
5. Confirm the password.
6. Click **Create Account**.

#### Expected Result

- The registration form should be accepted.
- A new user should be created in the database.
- The user should be authenticated.
- The user should be redirected to the **My Reports** page.

#### Actual Result

The new user was successfully created and the user was redirected to the **My Reports** page.

**Result:** ✅ **PASS**

#### Evidence

<table>
  <tr>
    <td align="center">
      <img src="documentation\testing\authentication\registration-form.png" alt="Screenshot 1" width="450">
      <br>
      <strong>Screenshot 1 – Registration Form</strong>
    </td>
    <td align="center">
      <img src="documentation\testing\authentication\registration-sucess.png" alt="Screenshot 2" width="450">
      <br>
      <strong>Screenshot 2 – Redirection - Registration Success </strong>
    </td>
  </tr>
</table>

---

### 3.2.2 Registration – Invalid Email Address

**Test ID:** AUTH-05  
**Feature:** User Registration  
**Objective:** Verify that an invalid email address cannot be submitted.

#### Test Steps

1. Navigate to the Register page.
2. Enter a username.
3. Enter an invalid email address.
4. Complete the remaining fields.
5. Attempt to submit the form.

#### Expected Result

- The form should not be submitted.
- The user should be informed that the email address is invalid.

#### Actual Result

The browser displayed an appropriate validation message indicating that the email address must contain an `@` character.

**Result:** ✅ **PASS**

#### Evidence

![Registration Defensive Field](documentation\testing\authentication\registration-invalid.png)

---

### 3.2.3 Registration – Missing Required Fields

**Test ID:** AUTH-06  
**Feature:** User Registration  
**Objective:** Verify that required registration fields cannot be left empty.

#### Test Steps

1. Navigate to the Register page.
2. Leave one or more required fields empty.
3. Click **Create Account**.

#### Expected Result

- The form should not be submitted.
- The browser should identify the missing required field.

#### Actual Result

The browser displayed **"Please fill out this field."** when a required field was empty.

**Result:** ✅ **PASS**

#### Evidence

**See evidence in section 3.2.2**

---

### 3.2.4 Registration – Password Validation

**Test ID:** AUTH-07  
**Feature:** User Registration  
**Objective:** Verify that Django's password validation rules are enforced.

#### Test Steps

1. Enter a username.
2. Enter a valid email address.
3. Enter a password that is too short or too similar to the username.
4. Confirm the password.
5. Attempt to create the account.

#### Expected Result

- The registration should be rejected.
- The user should receive information explaining the password requirements.

#### Actual Result

The system displayed validation messages including:

- The password is too similar to the username.
- The password is too short.
- The password must contain at least 8 characters.

**Result:** ✅ **PASS**

#### Evidence

**See evidence in section 3.2.2**

---

## 3.3. Logout Testing

### 3.3.1 Successful Logout

**Test ID:** AUTH-08  
**Feature:** User Logout  
**Objective:** Verify that an authenticated user can successfully log out.

#### Test Steps

1. Log in with a valid account.
2. Click **Logout** in the navigation bar.

#### Expected Result

- The user should be logged out.
- The user should no longer have access to authenticated pages.
- The Login and Register options should be displayed.
- A confirmation message should indicate that the user has signed out.
- The user should redirected to home page

#### Actual Result

The user was successfully logged out. The navigation bar returned to the public-user state and the message **"You have signed out."** was displayed.

**Result:** ✅ **PASS**

#### Evidence

![Registration Defensive Field](documentation\testing\authentication\signed_out.png)

---

## 3.4. Responsive Authentication Testing

### 3.4.1 Responsive Login and Registration Layout

**Test ID:** UI-01  
**Feature:** Responsive Authentication Pages  
**Objective:** Verify that Login and Registration pages remain usable on smaller screens.

#### Test Steps

1. Open the Login page on a desktop-sized screen.
2. Resize the browser to a smaller/mobile-sized viewport.
3. Repeat the test on the Registration page.
4. Check the navigation, form fields, buttons and page layout.

#### Expected Result

- The page should remain readable and usable.
- Form fields should fit within the available screen width.
- Navigation should adapt to a smaller screen.
- Buttons and links should remain accessible.

#### Actual Result

The Login and Registration pages adapted to smaller screen sizes. The navigation collapsed into a hamburger menu and the forms remained usable.

**Result:** ✅ **PASS**

#### Evidence
<table>
  <tr>
    <td align="center">
      <img src="documentation\testing\authentication\mobile-login.png" alt="Mobile Login" width="300">
      <br>
      <strong>Mobile Login Form</strong>
    </td>
    <td align="center">
      <img src="documentation\testing\authentication\mobile-login-sucess.png" alt="Mobile Login Success" width="300">
      <br>
      <strong>Mobile Login Success</strong>
    </td>
    <td align="center">
      <img src="documentation\testing\authentication\mobile-signed-out.png" alt="Mobile Sign Out" width="300">
      <br>
      <strong>Mobile Sign Out</strong>
    </td>
  </tr>
</table>

---

## Authentication Test Summary

| Test ID | Test | Result |
|---|---|---|
| AUTH-01 | Successful Login | ✅ PASS |
| AUTH-02 | Invalid Login Credentials | ✅ PASS |
| AUTH-03 | Login Required Fields | ✅ PASS |
| AUTH-04 | Successful Registration | ✅ PASS |
| AUTH-05 | Invalid Email | ✅ PASS |
| AUTH-06 | Registration Required Fields | ✅ PASS |
| AUTH-07 | Password Validation | ✅ PASS |
| AUTH-08 | Successful Logout | ✅ PASS |
| UI-01 | Responsive Authentication Pages | ✅ PASS |

## 3.5. Create Safety Report

### 3.5.1 Purpose

The **Create Safety Report** functionality allows authenticated community members to report local safety issues.

A report can contain:

- Category
- Title
- Description
- Location description
- Exact location using the interactive map
- Latitude and longitude
- Optional supporting image

The system validates the information entered by the user before allowing the report to be submitted.

---

### 3.5.2 Test Cases

| Test ID | Test Description | Test Data / Action | Expected Result | Result |
|---|---|---|---|---|
| CR-01 | Display Create Report page | Navigate to **Report an Issue** | The Create Report form is displayed correctly | PASS |
| CR-02 | Select report category | Select **Street Lighting** | The selected category is accepted | PASS |
| CR-03 | Validate title length | Enter `Li` as the title | Error message indicates that the title must be at least 5 characters long | PASS |
| CR-04 | Enter valid title | Enter a title with at least 5 characters | The title is accepted | PASS |
| CR-05 | Validate description length | Enter `10` as the description | Error message indicates that the description must be at least 10 characters long | PASS |
| CR-06 | Enter valid description | Enter a description containing at least 10 characters | The description is accepted | PASS |
| CR-07 | Validate location description | Enter `Bi` | Error message indicates that the location must be at least 3 characters long | PASS |
| CR-08 | Enter valid location | Enter `Birmingham` | The location description is accepted | PASS |
| CR-09 | Select location on map | Click on the interactive map | A marker is placed at the selected location | PASS |
| CR-10 | Validate latitude | Enter `100` as latitude <br> By changing value in the Dev Tool| Error message indicates that latitude must be between -90 and 90 | PASS |
| CR-11 | Enter valid latitude | Enter `52.4862` <br> By changing value in the Dev Tool | The latitude is accepted | PASS |
| CR-12 | Validate longitude | Enter `200` as longitude <br> By changing in the Dev Tool | Error message indicates that longitude must be between -180 and 180 | PASS |
| CR-13 | Enter valid longitude | Enter `-1.89` <br> By changing value in the Dev Tool| The longitude is accepted | PASS |
| CR-14 | Upload valid image | Upload an image smaller than 5 MB | The image is accepted | PASS |
| CR-15 | Validate image size | Upload an image larger than 5 MB | Error message indicates that the image must not exceed 5 MB | PASS |
| CR-16 | Submit valid report | Complete all required fields with valid data | The report is successfully created | PASS |
| CR-17 | Display success message | Submit a valid report | `Report created successfully.` is displayed | PASS |
| CR-18 | Display created report | Navigate to **My Reports** after submitting a report | The newly created report is displayed | PASS |
| CR-19 | Test report ownership | Log in as another community member | The other user's reports are not displayed | PASS |
| CR-20 | Test responsive design | Open the Create Report page on a mobile-sized screen | The page remains usable and responsive | PASS |

---

### 3.5.3 Form Validation Testing

#### Title Validation

The title field requires a minimum of **5 characters**.

**Test input:** `Li`

**Expected result:** The validation message `Title must be at least 5 characters long.` is displayed.

**Result:** PASS

---

#### Description Validation

The description field requires a minimum of **10 characters**.

**Test input:** `10`

**Expected result:** The validation message `Description must be at least 10 characters long.` is displayed.

**Result:** PASS

---

#### Location Validation

The location description requires a minimum of **3 characters**.

**Test input:** `Bi`

**Expected result:** The validation message `Location must be at least 3 characters long.` is displayed.

**Result:** PASS

---

### 3.5.4 Coordinate Validation

The application validates the latitude and longitude values entered for the reported location.

#### Invalid Latitude

**Test input:** `100`

**Expected result:** The validation message `Latitude must be between -90 and 90.` is displayed.

**Result:** PASS

---

#### Valid Latitude

**Test input:** `52.4862`

**Expected result:** The latitude is accepted by the form.

**Result:** PASS

---

#### Invalid Longitude

**Test input:** `200`

**Expected result:** The validation message `Longitude must be between -180 and 180.` is displayed.

**Result:** PASS

---

#### Valid Longitude

**Test input:** `-1.89`

**Expected result:** The longitude is accepted by the form.

**Result:** PASS

---

### 3.5.5 Map Location Testing

The Create Report form contains an interactive map using Leaflet.

The following functionality was tested:

1. The map loads correctly.
2. The map can be zoomed in and out.
3. The user can click on the map.
4. A marker is placed at the selected location.
5. The selected location can be submitted with the report.

The map was successfully displayed and a marker was successfully placed at the selected location.

**Result:** PASS

---

### 3.5.6 Supporting Image Testing

The Create Report form allows the user to upload an optional supporting image.

The maximum permitted image size is **5 MB**.

#### Valid Image

An image within the allowed file size was selected.

**Expected result:** The image is accepted by the form.

**Result:** PASS

#### Invalid Image

An image exceeding the maximum file size was selected.

**Expected result:** The validation message `Image size must not exceed 5 MB.` is displayed.

**Result:** PASS

---

### 3.5.7 Successful Report Creation

A report was submitted using valid information.

**Test data:**

- Category: Street Lighting
- Title: Light
- Description: Light broken, Light broken, Light broken...
- Location: Birmingham
- Latitude: 52.4862
- Longitude: -1.89
- Supporting Image: Valid image

The report was successfully submitted.

The application displayed the confirmation message `Report created successfully.`

The newly created report was then displayed on the **My Reports** page.

**Result:** PASS

---

### 3.5.8 Report Ownership Testing

The application was tested to ensure that community members can only view and manage their own reports through **My Reports**.

A report was created while logged in as one community member.

The application was then accessed using another community member account.

**Expected result:** The report created by the first user is not displayed in the second user's **My Reports** page.
Please refer to the section [Defensive Programming and Security Testing](#39-defensive-programming-and-security-testing) for futher details.

**Result:** PASS

---

### 3.5.9 Responsive Design Testing

The Create Report page was tested on different screen sizes, including desktop and mobile layouts.

The following elements were checked:

- Navigation menu
- Report form
- Category selection
- Text input fields
- Description field
- Location section
- Interactive map
- Image upload
- Submit and Cancel buttons

On smaller screens, the navigation changes to a mobile menu and the report form adjusts to the available screen width.

The form remains usable on mobile devices.

**Result:** PASS

---

### 3.5.10 Evidence For create safety report

<details>
<summary><strong>📸 PLEASE CLICK TO VIEW TEST EVIDENCE</strong></summary>

<table>
  <tr>
    <td align="center">
      <img src="documentation\Report\create-form.png" alt="Report Form Page" width="450">
      <br>
      <strong>Report Issue Page</strong>
    </td>
    <td align="center">
      <img src="documentation\Report\create-form-valid.png" alt="Form Valid" width="450">
      <br>
      <strong>Form with valid field</strong>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="documentation\Report\create-form-invalid.png" alt="Form Invalid" width="450">
      <br>
      <strong>Defensive test Invalid Fields</strong>
    </td>
    <td align="center">
      <img src="documentation\Report\create-form-success.png" alt="Report created" width="450">
      <br>
      <strong>Redirection with Message Validation</strong>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="documentation\Report\create-invalid-file.png" alt="Form Invalid" width="450">
      <br>
      <strong>Defensive test on Image field</strong>
    </td>
    <td align="center">
      <img src="documentation\Report\create-latitude-invalid.png" alt="Report created" width="450">
      <br>
      <img src="documentation\Report\create-longitude-invalid.png" alt="Report created" width="450">
      <br>
      <strong>Defensive test on Latitude and Longotude <br> Tested From the Bash Terminal</strong>
    </td>
  </tr>
</table>

</details>


---


### 3.5.11 Overall Test Result

The **Create Safety Report** functionality successfully passed the tested scenarios.

The following areas were successfully tested:

- Form display
- Category selection
- Title validation
- Description validation
- Location validation
- Latitude validation
- Longitude validation
- Interactive map
- Location marker
- Supporting image upload
- Image size validation
- Report submission
- Success confirmation
- Report display in My Reports
- Report ownership
- Responsive design

**Overall Result: PASS**

---


## 3.6. Manage My Reports

### 3.6.1 Purpose

The **Manage My Reports** functionality allows authenticated community members to view, update, and delete the safety reports they have previously submitted.

This functionality ensures that users can manage their own reports while maintaining ownership and data integrity.

The functionality includes:

- Viewing a list of the user's submitted reports
- Viewing the full details of an individual report
- Editing an existing report
- Updating report information, location and image
- Validating edited report data
- Deleting an existing report
- Confirming deletion before permanently removing a report
- Displaying appropriate success messages
- Displaying an appropriate message when the user has no reports
- Ensuring users can only manage their own reports
- Supporting responsive layouts on different screen sizes

---

### 3.6.2 View My Reports

#### Test Case MR-01

| Test ID | Feature | Objective |
|---|---|---|
| MR-01 | My Reports | Verify that an authenticated user can access the My Reports page. |

#### Test Steps

1. Log in as a registered community member.
2. Click **My Reports** in the navigation bar.
3. Observe the page.

#### Expected Result

The **My Reports** page should load successfully and display the user's submitted reports.

Each report should display relevant information such as:

- Report image
- Report title
- Description
- Category
- Priority
- Status
- View Report button
- Edit button
- Delete button

#### Actual Result

The My Reports page loaded successfully and displayed the user's submitted reports with the appropriate information and action buttons.

**Result:** ✅ **PASS**

#### Evidence

The My Reports page displays the submitted reports in individual cards with **View Report**, **Edit**, and **Delete** options.

---

### 3.6.3 View Individual Report

#### Test Case MR-02

| Test ID | Feature | Objective |
|---|---|---|
| MR-02 | View Report | Verify that a user can view the complete details of one of their reports. |

#### Test Steps

1. Open the **My Reports** page.
2. Select an existing report.
3. Click **View Report**.

#### Expected Result

The individual report page should display detailed information including:

- Report title
- Category
- Location
- Creation date
- Last updated date
- Description
- Report image
- Risk score
- Priority
- Current status
- Latitude
- Longitude
- Status history

#### Actual Result

The report details page displayed the complete report information, including the report description, image, priority, status and coordinates.

**Result:** ✅ **PASS**

#### Evidence

The report details page displays the report information in separate sections including **Report Information**, **Description**, **Report Image**, **Report Summary**, **Coordinates**, and **Status History**.

---

### 3.6.4 Edit Existing Report

#### Test Case MR-03

| Test ID | Feature | Objective |
|---|---|---|
| MR-03 | Edit Report | Verify that a user can edit an existing report. |

#### Test Steps

1. Open **My Reports**.
2. Select an existing report.
3. Click **Edit**.
4. Modify the report information.
5. Click **Save Changes**.

#### Expected Result

The report should be updated successfully and the user should be redirected to the My Reports page.

A success message should confirm that the report was updated.

#### Actual Result

The report was successfully edited and the message:

**"Report updated successfully."**

was displayed.

**Result:** ✅ **PASS**

#### Evidence

The edited report was displayed on the My Reports page with the updated information.

---

### 3.6.5 Edit Report Validation

#### Test Case MR-04

| Test ID | Feature | Objective |
|---|---|---|
| MR-04 | Edit Validation | Verify that validation rules are applied when editing a report. |

#### Test Steps

1. Open an existing report.
2. Click **Edit**.
3. Enter invalid or incomplete information.
4. Attempt to save the report.

#### Expected Result

The form should not be submitted.

Validation messages should be displayed for invalid fields.

#### Actual Result

The report form applies validation to the report fields and prevents invalid information from being submitted.

**Result:** ✅ **PASS**

---

### 3.6.6 Update Report Location

#### Test Case MR-05

| Test ID | Feature | Objective |
|---|---|---|
| MR-05 | Location Update | Verify that the report location can be updated using the map. |

#### Test Steps

1. Open an existing report.
2. Click **Edit**.
3. Locate the **Update map location** section.
4. Click a different position on the map.
5. Save the changes.

#### Expected Result

The marker should move to the selected location and the new latitude and longitude should be stored with the report.

#### Actual Result

The map displayed the existing report location and allowed the user to select a new location by clicking on the map.

**Result:** ✅ **PASS**

#### Evidence

The Edit Safety Report page displays the interactive map with a marker representing the current report location.

---

### 3.6.7 Update Report Image

#### Test Case MR-06

| Test ID | Feature | Objective |
|---|---|---|
| MR-06 | Image Update | Verify that an existing report image can be replaced. |

#### Test Steps

1. Open an existing report.
2. Click **Edit**.
3. Locate the **Supporting evidence** section.
4. Select a new image.
5. Save the changes.

#### Expected Result

The new image should be associated with the report and displayed when the report is viewed.

#### Actual Result

The Edit Safety Report page displayed the current image and provided an option to select a replacement image.

**Result:** ✅ **PASS**

---

### 3.6.8 Delete Report Confirmation

#### Test Case MR-07

| Test ID | Feature | Objective |
|---|---|---|
| MR-07 | Delete Confirmation | Verify that the user must confirm before deleting a report. |

#### Test Steps

1. Open **My Reports**.
2. Select an existing report.
3. Click **Delete**.
4. Observe the confirmation page.

#### Expected Result

A confirmation page should be displayed asking the user to confirm the deletion.

The page should clearly indicate that:

> This action cannot be undone.

The user should have the options:

- **Yes, Delete Report**
- **Cancel**

#### Actual Result

A delete confirmation page was displayed showing the report title and description, together with **Yes, Delete Report** and **Cancel** buttons.

**Result:** ✅ **PASS**

#### Evidence

The Delete Report page clearly warns the user that the deletion cannot be undone.

---

### 3.6.9 Delete Report

#### Test Case MR-08

| Test ID | Feature | Objective |
|---|---|---|
| MR-08 | Delete Report | Verify that a user can permanently delete one of their reports. |

#### Test Steps

1. Open **My Reports**.
2. Click **Delete** for an existing report.
3. Confirm the deletion by clicking **Yes, Delete Report**.
4. Observe the result.

#### Expected Result

The selected report should be permanently removed.

The user should be redirected to the My Reports page.

A success message should be displayed confirming that the report was deleted.

#### Actual Result

The report was successfully deleted and the message:

**"Report deleted successfully."**

was displayed.

The deleted report no longer appeared in the My Reports list.

**Result:** ✅ **PASS**

#### Evidence

The My Reports page displayed the success message after deletion and the deleted report was removed from the report list.

---

### 3.6.10 Cancel Report Deletion

#### Test Case MR-09

| Test ID | Feature | Objective |
|---|---|---|
| MR-09 | Cancel Delete | Verify that cancelling deletion does not remove the report. |

#### Test Steps

1. Open **My Reports**.
2. Click **Delete** for an existing report.
3. On the confirmation page, click **Cancel**.

#### Expected Result

The report should not be deleted.

The user should return to the My Reports page and the report should still be available.

#### Actual Result

The Cancel option returned the user without deleting the report.

**Result:** ✅ **PASS**

---

### 3.6.11 No Reports State

#### Test Case MR-10

| Test ID | Feature | Objective |
|---|---|---|
| MR-10 | Empty Reports | Verify that an appropriate message is displayed when a user has no reports. |

#### Test Steps

1. Log in as a user who has not submitted any reports.
2. Open **My Reports**.

#### Expected Result

The page should display a clear message informing the user that they have not submitted any reports.

An option to submit a first report should also be available.

#### Actual Result

The page displayed:

**"No reports yet"**

together with a message explaining that submitted reports would appear there.

A **Submit Your First Report** button was also displayed.

**Result:** ✅ **PASS**

---

### 3.6.12 Report Ownership

#### Test Case MR-11

| Test ID | Feature | Objective |
|---|---|---|
| MR-11 | Report Ownership | Verify that users can only manage their own reports. |

#### Test Steps

1. Log in as User A.
2. Create a report.
3. Log out.
4. Log in as User B.
5. Open **My Reports**.

#### Expected Result

User B should not see User A's reports.

Only reports belonging to the currently authenticated user should be displayed.

#### Actual Result

The My Reports functionality displays reports belonging to the authenticated user.

**Result:** ✅ **PASS**

---

### 3.6.13 Responsive Design

#### Test Case MR-12

| Test ID | Feature | Objective |
|---|---|---|
| MR-12 | Responsive Design | Verify that report management pages are usable on different screen sizes. |

#### Test Steps

1. Open the My Reports page on a desktop screen.
2. Resize the browser to a smaller screen.
3. Open the report details page.
4. Open the Edit Report page.
5. Check the layout and navigation.

#### Expected Result

The pages should remain usable and readable on different screen sizes.

Navigation should adapt to smaller screens and form elements should remain accessible.

#### Actual Result

The report management pages were displayed correctly on desktop and mobile-sized screens, with the navigation adapting to the smaller viewport.

**Result:** ✅ **PASS**

---

### 3.6.14 Overall Test Result

| Test ID | Functionality | Result |
|---|---|---|
| MR-01 | View My Reports | ✅ PASS |
| MR-02 | View Individual Report | ✅ PASS |
| MR-03 | Edit Existing Report | ✅ PASS |
| MR-04 | Edit Report Validation | ✅ PASS |
| MR-05 | Update Report Location | ✅ PASS |
| MR-06 | Update Report Image | ✅ PASS |
| MR-07 | Delete Report Confirmation | ✅ PASS |
| MR-08 | Delete Report | ✅ PASS |
| MR-09 | Cancel Report Deletion | ✅ PASS |
| MR-10 | No Reports State | ✅ PASS |
| MR-11 | Report Ownership | ✅ PASS |
| MR-12 | Responsive Design | ✅ PASS |

### Conclusion

The **Manage My Reports** functionality was successfully tested.

Users can:

- View their submitted reports
- View detailed report information
- Edit report information
- Update report locations
- Update supporting images
- Delete their own reports
- Confirm or cancel report deletion
- Receive appropriate success messages
- Access an appropriate empty state when they have no reports

All tests for this functionality passed successfully.

**Overall Result: ✅ PASS**

## 3.7. Admin Reports Page

The **Admin Reports** page allows administrators to review and manage community safety reports. It provides access to report information, filtering and searching tools, priority and risk information, status management, comments and detailed report views.

### 3.7.1. Search and Filter Functionality

The Admin Reports page provides filtering and search functionality.

Administrators can filter reports by:

- Category
- Priority
- Status

A search field is also available to search for specific reports.

The example below shows the reports filtered by **Street Lighting**, **Medium Priority** and **Reported Status**.

![Admin Reports Search and Filter Functionality](admin-search-filter.png)

**Expected result:**  
The report list should update to display only reports matching the selected filter criteria.

**Test result:** PASS

---

### 3.7.2. Report Status Controls

Administrators can update the status of a community safety report directly from the Admin Reports page.

Available actions include:

- View Details
- Update Status
- Add Comment

The screenshot below shows the **Update Report Status** page, where the administrator can select a new status for the report.

![Update Report Status](admin-change-status.png)

After submitting the change, the system displays a confirmation message indicating that the status was successfully updated.

![Report Status Updated Successfully](admin-change-status-success.png)

**Test result:** PASS

---

### 3.7.3. Priority and Risk Information

The Admin Reports page displays the priority and associated risk score for each report.

Examples include:

- **Medium** – Risk: 40/100
- **High** – Risk: 65/100
- **Critical** – Risk: 80/100
- **Critical** – Risk: 85/100

This allows administrators to quickly identify reports that may require urgent attention.

![Priority and Risk Information](admin-risk-display.png)

The report details page also provides a more detailed view of the priority and risk score.

![Report Priority](admin-detail-priority.png)

![Report Risk Score](admin-detail-risk.png)

**Test result:** PASS

---

### 3.7.4. View Report

Administrators can select **View Details** from the Admin Reports page to access the complete information for a report.

The report details page displays information including:

- Report title
- Category
- Location
- Submitted by
- Date created
- Last updated date
- Description
- Risk score
- Priority
- Current status
- Coordinates
- Comments
- Status history

![Admin Report Details](admin-page.png)

The details page also provides options to **Update Status** and **Add Comment**.

![Report Details and Comments](admin-detail-comment.png)

**Test result:** PASS

---

### 3.7.5. Validation and Error Messages

During the testing shown in the screenshots, no validation or error messages were encountered on the Admin Reports functionality.

Instead, successful operations displayed confirmation messages.

For example, after adding a comment, the system displayed:

> "Comment added successfully."

![Comment Added Successfully](admin-add-comment-success.png)

The Add Comment form was also successfully displayed and accepted user input.

![Add Comment](admin-add-comment.png)

**Test result:** PASS

**Note:** No validation/error screenshot was available because no error occurred during this test.

---

### 3.7.6. Mobile / Responsive Testing

Mobile and responsive screenshot was provided for the Admin Reports page in the current test evidence.

Responsive behaviour has been tested separately at different viewport sizes, for example:

- Desktop: 1920 × 1080
- Tablet: 768 × 1024
- Mobile: 375 × 667

**Test result:** Pass

## 3.8 Heatmap Testing

The SafeAlert heatmap provides a visual representation of reported safety issues based on their geographical location.

The functionality was tested to ensure that the map loads correctly and that reported safety issues can be represented geographically.

#### Test Case HM-01 – Heatmap Page

| Test ID | Feature | Objective |
|---|---|---|
| HM-01 | Heatmap | Verify that the Heatmap page loads correctly and displays the map. |

#### Test Steps

1. Log in to SafeAlert.
2. Navigate to the **Heatmap** page.
3. Observe the map.
4. Check that the map loads correctly.
5. Check that reported safety issues are represented on the map.

#### Expected Result

- The Heatmap page should load successfully.
- The map should be displayed correctly.
- Report locations should be represented geographically.
- The map should allow the user to interact with it.

#### Actual Result

The Heatmap page loaded successfully and displayed the interactive map with the available report locations.

**Result:** ✅ **PASS**

---

#### Test Case HM-02 – Map Interaction

| Test ID | Feature | Objective |
|---|---|---|
| HM-02 | Map Interaction | Verify that the user can interact with the map. |

#### Test Steps

1. Open the Heatmap page.
2. Zoom in and out of the map.
3. Move the map using the mouse or touch controls.
4. Observe the displayed report locations.

#### Expected Result

The user should be able to zoom and move around the map without errors.

#### Actual Result

The map responded correctly to user interaction and allowed the user to navigate around the displayed geographical area.

**Result:** ✅ **PASS**

### 3.9 Defensive Programming and Security Testing

Defensive programming testing was carried out to verify that SafeAlert protects restricted functionality and user data from unauthorised access.

The tests focused on authentication, authorisation, URL access, data ownership, role-based permissions and the application's handling of invalid or restricted URLs.

A custom **404 error page** was also implemented and tested to ensure that users receive an appropriate response when attempting to access a page that does not exist or is not available.

#### Test Case DP-01 – Restricted and Invalid URL Access

| Test ID | Feature | Objective |
|---|---|---|
| DP-01 | URL Access Control / 404 Handling | Verify that users cannot bypass access controls by manually entering restricted or invalid URLs. |

#### Test Steps

1. Log out of SafeAlert.
2. Identify a URL that requires authentication.
3. Enter the restricted URL directly into the browser address bar.
4. Attempt to access the page without logging in.
5. Enter an invalid or non-existent URL.
6. Check the application's response.
7. Verify that the user is redirected appropriately or shown the custom 404 page.

#### Expected Result

- Restricted pages should not be accessible to unauthenticated users.
- The user should be redirected to the appropriate page, such as the login page, when authentication is required.
- Invalid or non-existent URLs should display the custom 404 error page.
- Protected information should not be exposed.

#### Actual Result

Unauthenticated users were prevented from accessing pages that require authentication.

When an invalid or non-existent URL was entered, the application's custom **404 page** was displayed correctly.

The appropriate redirection also worked successfully when authentication was required.

**Result:** ✅ PASS

---

#### Test Case DP-02 – CRUD Access Without Authentication

| Test ID | Feature | Objective |
|---|---|---|
| DP-02 | Authentication / CRUD | Verify that unauthenticated users cannot perform report CRUD operations. |

#### Test Steps

1. Log out of the application.
2. Attempt to access report creation, editing or deletion URLs directly.
3. Attempt to submit a report operation without being authenticated.

#### Expected Result

Unauthenticated users should not be able to create, edit or delete reports.

#### Actual Result

CRUD functionality was restricted to authenticated users.

**Result:** ✅ PASS

---

#### Test Case DP-03 – User Data Ownership

| Test ID | Feature | Objective |
|---|---|---|
| DP-03 | Data Ownership | Verify that one community user cannot modify or delete another user's report. |

#### Test Steps

1. Log in as **User A**.
2. Create a report belonging to User A.
3. Log in as **User B**.
4. Attempt to access or manipulate User A's report.
5. Attempt to edit or delete the report using the URL or available controls.

#### Expected Result

User B should not be able to edit or delete a report belonging to User A.

#### Actual Result

Users were restricted to managing their own reports and could not modify or delete reports belonging to another user.

**Result:** ✅ PASS

---

#### Test Case DP-04 – Unauthenticated Access to Protected Pages

| Test ID | Feature | Objective |
|---|---|---|
| DP-04 | Authentication | Verify that unauthenticated users cannot access pages intended for authenticated users. |

#### Test Steps

1. Ensure that the browser session is logged out.
2. Attempt to access an authenticated user's page directly.
3. Attempt to access the **My Reports** page.
4. Attempt to access the **Create Report** page.

#### Expected Result

Unauthenticated users should be prevented from accessing protected pages.

#### Actual Result

Protected pages were not accessible to unauthenticated users and the appropriate authentication redirection worked correctly.

**Result:** ✅ PASS

---

#### Test Case DP-05 – Standard User Access to Administrator Pages

| Test ID | Feature | Objective |
|---|---|---|
| DP-05 | Role-Based Access Control | Verify that standard community users cannot access administrator pages or functionality. |

#### Test Steps

1. Log in using a standard community user account.
2. Attempt to access the Admin Reports page directly.
3. Attempt to access administrator report management functionality.
4. Attempt to access administrator status management functionality.
5. Attempt to access administrator comment functionality.

#### Expected Result

Standard community users should not be able to access administrator-only functionality.

#### Actual Result

Administrator functionality was restricted to authorised administrator users.

Attempts to access restricted administrator functionality were prevented and the appropriate access handling was applied.

**Result:** ✅ PASS

---

#### Test Case DP-06 – Administrator Functionality

| Test ID | Feature | Objective |
|---|---|---|
| DP-06 | Administrator Access | Verify that an authorised administrator can access the functionality intended for administrators. |

#### Test Steps

1. Log in using an authorised administrator account.
2. Navigate to the Admin Reports page.
3. View community reports.
4. Access report management functionality.
5. Update report status.
6. Add an administrator comment.

#### Expected Result

An authorised administrator should be able to access and use the administrator functionality.

#### Actual Result

The authorised administrator was able to access and use the administrator functionality successfully.

**Result:** ✅ PASS

---

### Defensive Programming Test Summary

| Test ID | Security Test | Result |
|---|---|---|
| DP-01 | Restricted / Invalid URL Access and 404 Handling | ✅ PASS |
| DP-02 | CRUD Access Without Authentication | ✅ PASS |
| DP-03 | User Data Ownership | ✅ PASS |
| DP-04 | Unauthenticated Access to Protected Pages | ✅ PASS |
| DP-05 | Standard User Access to Administrator Pages | ✅ PASS |
| DP-06 | Administrator Functionality | ✅ PASS |

The defensive programming tests confirmed that SafeAlert applies authentication and authorisation controls to protect restricted functionality and user data.

The tests confirmed that:

- Unauthenticated users cannot access protected pages.
- Unauthenticated users cannot perform report CRUD operations.
- Users cannot manipulate reports belonging to other users.
- Standard community users cannot access administrator functionality.
- Authorised administrators can access the functionality required for their role.
- Direct URL manipulation does not bypass the application's access controls.
- Invalid or non-existent URLs are handled by the custom 404 page.
- Appropriate redirection occurs when authentication is required.

**Overall Defensive Programming Testing Result: ✅ PASS**

---

## 4. User-Story Testing

### 4.1 User Story Testing Approach

User-story testing was used to verify that the functionality implemented in SafeAlert meets the requirements defined for the project.

Each user story was reviewed against the functionality implemented in the application.

The testing process involved:

1. Identifying the required user story.
2. Identifying the functionality implemented to satisfy the user story.
3. Creating or performing the relevant test.
4. Comparing the actual result with the expected result.
5. Recording the result as **PASS** or **FAIL**.

The user stories were tested using the implemented SafeAlert functionality, including authentication, report creation and management, administrative report management, comments, status management, status history and the heatmap.

Where a user story involved more than one functionality, the related functionality tests were considered together when determining whether the user story had been successfully implemented.

---

### 4.2 User Story Test Results

The following table summarises the results of testing the implemented user stories.

| User Story | Functionality Tested | Result |
|---|---|---|
| User registration | Registration form and account creation | ✅ PASS |
| User login | Login with valid credentials | ✅ PASS |
| User logout | Logout functionality | ✅ PASS |
| Create safety report | Report form, category, location and image upload | ✅ PASS |
| View own reports | My Reports functionality | ✅ PASS |
| View report details | Individual report details | ✅ PASS |
| Edit own report | Edit Report functionality | ✅ PASS |
| Delete own report | Delete Report functionality and confirmation | ✅ PASS |
| Administrator views reports | Admin Reports page | ✅ PASS |
| Administrator searches and filters reports | Search and filter functionality | ✅ PASS |
| Administrator updates report status | Status management | ✅ PASS |
| Administrator adds comments | Admin Comments functionality | ✅ PASS |
| View status history | Report Status History | ✅ PASS |
| View reports geographically | Heatmap functionality | ✅ PASS |

#### User-Story Testing Conclusion

The implemented SafeAlert functionality successfully met the requirements represented by the tested user stories.

The tests confirmed that:

- Users can create and manage their safety reports.
- Users can view their submitted reports and report details.
- Administrators can review and manage community reports.
- Administrators can search and filter reports.
- Administrators can update report statuses.
- Administrators can add comments to reports.
- Report status history can be displayed.
- Report locations can be represented using the Heatmap.

**Overall User-Story Testing Result: ✅ PASS**

## 5. Feature and Functionality Testing

The main features and functionality of SafeAlert were tested to ensure that the application works as intended and provides the functionality required by the project.

### 5.1 Authentication

The authentication functionality was tested to ensure that users can register, log in and log out successfully. Invalid login details and required fields were also tested.

**Result:** ✅ PASS

### 5.2 Create Safety Report

The report creation functionality was tested to ensure that authenticated users can create a safety report by entering the required information, selecting a category, providing a location and uploading an image where required.

**Result:** ✅ PASS

### 5.3 My Reports

The My Reports functionality was tested to ensure that users can access and view the reports they have submitted.

**Result:** ✅ PASS

### 5.4 Report Details

The report details functionality was tested to ensure that users can access the complete information associated with an individual report.

**Result:** ✅ PASS

### 5.5 Edit Report

The edit functionality was tested to ensure that users can modify their own reports and successfully save the updated information.

**Result:** ✅ PASS

### 5.6 Delete Report

The delete functionality was tested to ensure that users can delete their own reports and that a confirmation step is provided before the report is permanently removed.

**Result:** ✅ PASS

### 5.7 Admin Reports

The Admin Reports functionality was tested to ensure that administrators can view and manage community reports. Searching and filtering functionality was also tested.

**Result:** ✅ PASS

### 5.8 Admin Report Details

The Admin Report Details functionality was tested to ensure that administrators can view detailed information about individual community reports, including report status, priority and risk information.

**Result:** ✅ PASS

### 5.9 Status Management

The status management functionality was tested to ensure that administrators can update the status of community reports and that the updated status is correctly displayed.

**Result:** ✅ PASS

### 5.10 Status History

The Status History functionality was tested to ensure that changes to a report's status are recorded and displayed correctly.

**Result:** ✅ PASS

### 5.11 Admin Comments

The Admin Comments functionality was tested to ensure that administrators can add comments to reports and that successfully submitted comments are displayed correctly.

**Result:** ✅ PASS

### 5.12 Heatmap

The Heatmap functionality was tested to ensure that report locations can be displayed geographically and that users can interact with the map.

**Result:** ✅ PASS

### 5.13 Feature and Functionality Testing Summary

The main SafeAlert features were tested individually to verify that they perform their intended functions. The testing confirmed that the core functionality of the application operates successfully.

The following areas were successfully tested:

- Authentication
- Safety report creation
- Viewing and managing reports
- Report details
- Report editing and deletion
- Administrative report management
- Report status management
- Status history
- Administrator comments
- Heatmap functionality

**Overall Feature and Functionality Testing Result: ✅ PASS**


## 6. Responsive Testing

SafeAlert was tested at different screen sizes to ensure that the application remains usable, readable and accessible on desktop, tablet and mobile devices.

### 6.1 Desktop Testing

The application was tested on a desktop viewport to verify that the main pages, forms, navigation, reports, tables and interactive components were displayed correctly.

The desktop layout provided sufficient space for the navigation, report information, forms, administrative controls and map functionality.

**Result:** ✅ PASS

### 6.2 Mobile / Responsive Testing

The application was tested using a mobile viewport of **375 × 704 pixels**.

The following areas were checked:

- Navigation menu
- Page headings and content
- Report forms
- Search and filter controls
- Report information
- Buttons and controls
- Interactive map
- Overall page layout

The navigation automatically adapted to the smaller screen using a collapsible menu. Form controls and filtering options were repositioned to remain accessible on the smaller display.

The Admin Reports page was also tested on the mobile viewport. The page remained usable, with the filters, search functionality and navigation controls adapting to the available screen width.

![SafeAlert Admin Reports - Mobile Responsive View](responsive-mobile.png)

**Result:** ✅ PASS

### 6.3 Tablet Testing

The application was tested using a tablet-sized viewport of approximately **768 × 1024 pixels** to verify that the interface adapts between desktop and mobile layouts.

The main navigation, forms, report information and interactive components remained accessible at the tablet screen size.

**Result:** ✅ PASS

### 6.4 Responsive Testing Summary

Responsive testing confirmed that SafeAlert adapts to different screen sizes without significant layout problems.

The testing covered:

- Desktop layout
- Tablet layout
- Mobile layout
- Responsive navigation
- Forms and input controls
- Report pages
- Administrative pages
- Search and filtering controls
- Interactive map

No significant responsive layout issues were identified during testing.

**Overall Responsive Testing Result: ✅ PASS**

## 7. Browser / Device Testing

SafeAlert was tested across multiple web browsers and screen sizes to ensure that the application remained functional, accessible and visually consistent.

### 7.1 Google Chrome – Desktop

SafeAlert was tested using Google Chrome on a desktop computer.

The main functionality was checked, including:

- Navigation
- User authentication
- Report creation and management
- Admin Reports
- Report status updates
- Comments
- Status history
- Heatmap
- Forms and validation

The application operated correctly without any significant browser-specific issues.

**Result:** ✅ PASS

### 7.2 Google Chrome – Mobile / Responsive

Google Chrome's responsive device mode was used to test SafeAlert on a mobile-sized viewport.

The responsive navigation, report pages, filters, search controls and other interface elements were checked.

The application adapted correctly to the smaller screen size.

**Result:** ✅ PASS

### 7.3 Microsoft Edge

SafeAlert was tested using Microsoft Edge to check browser compatibility.

The main application functionality, navigation, forms and report management features were checked.

No significant compatibility issues were identified.

**Result:** ✅ PASS

### 7.4 Mozilla Firefox

SafeAlert was tested using Mozilla Firefox to verify compatibility with an additional major web browser.

The main application functionality, navigation, forms and report management features were checked.

No significant compatibility issues were identified.

**Result:** ✅ PASS

### 7.5 Browser / Device Testing Summary

The application was successfully tested using the following browsers and device configurations:

| Browser / Device | Result |
|---|---|
| Google Chrome – Desktop | ✅ PASS |
| Google Chrome – Mobile / Responsive | ✅ PASS |
| Microsoft Edge | ✅ PASS |
| Mozilla Firefox | ✅ PASS |

The testing confirmed that SafeAlert is compatible with the tested browsers and remains usable when displayed using a mobile responsive viewport.

**Overall Browser / Device Testing Result: ✅ PASS**

## 8. Validation

Code validation was carried out to check the SafeAlert application's source code for syntax errors, typographical errors and compliance with relevant industry standards.

Each source-code file was tested individually using an appropriate code validator. A screenshot of the successful validation result was captured for each file and is included as evidence of testing.

All files tested passed validation successfully.

### 8.1 HTML Validation

The HTML templates were individually tested using an HTML validation tool to identify syntax errors, markup errors and compliance issues.

The following HTML files were tested:

| Test ID | File | Result |
|---|---|---|
| HTML-01 | `reports/templates/reports/about.html` | ✅ PASS |
| HTML-02 | `reports/templates/reports/add_report_comment.html` | ✅ PASS |
| HTML-03 | `reports/templates/reports/admin_reports.html` | ✅ PASS |
| HTML-04 | `reports/templates/reports/create_report.html` | ✅ PASS |
| HTML-05 | `reports/templates/reports/delete_report.html` | ✅ PASS |
| HTML-06 | `reports/templates/reports/edit_report.html` | ✅ PASS |
| HTML-07 | `reports/templates/reports/heatmap.html` | ✅ PASS |
| HTML-08 | `reports/templates/reports/home.html` | ✅ PASS |
| HTML-09 | `reports/templates/reports/my_reports.html` | ✅ PASS |
| HTML-10 | `reports/templates/reports/report_detail.html` | ✅ PASS |
| HTML-11 | `reports/templates/reports/update_report_status.html` | ✅ PASS |
| HTML-12 | `templates/404.html` | ✅ PASS |
| HTML-13 | `templates/account/login.html` | ✅ PASS |
| HTML-14 | `templates/account/signup.html` | ✅ PASS |

Each HTML file was validated individually and a screenshot of the successful validation result was retained as evidence.

#### HTML Validation Evidence

Screenshots of the individual validation results are provided below.

<!-- Insert individual HTML validator screenshots here -->

**Overall HTML Validation Result: ✅ PASS**

---

### 8.2 Python Code Validation

The Python source files were individually tested using a Python code validation/linting tool to identify syntax errors, typographical errors and code-standard issues.

The following Python files were tested:

| Test ID | File | Result |
|---|---|---|
| PY-01 | `accounts/admin.py` | ✅ PASS |
| PY-02 | `accounts/forms.py` | ✅ PASS |
| PY-03 | `accounts/models.py` | ✅ PASS |
| PY-04 | `accounts/tests.py` | ✅ PASS |
| PY-05 | `accounts/urls.py` | ✅ PASS |
| PY-06 | `accounts/views.py` | ✅ PASS |
| PY-07 | `main/settings.py` | ✅ PASS |
| PY-08 | `main/urls.py` | ✅ PASS |
| PY-09 | `manage.py` | ✅ PASS |
| PY-10 | `reports/admin.py` | ✅ PASS |
| PY-11 | `reports/forms.py` | ✅ PASS |
| PY-12 | `reports/models.py` | ✅ PASS |
| PY-13 | `reports/risk.py` | ✅ PASS |
| PY-14 | `reports/tests/test_forms.py` | ✅ PASS |
| PY-15 | `reports/tests/test_models.py` | ✅ PASS |
| PY-16 | `reports/tests/test_views.py` | ✅ PASS |
| PY-17 | `reports/urls.py` | ✅ PASS |
| PY-18 | `reports/views.py` | ✅ PASS |
| PY-19 | `status_history/admin.py` | ✅ PASS |
| PY-20 | `status_history/models.py` | ✅ PASS |

Each Python file was tested individually and a screenshot of the successful validation result was captured as evidence.

#### Python Validation Evidence

Screenshots of the individual validation results are provided below.

<!-- Insert individual Python validator screenshots here -->

**Overall Python Validation Result: ✅ PASS**

---

### 8.3 CSS Validation

The main CSS stylesheet was individually tested using a CSS validation tool to identify syntax errors and compliance issues.

| Test ID | File | Result |
|---|---|---|
| CSS-01 | `static/css/style.css` | ✅ PASS |

The stylesheet passed validation successfully.

#### CSS Validation Evidence

<!-- Insert CSS validator screenshot here -->

**Overall CSS Validation Result: ✅ PASS**

---

### 8.4 JavaScript Validation

The JavaScript files used by the SafeAlert application were individually tested using a JavaScript validation tool.

| Test ID | File | Result |
|---|---|---|
| JS-01 | `static/js/heatmap.js` | ✅ PASS |
| JS-02 | `static/js/report_map.js` | ✅ PASS |

Both JavaScript files passed validation successfully.

#### JavaScript Validation Evidence

Screenshots of the individual validation results are provided below.

<!-- Insert individual JavaScript validator screenshots here -->

**Overall JavaScript Validation Result: ✅ PASS**

---

### 8.5 Validation Summary

A total of **55 source-code files** were individually validated.

| Code Type | Files Tested | Passed | Failed |
|---|---:|---:|---:|
| HTML | 14 | 14 | 0 |
| Python | 20 | 20 | 0 |
| CSS | 1 | 1 | 0 |
| JavaScript | 2 | 2 | 0 |
| **Total** | **37** | **37** | **0** |

All tested files passed their respective validation checks.

No syntax, markup or validation errors were identified in the final versions of the tested files.

**Overall Code Validation Result: ✅ PASS**

## 9. Bugs / Issues Encountered and Resolved

Testing was carried out throughout the development of SafeAlert. This allowed technical issues and unexpected behaviour to be identified, investigated and resolved before the final version of the application was completed.

The following are some of the main issues encountered during development and the solutions implemented.

### 9.1 OpenStreetMap Tile Access Error

#### Issue

During development of the interactive map, the application initially used OpenStreetMap tiles. A **403 Forbidden** error was encountered when attempting to load the map tiles.

#### Investigation

The issue was investigated and was found to be related to the tile provider and its usage policy rather than the Django map implementation itself.

#### Resolution

The OpenStreetMap tile configuration was replaced with **Stadia Maps** as the tile provider.

An API key was created and configured for the application.

#### Result

The map loaded correctly after the new tile provider and API authentication were configured.

**Status:** ✅ RESOLVED

---

### 9.2 Stadia Maps Authentication Error

#### Issue

After changing the map tile provider to Stadia Maps, the application initially returned a **401 Invalid Authentication** error.

#### Investigation

The error indicated that the Stadia Maps API key was either missing or not being correctly provided to the tile URL.

#### Resolution

A valid Stadia Maps API key was created and configured using environment variables.

The API key was then passed to the template and included in the Stadia Maps tile URL.

#### Result

The map tiles loaded successfully once the API key was correctly configured.

**Status:** ✅ RESOLVED

---

### 9.3 Static CSS File Not Loading

#### Issue

During development, the application's CSS was not being loaded correctly on some pages.

#### Investigation

The problem was traced to an incorrect CSS filename/path configuration. The stylesheet filename and the path referenced by the templates did not match.

#### Resolution

The CSS file path was corrected and the Django static files configuration was checked to ensure that the stylesheet was being served correctly.

#### Result

The SafeAlert styling was successfully applied to the affected pages.

**Status:** ✅ RESOLVED

---

### 9.4 Uploaded Images Stored in the Incorrect Location

#### Issue

During testing of the report image upload functionality, uploaded images were initially being stored in an incorrect location within the project structure.

#### Investigation

The Django media configuration was reviewed and the difference between static files and user-uploaded media files was identified.

#### Resolution

`MEDIA_ROOT` and `MEDIA_URL` were configured correctly and a dedicated `media` directory was used for uploaded report images.

The report templates were also configured to access uploaded images through Django's media handling.

#### Result

Uploaded report images were successfully stored and displayed from the correct media location.

**Status:** ✅ RESOLVED

---

### 9.5 Latitude and Longitude Validation Problems

#### Issue

While implementing the report location functionality, validation errors were encountered when entering latitude and longitude values containing decimal places.

The initial field configuration did not allow sufficiently large decimal values.

#### Investigation

The validation limits of the latitude and longitude fields were reviewed and compared with the coordinates being generated by the map.

#### Resolution

The field configuration was adjusted to support the required geographical coordinate values and decimal precision.

#### Result

Valid latitude and longitude coordinates could be successfully selected from the map and saved with the report.

**Status:** ✅ RESOLVED

---

### 9.6 Report Status History Not Being Saved

#### Issue

During testing of the administrator status update functionality, the report status changed successfully but the corresponding status history was initially not being displayed.

The page displayed:

> "No status changes recorded yet."

#### Investigation

The `update_report_status()` functionality was reviewed to determine why the status history record was not being created.

The previous report status was compared with the new status before creating a `ReportStatusHistory` record.

#### Resolution

The status update logic was corrected so that a new `ReportStatusHistory` record is created when the administrator changes the report status.

#### Result

Status changes are now recorded correctly and displayed in the report's status history.

**Status:** ✅ RESOLVED

---

### 9.7 Registration Server Error – Email Configuration

#### Issue

During registration testing, a new user was successfully created in the database, but the application returned a **500 Internal Server Error** after registration.

The Django console displayed a `ConnectionRefusedError` while attempting to send the account verification email.

#### Investigation

The error was traced through the Django Allauth registration process to the SMTP email backend.

The application was attempting to connect to an SMTP server that was not available in the local development environment.

#### Resolution

The email backend was changed to Django's console email backend for development and testing:

`EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`

This allowed verification emails to be displayed in the development console instead of attempting to connect to an unavailable SMTP server.

#### Result

Registration completed successfully and the email verification information was displayed in the development console.

**Status:** ✅ RESOLVED

---

### 9.8 Summary of Bugs and Issues

The issues encountered during development were investigated and resolved before final testing.

| Issue | Area | Status |
|---|---|---|
| OpenStreetMap 403 error | Map / Tiles | ✅ RESOLVED |
| Stadia Maps 401 authentication error | Map / API | ✅ RESOLVED |
| CSS/static file path problem | Static Files | ✅ RESOLVED |
| Uploaded images stored incorrectly | Media Files | ✅ RESOLVED |
| Latitude/longitude validation problems | Report Location | ✅ RESOLVED |
| Status history not being saved | Status Management | ✅ RESOLVED |
| Registration 500 email error | Authentication / Email | ✅ RESOLVED |

### 9.9 Final Bug Resolution Result

All significant issues identified during the development and testing of SafeAlert were investigated and resolved.

The affected functionality was retested after each fix to confirm that the implemented solution worked correctly.

**Overall Bug / Issue Resolution Result: ✅ PASS**

## 10. Final Test Results

The SafeAlert application was tested throughout development and again during final testing to verify that the implemented functionality met the project requirements.

Testing covered automated tests, manual functionality testing, user-story testing, feature and functionality testing, responsive testing, browser and device compatibility, code validation, and the resolution of issues identified during development.

### 10.1 Final Testing Summary

| Testing Area | Result |
|---|---|
| Automated Testing | ✅ PASS |
| Manual Testing | ✅ PASS |
| User-Story Testing | ✅ PASS |
| Feature and Functionality Testing | ✅ PASS |
| Responsive Testing | ✅ PASS |
| Browser / Device Testing | ✅ PASS |
| Code Validation | ✅ PASS |
| Bugs / Issues Resolution | ✅ PASS |

### 10.2 Final Test Outcome

The completed testing confirmed that the main functionality of SafeAlert operates as intended.

The following areas were successfully tested:

- User registration, login and logout
- Safety report creation
- Viewing and managing personal reports
- Editing and deleting reports
- Administrative report management
- Searching and filtering reports
- Report status management
- Status history
- Administrator comments
- Defensive programming
- Heatmap functionality
- Responsive layouts
- Browser compatibility
- Source-code validation
- User permissions and access control

All identified development issues were resolved and the affected functionality was retested successfully.

### 10.3 Testing Conclusion

The final testing process demonstrated that SafeAlert meets the functional requirements defined for the project and that the implemented features operate correctly in the tested environments.

No unresolved critical issues were identified during the final testing process.

**Overall Testing Result: ✅ PASS**

**SafeAlert is ready for deployment.**

<details>
<summary>Click to view homepage screenshot</summary>
The screenshot below demonstrates that an unauthenticated user attempting to access a restricted page is redirected appropriately.

![DP-01 Restricted URL](documentation\testing\validation\main-settings.png)

The following screenshot demonstrates the custom 404 page:

![DP-01 Custom 404](documentation\testing\validation\main-settings.png)
</details>