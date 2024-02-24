from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url="https://books.toscrape.com/"

chrome_options =Options()
chrome_options.add_experimental_option("detach",True)

driver = Chrome(service=service(ChromeDriverManager().install()),
                options=chrome_options)

driver.get(url)
driver.maximize_window()