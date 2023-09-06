# Weather Mood Music App

The Weather Mood Music App is a Django-based web application that provides users with music recommendations based current weather conditions.

## Features

- **User Authentication**: Users can create accounts, log in, and log out.
- **Custom User Model**: The project uses a custom user model that extends Django's built-in User model to include additional fields like the user's birthday.
- **Weather Integration**: The app fetches weather data from an external API to provide accurate weather information based on the user's location.
- **Mood Detection**: The app analyzes the user's mood based on user input or external factors like weather conditions.
- **Music Recommendations**: Users receive music recommendations tailored to their mood and the weather.

## Usage

To get started with the Weather Mood Music App, follow these steps:

````bash
# Clone the repository
git clone https://github.com/Faberizio/Weather-Mood-Music.git
cd weather-mood-music

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser for accessing the admin panel
python manage.py createsuperuser

# Start the development server
python manage.py runserver

Open your web browser and access the app at http://localhost:8000/


- Visit the registration page to create a new user account.

- Log in to your account using your credentials.

- Explore the app's features, weather detection and music recommendations.
Access the admin panel at http://localhost:8000/admin/ to manage user accounts and data.

- **Contributing**
If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository on GitHub.

- Clone your forked repository to your local machine.

- Create a new branch for your feature or bug fix:

```bash

- git checkout -b feature-name

- Make your changes, commit them, and push to your forked repository.

- Submit a pull request to the main repository.

- **License**

This project is licensed under the MIT License. See the LICENSE file for details.

- **Acknowledgments**

Special thanks to the Django community for creating a robust web framework.

Weather data provided by Weather API.

Mood analysis and music recommendations powered by Music API.

