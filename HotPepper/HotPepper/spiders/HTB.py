from __future__ import annotations
from email.generator import Generator
from typing import Final as const
import scrapy
from scrapy.http.response import Response


class HtbSpider(scrapy.Spider):
    
    name:str = 'HTB'
    allowed_domains:list[str] = ['beauty.hotpepper.jp']
    start_urls:list[str] = ['http://beauty.hotpepper.jp/']
    
    #TODO:freewordsearchから検索結果へScrapyで飛べるか検証すること

    def __init__(self, target_pref:str, genre:str) -> None:
        """_summary_\n
        Args:\n
            target_pref (str): 抽出対象都道府県
            genre (str): 抽出対象ジャンル
        """
        self.target_pref: const[str] = target_pref
        self.genre: const[str] = genre
        self.start_url: str = f'https://beauty.hotpepper.jp/CSP/bt/freewordSearch/?freeword={self.target_pref}&searchT=検索&genreAlias={self.genre}'
    
    def start_requests(self):
        """_summary_\n
        初期リクエストを実行するメソッド
        """
        yield scrapy.Request(self.start_url, callback=self.search_request)
    
    
    def search_request(self, response:Response) -> None:
        """_summary_\n
        都道府県別の検索結果一覧にて各店舗ページのリンクが存在する限りparseへのリクエストを実行
        """
        target_class:const[str] = 'slnName' if self.genre == 'hair' else 'slcHead' 
        target_link_list = response.css(f"h3.{target_class} > a::attr(href)").getall()
        print(target_link_list)
        
            
    
    
    def parse(self, response:Response) -> None:
        """_summary_\n
        店舗ページの対象タグ情報抽出処理
        """
        pass
