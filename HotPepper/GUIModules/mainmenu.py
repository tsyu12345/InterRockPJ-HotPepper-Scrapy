#型関係
from __future__ import annotations
from typing import Any, Final as const
#GUIモジュール
from Abstract import *
import PySimpleGUI as gui
import sys
sys.path.append('../')
from ..JisCode.jiscode import JisCode

class AreaInput(AbsGUIComponent):
    """_summary_\n
    対象都道府県の入力オブジェクト
    """
    BUTTON_KEY: const[str] = "SELECTAREA"
    INPUT_KEY: const[str] = "AREAINPUT"
    TITLE_KEY: const[str] = "AREATITLE"
    
    def __init__(self) -> None:
        
        self.layout:const[list[list[Any]]] = self.__layout__()
        
    def __layout__(self) -> list[list[Any]]:
        
        L: const[list[Any]] = [
            [gui.Text("都道府県", key=self.TITLE_KEY, size=(60, None))],
            [gui.InputText(key=self.INPUT_KEY), gui.Button('エリア選択', key=self.BUTTON_KEY)],
        ]
        
        return L
    
class JunleInput(AbsGUIComponent):
    """_summary_\n
    対象ジャンルの入力オブジェクト
    """
    
    INPUT_KEY: const[str] = "JUNLEINPUT"
    TITLE_KEY: const[str] = "JUNLETITLE"
    MENU: const[list[str]] = [
        "ヘアサロン",
        "ネイル・まつげサロン",
        "リラクサロン",
        "エステサロン",
        "すべてのジャンル"
    ]
    
    def __init__(self) -> None:
        
        self.layout:const[list[list[Any]]] = self.__layout__()
        
    def __layout__(self) -> list[list[Any]]:
        
        L: const[list[Any]] = [
            [gui.Text("ジャンル", key=self.TITLE_KEY, size=(60, None))],
            [gui.InputOptionMenu(self.MENU, key=self.INPUT_KEY, size=(40, None))]
        ]
        
        return L

class PathInput(AbsGUIComponent):
    """_summary_\n
    保存先のパスを入力するオブジェクト。
    """
    
    INPUT_KEY: const[str] = "PATHINPUT"
    TITLE_KEY: const[str] = "PATHTITLE"
    BUTTON_KEY: const[str] = "PATHSELECT"
    
    def __init__(self) -> None:
        
        self.layout:const[list[list[Any]]] = self.__layout__()
    
    def __layout__(self) -> list[list[Any]]:
        
        L: const[list[list[Any]]] = [
            [gui.Text("フォルダ選択", key=self.TITLE_KEY, size=(60, None))],
            [
                gui.InputText(key=self.INPUT_KEY), 
                gui.SaveAs("・・・", file_types=([('Excelファイル', '*.xlsx')]), key=self.BUTTON_KEY)
            ]
        ]
        
        return L

class AreaSelectWindow(AbsWindowComponent):
    """_summary_\n
    都道府県選択画面
    """
    OK_KEY: const[str] = "OK"
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
    def __layout__(self) -> list[list[Any]]:
        
        area_list: list[str] #TODO:JISコードオブジェクトから都道府県リストを取得する
        L: list[list[Any]] = []
        cnt: int = 0
        for i in range(8):
            add = []
            for j in range(6):
                if cnt != 47:
                    add.append(gui.Checkbox(area_list[cnt], key=area_list[cnt]))
                    cnt += 1
            L.append(add)
        L.append([gui.Button('OK', key=self.OK_KEY)])
        
        return L


class MainMenu(AbsWindowComponent):
    """_summary_\n
    メインメニュー画面
    """
    
    def __init__(self, name: str) -> None:
        super().__init__(name)