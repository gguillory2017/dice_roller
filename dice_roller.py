# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dice_roller.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 778)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.misc_rolls_box = QtWidgets.QGroupBox(self.centralwidget)
        self.misc_rolls_box.setGeometry(QtCore.QRect(10, 580, 721, 151))
        self.misc_rolls_box.setFlat(False)
        self.misc_rolls_box.setObjectName("misc_rolls_box")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.misc_rolls_box)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 30, 699, 48))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pct_label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.pct_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pct_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pct_label.setLineWidth(3)
        self.pct_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pct_label.setObjectName("pct_label")
        self.horizontalLayout_8.addWidget(self.pct_label)
        self.roll_pct_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_8, clicked = lambda: self.rollDie(self.pct_value, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.roll_pct_button.setPalette(palette)
        self.roll_pct_button.setObjectName("roll_pct_button")
        self.horizontalLayout_8.addWidget(self.roll_pct_button)
        self.pct_value = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.pct_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pct_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pct_value.setAlignment(QtCore.Qt.AlignCenter)
        self.pct_value.setObjectName("pct_value")
        self.clear_pct_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_8, clicked = lambda: self.clearValue(self.pct_value))
        self.clear_pct_button.setObjectName("clear_pct_button")
        self.horizontalLayout_8.addWidget(self.clear_pct_button)
        self.horizontalLayout_8.addWidget(self.pct_value)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.misc_rolls_box)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 90, 699, 48))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.coin_label = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.coin_label.setFrameShape(QtWidgets.QFrame.Box)
        self.coin_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.coin_label.setLineWidth(3)
        self.coin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.coin_label.setObjectName("coin_label")
        self.horizontalLayout_9.addWidget(self.coin_label)
        self.coin_flip_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_9, clicked = lambda: self.coinFlip())
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.coin_flip_button.setPalette(palette)
        self.coin_flip_button.setObjectName("coin_flip_button")
        self.horizontalLayout_9.addWidget(self.coin_flip_button)
        self.coin_flip_value = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.coin_flip_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.coin_flip_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.coin_flip_value.setAlignment(QtCore.Qt.AlignCenter)
        self.coin_flip_value.setObjectName("coin_flip_value")
        self.clear_coin_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_9, clicked = lambda: self.clearCoinFlip())
        self.clear_coin_button.setObjectName("clear_coin_button")
        self.horizontalLayout_9.addWidget(self.clear_coin_button)
        self.horizontalLayout_9.addWidget(self.coin_flip_value)
        self.group_die_actions_box = QtWidgets.QGroupBox(self.centralwidget)
        self.group_die_actions_box.setGeometry(QtCore.QRect(10, 460, 481, 91))
        self.group_die_actions_box.setObjectName("group_die_actions_box")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.group_die_actions_box)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(9, 30, 458, 41))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.clear_dies_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.clear_dies_button.setObjectName("clear_dies_button")
        self.horizontalLayout_10.addWidget(self.clear_dies_button)
        self.sum_dies_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.sum_dies_button.setObjectName("sum_dies_button")
        self.horizontalLayout_10.addWidget(self.sum_dies_button)
        self.clear_sum_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.clear_sum_button.setObjectName("clear_sum_button")
        self.horizontalLayout_10.addWidget(self.clear_sum_button)
        self.sum_dies_value = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.sum_dies_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sum_dies_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sum_dies_value.setObjectName("sum_dies_value")
        self.horizontalLayout_10.addWidget(self.sum_dies_value)
        self.clear_sum_button.clicked.connect(lambda:self.clearValue(self.sum_dies_value))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 550, 701, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 440, 701, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.main_dies_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.main_dies_layout.setContentsMargins(0, 0, 0, 0)
        self.main_dies_layout.setObjectName("main_dies_layout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.d4_label = QtWidgets.QLabel(self.layoutWidget)
        self.d4_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d4_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d4_label.setLineWidth(3)
        self.d4_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d4_label.setObjectName("d4_label")
        self.horizontalLayout_7.addWidget(self.d4_label)
        self.roll_d4_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d4_value, 4))
        self.roll_d4_button.setObjectName("roll_d4_button")
        self.horizontalLayout_7.addWidget(self.roll_d4_button)
        self.clear_d4_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d4_value))
        self.clear_d4_button.setObjectName("clear_d4_button")
        self.horizontalLayout_7.addWidget(self.clear_d4_button)
        self.d4_value = QtWidgets.QLabel(self.layoutWidget)
        self.d4_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d4_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d4_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d4_value.setObjectName("d4_value")
        self.horizontalLayout_7.addWidget(self.d4_value)
        self.main_dies_layout.addLayout(self.horizontalLayout_7, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.d10_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.d10_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.d10_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d10_label_2.setLineWidth(3)
        self.d10_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.d10_label_2.setObjectName("d10_label_2")
        self.horizontalLayout_4.addWidget(self.d10_label_2)
        self.roll_d10_button_2 = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d10_value_2, 10))
        self.roll_d10_button_2.setObjectName("roll_d10_button_2")
        self.horizontalLayout_4.addWidget(self.roll_d10_button_2)
        self.clear_d10_button_2 = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d10_value_2))
        self.clear_d10_button_2.setObjectName("clear_d10_button_2")
        self.horizontalLayout_4.addWidget(self.clear_d10_button_2)
        self.d10_value_2 = QtWidgets.QLabel(self.layoutWidget)
        self.d10_value_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d10_value_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d10_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.d10_value_2.setObjectName("d10_value_2")
        self.horizontalLayout_4.addWidget(self.d10_value_2)
        self.main_dies_layout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.d12_label = QtWidgets.QLabel(self.layoutWidget)
        self.d12_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d12_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d12_label.setLineWidth(3)
        self.d12_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d12_label.setObjectName("d12_label")
        self.horizontalLayout_2.addWidget(self.d12_label)
        self.roll_d12_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d12_value, 12))
        self.roll_d12_button.setObjectName("roll_d12_button")
        self.horizontalLayout_2.addWidget(self.roll_d12_button)
        self.clear_d12_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d12_value))
        self.clear_d12_button.setObjectName("clear_d12_button")
        self.horizontalLayout_2.addWidget(self.clear_d12_button)
        self.d12_value = QtWidgets.QLabel(self.layoutWidget)
        self.d12_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d12_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d12_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d12_value.setObjectName("d12_value")
        self.horizontalLayout_2.addWidget(self.d12_value)
        self.main_dies_layout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.d8_label = QtWidgets.QLabel(self.layoutWidget)
        self.d8_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d8_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d8_label.setLineWidth(3)
        self.d8_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d8_label.setObjectName("d8_label")
        self.horizontalLayout_5.addWidget(self.d8_label)
        self.roll_d8_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d8_value, 8))
        self.roll_d8_button.setObjectName("roll_d8_button")
        self.horizontalLayout_5.addWidget(self.roll_d8_button)
        self.clear_d8_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d8_value))
        self.clear_d8_button.setObjectName("clear_d8_button")
        self.horizontalLayout_5.addWidget(self.clear_d8_button)
        self.d8_value = QtWidgets.QLabel(self.layoutWidget)
        self.d8_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d8_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d8_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d8_value.setObjectName("d8_value")
        self.horizontalLayout_5.addWidget(self.d8_value)
        self.main_dies_layout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.d6_label = QtWidgets.QLabel(self.layoutWidget)
        self.d6_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d6_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d6_label.setLineWidth(3)
        self.d6_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d6_label.setObjectName("d6_label")
        self.horizontalLayout_6.addWidget(self.d6_label)
        self.roll_d6_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d6_value, 6))
        self.roll_d6_button.setObjectName("roll_d6_button")
        self.horizontalLayout_6.addWidget(self.roll_d6_button)
        self.clear_d6_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d6_value))
        self.clear_d6_button.setObjectName("clear_d6_button")
        self.horizontalLayout_6.addWidget(self.clear_d6_button)
        self.d6_value = QtWidgets.QLabel(self.layoutWidget)
        self.d6_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d6_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d6_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d6_value.setObjectName("d6_value")
        self.horizontalLayout_6.addWidget(self.d6_value)
        self.main_dies_layout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.d10_label = QtWidgets.QLabel(self.layoutWidget)
        self.d10_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d10_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d10_label.setLineWidth(3)
        self.d10_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d10_label.setObjectName("d10_label")
        self.horizontalLayout_3.addWidget(self.d10_label)
        self.roll_d10_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d10_value, 10))
        self.roll_d10_button.setObjectName("roll_d10_button")
        self.horizontalLayout_3.addWidget(self.roll_d10_button)
        self.clear_d10_button = QtWidgets.QPushButton(self.layoutWidget,clicked = lambda: self.clearValue(self.d10_value))
        self.clear_d10_button.setObjectName("clear_d10_button")
        self.horizontalLayout_3.addWidget(self.clear_d10_button)
        self.d10_value = QtWidgets.QLabel(self.layoutWidget)
        self.d10_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d10_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d10_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d10_value.setObjectName("d10_value")
        self.horizontalLayout_3.addWidget(self.d10_value)
        self.main_dies_layout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.d20_label = QtWidgets.QLabel(self.layoutWidget)
        self.d20_label.setAcceptDrops(False)
        self.d20_label.setFrameShape(QtWidgets.QFrame.Box)
        self.d20_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d20_label.setLineWidth(3)
        self.d20_label.setMidLineWidth(0)
        self.d20_label.setScaledContents(False)
        self.d20_label.setAlignment(QtCore.Qt.AlignCenter)
        self.d20_label.setObjectName("d20_label")
        self.horizontalLayout.addWidget(self.d20_label)
        self.roll_d20_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.rollDie(self.d20_value, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.roll_d20_button.setPalette(palette)
        self.roll_d20_button.setObjectName("roll_d20_button")
        self.horizontalLayout.addWidget(self.roll_d20_button)
        self.clear_d20_button = QtWidgets.QPushButton(self.layoutWidget, clicked = lambda: self.clearValue(self.d20_value))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 140, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.clear_d20_button.setPalette(palette)
        self.clear_d20_button.setObjectName("clear_d20_button")
        self.horizontalLayout.addWidget(self.clear_d20_button)
        self.d20_value = QtWidgets.QLabel(self.layoutWidget)
        self.d20_value.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.d20_value.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d20_value.setLineWidth(1)
        self.d20_value.setAlignment(QtCore.Qt.AlignCenter)
        self.d20_value.setObjectName("d20_value")
        self.horizontalLayout.addWidget(self.d20_value)
        self.main_dies_layout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DnD dice roller"))
        self.misc_rolls_box.setTitle(_translate("MainWindow", "Miscellaneous rolls"))
        self.pct_label.setText(_translate("MainWindow", "Percentage"))
        self.roll_pct_button.setText(_translate("MainWindow", "roll"))
        self.clear_pct_button.setText(_translate("MainWindow", "clear"))
        self.pct_value.setText(_translate("MainWindow", "0"))
        self.coin_label.setText(_translate("MainWindow", "Coin flip (D2 die)"))
        self.coin_flip_button.setText(_translate("MainWindow", "roll"))
        self.clear_coin_button.setText(_translate("MainWindow", "clear"))
        self.coin_flip_value.setText(_translate("MainWindow", "none"))
        self.group_die_actions_box.setTitle(_translate("MainWindow", "Die actions"))
        self.clear_dies_button.setText(_translate("MainWindow", "Clear all dies"))
        self.clear_sum_button.setText(_translate("MainWindow", "Clear sum"))
        self.sum_dies_button.setText(_translate("MainWindow", "Sum all dies"))
        self.sum_dies_value.setText(_translate("MainWindow", "sum of dies"))
        self.d4_label.setText(_translate("MainWindow", "D4 die"))
        self.roll_d4_button.setText(_translate("MainWindow", "roll"))
        self.clear_d4_button.setText(_translate("MainWindow", "clear"))
        self.d4_value.setText(_translate("MainWindow", "0"))
        self.d10_label_2.setText(_translate("MainWindow", "D10 die"))
        self.roll_d10_button_2.setText(_translate("MainWindow", "roll"))
        self.clear_d10_button_2.setText(_translate("MainWindow", "clear"))
        self.d10_value_2.setText(_translate("MainWindow", "0"))
        self.d12_label.setText(_translate("MainWindow", "D12 die"))
        self.roll_d12_button.setText(_translate("MainWindow", "roll"))
        self.clear_d12_button.setText(_translate("MainWindow", "clear"))
        self.d12_value.setText(_translate("MainWindow", "0"))
        self.d8_label.setText(_translate("MainWindow", "D8 die"))
        self.roll_d8_button.setText(_translate("MainWindow", "roll"))
        self.clear_d8_button.setText(_translate("MainWindow", "clear"))
        self.d8_value.setText(_translate("MainWindow", "0"))
        self.d6_label.setText(_translate("MainWindow", "D6 die"))
        self.roll_d6_button.setText(_translate("MainWindow", "roll"))
        self.clear_d6_button.setText(_translate("MainWindow", "clear"))
        self.d6_value.setText(_translate("MainWindow", "0"))
        self.d10_label.setText(_translate("MainWindow", "D10 die"))
        self.roll_d10_button.setText(_translate("MainWindow", "roll"))
        self.clear_d10_button.setText(_translate("MainWindow", "clear"))
        self.d10_value.setText(_translate("MainWindow", "0"))
        self.d20_label.setText(_translate("MainWindow", "D20 die"))
        self.roll_d20_button.setText(_translate("MainWindow", "roll"))
        self.clear_d20_button.setText(_translate("MainWindow", "clear"))
        self.d20_value.setText(_translate("MainWindow", "0"))
        
    def rollDie(self, roll_label, die_size):
        value_rolled = random.randint(1,die_size)
        roll_label.setText(str(value_rolled))
        
    def clearValue(self, roll_label):
        roll_label.setText(str(0))
        
    def clearCoinFlip(self):
        self.coin_flip_value.setText("None")
    
    def coinFlip(self):
        value = random.choice([True,False])
        if(value):
            self.coin_flip_value.setText("Heads")
        else:
            self.coin_flip_value.setText("Tails")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
