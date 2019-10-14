# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseVideo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 600)
        MainWindow.setStyleSheet("background-color: rgb(59, 59, 59)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#
# ADD BUTTON
#
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(40, 330, 131, 101))
        self.Add_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Add_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.Add_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/add_button_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_button.setIcon(icon)
        self.Add_button.setIconSize(QtCore.QSize(100, 100))
        self.Add_button.setDefault(False)
        self.Add_button.setFlat(False)
        self.Add_button.setObjectName("Add_button")
#
# DELETE BUTTON
#       
        self.Delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_button.setGeometry(QtCore.QRect(210, 330, 131, 101))
        self.Delete_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.Delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/delete_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete_button.setIcon(icon1)
        self.Delete_button.setIconSize(QtCore.QSize(100, 100))
        self.Delete_button.setObjectName("Delete_button")
#
# VIEW BUTTON
#
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setGeometry(QtCore.QRect(400, 330, 131, 101))
        self.view_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;\n"
"")
        self.view_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Pictures/view_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_button.setIcon(icon2)
        self.view_button.setIconSize(QtCore.QSize(90, 90))
        self.view_button.setObjectName("view_button")
#
# SEARCH BUTTON       
#
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setEnabled(True)
        self.search_button.setGeometry(QtCore.QRect(590, 330, 131, 101))
        self.search_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.search_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.search_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Pictures/search_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon3)
        self.search_button.setIconSize(QtCore.QSize(90, 90))
        self.search_button.setAutoDefault(False)
        self.search_button.setObjectName("search_button")
#
# EXIT BUTTON
#       
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(220, 450, 321, 101))
        self.Exit_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.Exit_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Pictures/exit_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_button.setIcon(icon4)
        self.Exit_button.setIconSize(QtCore.QSize(100, 80))
        self.Exit_button.setObjectName("Exit_button")

#
# SORTON LOGO
#
        self.Sorton = QtWidgets.QLabel(self.centralwidget)
        self.Sorton.setGeometry(QtCore.QRect(130, 20, 511, 131))
        self.Sorton.setText("")
        self.Sorton.setPixmap(QtGui.QPixmap("Pictures/sorton.png"))
        self.Sorton.setObjectName("Sorton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
# RetranslateUi
#
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#
# main loop
#
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Video = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Video)
    Video.show()
    sys.exit(app.exec_())


