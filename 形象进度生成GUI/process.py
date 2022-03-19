# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 886)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionfeedback = QAction(MainWindow)
        self.actionfeedback.setObjectName(u"actionfeedback")
        self.actionopen_database = QAction(MainWindow)
        self.actionopen_database.setObjectName(u"actionopen_database")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 25, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.start_date = QDateEdit(self.centralwidget)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setFont(font1)

        self.horizontalLayout.addWidget(self.start_date)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.end_date = QDateEdit(self.centralwidget)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setFont(font1)

        self.horizontalLayout_2.addWidget(self.end_date)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(10)
        self.pushButton.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"\u9ed1\u4f53")
        font3.setPointSize(10)
        self.label_4.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_4)

        self.beam_casted = QTextEdit(self.centralwidget)
        self.beam_casted.setObjectName(u"beam_casted")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.beam_casted.setPalette(palette)

        self.verticalLayout_3.addWidget(self.beam_casted)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_5)

        self.beam_ins = QTextEdit(self.centralwidget)
        self.beam_ins.setObjectName(u"beam_ins")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.beam_ins.setPalette(palette1)

        self.verticalLayout_3.addWidget(self.beam_ins)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_6)

        self.seam = QTextEdit(self.centralwidget)
        self.seam.setObjectName(u"seam")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.seam.setPalette(palette2)

        self.verticalLayout_3.addWidget(self.seam)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_7)

        self.guardrail = QTextEdit(self.centralwidget)
        self.guardrail.setObjectName(u"guardrail")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.guardrail.setPalette(palette3)

        self.verticalLayout_3.addWidget(self.guardrail)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_8)

        self.formation = QTextEdit(self.centralwidget)
        self.formation.setObjectName(u"formation")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.formation.setPalette(palette4)

        self.verticalLayout_3.addWidget(self.formation)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.start_date, self.end_date)
        QWidget.setTabOrder(self.end_date, self.beam_casted)
        QWidget.setTabOrder(self.beam_casted, self.beam_ins)
        QWidget.setTabOrder(self.beam_ins, self.seam)
        QWidget.setTabOrder(self.seam, self.guardrail)
        QWidget.setTabOrder(self.guardrail, self.formation)

        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionfeedback)
        self.menu_2.addAction(self.actionopen_database)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5f62\u8c61\u8fdb\u5ea6", None))
        self.actionfeedback.setText(QCoreApplication.translate("MainWindow", u"direction for use", None))
        self.actionopen_database.setText(QCoreApplication.translate("MainWindow", u"open database", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f62\u8c61\u8fdb\u5ea6\u6587\u5b57\u6c47\u603b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u8fdb\u5ea6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"T\u6881\u9884\u5236\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u6881\u5b89\u88c5\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6e7f\u63a5\u7f1d\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9632\u649e\u62a4\u680f\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6865\u9762\u94fa\u88c5\uff1a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6570\u636e\u5e93", None))
    # retranslateUi

