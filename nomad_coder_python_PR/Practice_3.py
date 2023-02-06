from requests import get
from bs4 import BeautifulSoup
from extractros.wwr import extractor_wwr_jobs

jobs = extractor_wwr_jobs("java")
print(jobs)