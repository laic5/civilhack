import time
import re
import pandas as pd
import json
import requests_cache
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

requests_cache.install_cache('evictions_cache')
specialChar = "%2F"
#https://services.saccourt.ca.gov/PublicCaseAccess/UD/SearchByFilingDate?FilingDateBegin=8%2F1%2F2017&FilingDateEnd=9%2F23%2F2017

searchResultsUrl = "https://services.saccourt.ca.gov/PublicCaseAccess/UD/SearchByFilingDate"
endString = "FilingDateEnd="

# we can always use 08/21/2011 as our start date since it'll return the last 1000 results
def buildSearchParams(month, day, year):
    stringDate = str(month) + specialChar + str(day) + specialChar + str(year)
    dateSearchString = endString + stringDate

    return dateSearchString

def getSearchURl(end):
    url = searchResultsUrl + "?FilingDateBegin=8%2F1%2F2010&" + end
    return url

def getMDYFromString(dateIn):
    splitted = dateIn.split('/')
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    print(splitted)
    return (month, day, year)

def getPageToScrape(lastEnd):
    endDate = getMDYFromString(lastEnd)
    endQueryString = buildSearchParams(endDate[0], endDate[1], endDate[2])
    url = getSearchURl(endQueryString)
    print(url)
    return url

def getDateFromLastResult(bfsoupObject):
    return time.strftime("%Y/%m/%d")

def getSearchPageFromDate(lastEnd = time.strftime("%Y/%m/%d")):
    url = getPageToScrape(lastEnd)
    return url

def clickSearchButton(url):
    driver = webdriver.Chrome()
    driver.get(url)
    elem = driver.find_element_by_name('SearchButton').click()
    print(elem)

def parsePage(page):
    soup = BeautifulSoup(page)
    caseEntry = soup.find_all(id = "fa fa-search-plus")
    print(caseEntry)
    #last = caseEntry[-1]

clickSearchButton("https://services.saccourt.ca.gov/PublicCaseAccess/UD/SearchByFilingDate?FilingDateBegin=1%2F1%2F2011&FilingDateEnd=6%2F1%2F2017")
#scrapePage()
