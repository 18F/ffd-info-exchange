from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class FafsaTest(unittest.TestCase):

    def setUp(self):
        # Bring up the capabilities object for editing and call on FIREFOX
        caps = DesiredCapabilities.FIREFOX

        # Specify the exact Firefox binary you want to use. 47 is behaving.
        # @todo: Refactor as environment variable.
        caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"

        # Specify geckodriver location
        # @todo: Refactor as environment variable.
        geckodriver = '/path/to/geckodriver'

        # Now we can call the Firefox webdriver, but this time with specified flags for the capabilities and geckodriver exec location
        self.browser = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_fafsa_form(self):
        # The user opens a web browser and sees the FAFSA form.
        # @todo: Reimplement with live_server_url.
        self.browser.get('http://127.0.0.1:8000')
        assert 'FAFSA - Federal Student Aid' in self.browser.title

        # They see some FAFSA branding.

        # They see the 'An official website of the U.S. Government' footer.

        # TODO: fill out the form.
#        self.fail('Finish these tests.')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
