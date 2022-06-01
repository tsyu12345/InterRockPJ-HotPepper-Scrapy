#型関係
from __future__ import annotations
from typing import Any, Final as const, Tuple
#GUIモジュール
from Abstract import *
import PySimpleGUI as gui
import sys
sys.path.append('../')
from ..JisCode.jiscode import Jiscode


class AreaInput(AbsGUIComponent):
    """_summary_\n
    対象都道府県の入力オブジェクト.\n
    イベントキーは以下の通り\n
    ・エリア選択ボタン押下: BUTTON_KEY\n
    ・エリア入力: INPUT_KEY\n
    ・タイトルキー: TITLE_KEY\n
    
    """
    BUTTON_KEY: const[str] = "SELECTAREA"
    INPUT_KEY: const[str] = "AREAINPUT"
    TITLE_KEY: const[str] = "AREATITLE"
    
    def __init__(self) -> None:
        
        self.lay_out:const[list[list[Any]]] = self.__layout()
        self.titleText: list[gui.Text] = self.lay_out[0]
        self.Input: list[gui.InputText | gui.Button] = self.lay_out[1]
        
    def __layout(self) -> list[list[Any]]:
        
        L: const[list[Any]] = [
            [gui.Text("都道府県", key=self.TITLE_KEY, size=(60, None))],
            [gui.InputText(key=self.INPUT_KEY), gui.Button('エリア選択', key=self.BUTTON_KEY)],
        ]
        
        return L
    
class JunleInput(AbsGUIComponent):
    """_summary_\n
    対象ジャンルの入力オブジェクト。\n
    イベントキーは以下の通り\n
    ・ジャンル入力キー:INPUT_KEY\n
    ・タイトルキー:TITLE_KEY\n
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
        
        self.layout:const[list[list[Any]]] = self.__layout()
        self.titleText:list[gui.Text] = self.layout[0]
        self.select: list[gui.InputOptionMenu] = self.layout[1]
        
    def __layout(self) -> list[list[Any]]:
        
        L: const[list[Any]] = [
            [gui.Text("ジャンル", key=self.TITLE_KEY, size=(60, None))],
            [gui.InputOptionMenu(self.MENU, key=self.INPUT_KEY, size=(40, None))]
        ]
        
        return L

class PathInput(AbsGUIComponent):
    """_summary_\n
    保存先のパスを入力するオブジェクト。
    イベントキーは以下の通り\n
    ・入力値キー:INPUT_KEY\n
    ・参照ボタン押下キー:BUTTON_KEY\n
    ・タイトルキー:TITLE_KEY\n
    """
    
    INPUT_KEY: const[str] = "PATHINPUT"
    TITLE_KEY: const[str] = "PATHTITLE"
    BUTTON_KEY: const[str] = "PATHSELECT"
    FILE_FORMAT: Tuple[str, str] = ("Excelファイル", "*.xlsx")
    
    def __init__(self) -> None:
        
        self.layout:const[list[list[Any]]] = self.__layout()
        self.titleText:list[gui.Text] = self.layout[0]
        self.InputArea: list[gui.InputText | gui.Button] = self.layout[1]
    
    def __layout(self) -> list[list[Any]]:
        
        L: const[list[list[Any]]] = [
            [gui.Text("フォルダ選択", key=self.TITLE_KEY, size=(60, None))],
            [
                gui.InputText(key=self.INPUT_KEY), 
                gui.SaveAs("・・・", file_types=([self.FILE_FORMAT]), key=self.BUTTON_KEY)
            ]
        ]
        
        return L

class AreaSelectWindow(AbsWindowComponent):
    """_summary_\n
    都道府県選択画面.
    イベントキーは以下の通り\n
    ・完了ボタン押下: OK_KEY\n
    """
    OK_KEY: const[str] = "OK"
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.window = gui.Window(
            name, 
            layout=self.layout(),
            debugger_enabled=True
        )
        self.selected_prefecture: list[str] = []
        
    def layout(self) -> list[list[Any]]:
        #TODO:JISコードオブジェクトから都道府県リストを取得する
    
        all_strings:const[str] = Jiscode.get_all_prefecture_string()
        area_list: list[str] = all_strings.split(",")
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
    
    def __save_selected_prefecture(self) -> None:
        """_summary_\n
        選択された都道府県を保存する
        """
        for v in self.value.keys():
            if self.value[v] == True and v not in self.selected_prefecture:
                self.selected_prefecture.append(v)
        print("SELECTED AREA:", self.selected_prefecture)
        
    def get_selected_area(self, sep:str=",") -> str:
        """_summary_\n
        選択された都道府県を返す。
        Args:\n
            sep: 区切り文字
        """
        string:str = sep.join(self.selected_prefecture)
        return string
    
    def dispose(self) -> None:
        """_summary_\n
        ウィンドウを閉じた際のイベント処理
        """ 
        self.__save_selected_prefecture()
        self.window.close()


class MainMenu(AbsWindowComponent):
    """_summary_\n
    メインメニュー画面
    """
    EXECUTE_BTN_KEY: str = "execute"
    CUSTOM_WINDOW_TITLE: str = "抽出条件入力画面"
    
    def __init__(self, name: str="") -> None:
        super().__init__(name)
        
        self.area_module = AreaInput()
        self.junle_module = JunleInput()
        self.path_module = PathInput()
        
        self.lay_out = self.__layout()
        
        self.window = gui.Window(
            name+self.CUSTOM_WINDOW_TITLE,
            layout=self.lay_out,
            debugger_enabled=True
        )
        
    def __layout(self) -> list[list[Any]]:
        
        L:list[list[Any]] = [
            [
                gui.Frame(
                        "抽出条件", [
                            self.area_module.titleText, 
                            self.area_module.Input,
                            self.junle_module.titleText, 
                            self.junle_module.select,
                        ]
                    )
            ],
            [
                gui.Frame(
                    "保存先",
                    [
                        self.path_module.titleText,
                        self.path_module.InputArea
                    ]
                )
            ],
            [
                gui.Button("抽出開始", key=self.EXECUTE_BTN_KEY)
            ]
        ]
        
        return L
        
    def dispose(self) -> None:
        self.window.close()