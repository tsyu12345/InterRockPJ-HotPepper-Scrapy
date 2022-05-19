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

class DOMSelector(object):
    
    RESULT_COUNT_DOM_WRAPPER: const[dict[str, str]] = {
        "hair": "div.preListHead",
        "neil": "",
        "relax": "",
        "esthetic": "",
    }
    
    RESULT_COUNT_DOM: const[dict[str, str]] = {
        "hair": RESULT_COUNT_DOM_WRAPPER["hair"]+" > p > span.numberOfResult",
        "neil": "div.",
        "relax": "div.",
        "esthetic": "div.",
    }
    
    RESULT_PAGE_COUNT_DOM: const[dict[str, str]] = {
        "hair": RESULT_COUNT_DOM_WRAPPER["hair"]+" > p.pa.bottom0.right0",
    }
    
    
    