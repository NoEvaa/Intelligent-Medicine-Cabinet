# -*- coding: utf-8 -*-
"""
Welcome to NPark
4逻辑层
主窗口事件监听与各窗口跳转逻辑
"""
import PySimpleGUI as sg
from ImcAct import ImcAct

class ImcUi(ImcAct):
    def __init__(self):
        ImcAct.__init__(self)
    def loop(self):
        winm = self.win0()
        
        while True:
            event, values = winm.read(timeout=20)
            self.update_time(winm)
            self.vedio(winm, 0)
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
                if sg.popup_get_text('PASSWORD', '') == 'aa':
                    break
            elif event == 'Open':
                if self.start_win1(): #人脸识别
                    continue #主动退出
                if self.check_apply():
                    continue #no access
                self.record_curtime() #记录开柜时间
                self.start_win2() #存取
                if not self.state[0]:
                    pass #关柜
                self.record_curtime(1) #记录关柜时间
                self.save_log() #日志存档
                self.initial() #初始化，等待下次开柜
            elif event == 'Log':
                self.start_win3()
            elif event == 'Setting':
                continue
        winm.close()
        
if __name__ == '__main__':
    app = ImcUi()
    app.loop()
    app.cam_stop()
    del app
