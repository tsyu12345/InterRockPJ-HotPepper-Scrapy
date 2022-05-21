from __future__ import annotations
from typing import Final as const
from urllib import response
import scrapy
import re
from scrapy.http.response import Response
from .selector_dict import DOMSelector


class HtbSpider(scrapy.Spider):
    
    name:const[str] = 'HTB'
    allowed_domains:const[list[str]] = ['beauty.hotpepper.jp']
    start_urls:const[list[str]] = ['http://beauty.hotpepper.jp/']
    BASE_URL:const[str] = "https://beauty.hotpepper.jp/CSP/bt/freewordSearch/"
    
    #TODO:freewordsearchから検索結果へScrapyで飛べるか検証すること

    def __init__(self, target_pref:str, genre:str) -> None:
        """_summary_\n
        Args:\n
            target_pref (str): 抽出対象都道府県
            genre (str): 抽出対象ジャンル
        """
        self.target_pref: const[str] = target_pref
        self.genre: const[str] = genre
        self.start_url: str = self.BASE_URL + f'?freeword={self.target_pref}&searchT=検索&genreAlias={self.genre}'
    
    def start_requests(self):
        """_summary_\n
        初期リクエストを実行するメソッド
        指定都道府県とジャンル名で検索する。
        """
        yield scrapy.Request(self.start_url, callback=self.search_request)
    
    
    def search_request(self, response):
        """_summary_\n
        都道府県別の検索結果一覧にて各店舗ページのリンクが存在する限りparseへのリクエストを実行
        """
        page_count: const[int] = self.__get_total_page_count(response)
        
        for current_page in range(1, page_count+1):
            target_class:const[str] = 'slnName' if self.genre == 'hair' else 'slcHead' 
            target_link_list:const[list[str]] = response.css(f"h3.{target_class} > a::attr(href)").getall()
        
            for url in target_link_list:
                print(url)
                yield scrapy.Request(url, callback=self.parse)

            next_page_url: const[str] = self.BASE_URL + f'?freeword={self.target_pref}&searchGender=ALL&genreAlias={self.genre}&pn={current_page+1}'
            scrapy.Request(next_page_url)

    
    def parse(self, response:Response) -> None:
        """_summary_\n
        店舗ページの対象タグ情報抽出処理
        """
        pass
    
    
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
            print(response.css(selector+"::text"))
            counter_text: const[str] = response.css(selector+"::text").extract_first()
            print("COUNTER_TEXT:", counter_text)
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
        
    
        