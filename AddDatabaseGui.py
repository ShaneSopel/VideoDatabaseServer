# Developed by Shane Sopel
# Video Data Base Gui Add Window

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add(object):
    
    def setupUi(self, Add):
        Add.setObjectName("Add")
        Add.resize(464, 301)
        Add.setStyleSheet("background-color: rgb(59, 59, 59)")
        self.layoutWidget = QtWidgets.QWidget(Add)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 140, 241, 42))
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
        self.buttonBox_2.setGeometry(QtCore.QRect(270, 350, 176, 27))
        self.buttonBox_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));")
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(Add)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 50, 138, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Ownerid = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Ownerid.setContentsMargins(0, 0, 0, 0)
        self.Ownerid.setObjectName("Ownerid")
        self.OwnerLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.OwnerLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.5 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.OwnerLabel.setObjectName("OwnerLabel")
        self.Ownerid.addWidget(self.OwnerLabel)
        self.OwnerInput = QtWidgets.QSpinBox(self.layoutWidget1)
        self.OwnerInput.setObjectName("OwnerInput")
        self.Ownerid.addWidget(self.OwnerInput)
        self.layoutWidget2 = QtWidgets.QWidget(Add)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 80, 181, 31))
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
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 110, 221, 31))
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
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 210, 141, 31))
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
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 180, 161, 31))
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
        self.layoutWidget_2 = QtWidgets.QWidget(Add)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 127, 24))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.Movie = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.Movie.setContentsMargins(0, 0, 0, 0)
        self.Movie.setObjectName("Movie")
        self.Movielabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.Movielabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.5 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 8px;")
        self.Movielabel.setObjectName("Movielabel")
        self.Movie.addWidget(self.Movielabel)
        self.Movie_ID = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.Movie_ID.setObjectName("Movie_ID")
        self.Movie.addWidget(self.Movie_ID)
        self.buttonBox = QtWidgets.QDialogButtonBox(Add)
        self.buttonBox.setGeometry(QtCore.QRect(260, 260, 176, 27))
        self.buttonBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.5 rgba(59, 59, 59), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.buttonBox_2.raise_()
        self.layoutWidget_2.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(Add)
        QtCore.QMetaObject.connectSlotsByName(Add)

    def retranslateUi(self, Add):
        _translate = QtCore.QCoreApplication.translate
        Add.setWindowTitle(_translate("Add", "Dialog"))
        self.Actorslabel.setText(_translate("Add", "Actors"))
        self.OwnerLabel.setText(_translate("Add", "Owner ID"))
        self.Titlelabel.setText(_translate("Add", "Title"))
        self.ReleaseYearlabel.setText(_translate("Add", "Release Year"))
        self.Ratinglabel.setText(_translate("Add", "Rating"))
        self.Lengthlabel.setText(_translate("Add", "Length"))
        self.Movielabel.setText(_translate("Add", "Movie ID"))

# main loop
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add = QtWidgets.QMainWindow()
    ui = Ui_Add()
    ui.setupUi(Add)
    Add.show()
    sys.exit(app.exec_())
