import scrapy
from scrapy.http.response import Response


class HtbSpider(scrapy.Spider):
    name:str = 'HTB'
    allowed_domains:list[str] = ['beauty.hotpepper.jp']
    start_urls:list[str] = ['http://beauty.hotpepper.jp/']
    
    #TODO:freewordsearchから検索結果へScrapyで飛べるか検証すること

    def __init__(self) -> None:
        pass
    
    def start_requests(self):
        """_summary_\n
        初期リクエストを実行するメソッド
        """
        pass
    
    def call_request(self, response:Response) -> None:
        """_summary_\n
        検索結果一覧における各店舗ページのparseへのリクエストを実行
        """
        pass    
    
    def parse(self, response:Response) -> None:
        """_summary_\n
        店舗ページの対象タグ情報抽出処理
        """
        pass
