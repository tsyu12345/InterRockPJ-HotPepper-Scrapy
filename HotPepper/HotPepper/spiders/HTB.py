from __future__ import annotations
from typing import Final as const

import scrapy
from scrapy.http import Response
import re
from HotPepper.items import HotpepperItem

from variable_def import DOMSelector, Genre
class HtbSpider(scrapy.Spider):
    
    name:const[str] = 'HTB'
    allowed_domains:const[list[str]] = ['beauty.hotpepper.jp']
    start_urls:const[list[str]] = ['http://beauty.hotpepper.jp/']
    BASE_URL:const[str] = "https://beauty.hotpepper.jp/CSP/bt/freewordSearch/"
    
    #Done:freewordsearchから検索結果へScrapyで飛べるか検証すること -> 飛べる。

    def __init__(self, target_pref:str, genre:str) -> None:
        """_summary_\n
        Args:\n
            target_pref (str): 抽出対象都道府県
            genre (str): 抽出対象ジャンル
        """
        self.target_pref: const[str] = target_pref
        self.genre: const[str] = Genre(genre).genre
        
        self.start_url: str = self.BASE_URL + f'?freeword={self.target_pref}&searchT=検索&genreAlias={self.genre}'
    
    def start_requests(self):
        """_summary_\n
        初期リクエストを実行するメソッド
        指定都道府県とジャンル名で検索する。
        """
        yield scrapy.Request(self.start_url, callback=self.__search_transition)
    
    
    def __search_transition(self, response):
        """_summary_
        検索結果一覧のページ処理。ページが存在する限り、次の検索結果ページへ遷移する。
        """
        page_count: const[int] = self.__get_total_page_count(response)

        for current_page_num in range(1, page_count+1):
            url: const[str] = self.BASE_URL + f'?freeword={self.target_pref}&searchGender=ALL&genreAlias={self.genre}&pn={current_page_num}'
            print("Request for ", url)
            yield scrapy.Request(url, callback=self.__storePage_transition)

        
    
    
    def __storePage_transition(self, response):
        """_summary_\n
        都道府県別の検索結果一覧にて各店舗ページのリンクが存在する限りparseへのリクエストを実行
        """
        target_class:const[str] = 'slnName' if self.genre == Genre.HAIR else 'slcHead' 
        target_link_list:const[list[str]] = response.css(f"h3.{target_class} > a::attr(href)").getall()
        for url in target_link_list:
            yield scrapy.Request(url, callback=self.parse)

    
    def parse(self, response) -> None:
        """_summary_\n
        店舗ページの対象タグ情報抽出処理
        """
        item: HotpepperItem = HotpepperItem()
        #genre
        item['genre'] = Genre.parse_genre_japanese(self.genre)
        #name
        item['name'] = response.css(DOMSelector.STORE_NAME[self.genre]).get()
        #kana
        item['kana'] = response.css(DOMSelector.NAME_KANA[self.genre]).get()
        
        
        #tel
        
        #area
        
        #jiscode
        
        #address
        
        #url
        
        #data_date
        
        #store_homepage
        
        #pankuzu
        
        #is_headerimg
        
        #is_kodawari
        
        #slideimg_coun
        
        #catchcopy
        
        #access_info
        
        #business_hours
        
        #regular_holiday
        
        #payment
        
        #facility
        
        #price
        
        #seat_count
        
        #stuff_count
        
        #parking
        
        #kodawari
        
        #note
        
        #reculute
        
        
    
    ## private methods ##
    
    def __table_extraction(self, response, target:str) -> str | None:
        """_summary_\n
        店舗ページのテーブルから情報を抽出する。\n
        Args:\n
            response\n
            menu (str): 対象の列名\n
        """
        table:const = response.css(DOMSelector.TABLE[self.genre])
        th: const[list[str]] = table.css("tr > th::text").getall()
        for menu in th:
            if menu == target:
                return table.css("tr > td::text").get()
            
        return None
    
    
    def __get_total_store_count(self, response) -> int:
        """_summary_\n
        検索結果一覧にある、店舗総数を取得する
        Args:
            response (Response): Responseオブジェクト

        Returns:
            int: 検索結果一覧にある、店舗総数
        """
        selector: const[str] = DOMSelector.RESULT_COUNT_DOM[self.genre]
        counter_text: const[str] = response.css(selector+"::text").get()
        try:
            counter = int(counter_text)
        except ValueError:
            raise ValueError("検索結果一覧にある、店舗総数が数値ではない、あるいは、数値変換に失敗しました。")
        else:
            return counter
        
        
    def __get_total_page_count(self, response) -> int:
        """_summary_\n
        検索結果一覧にある、ページ総数を取得する
        """
        selector: const[str] = DOMSelector.RESULT_PAGE_COUNT_DOM[self.genre]
        try:
            #print(response.css(selector+"::text"))
            counter_text: const[str] = response.css(selector+"::text").extract_first()
            #print("COUNTER_TEXT:", counter_text)
        except TypeError:
            raise TypeError("検索結果一覧にある、ページ総数が取得できませんでした。")
        
        page_text_all:const[list[str]] = re.split('[/ ]', counter_text)
        page_text:const[str] = re.sub(r"\D", "", page_text_all[1])
        try:
            if page_text is not None:
                counter = int(page_text)
        except ValueError:
            raise ValueError("検索結果一覧にある、ページ総数が数値ではない、あるいは、数値変換に失敗しました。")
        else:
            return counter
        
    
        