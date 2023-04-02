from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse

scrapeRepo = input("What page should i scrape? ")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(f"{scrapeRepo}")
listReposLinks = []
listReposName = []
resultsRepo = driver.find_elements(By.CLASS_NAME, "repo")

def goingForRaw(filePage):
    driver.get(filePage)
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()
    time.sleep(1)
    html = driver.page_source
    html = f"{html}"

    if "password" in html:
        print(f"Found Password {filePage}")

def subFolderSearch(searchpage):
    driver.get(searchpage)
    listSubFolder = []
    current_URL = driver.current_url

    # Parsing URL for splitting and formatting for file URLs
    # Extracting Domain from the URL
    parsed_url = urlparse(current_URL)

    # Extracting the schema (protocol used "https"), netloc parts
    # (domain name "www.github.com")and path (specifies the path to the resource)
    # from parsed URL
    schema = parsed_url.scheme
    netloc = parsed_url.netloc
    # Alles nach .com
    path = parsed_url.path

    # Searching just for subfolder-webelement
    try:
        subFolderPart1 = driver.find_elements(By.XPATH, "//a[contains(@href, '/tree/main') and contains(@class, 'js-navigation-open') and contains(@data-turbo-frame, 'repo-content-turbo-frame')]")
    except NoSuchElementException:
        print("NO Subordner")
    else:
        # Check if there even is a subfolder
        # If not return None
        if subFolderPart1:
            pass
        else:
            return None

        for n in subFolderPart1:
            listSubFolder.append(n.text)

        for m in listSubFolder:
            if "/tree/main" in current_URL:
                subFolderUrl = f"{schema}://{netloc}{path}/{m}"
                searchloop(subFolderUrl)
            else:
                subFolderUrl = f"{schema}://{netloc}{path}/tree/main/{m}"
                searchloop(subFolderUrl)

def searchloop(nextPage):
    driver.get(nextPage)
    siteFiles = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    listSiteFiles = []
    current_URL = driver.current_url

    # Parsing URL for splitting and formatting for file URLs
    # Extracting Domain from the URL
    parsed_url = urlparse(current_URL)

    # Extracting the schema (protocol used "https"), netloc parts
    # (domain name "www.github.com")and path (specifies the path to the resource)
    # from parsed URL
    schema = parsed_url.scheme
    netloc = parsed_url.netloc
    # Everything after the ".com"
    path = parsed_url.path

    for s in siteFiles:
        listSiteFiles.append(s.text)

    # Searching for file extension and splitting
    # URL in two Parts, so the URL for the file can be made
    for s in listSiteFiles:
        if ".py" in s:
            if "/tree/main" in current_URL:
                partOne = f"{schema}://{netloc}{path.split('/tree')[0]}"
                partTwo = path.split('/tree')[1]
                filePage = f"{partOne}/blob{partTwo}/{s}"
            else:
                filePage = f"{schema}://{netloc}{path}/blob/main/{s}"
            goingForRaw(filePage)
        elif ".js" in s:
            if "/tree/main" in current_URL:
                partOne = f"{schema}://{netloc}{path.split('/tree')[0]}"
                partTwo = path.split('/tree')[1]
                filePage = f"{partOne}/blob{partTwo}/{s}"
            else:
                filePage = f"{schema}://{netloc}{path}/blob/main/{s}"
            goingForRaw(filePage)
        elif ".php" in s:
            if "/tree/main" in current_URL:
                partOne = f"{schema}://{netloc}{path.split('/tree')[0]}"
                partTwo = path.split('/tree')[1]
                filePage = f"{partOne}/blob{partTwo}/{s}"
            else:
                filePage = f"{schema}://{netloc}{path}/blob/main/{s}"
            goingForRaw(filePage)
        elif ".json" in s:
            if "/tree/main" in current_URL:
                partOne = f"{schema}://{netloc}{path.split('/tree')[0]}"
                partTwo = path.split('/tree')[1]
                filePage = f"{partOne}/blob{partTwo}/{s}"
            else:
                filePage = f"{schema}://{netloc}{path}/blob/main/{s}"
            goingForRaw(filePage)
        else:
            pass
    subFolderSearch(nextPage)

for i in resultsRepo:
    listReposName.append(i.text)

for l in listReposName:
    nextPage = f"{scrapeRepo}/{l}"
    listReposLinks.append(nextPage)
    searchloop(nextPage)
print(listReposLinks)

driver.quit()

