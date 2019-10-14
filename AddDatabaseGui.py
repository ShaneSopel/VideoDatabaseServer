# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add(object):
    def setupUi(self, Add):
        Add.setObjectName("Add")
        Add.resize(400, 300)
        Add.setStyleSheet("background-color: rgb(59, 59, 59)")
        self.layoutWidget = QtWidgets.QWidget(Add)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 241, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Actor = QtWidgets.QGridLayout(self.layoutWidget)
        self.Actor.setContentsMargins(0, 0, 0, 0)
        self.Actor.setObjectName("Actor")
        self.Actorslabel = QtWidgets.QLabel(self.layoutWidget)
        self.Actorslabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.Actorslabel.setObjectName("Actorslabel")
        self.Actor.addWidget(self.Actorslabel, 0, 0, 1, 1)
        self.ActorInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.ActorInput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.ActorInput.setObjectName("ActorInput")
        self.Actor.addWidget(self.ActorInput, 0, 1, 1, 1)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(Add)
        self.buttonBox_2.setGeometry(QtCore.QRect(200, 260, 176, 27))
        self.buttonBox_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));")
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(Add)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 115, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.FilmId = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.FilmId.setContentsMargins(0, 0, 0, 0)
        self.FilmId.setObjectName("FilmId")
        self.FilmIdLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.FilmIdLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.5 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.FilmIdLabel.setObjectName("FilmIdLabel")
        self.FilmId.addWidget(self.FilmIdLabel)
        self.FilmIdInput = QtWidgets.QSpinBox(self.layoutWidget1)
        self.FilmIdInput.setObjectName("FilmIdInput")
        self.FilmId.addWidget(self.FilmIdInput)
        self.layoutWidget2 = QtWidgets.QWidget(Add)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Title = QtWidgets.QGridLayout(self.layoutWidget2)
        self.Title.setContentsMargins(0, 0, 0, 0)
        self.Title.setObjectName("Title")
        self.Titlelabel = QtWidgets.QLabel(self.layoutWidget2)
        self.Titlelabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.Titlelabel.setObjectName("Titlelabel")
        self.Title.addWidget(self.Titlelabel, 0, 0, 1, 1)
        self.TitleInput = QtWidgets.QLineEdit(self.layoutWidget2)
        self.TitleInput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.TitleInput.setObjectName("TitleInput")
        self.Title.addWidget(self.TitleInput, 0, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(Add)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 90, 221, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.ReleaseYear = QtWidgets.QGridLayout(self.layoutWidget3)
        self.ReleaseYear.setContentsMargins(0, 0, 0, 0)
        self.ReleaseYear.setObjectName("ReleaseYear")
        self.ReleaseYearInput = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ReleaseYearInput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.ReleaseYearInput.setObjectName("ReleaseYearInput")
        self.ReleaseYear.addWidget(self.ReleaseYearInput, 0, 1, 1, 1)
        self.ReleaseYearlabel = QtWidgets.QLabel(self.layoutWidget3)
        self.ReleaseYearlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.ReleaseYearlabel.setObjectName("ReleaseYearlabel")
        self.ReleaseYear.addWidget(self.ReleaseYearlabel, 0, 0, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(Add)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 190, 141, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.Rating = QtWidgets.QGridLayout(self.layoutWidget4)
        self.Rating.setContentsMargins(0, 0, 0, 0)
        self.Rating.setObjectName("Rating")
        self.Ratinglabel = QtWidgets.QLabel(self.layoutWidget4)
        self.Ratinglabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.5 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.Ratinglabel.setObjectName("Ratinglabel")
        self.Rating.addWidget(self.Ratinglabel, 0, 0, 1, 1)
        self.RatingInput = QtWidgets.QDoubleSpinBox(self.layoutWidget4)
        self.RatingInput.setObjectName("RatingInput")
        self.Rating.addWidget(self.RatingInput, 0, 1, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(Add)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.Length = QtWidgets.QGridLayout(self.layoutWidget5)
        self.Length.setContentsMargins(0, 0, 0, 0)
        self.Length.setObjectName("Length")
        self.Lengthlabel = QtWidgets.QLabel(self.layoutWidget5)
        self.Lengthlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.Lengthlabel.setObjectName("Lengthlabel")
        self.Length.addWidget(self.Lengthlabel, 0, 0, 1, 1)
        self.LengthInput = QtWidgets.QDoubleSpinBox(self.layoutWidget5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LengthInput.setFont(font)
        self.LengthInput.setStyleSheet("")
        self.LengthInput.setObjectName("LengthInput")
        self.Length.addWidget(self.LengthInput, 0, 1, 1, 1)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.buttonBox_2.raise_()
        self.LengthInput.raise_()

        self.retranslateUi(Add)
        QtCore.QMetaObject.connectSlotsByName(Add)

    def retranslateUi(self, Add):
        _translate = QtCore.QCoreApplication.translate
        Add.setWindowTitle(_translate("Add", "Add To DataBase"))
        self.Actorslabel.setText(_translate("Add", "Actors"))
        self.FilmIdLabel.setText(_translate("Add", "Film ID"))
        self.Titlelabel.setText(_translate("Add", "Title"))
        self.ReleaseYearlabel.setText(_translate("Add", "Release Year"))
        self.Ratinglabel.setText(_translate("Add", "Rating"))
        self.Lengthlabel.setText(_translate("Add", "Length"))

# main loop
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add = QtWidgets.QMainWindow()
    ui = Ui_Add()
    ui.setupUi(Add)
    Add.show()
    sys.exit(app.exec_())
