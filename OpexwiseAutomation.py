from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    username_textbox_xpath = "//input[@formcontrolname='username']"
    password_textbox_xpath = "//input[@formcontrolname='password']"
    login_button_xpath = "//button[@class='btn btn-submit']"
    userprofile_xpath = "//li[@id='profile-views']"
    logoutbutton_xpath = "//button[@title='Logout']"
    logout_confusing_yes = "//button[@class='mat-focus-indicator cancel form-control mat-button mat-button-base'][2]"
    logout_confusing_no = "//button[@class='mat-focus-indicator cancel form-control mat-button mat-button-base'][1]"
    error_msg1 = "//*[@id='login']/div/div/div[2]/div/form/div[1]/div/div"
    error_msg2 = "//*[@id='login']/div/div/div[2]/div/form/div[2]/div/div"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def Username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def Click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_userprofile(self):
        self.driver.find_element(By.XPATH, self.userprofile_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logoutbutton_xpath).click()

    def click_yes(self):
        self.driver.find_element(By.XPATH, self.logout_confusing_yes).click()

    def click_no(self):
        self.driver.find_element(By.XPATH, self.logout_confusing_no).click()

    def msg1(self):
        self.driver.find_element(By.XPATH, self.error_msg1).text()

    def msg2(self):
        self.driver.find_element(By.XPATH, self.error_msg2).text()


class ConnectionPage:

    username_textbox_xpath = "//input[@formcontrolname='username']"
    password_textbox_xpath = "//input[@formcontrolname='password']"
    login_button_xpath = "//button[@class='btn btn-submit']"
    configuration_xpath = "//li[@id='Configuration']"
    connection_xpath = "(//span[text()='Connections'])[1]"
    refresh_xpath = "//button[@class='mat-focus-indicator createbtn refresh-btn form-control mat-button mat-button-base']"
    new_conn_xpath = "//button[@class='mat-focus-indicator createbtn form-control mat-button mat-button-base']"
    conn_host_name = "//input[@id='mat-input-2']"
    conn_port_num = "//input[@id='mat-input-3']"
    conn_username = "//input[@id='mat-input-4']"
    conn_password = "//input[@id='mat-input-5']"
    t_con_btn = "(//span[@class='mat-button-wrapper'])[6]"
    cancel_btn = "(//span[@class='mat-button-wrapper'])[7]"
    create_btn = "(//span[@class='mat-button-wrapper'])[8]"
    type_conn_drp = "//input[@formcontrolname='connectionType']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def SetUsername(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def SetPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def Login_click(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_config(self):
        self.driver.find_element(By.XPATH, self.configuration_xpath).click()

    def click_connection(self):
        self.driver.find_element(By.XPATH, self.connection_xpath).click()

    def click_refresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()

    def click_new_connection(self):
        self.driver.find_element(By.XPATH, self.new_conn_xpath).click()

    def Set_Host_name(self, hostname):
        self.driver.find_element(By.XPATH, self.conn_host_name).clear()
        self.driver.find_element(By.XPATH, self.conn_host_name).send_keys(hostname)

    def Set_port_num(self, portnum):
        self.driver.find_element(By.XPATH, self.conn_port_num).clear()
        self.driver.find_element(By.XPATH, self.conn_port_num).send_keys(portnum)

    def Set_conn_username(self, conneuname):
        self.driver.find_element(By.XPATH, self.conn_username).clear()
        self.driver.find_element(By.XPATH, self.conn_username).send_keys(conneuname)

    def Set_conn_password(self, connpassword):
        self.driver.find_element(By.XPATH, self.conn_password).clear()
        self.driver.find_element(By.XPATH, self.conn_password).send_keys(connpassword)

    def test_conn_btn(self):
        self.driver.find_element(By.XPATH, self.t_con_btn).click()

    def conn_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()

    def conn_create_btn(self):
        self.driver.find_element(By.XPATH, self.create_btn).click()




