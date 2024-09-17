import sys  
from PyQt5.QtCore import QUrl, Qt  
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton,  
                             QToolBar, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,  
                             QMenuBar, QMenu, QAction, QLabel, QMessageBox)  
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage  
  
class Tab(QWidget):    
    def __init__(self, parent=None):    
        super().__init__(parent)    
    
        # 创建垂直布局来放置地址栏、工具栏和网页视图    
        layout = QVBoxLayout()    
        self.setLayout(layout)    
    
        # 地址栏    
        self.url_bar = QLineEdit()    
        self.url_bar.returnPressed.connect(self.load_page)    
    
        # 网页视图    
        self.browser = QWebEngineView()    
        self.browser.urlChanged.connect(self.update_urlbar)    
        self.browser.titleChanged.connect(self.update_tab_title)    
        self.browser.loadProgress.connect(self.update_loading_status)    
  
        # 工具栏    
        toolbar = QToolBar()

        visit_button = QPushButton('访问')  
        visit_button.clicked.connect(self.load_page)  
        toolbar.addWidget(visit_button)  
  
        search_button = QPushButton('搜索')  
        search_button.clicked.connect(self.search_page)  
        toolbar.addWidget(search_button)  
        
        back_button = QPushButton('后退')    
        back_button.clicked.connect(self.browser.back)    
        toolbar.addWidget(back_button)    
    
        forward_button = QPushButton('前进')    
        forward_button.clicked.connect(self.browser.forward)    
        toolbar.addWidget(forward_button)    
    
        refresh_button = QPushButton('刷新')    
        refresh_button.clicked.connect(self.browser.reload)    
        toolbar.addWidget(refresh_button)    
    
        # 将地址栏和工具栏添加到布局中    
        toolbar_layout = QHBoxLayout()    
        toolbar_layout.addWidget(self.url_bar)    
        toolbar_layout.addWidget(toolbar)    
        layout.addLayout(toolbar_layout)    
    
        # 将网页视图添加到布局中    
        layout.addWidget(self.browser)    
    
        # 加载状态标签    
        self.loading_label = QLabel()    
        self.loading_label.setHidden(True)    
        layout.addWidget(self.loading_label)

    def search_page(self):  
        search_query = self.url_bar.text()  
        search_url = f"https://cn.bing.com/search?q={search_query.replace(' ', '+')}"  
        self.browser.setUrl(QUrl(search_url))  
  
    def load_page(self):  
        url = self.url_bar.text()  
        if not url.startswith('http://') and not url.startswith('https://'):  
            url = 'http://' + url  
        self.browser.setUrl(QUrl(url))  
  
    def update_urlbar(self, url):  
        self.url_bar.setText(url.toString())  
  
    def update_tab_title(self, title):  
        self.setWindowTitle(title)  
  
    def update_loading_status(self, progress):  
        if progress < 100:  
            self.loading_label.setText(f"Loading... {progress}%")  
            self.loading_label.setHidden(False)  
        else:  
            self.loading_label.setHidden(True)  
  
class SimpleBrowser(QMainWindow):  
    def __init__(self):  
        super().__init__()  
  
        # 设置窗口标题和初始大小  
        self.setWindowTitle('简易浏览器')  
        self.setGeometry(100, 100, 800, 600)  
  
        # 菜单栏  
        menubar = QMenuBar()  
        file_menu = menubar.addMenu('新建')  
        self.setMenuBar(menubar)  
  
        # 创建标签页部件  
        self.tab_widget = QTabWidget()  
        self.setCentralWidget(self.tab_widget)  
  
        # 设置标签页的关闭按钮和右键菜单  
        self.tab_widget.setTabsClosable(True)  
        self.tab_widget.tabCloseRequested.connect(self.close_tab)  
        self.tab_widget.setContextMenuPolicy(Qt.CustomContextMenu)  
        self.tab_widget.customContextMenuRequested.connect(self.show_tab_context_menu)  
  
        # 新建标签页动作  
        new_tab_action = QAction('新建标签页', self)  
        new_tab_action.triggered.connect(self.add_new_tab)  
        file_menu.addAction(new_tab_action)  
  
        # 初始化时打开一个空白标签页  
        self.add_new_tab('https://www.example.com')  
  
    def add_new_tab(self, url=None):  
        tab = Tab()  
        index = self.tab_widget.addTab(tab, '新标签页')  
        self.tab_widget.setCurrentIndex(index)  
  
        if url:  
            tab.browser.setUrl(QUrl(url))  
  
    def close_tab(self, index):  
        if self.tab_widget.count() > 1:  
            self.tab_widget.removeTab(index)  
        else:  
            # 当关闭最后一个标签页时，询问用户是否退出程序  
            reply = QMessageBox.question(self, '确认', '确定要退出浏览器吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
            if reply == QMessageBox.Yes:  
                self.close()  
  
    def show_tab_context_menu(self, position):  
        tab_bar = self.tab_widget.tabBar()  
        tab_index = tab_bar.tabAt(position)  
        if tab_index != -1:  
            menu = QMenu()  
            close_action = QAction('关闭标签页', menu)  
            close_action.triggered.connect(lambda: self.close_tab(tab_index))  
            menu.addAction(close_action)  
            menu.exec_(tab_bar.mapToGlobal(position))  
  
# 运行应用  
app = QApplication(sys.argv)  
browser = SimpleBrowser()  
browser.show()  
sys.exit(app.exec_())
