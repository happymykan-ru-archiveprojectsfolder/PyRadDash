# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceweryth.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc
import icons_white_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(758, 510)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(9,5,13);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 80))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lv1_header = QFrame(self.header_frame)
        self.lv1_header.setObjectName(u"lv1_header")
        self.lv1_header.setMaximumSize(QSize(16777215, 40))
        self.lv1_header.setStyleSheet(u"QFrame#app_header{\n"
"border-bottom: 1px solid rgb(230,5,64);\n"
"}\n"
"QLabel{\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 1px solid rgb(230,5,64);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(240, 105, 140);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(115,2,32);\n"
"}")
        self.lv1_header.setFrameShape(QFrame.StyledPanel)
        self.lv1_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.lv1_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app_header = QFrame(self.lv1_header)
        self.app_header.setObjectName(u"app_header")
        self.app_header.setFrameShape(QFrame.StyledPanel)
        self.app_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.app_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, -1, 0)
        self.app_name = QLabel(self.app_header)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setMaximumSize(QSize(80, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.app_name.setFont(font)
        self.app_name.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.app_name)

        self.app_logo = QLabel(self.app_header)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setPixmap(QPixmap(u":/icons/icons/github.svg"))

        self.horizontalLayout_4.addWidget(self.app_logo)


        self.horizontalLayout_2.addWidget(self.app_header)

        self.date = QLabel(self.lv1_header)
        self.date.setObjectName(u"date")
        self.date.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.date.setFont(font1)
        self.date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.date)

        self.clock = QLCDNumber(self.lv1_header)
        self.clock.setObjectName(u"clock")
        self.clock.setMaximumSize(QSize(50, 15))
        self.clock.setProperty("value", 0.000000000000000)

        self.horizontalLayout_2.addWidget(self.clock)

        self.minimize = QPushButton(self.lv1_header)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMaximumSize(QSize(20, 20))
        self.minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.On)
        self.minimize.setIcon(icon)
        self.minimize.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.minimize)

        self.maximize = QPushButton(self.lv1_header)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize.setIcon(icon1)
        self.maximize.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.maximize)

        self.close = QPushButton(self.lv1_header)
        self.close.setObjectName(u"close")
        self.close.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon2)
        self.close.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.close)


        self.verticalLayout_2.addWidget(self.lv1_header)

        self.lv2_header = QFrame(self.header_frame)
        self.lv2_header.setObjectName(u"lv2_header")
        self.lv2_header.setMaximumSize(QSize(16777215, 40))
        self.lv2_header.setStyleSheet(u"QLabel{\n"
"color: rgb(230,5,64);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 105, 140, 100);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(115,2,32);\n"
"}")
        self.lv2_header.setFrameShape(QFrame.StyledPanel)
        self.lv2_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.lv2_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbox_outerframe = QFrame(self.lv2_header)
        self.toolbox_outerframe.setObjectName(u"toolbox_outerframe")
        self.toolbox_outerframe.setMaximumSize(QSize(40, 40))
        self.toolbox_outerframe.setFrameShape(QFrame.StyledPanel)
        self.toolbox_outerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.toolbox_outerframe)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolbox_innerframe = QFrame(self.toolbox_outerframe)
        self.toolbox_innerframe.setObjectName(u"toolbox_innerframe")
        self.toolbox_innerframe.setMaximumSize(QSize(40, 40))
        self.toolbox_innerframe.setFrameShape(QFrame.StyledPanel)
        self.toolbox_innerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.toolbox_innerframe)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolbox_button = QPushButton(self.toolbox_innerframe)
        self.toolbox_button.setObjectName(u"toolbox_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolbox_button.setIcon(icon3)
        self.toolbox_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.toolbox_button)


        self.horizontalLayout_5.addWidget(self.toolbox_innerframe)


        self.horizontalLayout.addWidget(self.toolbox_outerframe)

        self.name_bar = QFrame(self.lv2_header)
        self.name_bar.setObjectName(u"name_bar")
        self.name_bar.setFrameShape(QFrame.StyledPanel)
        self.name_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.name_bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lv2_namebar = QFrame(self.name_bar)
        self.lv2_namebar.setObjectName(u"lv2_namebar")
        self.lv2_namebar.setFrameShape(QFrame.StyledPanel)
        self.lv2_namebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.lv2_namebar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.name_key = QLabel(self.lv2_namebar)
        self.name_key.setObjectName(u"name_key")
        self.name_key.setMaximumSize(QSize(100, 40))
        self.name_key.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.name_key)

        self.name_value = QLabel(self.lv2_namebar)
        self.name_value.setObjectName(u"name_value")
        self.name_value.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.name_value)

        self.name_editor = QFrame(self.lv2_namebar)
        self.name_editor.setObjectName(u"name_editor")
        self.name_editor.setMaximumSize(QSize(150, 16777211))
        self.name_editor.setStyleSheet(u"QLineEdit:focus{\n"
"border: 1px inset rgb(115,2,32);\n"
"}")
        self.name_editor.setFrameShape(QFrame.StyledPanel)
        self.name_editor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.name_editor)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.name_confirm = QPushButton(self.name_editor)
        self.name_confirm.setObjectName(u"name_confirm")
        self.name_confirm.setMaximumSize(QSize(16, 16))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.name_confirm.setIcon(icon4)

        self.horizontalLayout_8.addWidget(self.name_confirm)

        self.name_input = QLineEdit(self.name_editor)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(100, 25))
        self.name_input.setMaximumSize(QSize(150, 25))
        self.name_input.setAutoFillBackground(False)
        self.name_input.setStyleSheet(u"color:rgb(160, 160, 160);\n"
"background-color: rgb(50,50,50);\n"
"border-radius: 10px;\n"
"border-color: rgb(230,5,64);\n"
"border-width: 2px;\n"
"")

        self.horizontalLayout_8.addWidget(self.name_input)


        self.horizontalLayout_7.addWidget(self.name_editor)


        self.horizontalLayout_3.addWidget(self.lv2_namebar)

        self.settings = QPushButton(self.name_bar)
        self.settings.setObjectName(u"settings")
        self.settings.setMaximumSize(QSize(20, 20))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.settings)

        self.notification = QPushButton(self.name_bar)
        self.notification.setObjectName(u"notification")
        self.notification.setMaximumSize(QSize(20, 20))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notification.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.notification)


        self.horizontalLayout.addWidget(self.name_bar)


        self.verticalLayout_2.addWidget(self.lv2_header)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.main_body)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.main_body)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        self.sidebar.setFont(font2)
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.worklist_sidebar = QFrame(self.sidebar)
        self.worklist_sidebar.setObjectName(u"worklist_sidebar")
        self.worklist_sidebar.setStyleSheet(u"QPushButton {\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(93,93,101);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(230,5,64);\n"
"}")
        self.worklist_sidebar.setFrameShape(QFrame.StyledPanel)
        self.worklist_sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.worklist_sidebar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, 0, 4)
        self.home = QPushButton(self.worklist_sidebar)
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"QPushButton{\n"
"color: rgb(230,5,64);\n"
"background-color: rgb(24,24,36);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(93,93,101);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(240,105,140);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon7)
        self.home.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.home)

        self.add_case = QPushButton(self.worklist_sidebar)
        self.add_case.setObjectName(u"add_case")
        icon8 = QIcon()
        icon8.addFile(u":/icons_white/icons_white/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_case.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.add_case)

        self.modify_case = QPushButton(self.worklist_sidebar)
        self.modify_case.setObjectName(u"modify_case")
        icon9 = QIcon()
        icon9.addFile(u":/icons_white/icons_white/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.modify_case.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.modify_case)

        self.delete_case = QPushButton(self.worklist_sidebar)
        self.delete_case.setObjectName(u"delete_case")
        icon10 = QIcon()
        icon10.addFile(u":/icons_white/icons_white/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_case.setIcon(icon10)

        self.verticalLayout_4.addWidget(self.delete_case)


        self.verticalLayout_3.addWidget(self.worklist_sidebar)

        self.filter_sidebar = QFrame(self.sidebar)
        self.filter_sidebar.setObjectName(u"filter_sidebar")
        self.filter_sidebar.setStyleSheet(u"QPushButton {\n"
"padding: 2px 20px;\n"
"text-align: left;\n"
"font-size: 10px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"color: rgb(255,255,255);\n"
"border-radius: 4px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230,5,64,150), stop:1 rgba(24, 24, 36, 100));\n"
"border: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240,105,140,150), stop:1 rgba(24, 24, 36, 100));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230,5,64,255), stop:1 rgba(24, 24, 36, 100));\n"
"}")
        self.filter_sidebar.setFrameShape(QFrame.StyledPanel)
        self.filter_sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.filter_sidebar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.filter_2 = QFrame(self.filter_sidebar)
        self.filter_2.setObjectName(u"filter_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_2.sizePolicy().hasHeightForWidth())
        self.filter_2.setSizePolicy(sizePolicy)
        self.filter_2.setMaximumSize(QSize(16777215, 200))
        self.filter_2.setStyleSheet(u"QFrame{\n"
"border-top-left-radius: 20px;\n"
"background-color: rgb(24,24,36);\n"
"}")
        self.filter_2.setFrameShape(QFrame.StyledPanel)
        self.filter_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.filter_2)
        self.verticalLayout_6.setSpacing(14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 12)
        self.filter_header = QFrame(self.filter_2)
        self.filter_header.setObjectName(u"filter_header")
        self.filter_header.setMaximumSize(QSize(100, 50))
        self.filter_header.setFrameShape(QFrame.StyledPanel)
        self.filter_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.filter_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.filter_logo = QLabel(self.filter_header)
        self.filter_logo.setObjectName(u"filter_logo")
        self.filter_logo.setMaximumSize(QSize(16, 16))
        self.filter_logo.setPixmap(QPixmap(u":/icons/icons/eye.svg"))
        self.filter_logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.filter_logo)

        self.filter_text = QLabel(self.filter_header)
        self.filter_text.setObjectName(u"filter_text")
        self.filter_text.setStyleSheet(u"text-align: center;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"color: rgb(230,5,64);")

        self.horizontalLayout_10.addWidget(self.filter_text)


        self.verticalLayout_6.addWidget(self.filter_header)

        self.Rm7 = QPushButton(self.filter_2)
        self.Rm7.setObjectName(u"Rm7")

        self.verticalLayout_6.addWidget(self.Rm7)

        self.Rm15 = QPushButton(self.filter_2)
        self.Rm15.setObjectName(u"Rm15")

        self.verticalLayout_6.addWidget(self.Rm15)

        self.Rm13USIR = QPushButton(self.filter_2)
        self.Rm13USIR.setObjectName(u"Rm13USIR")

        self.verticalLayout_6.addWidget(self.Rm13USIR)

        self.K1_CT = QPushButton(self.filter_2)
        self.K1_CT.setObjectName(u"K1_CT")

        self.verticalLayout_6.addWidget(self.K1_CT)


        self.verticalLayout_5.addWidget(self.filter_2)


        self.verticalLayout_3.addWidget(self.filter_sidebar)


        self.horizontalLayout_9.addWidget(self.sidebar)

        self.table = QFrame(self.main_body)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background-color: rgb(24, 23, 35);\n"
"border-radius: 4px")
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.table)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget = QTableWidget(self.table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_11.addWidget(self.tableWidget)


        self.horizontalLayout_9.addWidget(self.table)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"RadDash", None))
        self.app_logo.setText("")
        self.date.setText(QCoreApplication.translate("MainWindow", u"2023-09-04 Monday", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.close.setText("")
        self.toolbox_button.setText("")
        self.name_key.setText(QCoreApplication.translate("MainWindow", u"Radiologist:", None))
        self.name_value.setText(QCoreApplication.translate("MainWindow", u"Dr. Poon WL/ Dr. Liu SH", None))
        self.name_confirm.setText("")
        self.name_input.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Radiologist", None))
        self.settings.setText("")
        self.notification.setText("")
        self.home.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.add_case.setText(QCoreApplication.translate("MainWindow", u"  Add", None))
        self.modify_case.setText(QCoreApplication.translate("MainWindow", u"  Modify", None))
        self.delete_case.setText(QCoreApplication.translate("MainWindow", u"  Cancel", None))
        self.filter_logo.setText("")
        self.filter_text.setText(QCoreApplication.translate("MainWindow", u"  Filter By", None))
        self.Rm7.setText(QCoreApplication.translate("MainWindow", u"Rm 7", None))
        self.Rm15.setText(QCoreApplication.translate("MainWindow", u"Rm 15", None))
        self.Rm13USIR.setText(QCoreApplication.translate("MainWindow", u"Rm 13 USIR", None))
        self.K1_CT.setText(QCoreApplication.translate("MainWindow", u"K1-CT", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Exam Room", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Scheduled Time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ward", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Patient", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Procedure", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Clotting Profile", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Details", None));
    # retranslateUi

