#型関係
from __future__ import annotations
from typing import Any, Final as const
from abc import abstractmethod, ABCMeta
#selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
#Other
import time

class AbsLinkExtraction(object, metaclass=ABCMeta):
    """
    SpiderにクロールするURLを収集するためのミドルウェアオブジェクト。
    その抽象クラス。
    """
    RETRY_UPPER: const[int] = 3
    DOM_WAIT_TIME: const[int] = 10 #秒 
    RESTART_WAIT: const[int] = 300 #再起動後の待機時間ミリ秒
    DRIVER_PATH: const[str] = "" #TODO:最新安定板のドライバをインストールし呼び出す。
    BROTHER_PATH: const[str] = "" #TODO:ドライバのバージョンに合わせてchromiumをインストールする。
    OPTIONS_ARGS: list[str] = [
        "start-maximized",
        "enable-automation",
        "--no-sandbox",
        "--disable-infobars",
        '--disable-extensions',
        "--disable-dev-shm-usage",
        "--disable-browser-side-navigation",
        "--disable-gpu",
        '--ignore-certificate-errors',
        '--ignore-ssl-errors'
    ]
    PROFILE_OPTION: const[dict[str, int]] = {
        "profile.default_content_setting_values.notifications": 2
    }
    
    TOP_PAGE: const[str] = "https://beauty.hotpepper.jp/top/"
    
    
    def __init__(self, headless_mode:bool=True) -> None:
        """_summary_\n
        コンストラクタ。ドライバの初期化を行う。
        Args:
            headless_mode (bool, optional):activate headless mode. Defaults to True.
        """
        self.options:Options = webdriver.ChromeOptions() #type: ignore
        if headless_mode:
            self.OPTIONS_ARGS.append("--headless")
        
        for args in self.OPTIONS_ARGS:
            self.options.add_argument(args)
        
        self.options.binary_location = self.BROTHER_PATH
        self.options.add_experimental_option("prefs",self.PROFILE_OPTION)
        
    
    
    
    @abstractmethod
    def extration(self) -> list[str]:
        """_summary_\n
        クロール対象URLをスクレイピングし、結果を返す。
        Returns:
            list[str]: URL文字列のリスト。
        """
        pass
    
    
    
        



