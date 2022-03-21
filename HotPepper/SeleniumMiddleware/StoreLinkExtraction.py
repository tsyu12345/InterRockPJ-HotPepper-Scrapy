from AbsMiddleware import AbsLinkExtraction
from __future__ import annotations
from typing import Final as const, Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from Utils import Utils

from multiprocessing import Pool, freeze_support


class StoreLinkExtraction(AbsLinkExtraction):
    """
    ミドルウェア本体。実装クラス。\n
    GUIからの抽出条件を受け取り、各店舗のページURLをスクレイピングする。
    """
    HAIRSALON: const[str] = "ヘアサロン"
    NAILSALON: const[str] = "ネイルサロン"
    RELAXSALON: const[str] = "リラクサロン"
    ESTHETIC: const[str] = "エステサロン"
    
    
    def __init__(self, target_area: str, genre:str, headless_mode: bool = True) -> None:
        """_summary_\n
        Args:
            target_area (str): クロール対象都道府県\n
            genre (str): クロール対象ジャンル\n
            headless_mode (bool, optional):. Defaults to True.\n
        """
        super().__init__(headless_mode)
        self.target_area = target_area
        self.genre = genre
        self.result_list: list[str] = []
        self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH, options=self.options) #type: ignore
    
    def extarction(self) -> list[str]: #←呼び出し可能メソッド
        #DO SOMETHING...
        self.__start()
        self.__move_genre_page()
        #TODO:ここで各店舗のaタグを取得し、それをリストに格納する。
        return self.result_list
    
    #private method群↓
    
    def __start(self) -> None:
        """_summary_\n
        ブラウザリクエストを開始する。
        """
        self.driver.get(self.TOP_PAGE)
        Utils.DOM_wait(self.driver, self.DOM_WAIT_TIME, "id", "logoNavi") #TOPページのメニューバーを待機。
    
    
    def __move_genre_page(self) -> None:
        """_summary_\n
        指定ジャンルページに移動する。
        """
        nav_menu:list[WebElement] = self.driver.find_elements_by_css_selector('#logoNavi > ul.move.cFix.globalNavi > li > a')
        if nav_menu != []: #when nav_menu is not empty
            for a in nav_menu:
                if a.text == self.genre:
                    url:str = a.get_attribute('href')
                    self.driver.get(url)
                    Utils.wait_for_all_DOM(self.driver) #ジャンルページを待機。
                    break
        else:
            raise NoSuchElementException(
                "ジャンルのナビゲーションバーが見つからないため、" + self.genre + "のジャンルページに移動できませんでした。"
            )
            
            
    def __input_area(self) -> None:
        """_summary_\n
        入力ボックスにターゲット値を入れ、検索を開始する。
        """
        input_id: str
        if self.genre == self.HAIRSALON:
            input_id = "freeWordSearch1"
        else:
            input_id = "freeWordSearch2"
        
        input_elm: WebElement = self.driver.find_element_by_id(input_id)
        #TODO:ここで入力ボックスにターゲット値を入れる。
        #MEMO:各店舗のURL抽出は、Scrapy単体でできそう。JS無くてもリンク乗ってた。
        
    def __next_page(self) -> None:
        """_summary_\n
        次のページへ移動する。
        """
        pass
    
    
        
        
        
    
    
    
    
        