from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless=True
Path="database\\chromedriver.exe"
driver= webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()


website=r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
buttonselection=Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
buttonselection.select_by_visible_text('British English / Brian')


def speak(Text):
    l=len(str(Text))
    if l==0:
        pass
    else:
        print("")
        print(f"Jarvis : {Text}")

        print("")
        data=str(Text)
        xpathofsec='/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()


        if l>=30:
            sleep(4)
        elif l>=40:
            sleep(6)
        elif l>=55:
            sleep(8)
        elif l>=70:
            sleep(10)
        elif l>=100:
            sleep(13)
        elif l>=120:
            sleep(14)
        else:
            sleep(2)



speak("hello sir")     


