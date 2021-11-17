# 需要安装一下库
# pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip install PyQtQtWebEngine -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip install PyQtDesigner -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip install qdarkstyle -i https://pypi.tuna.tsinghua.edu.cn/simple/


import sys, qdarkstyle, webbrowser, re,requests,functools,json,bs4
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui.MainWindow import Ui_MainWindow
from mode.window import get_mode_window
from mode.connect import get_mode_connect,get_mode_qevent


class Window(QMainWindow, Ui_MainWindow):  # 类的多继承
    def __init__(self):

        super().__init__()
        self.set_ui()
        self.setupUi(self)  # 当前类继承了父类的方法,直接调用


        self.setWindowTitle('懒人工具--PyQt5代码生成器     ')
        self.setWindowIcon(QIcon('./logo.ico'))
        self.connects = []
        self.currenSignal_class = ''  # 当前的控件类型
        self.bt_code_generation.clicked.connect(self.clicked_code_generation)  # 界面预览
        self.cbb_signal.activated.connect(self.activated_cbb_signal)  # 选中某个信号时
        self.cbb_qevent.activated.connect(self.activated_cbb_qevent)  # 选中某个重写事件时
        self.bt_ui_path.clicked.connect(self.clicked_bt_ui_path)#选择文件
        #复制按钮
        self.bt_copy_import.clicked.connect(functools.partial(self.copy, self.ed_code_import))
        self.bt_copy_class.clicked.connect(functools.partial(self.copy, self.ed_code_class))
        self.bt_copy_init.clicked.connect(functools.partial(self.copy, self.ed_code_init))
        #复制按钮
        self.bt_copy_bind.clicked.connect(functools.partial(self.copy, self.ed_signal))
        self.bt_copy_connect.clicked.connect(functools.partial(self.copy, self.ed_connect))
        with open('datas\\qevent.txt','r',encoding='utf-8')as f:
            text=f.read()
        self.qevents=json.loads(text.replace('\'','"'))
        for item in self.qevents:

            self.cbb_qevent.addItem(item['name']+'  '+item['note'])

        #资料网站
        self.bt_pyqtapi.clicked.connect(lambda: webbrowser.open(
            "https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html"))
        self.bt_qss.clicked.connect(lambda: webbrowser.open(
            "https://doc.qt.io/qt-5/stylesheet-reference.html"))
        self.bt_qss_2.clicked.connect(lambda: webbrowser.open(
            "https://www.cnblogs.com/linuxAndMcu/p/11039769.html"))
    def set_ui(self):
        pass
    def connect_widgets(self, code, widgets_list):
        '''
        绑定单击信号,方便获取当前的控件
        :param code:
        :param widgets_list:
        :return:
        '''
        text = ''
        for item in widgets_list:
            text += item + '\n' + '        '
        code = re.sub(r'#connect-start#(.*?)#connect-end#', text[:-2], code)  # 将代码替换进去
        return code
    def clicked_code_generation(self):
        '''
        窗口初始化代码生成按钮事件
        :return:
        '''
        try:
            # 读取选中的UI文件
            with open(self.ed_ui_path.text(), 'r', encoding='utf-8')as f:
                code = f.read()
                class_name = re.findall(r'class (.*?)\(object\):', code)[0]

            # 将次UI文件内容拷贝到mode中的test_ui
            with open('mode\\test_ui.py', 'w', encoding='utf-8')as f:
                f.write(code)
            widgets_s = []
            #遍历除所有的控件
            widgets_list = re.findall(r'self.(.*.) = QtWidgets.', code)
            for item in widgets_list:
                # 排除一些不用的控件
                if 'Layout' not in item and 'centralwidget' not in item:
                    #将所有控件都加上鼠标点击事件
                    widgets_s.append(
                        f"self.{item}.mousePressEvent=functools.partial(self.clicked_signal,widget=self.{item})")
            #读取我们的预览界面模板
            with open('mode/test_object.py', 'r', encoding='utf-8')as f:
                code = f.read()
            #将ui名替换成刚修改的
            code = re.sub(r'class (.*.)(object):', class_name, code)  # 替换ui类名
            code = self.connect_widgets(code, widgets_s)#执行代码替换,将所有的点击事件加入进去
            #将ui名替换成刚修改的
            code = code.replace('Ui_main', class_name)  # 替换ui类名
            #下方为生成代码的步骤
            class_ = self.cbb_class.currentText()
            size = self.sizeLineEdit.text().split('*')
            move = self.moveLineEdit.text().split(',')
            flags = ''
            if self.cb_max_bt.isChecked() == True:  # 最大化按钮
                flags += 'Qt.WindowMaximizeButtonHint' + ' | '
            if self.cb_min_bt.isChecked() == True:  # 最小化按钮
                flags += 'Qt.WindowMinimizeButtonHint' + ' | '
            if self.cb_exit.isChecked() == True:  # 退出按钮
                flags += 'Qt.WindowCloseButtonHint' + ' | '
            if self.cb_top.isChecked() == True:  # 置顶
                flags += 'Qt.WindowStaysOnTopHint' + ' | '
            if self.cb_wbk.isChecked() == True:  # 窗口无边框
                flags += 'Qt.FramelessWindowHint' + ' | '
            if self.cbb_flags.currentIndex() == 0:  # 默认widget
                flags += 'Qt.Widget'
            elif self.cbb_flags.currentIndex() == 1:  # 部件始终为窗口
                flags += 'Qt.Window'
            elif self.cbb_flags.currentIndex() == 2:  # 部件为对话框
                flags += 'Qt.Dialog'
            elif self.cbb_flags.currentIndex() == 3:  # 部件是一个Macintosh表单
                flags += 'Qt.Sheet'
            elif self.cbb_flags.currentIndex() == 4:  # 部件是一个Macintosh抽屉
                flags += 'Qt.Drawer'
            elif self.cbb_flags.currentIndex() == 5:  # 部件是一个弹出式顶层窗口
                flags += 'Qt.Popup'
            elif self.cbb_flags.currentIndex() == 6:  # 部件是一个工具窗口
                flags += 'Qt.Tool'
            elif self.cbb_flags.currentIndex() == 7:  # 部件是一个提示窗口
                flags += 'Qt.ToolTip'
            elif self.cbb_flags.currentIndex() == 8:  # 部件是一个桌面
                flags += 'Qt.Desktop'
            else:
                # 部件是一个欢迎窗口
                flags += 'Qt.SplashScreen'
            # 加载窗口模板,生成代码,填参数
            mode_window, mode_quote, mode_init = get_mode_window(self.nameLineEdit.text(),
                                                                 class_,
                                                                 self.ed_ui_path.text().split('.')[0].split('/')[-1],class_name,
                                                                 self.titleLineEdit.text(),
                                                                 size,
                                                                 move, flags,self.cb_bjtm.isChecked(), float(self.ed_transp.text()))
            self.ed_code_init.setText(mode_init)
            self.ed_code_class.setText(mode_window)
            self.ed_code_import.setText(mode_quote)
            #将设置内容放入预览窗口模板中
            set_text=mode_window.split('self.setupUi(self)')[-1].split('def set_ui(self):')[0]#取出设置部分
            code=code.replace('#set_txt#',set_text)#将设置导入
            #预览窗口
            __ret = {}  # 用来传全局变量和返回变量
            exec(code, __ret, __ret)  # 执行脚本
            self.tw = __ret['tw']#实例化预览窗口
            self.tw.cbb = self.cbb_signal#将下拉列表框传递过去
            self.tw.widget = self.lb_title#将当前控件的标签框传过去
            self.tw.tab_testXX = self.tabWidget#将分组框传过去
            self.tw.show()
        except Exception as err:
            QMessageBox.warning(self,'预览失败!',str(err))


    def clicked_bt_ui_path(self):

        file, filetype = QFileDialog.getOpenFileName(self,
                                                       "请选择您的ui转py的文件,注意您的主程序根目录需要创建一个名字为ui的文件夹来装",
                                                       '',
                                                       "PyQtUI Files (*.py)")

        if len(file) == 0:
            print("\n取消选择")
            return

        self.ed_ui_path.setText(file)
        with open(self.ed_ui_path.text(), 'r', encoding='utf-8')as f:
            code = f.read()
            size=code.split('.resize(')[-1].split(')')[0].replace(', ','*')
        self.sizeLineEdit.setText(size)
    def copy(self,widget):
        '''
        复制到剪切板
        :param widget:
        :return:
        '''
        mimeData = QMimeData()
        mimeData.setText(widget.toPlainText())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)


    def activated_cbb_signal(self, i):
        try:
            connect, bound = get_mode_connect(self.tw.widget_name, self.tw.signals[i])
            self.ed_signal.setText(bound)
            self.ed_connect.setText(connect)
        except:
            QMessageBox.warning(self,'错误','预览窗口不能提前关闭')
    def activated_cbb_qevent(self, i):
        try:
            connect, bound = get_mode_qevent(self.tw.widget_name, self.qevents[i])
            self.ed_signal.setText(bound)
            self.ed_connect.setText(connect)
        except Exception as  err:
            QMessageBox.warning(self,'错误','预览窗口不能提前关闭\n'+str(err))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Window()
    window.show()
    sys.exit(app.exec_())
