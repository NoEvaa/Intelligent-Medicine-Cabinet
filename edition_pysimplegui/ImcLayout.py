# -*- coding: utf-8 -*-
"""
Welcome to NPark
2布局层
提供ui界面生成接口
"""
import PySimpleGUI as sg
import pandas as pd
from ImcSys import ImcSys
from ImcInf import Pic, ElemSize, FilePath

class ImcLayout(ImcSys):
    def __init__(self):
        ImcSys.__init__(self)
        sg.ChangeLookAndFeel('Topanga')
        self.pic = Pic() #素材库
        self.size = ElemSize() #尺寸库
    def win0(self): #待机界面
        return self.create_win(self.layout_win0())
    def win1(self): #认证界面
        return self.create_win(self.layout_win1(), 'IMC-fr', 0)
    def win2(self): #控制界面
        return self.create_win(self.layout_win2(), 'IMC-cp', 0)
    def win3(self): #日志界面
        return self.create_win(self.layout_win3(), 'IMC-lg')
    def win4(self): #设置界面
        return self.create_win(self.layout_win4(), 'IMC-st')
    def create_win(self, layout=[[]], name='IMC', r_e = 1):
        if r_e:
            rcm = [[''], ['Exit',]]
        else:
            rcm = None
        winm = sg.Window(name, layout, no_titlebar=True, finalize=True, keep_on_top=True, right_click_menu=rcm)
        winm.Maximize()
        winm.set_cursor('no')
        return winm
    def layout_win0(self):
        layout = [[sg.T('当前时间:'), sg.T(size=(20, 1), key='-TIME-')]]
        layout += [[sg.T(' '  * 1)]]
        layout += [[sg.T(' '  * 10), 
                    sg.Column([[sg.Frame('全景图', [[sg.Image(key='-FRV1-')]])], 
                               [sg.T(' ')], [sg.T(' ')], 
                               [sg.Frame('药剂监视器', [[sg.Image(key='-FRV2-')]])]], 
                              element_justification='c'),
                    sg.T(' '  * 50), 
                    sg.Column([[sg.T(' '  * 1)], [sg.T(' '  * 1)], 
                               [sg.Button('', image_data=self.pic.img_data['btn_void'], image_subsample=10, button_color=(self.pic.color[4], self.pic.color[4]), key='Void', border_width=0),], 
                               [sg.T(' '  * 1)], [sg.T(' '  * 1)], 
                               [sg.Button('开柜', image_data=self.pic.img_data['btn_main'], button_color=('grey20', self.pic.color[4]), key='Open', border_width=0, font='宋体 20'),], 
                               [sg.T(' '  * 1)], [sg.T(' '  * 1)], 
                               [sg.Button('日志', image_data=self.pic.img_data['btn_main'], button_color=('grey20', self.pic.color[4]), key='Log', border_width=0, font='宋体 20')],
                               [sg.T(' '  * 1)], [sg.T(' '  * 1)], 
                               [sg.Button('设置', image_data=self.pic.img_data['btn_main'], button_color=('grey20', self.pic.color[4]), key='Setting', border_width=0, font='宋体 20')]]),
                  ]]
        return layout
    def layout_win1(self):
        layout = [[sg.Button('', image_data=self.pic.img_data['btn_back'], button_color=('white', self.pic.color[4]), key='Back', border_width=0)]]
        layout += [[sg.T(' ')]]
        layout += [[sg.T(' '  * 10),
                   self.layout_win1_cam(), 
                   sg.T(' '  * 5),
                   self.layout_win1_part()]
                  ]
        return layout
    def layout_win1_part(self):
        font = self.size.size_font[1]
        elem = self.size.size_elem[1]
        return sg.Frame('识别结果',[[sg.Frame('申请人1',[[sg.T('姓名:', size=elem[0], font=font[0]),sg.T(size=elem[1], key=('NAM', '1'), font=font[0])],
                                                        [sg.T('ID:', size=elem[0], font=font[1]),sg.T(size=elem[1], key=('ID', '1'), font=font[1])],
                                                        [sg.Image(key=('POR', '1'))],
                                                        [sg.T('状态:', size=elem[0], font=font[0]),sg.T('', size=elem[1], key=('SAT', '1'), font=font[0])]], font=font[2])],
                                    [sg.Frame('申请人2',[[sg.T('姓名:', size=elem[0], font=font[0]),sg.T('', size=elem[1], key=('NAM', '2'), font=font[0])],
                                                        [sg.T('ID:', size=elem[0], font=font[1]),sg.T('', size=elem[1], key=('ID', '2'), font=font[1])],
                                                        [sg.Image(key=('POR', '2'))],
                                                        [sg.T('状态:', size=elem[0], font=font[0]),sg.T('', size=elem[1], key=('SAT', '2'), font=font[0])]], font=font[2])],
                                    [sg.T(' ')],[sg.T(' ')],
                                    [sg.T(' '*20), sg.Button('', image_data=self.pic.img_data['btn_yes'], button_color=('aquamarine', self.pic.color[4]), key='Yes', border_width=0), 
                                     sg.T(' '*30), sg.Button('', image_data=self.pic.img_data['btn_no'], button_color=('aquamarine', self.pic.color[4]), key='No', border_width=0)],
                                    [sg.T(' ')],])
    def layout_win2(self):
        layout  = [[sg.Button('', image_data=self.pic.img_data['btn_back'], button_color=('white', self.pic.color[4]), key='Back', border_width=0), sg.T(' ' * 16), sg.T('',key='-TIME-',font='any 30',text_color='red')]]
        layout += [[sg.T(' ')]]
        layout += [[sg.T(' '  * 10),
                    self.layout_win2_cam(),
                    sg.T(' '  * 10),
                    self.layout_win2_part()
                    ]]
        return layout
    def layout_win2_part(self):
        font = self.size.size_font[2]
        return sg.Column([[sg.Frame('', [[sg.LBox([], size=(23,12), key='-COUNTER-',font=font[0])]])], 
                          [sg.T(' ')],
                          [sg.T(' ')],
                          [sg.T(' ')],
                          [sg.Button(image_data=self.pic.img_data['btn_put'] if self.state[1] else self.pic.img_data['btn_get'], 
                                     key='-Act-', border_width=0,
                                     button_color=(self.pic.color[4], self.pic.color[4]),
                                     metadata=self.state[1])], 
                          [sg.T(' ')],
                          [sg.T(' ')],
                          [sg.T(' ')],
                          [sg.T(' '  * 1), sg.T('柜门 ',font=font[1]), 
                           sg.Button(image_data=self.pic.img_data['btn_off'] if self.state[0] else self.pic.img_data['btn_on'], 
                                     key='-Switch-', border_width=0,
                                     button_color=(self.pic.color[4], self.pic.color[4]),
                                     metadata=self.state[0])]], 
                         element_justification='c')
    def layout_win1_cam(self):
        return sg.Column([[sg.Frame('全景图', [[sg.Image(key='-FRV1-')]]), sg.T(' '  * 5), 
                           sg.Frame('药剂监视器', [[sg.Image(key='-FRV2-')]])], 
                          [sg.Frame('身份识别窗口', [[sg.Image(key='-FRV3-')]])]], 
                         element_justification='c')
    def layout_win2_cam(self):
        return sg.Column([[sg.Frame('药剂监视器', [[sg.Image(key='-FRV1-')]]), sg.T(' '  * 5), 
                           sg.Frame('身份识别窗口', [[sg.Image(key='-FRV2-')]])], 
                          [sg.Frame('全景图', [[sg.Image(key='-FRV3-')]])]], 
                         element_justification='c')
    def layout_win3(self):
        layout = [[sg.Button('', image_data=self.pic.img_data['btn_back'], button_color=('white', self.pic.color[4]), key='Back', border_width=0)]]
        data = []
        header_list = []
        try:
            df = pd.read_csv(FilePath.log, sep=',', encoding='utf-8', engine='python', header=None)
            header_list = df.iloc[0].tolist()
            data = df[1:].values.tolist()
        except:
            return layout
        layout += [[sg.T(' ')]]
        layout += [[sg.T(' '*6),
                    sg.Table(values=data,
                             headings=header_list,
                             font='宋体 20',
                             display_row_numbers=True,
                             auto_size_columns=False,
                             vertical_scroll_only = False,
                             expand_x=True,
                             expand_y=True), 
                    sg.T(' '*6)]]
        layout += [[sg.T(' ')]]
        return layout
    def layout_win4(self):
        layout = [[sg.Button('', image_data=self.pic.img_data['btn_back'], button_color=('white', self.pic.color[4]), key='Back', border_width=0)]]
        return layout
    

