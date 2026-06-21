import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

def pytest_setup_options():
    options = Options()
    options.add_argument("--disable-features=HttpsUpgrades,InsecureDownloadWarnings")
    options.add_argument("--ignore-certificate-errors")
    return options