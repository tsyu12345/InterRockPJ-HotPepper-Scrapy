#型関係
from __future__ import annotations
from typing import Any, Final as const

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from HotPepper.SeleniumMiddleware.AbsMiddleware import AbsLinkExtraction 

class Utils():
    
    def __init__(self) -> None:
        pass
    
    @classmethod 
    def driver_restart(cls, driver:webdriver.Chrome):
        driver.quit()
        #time.sleep(cls.RESTART_WAIT)
    
    @classmethod
    def DOM_wait(cls, driver:webdriver.Chrome, wait_time:int, term:str, attr:str):
        """_summary_\n
        指定秒数DOMの構築を待機する。
        Args:
            driver (webdriver.Chrome): webdriverインスタンス\n
            wait_time (int): 待機時間（秒）\n
            term (str): 基準の属性名{class, id, xpath, selector}\n
            attr (str): その属性値.selectorの場合はその文字列。\n
        """
        wait = WebDriverWait(driver, wait_time)
        if term == "class":
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, attr)))
        elif term == "id":
            wait.until(EC.presence_of_element_located((By.ID, attr)))
        elif term == "xpath":
            wait.until(EC.presence_of_element_located((By.XPATH, attr)))
        elif term == "selector":
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, attr)))
        else:
            raise NotAllowWaitTerm("指定された条件は未定義です。")
        
    @classmethod
    def wait_for_all_DOM(cls, driver:webdriver.Chrome) -> None:
        """_summary_\n
        全要素のロード完了を待機する。
        Args:
            driver (webdriver.Chrome): webdriverインスタンス
        """
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body")))
        
        
class NotAllowWaitTerm(Exception):
    """_summary_\n
    使用できないタームを指定した場合に発生する例外。
    """