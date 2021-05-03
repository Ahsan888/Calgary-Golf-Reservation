import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.chrome.options
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-user-media-security=true")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://sc.cps.golf/CityCalgaryGolfReservations/(S(xg0wuqioelaugs2lalays32w))/Account/nLogOn#Hash")
time.sleep(3)

email = driver.find_element_by_id("Email")
email.send_keys("")

password = driver.find_element_by_id("Password")
password.send_keys("")
a =2

driver.find_element_by_class_name("btn-primary").click()
driver.maximize_window()
#driver.find_element_by_xpath("//*[contains(text(), 'Sign In')]").click()

time.sleep(3)
while a ==2:
    driver.get("https://sc.cps.golf/CityCalgaryGolfReservations/(S(dxz2elbcpj3wxqfonvwp2amm))/Home/WidgetView/")
    driver.find_element_by_id("FromDate").click()
    time.sleep(3)

    data=driver.find_element_by_class_name("datepicker-days")
    date= driver.find_element_by_id('FromDate')
    driver.execute_script('document.getElementsByName("FromDate")[0].removeAttribute("readonly")')
    driver.find_element_by_id('FromDate').clear()
    date.send_keys("04/18/2021")

    select = Select(driver.find_element_by_id('StartTimeDropDown'))
    options = select.options
    select.select_by_visible_text("Afternoon(12PM - 4PM)")

    select2 = Select(driver.find_element_by_id('ddlCourse'))
    options = select2.options
    select2.select_by_visible_text("Shaganappi Point (18)")

    number = driver.find_element_by_id("playerNumberGroup")
    number1 = number.find_elements_by_class_name("btn")
    number1[3].click()

    hole = driver.find_element_by_id("holeNumberGroup")
    hole1 = hole.find_elements_by_class_name("btn")
    hole1[1].click()



    driver.find_element_by_id("btnSubmit").click()
    time.sleep(4)

    data = driver.find_element_by_class_name("teeSheet")
    data1 = data.find_elements_by_class_name("col-xs-12")
    for i in data1:
            tee = i.get_attribute("teetime")

            if tee != None:
                if tee[0] == "2":
                    i.click()
                    time.sleep(5)
                    modal = driver.find_element_by_id("divSelectPlayersAndHole")
                    asd = modal.find_element_by_class_name("btn-primary")
                    driver.execute_script("arguments[0].click();", asd)
                    time.sleep(6)
                    driver.find_element_by_class_name("cbx-icon").click()
                    time.sleep(2)
                    driver.find_element_by_id("btnBook").click()
                    a=3

                else:
                    time.sleep(120)
                    pass
            else:
                pass
