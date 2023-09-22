# Run Functional Tests:
# python manage.py test weather_app.tests.test_functional



# weather_app/tests/test_functional.py

from selenium import webdriver
from django.test import LiveServerTestCase

class WeatherAppFunctionalTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(executable_path='/path/to/geckodriver')  # Provide the path to your geckodriver executable
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_weather_information(self):
        self.selenium.get(self.live_server_url + '/weather/')
        # Simulate user interactions with the weather page
        # For example, fill out the location form and click the submit button
        location_input = self.selenium.find_element_by_id('location')
        location_input.send_keys('New York')
        submit_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()

        # Assert that the weather information is displayed correctly on the page
        # Example:
        # self.assertIn('Temperature:', self.selenium.page_source)
        # self.assertIn('Weather:', self.selenium.page_source)
