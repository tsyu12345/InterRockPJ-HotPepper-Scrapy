# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class HotpepperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #各店舗ページでの抽出項目定義
    
    genre = Field() #ジャンル
    name = Field() #店舗名
    kana = Field() #店舗名カナ
    tel = Field() #電話番号
    area = Field() #都道府県
    jiscode = Field() #JISコード
    address = Field() #住所(市区町村)
    url = Field() #ページURL
    data_date = Field() #データ更新日
    store_homepage = Field() #店舗ホームページ
    pankuzu = Field() #パンクズヘッダー
    is_headerimg = Field() #ヘッダー画像有無
    is_kodawari = Field() #こだわり有無
    slideimg_count = Field() #スライド画像数
    catchcopy = Field() #キャッチコピー
    access_info = Field() #アクセス
    business_hours = Field() #営業時間
    regular_holiday = Field() #定休日
    payment = Field() #支払方法
    facility = Field() #設備
    price = Field() #価格
    seat_count = Field() #座席数
    stuff_count = Field() #スタッフ数
    parking = Field() #駐車場
    kodawari = Field() #こだわり
    note = Field() #備考
    reculute = Field() #採用情報
    
        
    
    
