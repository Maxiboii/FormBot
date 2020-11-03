# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class Google:

    def __init__(self,username, password, link):
        self.username = username
        self.password = password
        self.link = link

    def fillForm(self):
        try:
            self.driver=webdriver.Chrome('/Users/Max/Desktop/Code/Selenium/chromedriver')
        except:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome('/home/maksimchichkan90/Downloads/chromedriver', chrome_options=chrome_options)

        try:
            self.driver.get('https://www.coursera.org/?authMode=login') #coursera
            original_window = self.driver.current_window_handle #coursera
            sleep(5)
            self.driver.find_element_by_xpath('//*[@id="authentication-box-content"]/div/div[1]/div[1]/button/span').click() #coursera
            sleep(5)
            for window_handle in self.driver.window_handles: #coursera
                if window_handle != original_window: #coursera
                    self.driver.switch_to.window(window_handle) #coursera
                    break  #coursera
            self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(Keys.RETURN)
            sleep(5)
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(Keys.RETURN)
            sleep(5)
            self.driver.switch_to.window(original_window) #coursera
            self.driver.get(self.link)
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

            sleep(30)
            self.driver.quit()
            return True
        except:
            self.driver.quit()
            return False


class Ui_Formbot(object):
    def setupUi(self, Formbot):
        Formbot.setObjectName("Formbot")
        Formbot.setEnabled(True)
        Formbot.resize(630, 441)
        self.centralwidget = QtWidgets.QWidget(Formbot)
        self.centralwidget.setObjectName("centralwidget")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(40, 290, 221, 31))
        self.goButton.setObjectName("goButton")
        self.emailField = QtWidgets.QLineEdit(self.centralwidget)
        self.emailField.setGeometry(QtCore.QRect(40, 110, 221, 21))
        self.emailField.setObjectName("emailField")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(40, 170, 221, 21))
        self.passwordField.setObjectName("passwordField")
        self.linkField = QtWidgets.QLineEdit(self.centralwidget)
        self.linkField.setGeometry(QtCore.QRect(40, 230, 221, 21))
        self.linkField.setObjectName("linkField")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.log = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(290, 10, 331, 381))
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        Formbot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Formbot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 22))
        self.menubar.setObjectName("menubar")
        Formbot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Formbot)
        self.statusbar.setObjectName("statusbar")
        Formbot.setStatusBar(self.statusbar)
        self.actionOther = QtWidgets.QAction(Formbot)
        self.actionOther.setObjectName("actionOther")

        self.retranslateUi(Formbot)
        QtCore.QMetaObject.connectSlotsByName(Formbot)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Formbot):
        _translate = QtCore.QCoreApplication.translate
        Formbot.setWindowTitle(_translate("Formbot", "Formbot"))
        self.goButton.setText(_translate("Formbot", "Go"))
        self.label_2.setText(_translate("Formbot", "Formbot v.1"))
        self.label_3.setText(_translate("Formbot", "Email"))
        self.label_4.setText(_translate("Formbot", "Password"))
        self.label_5.setText(_translate("Formbot", "Link"))
        self.log.setPlainText(_translate("Formbot", "Log"))
        self.actionOther.setText(_translate("Formbot", "Other"))


        self.goButton.clicked.connect(self.go)
    def go(self):
        usern = self.emailField.text()
        passw = self.passwordField.text()
        l = self.linkField.text()
        self.log.appendPlainText('Got the data')
        self.log.appendPlainText('Working...')
        myBot = Google(usern,passw,l)
        if myBot.fillForm():
            self.log.appendPlainText('Success!')
        else:
            self.log.appendPlainText('Error')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formbot = QtWidgets.QMainWindow()
    ui = Ui_Formbot()
    ui.setupUi(Formbot)
    Formbot.show()
    sys.exit(app.exec_())