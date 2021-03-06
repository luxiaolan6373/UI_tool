def get_mode_window(name, class_, ui_class,class_name, title, size, move, flags,background_tran,transp):
    if background_tran:
        mode_window = f'''class {ui_class}({class_}, {class_name}):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.setupUi(self)
        self.setWindowTitle('{title}')#标题
        self.setWindowFlags({flags})#风格
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowOpacity({transp})#设置1-0之间设置窗口透明度
        self.resize({size[0]}, {size[1]})#大小
        self.move({move[0]}, {move[1]})#位置
    def set_ui(self):
        pass'''
    else:
        mode_window = f'''class {ui_class}({class_}, {class_name}):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.setupUi(self)
        self.setWindowTitle('{title}')#标题
        self.setWindowFlags({flags})#风格
        self.setWindowOpacity({transp})#设置1-0之间设置窗口透明度
        self.resize({size[0]}, {size[1]})#大小
        self.move({move[0]}, {move[1]})#位置
    def set_ui(self):
        pass
            '''


    mode_quote = f'''import sys
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui.{ui_class} import {class_name}'''
    mode_init=f'''if __name__ == "__main__":
    app = QApplication(sys.argv)#初始化Qt应用
    {name} = {ui_class}()
    {name}.show()
    sys.exit(app.exec_())#监听消息不关闭
'''
    return mode_window,mode_quote,mode_init
