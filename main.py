#需要安装一下库
# pip insatll PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip insatll PyQtQtWebEngine -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip insatll PyQtDesigner -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip insatll qdarkstyle -i https://pypi.tuna.tsinghua.edu.cn/simple/


import sys, qdarkstyle,functools
from PyQt5 import QtWebEngineWidgets#PyQtWebEngine
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui.MainWindow import Ui_MainWindow
from mode.window import get_mode_window
from mode.connect import get_mode_connect

class Window(QMainWindow, Ui_MainWindow):  # 类的多继承
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.setupUi(self)  # 当前类继承了父类的方法,直接调用
        self.setWindowTitle('懒人工具--PyQt5代码生成器')
        self.setWindowIcon(QIcon('./logo.ico'))
        self.connects = []
        self.currenSignal_class = ''  # 当前的控件类型
        self.bt_code_generation.clicked.connect(self.clicked_code_generation)
        self.bt_code_signal.clicked.connect(self.clicked_code_signal)
        self.cbb_buttons.activated.connect(self.activated_buttons)
        self.cbb_input.activated.connect(self.activated_input)
        self.cbb_display.activated.connect(self.activated_display)


        #加载浏览器插件
        self.webView_pyqt5 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.vbox_web.addWidget(self.webView_pyqt5)
        #开启js加载
        settings = QtWebEngineWidgets.QWebEngineSettings.globalSettings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)
        self.webView_pyqt5.setUrl(QUrl("https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html"))
        self.webView_pyqt5.setObjectName("webView")


        # 加载浏览器插件QSS
        self.webView_QSS = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.vbox_QSS_web.addWidget(self.webView_QSS)
        self.webView_QSS.setUrl(
            QUrl("https://www.cnblogs.com/linuxAndMcu/p/11039769.html"))
        self.webView_QSS.setObjectName("webView")
        self.bt_qss.clicked.connect(self.clicked_qss)
        self.bt_find_api.clicked.connect(functools.partial(self.callback_,self.webView_pyqt5, self.ed_api))
        self.bt_find_qss.clicked.connect(functools.partial(self.callback_,self.webView_QSS, self.ed_qss))

    def set_ui(self):
        pass
    def clicked_qss(self):
        if self.bt_qss.text()=='官方QSS文档英文版 建议使用有道词典的截图翻译':
            self.bt_qss.setText('网络上找到的中文QSS帮助文档 建议使用有道词典的截图翻译')
            self.webView_QSS.setUrl(
                QUrl("https://doc.qt.io/qt-5/stylesheet-reference.html"))
        else:
            self.bt_qss.setText('官方QSS文档英文版 建议使用有道词典的截图翻译')
            self.webView_QSS.setUrl(
                QUrl("https://www.cnblogs.com/linuxAndMcu/p/11039769.html"))

    def clicked_code_generation(self):
        '''
        窗口初始化代码生成按钮事件
        :return:
        '''
        transp = 1
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
        if self.cb_bjtm.isChecked() == True:  # 背景透明
            transp = 0.5
            flags += 'Qt.WA_TranslucentBackground' + ' | '
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
        # 加载窗口模板
        mode_window, mode_quote, mode_init = get_mode_window(self.nameLineEdit.text(),
                                                             class_,
                                                             self.uiClassLineEdit.text(),
                                                             self.titleLineEdit.text(),
                                                             size,
                                                             move, flags, transp)
        self.ed_code_init.setText(mode_init)
        self.ed_code_class.setText(mode_window)
        self.ed_code_import.setText(mode_quote)


    def clicked_code_signal(self):
        signal, note = self.cbb_signal.currentText().split(' ')
        if  signal == 'stateChanged':
            args = ',i'  # 参数必须,开头
            note += ' i为状态'  # 注释
        elif signal == 'toggled':
            args = ',b'  # 参数必须,开头
            note += ' b为状态'  # 注释
        elif signal == 'activated':
            args = ',i:int'  # 参数必须,开头
            note += ' 参数int类型代表了被选中项的索引，String类型代表了被选中项的内容。自行修改'  # 注释
        elif signal == 'currentIndexChanged':
            args = ',i:int'  # 参数必须,开头
            note += ' 参数int类型代表了被选中项的索引，String类型代表了被选中项的内容。自行修改'  # 注释
        elif signal == 'currentTextChanged':
            args = ',s'  # 参数必须,开头
            note += ' String类型代表了被选中项的内容。'  # 注释
        elif signal == 'editTextChanged':
            args = ',s'  # 参数必须,开头
            note += ' String类型代表了被选中项的内容。'  # 注释
        elif signal == 'highlighted':
            args = ',i:int'  # 参数必须,开头
            note += ' 参数int类型代表了被选中项的索引，String类型代表了被选中项的内容。自行修改'  # 注释
        elif signal == 'textActivated':
            args = ',s'  # 参数必须,开头
            note += ' String类型代表了被选中项的内容。'  # 注释
        elif signal == 'textHighlighted':
            args = ',s'  # 参数必须,开头
            note += ' String类型代表了被选中项的内容。'  # 注释
        elif signal == 'keySequenceChanged':
            args = ',key'  # 参数必须,开头
            note += ' 按下的键值'  # 注释
        elif signal == 'currentFontChanged':
            args = ',f'  # 参数必须,开头
            note += ' 返回改变的QFont  字体'   # 注释
        elif signal == 'cursorPositionChanged':
            args = ',x,y'  # 参数必须,开头
            note += ' 光标位置x,y'  # 注释
        elif signal == 'undoAvailable':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'copyAvailable':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'redoAvailable':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'backwardAvailable':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'forwardAvailable':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'anchorClicked':
            args = ',url'  # 参数必须,开头
            note += ' 链接'  # 注释
        elif signal == 'blockCountChanged':
            args = ',i'  # 参数必须,开头
            note += ' 字符改变数量'  # 注释
        elif signal == 'updateRequest':
            args = ',rect,i'  # 参数必须,开头
            note += ' rect矩形,i滚动的步长'  # 注释
        elif signal == 'modificationChanged':
            args = ',b'  # 参数必须,开头
            note += ' 被编辑状态True or False'  # 注释
        elif signal == 'textChanged':
            args = ',s'  # 参数必须,开头
            note += ' 修改的文本'  # 注释
        elif signal == 'valueChanged':
            args = ',i'  # 参数必须,开头
            note += ' 数值'  # 注释
        elif signal == 'actionTriggered':
            args = ',i'  # 参数必须,开头
            note += ' 数值'  # 注释
        elif signal == 'rangeChanged':
            args = ',star,end'  # 参数必须,开头
            note += ' 范围'  # 注释
        elif signal == 'rangeChanged':
            args = ',i'  # 参数必须,开头
            note += ' 数值'  # 注释
        elif signal == 'dateChanged':
            args = ',date'  # 参数必须,开头
            note += ' 改变的日期'  # 注释
        elif signal == 'dateTimeChanged':
            args = ',datet'  # 参数必须,开头
            note += ' 改变的日期时间'  # 注释
        elif signal == 'timeChanged':
            args = ',t'  # 参数必须,开头
            note += ' 改变的时间'  # 注释
        else:
            args = ''  # 参数必须,开头
            note += ''  # 注释

        connect_text, bound = get_mode_connect(self.nameLineEdit_2.text(), self.suffixLineEdit.text(), signal, args,note)
        self.ed_signal.setText(bound)
        self.ed_connect.setText(connect_text)

    def activated_buttons(self, i):
        # i为现行选中项
        if i == 0:
            self.connects = ['clicked 鼠标单击', 'pressed 鼠标按下', 'released 鼠标释放', 'toggled 切换按钮状态']
        elif i == 1:
            self.connects = ['triggered 触发状态', 'clicked 鼠标单击', 'pressed 鼠标按下', 'released 鼠标释放', 'toggled 切换按钮状态']
        elif i == 2:
            self.connects = ['toggled 切换状态', 'clicked 鼠标单击', 'pressed 鼠标按下', 'released 鼠标释放']
        elif i == 3:
            self.connects = ['stateChanged 改变现行选中项时', 'clicked 鼠标单击', 'pressed 鼠标按下', 'released 鼠标释放']
        elif i == 4:
            self.connects = ['clicked 鼠标单击', 'pressed 鼠标按下', 'released 鼠标释放', 'toggled 切换按钮状态']
        elif i == 5:
            self.connects = ['accepted 接受对话内容', 'clicked 鼠标单击', 'helpRequested 寻求帮助', 'rejected 拒绝对话内容']
        self.cbb_signal.clear()  # 清空信号组合框的内容
        self.cbb_signal.addItems(self.connects)  # 给组合框重新增加成员
        self.currenSignal_class = self.cbb_buttons.currentText()  # 切换控件类型

    def callback_(self, webView,ed):
        webView.findText(ed.text())

    def activated_input(self, i):

        # i为现行选中项
        if i == 0:
            self.connects = ['activated 单击选项时', 'currentIndexChanged 目前选项变化', 'currentTextChanged 当前文本改变',
                             'editTextChanged 编辑文本改变', 'highlighted 突出显示', 'textActivated 文本被激活',
                             'textHighlighted 文本高亮显示']
        elif i == 1:
            self.connects = ['currentFontChanged 当前字体改变了', 'activated 单击选项时', 'currentIndexChanged 目前选项变化',
                             'currentTextChanged 当前文本改变','editTextChanged 编辑文本改变', 'highlighted 突出显示',
                             'textActivated 文本被激活', 'textHighlighted 文本高亮显示']
        elif i == 2:
            self.connects = ['textChanged 文本改变', 'textEdited 文本编辑', 'cursorPositionChanged 光标位置改变了',
                             'editingFinished 编辑完成', 'inputRejected 输入拒绝', 'returnPressed 按下回车',
                             'selectionChanged 选择改变']
        elif i == 3:
            self.connects = ['textChanged 文本改变','undoAvailable 撤销可用', 'anchorClicked 链接被点击', 'backwardAvailable 向后可用',
                             'forwardAvailable 向前可用', 'highlighted 突出显示',
                             'historyChanged 改变了历史', 'sourceChanged 源变化', 'copyAvailable 复制可用',
                             'currentCharFormatChanged 当前字符格式改变',
                             'cursorPositionChanged 光标位置改变了', 'redoAvailable 准备完毕', 'selectionChanged 选择改变']
        elif i == 4:
            self.connects = ['textChanged 文本改变','undoAvailable 撤销可用','blockCountChanged 字符块数量改变了', 'copyAvailable 复制可用','cursorPositionChanged 光标位置改变了',
                             'modificationChanged 编辑后触发','redoAvailable 准备完毕','selectionChanged 选择改变','updateRequest 更新请求']
        elif i == 5:
            self.connects = ['textChanged 文本改变', 'valueChanged 值改变', 'editingFinished 编辑完成']
        elif i == 6:
            self.connects = ['textChanged 文本改变', 'valueChanged 值改变', 'editingFinished 编辑完成']
        elif i == 7:
            self.connects = ['dateChanged 日期改变了', 'dateTimeChanged 日期时间改变了', 'timeChanged 时间改变了']
        elif i == 8:
            self.connects = ['dateChanged 日期改变了', 'dateTimeChanged 日期时间改变了', 'timeChanged 时间改变了']
        elif i == 9:
            self.connects = ['dateChanged 日期改变了', 'dateTimeChanged 日期时间改变了', 'timeChanged 时间改变了']
        elif i == 10:
            self.connects = ['actionTriggered 行动引发了', 'rangeChanged 范围变化', 'sliderMoved 滑块移动','sliderPressed 滑块按下',
                             'sliderReleased 滑块弹起','valueChanged 值改变']
        elif i == 11:
            self.connects = ['actionTriggered 行动引发了', 'rangeChanged 范围变化', 'sliderMoved 滑块移动','sliderPressed 滑块按下',
                             'sliderReleased 滑块弹起','valueChanged 值改变']
        elif i == 12:
            self.connects = ['actionTriggered 行动引发了', 'rangeChanged 范围变化', 'sliderMoved 滑块移动','sliderPressed 滑块按下',
                             'sliderReleased 滑块弹起','valueChanged 值改变']
        elif i == 13:
            self.connects = ['actionTriggered 行动引发了', 'rangeChanged 范围变化', 'sliderMoved 滑块移动','sliderPressed 滑块按下',
                             'sliderReleased 滑块弹起','valueChanged 值改变']
        elif i == 14:
            self.connects = ['actionTriggered 行动引发了', 'rangeChanged 范围变化', 'sliderMoved 滑块移动','sliderPressed 滑块按下',
                             'sliderReleased 滑块弹起','valueChanged 值改变']
        elif i == 15:
            self.connects = ['editingFinished 编辑完成', 'keySequenceChanged 键序列改变']
        self.cbb_signal.clear()  # 清空信号组合框的内容
        self.cbb_signal.addItems(self.connects)  # 给组合框重新增加成员
        self.currenSignal_class = self.cbb_buttons.currentText()  # 切换控件类型
    def activated_display(self, i):
        # i为现行选中项
        if i == 0:
            self.connects = ['activated 单击选项时', 'currentIndexChanged 目前选项变化', 'currentTextChanged 当前文本改变',
                             'editTextChanged 编辑文本改变', 'highlighted 突出显示', 'textActivated 文本被激活',
                             'textHighlighted 文本高亮显示']
        elif i == 1:
            self.connects = ['currentFontChanged 当前字体改变了', 'activated 单击选项时', 'currentIndexChanged 目前选项变化',
                             'currentTextChanged 当前文本改变','editTextChanged 编辑文本改变', 'highlighted 突出显示',
                             'textActivated 文本被激活', 'textHighlighted 文本高亮显示']
        elif i == 2:
            self.connects = ['textChanged 文本改变', 'textEdited 文本编辑', 'cursorPositionChanged 光标位置改变了',
                             'editingFinished 编辑完成', 'inputRejected 输入拒绝', 'returnPressed 按下回车',
                             'selectionChanged 选择改变']
        elif i == 3:
            self.connects = ['textChanged 文本改变','undoAvailable 撤销可用', 'anchorClicked 链接被点击', 'backwardAvailable 向后可用',
                             'forwardAvailable 向前可用', 'highlighted 突出显示',
                             'historyChanged 改变了历史', 'sourceChanged 源变化', 'copyAvailable 复制可用',
                             'currentCharFormatChanged 当前字符格式改变',
                             'cursorPositionChanged 光标位置改变了', 'redoAvailable 准备完毕', 'selectionChanged 选择改变']
        elif i == 4:
            self.connects = ['textChanged 文本改变','undoAvailable 撤销可用','blockCountChanged 字符块数量改变了', 'copyAvailable 复制可用','cursorPositionChanged 光标位置改变了',
                             'modificationChanged 编辑后触发','redoAvailable 准备完毕','selectionChanged 选择改变','updateRequest 更新请求']
        elif i == 5:
            self.connects = ['textChanged 文本改变', 'valueChanged 值改变', 'editingFinished 编辑完成']
        self.cbb_signal.clear()  # 清空信号组合框的内容
        self.cbb_signal.addItems(self.connects)  # 给组合框重新增加成员
        self.currenSignal_class = self.cbb_buttons.currentText()  # 切换控件类型


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Window()
    window.show()
    sys.exit(app.exec_())
