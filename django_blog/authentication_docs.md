# Django Blog Authentication System Documentation

This document provides an overview of the authentication system implemented in the Django Blog project. The system enables user registration, login, logout, and profile management.

## Features

1. **User Registration**: New users can create accounts with username, email, and password.
2. **User Login**: Registered users can log in using their credentials.
3. **User Logout**: Logged-in users can log out of their accounts.
4. **Profile Management**: Users can view and update their profile information.

## Implementation Details

### Forms

- `UserRegisterForm`: Extends Django's `UserCreationForm` to include an email field.
- `UserUpdateForm`: Allows users to update their username and email.

### Views

- `register`: Handles user registration with form validation.
- `profile`: Displays and processes updates to user profile information.
- Django's built-in authentication views are used for login and logout.

### Templates

- `login.html`: User login form.
- `register.html`: User registration form.
- `profile.html`: User profile display and edit form.
- `logout.html`: Confirmation page after logout.

### URL Configuration

- `/register/`: User registration page.
- `/login/`: User login page.
- `/logout/`: User logout confirmation.
- `/profile/`: User profile management.

## Security Features

1. **CSRF Protection**: All forms include CSRF tokens to prevent cross-site request forgery attacks.
2. **Password Hashing**: User passwords are securely hashed using Django's built-in hashing algorithms.
3. **Login Required**: Profile page is protected with the `@login_required` decorator.

## Testing the Authentication System

1. **Registration Test**:
   - Navigate to http://127.0.0.1:8000/register/
   - Fill in the registration form with a username, email, and password.
   - Submit the form and verify that you are redirected to the login page with a success message.

2. **Login Test**:
   - Navigate to http://127.0.0.1:8000/login/
   - Enter your username and password.
   - Submit the form and verify that you are redirected to the home page.

3. **Profile Test**:
   - Ensure you are logged in.
   - Navigate to http://127.0.0.1:8000/profile/
   - Verify that your current username and email are displayed.
   - Update your email address and submit the form.
   - Verify that the changes are saved and a success message is displayed.

4. **Logout Test**:
   - Ensure you are logged in.
   - Click on the "Logout" link in the navigation bar.
   - Verify that you are redirected to the logout confirmation page.
   - Click "Log In Again" to return to the login page.

## Troubleshooting

- If you encounter issues with user registration, check the form validation errors displayed on the registration page.
- If you cannot log in, ensure that you are using the correct username and password.
- If you cannot access the profile page, make sure you are logged in.