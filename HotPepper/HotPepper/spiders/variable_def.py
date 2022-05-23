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
from typing import Final as const


class Genre(object):
    
    HAIR: const[str] = 'hair'
    NEIL: const[str] = 'neil'
    RELAX: const[str] = 'relax'
    ESTHE: const[str] = 'esthetic'

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
    
    
    
    