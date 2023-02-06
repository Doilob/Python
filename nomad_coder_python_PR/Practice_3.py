from bs4 import BeautifulSoup
from extractros.wwr import extractor_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python")

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")
# print(f"{base_url}{search_term}")
# if response.status_code != 200:
#     print("Can't request page" )
# else:
#     print(response.text)