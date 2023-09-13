#IMPORT THESE PACKAGES
import selenium
from selenium import webdriver
#OPTIONAL PACKAGE, BUY MAYBE NEEDED
from webdriver_manager.chrome import ChromeDriverManager

#THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
driver = webdriver.Chrome(ChromeDriverManager().install())

#THIS PRETTY MUCH TELLS THE WEB BROWSER WHICH WEBSITE TO GO TO
driver.get('https://www.tiktok.com/@gordonramsayofficial/video/6916583398500748550?lang=en')

#THIS IS THE IMPORTANT PART SO I'LL BREAK IT DOWN IN A COUPLE DIFFERENT PARTS LOL

#THIS 'TEXT' PORTION         |       THIS PORTION WILL TAKE THE ELEMENT THAT
#PRETTY MUCH STORES THE      |       WE WANT FROM THE WEBSITE, THE .TEXT WILL
#WEBSITE DATA THAT WE WANT   |       SAVE THE INFORMATION AS A TEXT DOCUMENT
#IN THIS VARIABLE            |
TEXT = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[4]/div[2]/div[1]/strong').text

print(TEXT)
