from __future__ import annotations
from typing import Final as const
#Scrapy関係のインポート
from scrapy.crawler import CrawlerProcess 
from scrapy.utils.project import get_project_settings 
from scrapy.settings import Settings
from HotPepper.spiders.HTB import HtbSpider
class SpiderCall():
    
    #TODO:出力順に各itemの辞書を作成する。
    #FEED_EXPORT_FIELDS: const[list[str]] = [item_key for item_key in COLUMN_MENUS.keys()]
    FILE_FORMAT: const[str] = 'xlsx'
    FILE_EXTENSION: const[str] = '.' + FILE_FORMAT
    
    def __init__(self, target_pref_list:list[str], genre:str) -> None:
        """_summary_\n
        Args:
            target_pref_list (list[str]): 都道府県のリスト
            genre (str): ジャンル名
        """
        self.target_pref_list: const[list[str]] = target_pref_list
        self.genre: const[str] = genre
        self.settings: const[Settings] = self.__spider_setting()
        self.crawler = CrawlerProcess(self.settings)
        
        
    def __spider_setting(self) -> Settings:
        
        settings: Settings = get_project_settings()
        settings.set('FEED_FORMAT', self.FILE_FORMAT)
        settings.set('FEED_URI', '%(filename)s'  + self.FILE_EXTENSION)
        #settings.set('FEED_EXPORT_FIELDS', self.FEED_EXPORT_FIELDS)
        settings.set('TELNETCONSOLE_ENABLED', False)
        
        return settings
        
        
    def run(self) -> None:
        
        self.crawler.crawl(HtbSpider, self.target_pref_list[0], self.genre)
        self.crawler.start()
        
    
    
if __name__ == '__main__':
    
    test = SpiderCall(['高知県'], 'hair')
    test.run()
    
    