import os
import platform
import requests
from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem



def get_platform():
    ops = platform.platform()[:3].lower()
    return ops


def get_advice():
    try:
        response = requests.get('http://fucking-great-advice.ru/api/random').json()
        return response["text"]
    except ConnectionError:
        pass


def get_key(Email):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    text = Email.encode('UTF-8')
    encrypted_text = cipher.encrypt(text)
    return encrypted_text.decode('UTF-8')


def get_company(TIN):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.get('https://egrul.nalog.ru/index.html')
        search_field = driver.find_element(By.ID, 'query')
        search_field.send_keys(TIN)
        search_btn = driver.find_element(By.ID, 'btnSearch')
        search_btn.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'op-excerpt')))
        search_result = driver.find_element(By.CLASS_NAME, 'op-excerpt')
        result = search_result.get_attribute('title')
        return {'status': 'OK', 'name': result, 'TIN': TIN}
    except TimeoutException as err:
        return {'status': 'NOT OK', 'err': err}



def iterate_row(parent_table, parent_column_logical_index: int,
                child_table, child_column_logical_index: int):
    child_table.setRowCount(parent_table.rowCount())
    for row_num in range(parent_table.rowCount()):
        child_table.setRowHeight(row_num, 40)
        item = parent_table.item(row_num, parent_column_logical_index)
        if item:
            data = item.data(Qt.ItemDataRole.UserRole)
            copy_item = QTableWidgetItem(item.text())
            copy_item.setData(Qt.ItemDataRole.UserRole, data)
            child_table.setItem(row_num, child_column_logical_index, copy_item)

def get_username():
    ops = platform.platform()[:3].lower()
    if ops == 'mac':
        os_login = (os.path.expanduser('~')).split('/')[-1]
        return os_login
    return os.getlogin()

