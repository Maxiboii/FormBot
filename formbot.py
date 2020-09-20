from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Google:

    def __init__(self,username,password):
        link = input('Enter the link: ')
        try:
            self.driver=webdriver.Chrome('/Users/Max/Desktop/Code/Selenium/chromedriver')
        except:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome('/home/maksimchichkan90/Downloads/chromedriver', chrome_options=chrome_options)
        #self.driver.get('https://stackoverflow.com/users/login') #stack
        self.driver.get('https://www.coursera.org/?authMode=login') #coursera
        original_window = self.driver.current_window_handle #coursera
        sleep(5)
        #self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click() #stack
        self.driver.find_element_by_xpath('//*[@id="authentication-box-content"]/div/div[1]/div[1]/button/span').click() #coursera
        sleep(5)
        for window_handle in self.driver.window_handles: #coursera
            if window_handle != original_window: #coursera
                self.driver.switch_to.window(window_handle) #coursera
                break  #coursera
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        #self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click() #stack
        sleep(5)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        # self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click() #stack
        sleep(5)
        self.driver.switch_to.window(original_window) #coursera
        self.driver.get(link)
        self.next_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="i5"]/div[3]/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="i11"]/div[3]/div').click()
        self.driver.find_element_by_xpath(self.next_button).click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="i8"]/div[3]/div').click()
        self.driver.find_element_by_xpath(self.next_button).click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/label[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/label[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/label[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/label[3]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/label[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[12]/label[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/label[2]/div/div').click()

        self.driver.find_element_by_xpath('//*[@id="i19"]/div[3]/div').click()

        x = input('quit? (y/n) ')
        if x == 'y':
            self.driver.quit()


passw = open('passw.txt',"r",encoding="utf-8")
password=str(passw.read())
user=open('user.txt',"r",encoding="utf-8")
username=str(user.read())
mylike = Google(username,password)
