"""_summary_\n
各ジャンルごとの、スクレイピングを行う際
ジャンルごとに微妙にDOMのセレクタが異なるので、
この定義ファイルで、DOMのセレクタを定義する。\n
<構成定義>\n
任意のターゲット {\n
    "hair":"DOMのセレクタ",\n
    "neil":"DOMのセレクタ",\n
    "relax":"DOMのセレクタ",\n
    "esthetic":"DOMのセレクタ",\n
}\n
"""
from __future__ import annotations
from re import S
from typing import Final as const


class Genre(object):
    
    HAIR: const[str] = 'hair'
    NEIL: const[str] = 'neil'
    RELAX: const[str] = 'relax'
    ESTHE: const[str] = 'esthetic'

    def __init__(self, genre:str) -> None:
        """_summary_\n
        Args:\n
            genre (str): 抽出対象ジャンル
        """
        self.genre: str
        
        if genre == "h":
            self.genre = self.HAIR
        elif genre == "n":
            self.genre = self.NEIL
        elif genre == "r":
            self.genre = self.RELAX
        elif genre == "e":
            self.genre = self.ESTHE
        else:
            raise ValueError("Invalid genre")
    
    @classmethod
    def parse_genre_japanese(cls, genre:str) -> str:
        """_summary_\n
        ジャンルオブジェクトを日本語変換する。
        Args:
            genre (Genre): ジャンルオブジェクト
        Returns:
            str: 日本語ジャンル名
        """
        if genre == cls.HAIR:
            return 'ヘアサロン'
        elif genre == cls.NEIL:
            return 'ネイルサロン'
        elif genre == cls.RELAX:
            return "リラクサロン"
        elif genre == cls.ESTHE:
            return "エステサロン"
        else:
            raise ValueError("Invalid genre")
    
class DOMSelector(object):
    
    
    RESULT_COUNT_DOM_WRAPPER: const[dict[str, str]] = {
        Genre.HAIR: "div.preListHead > div.pr",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    RESULT_COUNT_DOM: const[dict[str, str]] = {
        Genre.HAIR: RESULT_COUNT_DOM_WRAPPER['hair'] +" > p > span.numberOfResult",
        Genre.NEIL: "div.",
        Genre.RELAX: "div.",
        Genre.ESTHE: "div.",
    }
    
    RESULT_PAGE_COUNT_DOM: const[dict[str, str]] = {
        Genre.HAIR: RESULT_COUNT_DOM_WRAPPER[Genre.HAIR]+" > p.pa.bottom0.right0",
    }
    
    #店舗ページでの抽出タグ#
    STORE_NAME: const[dict[str, str]] = {
        Genre.HAIR: "div.sprtHeaderInner.pV10.pR5 > p.detailTitle",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    
    NAME_KANA: const[dict[str, str]] = {
        Genre.HAIR:"div.sprtHeaderInner.pV10.pR5 > p.fs10.fgGray",
        Genre.NEIL:"",
        Genre.RELAX:"",
        Genre.ESTHE:"",
    }
    
    
    TABLE: const[dict[str, str]] = {
        Genre.HAIR: "table.slnDataTbl",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    
    
    PANKUZU: const[dict[str, str]] = {
        Genre.HAIR: "div#preContents > ol > li > a",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    HEADER_IMG: const[dict[str, str]] = {
        Genre.HAIR: "#jsiNavCarousel",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    
    SLIDE_IMG: const[dict[str, str]] = {
        Genre.HAIR: "ul.slnTopImgCarousel.jscThumb > li",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    CATCH_COPY: const[dict[str, str]] = {
        Genre.HAIR: "p.shopCatchCopy > b > strong",
        Genre.NEIL: "",
        Genre.RELAX: "",
        Genre.ESTHE: "",
    }
    
    
    
    
    
    