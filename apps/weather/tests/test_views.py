#Run Unit Tests:
# python manage.py test weather_app.tests


# weather_app/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from weather_data import get_weather_data

class WeatherViewTestCase(TestCase):
    def test_weather_view(self):
        response = self.client.get(reverse('weather'))
        self.assertEqual(response.status_code, 200)

        # You can further test the response content, context, and behavior here
        # Example:
        # self.assertContains(response, 'Weather Information')
        # self.assertTemplateUsed(response, 'weather_app/weather.html')

    def test_weather_data_fetching(self):
        # Test the weather data fetching function
        data = get_weather_data('New York')
        self.assertIsNotNone(data)
        self.assertIn('weather', data)
        self.assertIn('main', data)
