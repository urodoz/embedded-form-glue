import time
import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def factory_firefox():
    driver = Firefox()
    return driver

class TestRoot(unittest.TestCase):

    def setUp(self):
        self.selenium = factory_firefox()

    def test_failed(self):
        self.selenium.get("http://127.0.0.1:8000/tests/views/index.html")
        window_keys = self.selenium.execute_script(u"""
        return Object.keys(window);
        """)

        assert "KRGlue" in window_keys


if __name__ == '__main__':
    unittest.main()
