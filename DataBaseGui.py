# sopels temp server

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import struct
import sys
import threading
import time
import os
 
#define multicast group
multicast_group = ('239.0.0.1', 5007)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive datta
sock.settimeout(None)


# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

var = 2

class Ui_TempService(object):
    def setupUi(self, TempService):
        TempService.setObjectName("TempService")
        TempService.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(TempService)
        self.centralwidget.setObjectName("centralwidget")

        # the three buttons
        # Shutdown the program
        self.shutDown = QtWidgets.QPushButton(self.centralwidget)
        self.shutDown.setGeometry(QtCore.QRect(90, 330, 131, 81))
        self.shutDown.setObjectName("ShutDown")
        self.shutDown.clicked.connect(self.shutdownIt)

        # Reboot the program
        self.reboot = QtWidgets.QPushButton(self.centralwidget)
        self.reboot.setGeometry(QtCore.QRect(260, 330, 131, 81))
        self.reboot.setObjectName("Reboot")
        self.reboot.clicked.connect(self.rebootIt)

        # Exit the program
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(420, 330, 131, 81))
        self.exit.setObjectName("Exit")
        self.exit.clicked.connect(self.closeIt)

        # lcd inputs and their icons
        self.Temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(485, 40, 300, 81))
        self.Temp.setObjectName("Temp")
        self.Humid = QtWidgets.QLCDNumber(self.centralwidget)
        self.Humid.setGeometry(QtCore.QRect(485, 160, 300, 81))
        self.Humid.setObjectName("Humid")
        self.TempImg = QtWidgets.QLabel(self.centralwidget)
        self.TempImg.setGeometry(QtCore.QRect(425, 60, 50, 50))
        self.TempImg.setText("")
        self.TempImg.setPixmap(QtGui.QPixmap("Pictures/temp.jpg"))
        self.TempImg.setObjectName("TempImg")
        self.HumidImg = QtWidgets.QLabel(self.centralwidget)
        self.HumidImg.setGeometry(QtCore.QRect(425, 180, 50, 50))
        self.HumidImg.setText("")
        self.HumidImg.setPixmap(QtGui.QPixmap("Pictures/humid.jpeg"))
        self.HumidImg.setObjectName("HumidImg")

        # this section of code handles the labels for the gui
        # the labels are the server icons.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 10, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 151, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 10, 151, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 180, 151, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 180, 151, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 180, 151, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Pictures/server.png"))
        self.label_6.setObjectName("label_6")
        
        TempService.setCentralWidget(self.centralwidget)
        self.TempServ = QtWidgets.QMenuBar(TempService)
        self.TempServ.setGeometry(QtCore.QRect(0, 0, 924, 19))
        self.TempServ.setObjectName("TempServ")
        TempService.setMenuBar(self.TempServ)
        self.statusbar = QtWidgets.QStatusBar(TempService)
        self.statusbar.setObjectName("TempServ")
        TempService.setStatusBar(self.statusbar)

        self.retranslateUi(TempService)
        QtCore.QMetaObject.connectSlotsByName(TempService)

        # threads are used to handle the temp settings, sending server readings,
        # and handling the server callbacks
        temp = threading.Thread(target=self.setTemp)
        temp.start()
        
        serverResponse = threading.Thread(target=self.serverResponse)
        serverResponse.start()

        serverSend = threading.Thread(target=self.serverSend)
        serverSend.start()


    def retranslateUi(self, TempService):
        _translate = QtCore.QCoreApplication.translate
        TempService.setWindowTitle(_translate("TempService", "Temperature Service"))
        self.shutDown.setText(_translate("TempService", "Shut Down"))
        self.reboot.setText(_translate("TempService", "reboot"))
        self.exit.setText(_translate("TempService", "Exit"))

        
    # def for setting temp and humidity data on the screen
    def setTemp(self):
        while True:
            # humidity and temperature data

            # printing an update to the log
            print ('updating temp:' )
            print ('\n')
            print ('updating Humid: ')
            print ('\n')

            #update every second
            time.sleep(1)


    # def for handling the server response.
    # When the servers are on it will change the labels.
    def serverResponse(self):
        print ("swag")

    def serverSend(self):
        print ("Swagger")
        
    def shutdownIt(self):
        os.system('shutdown --poweroff')

    def rebootIt(self):
        os.system('reboot now')
    
    def closeIt(self):
        self.close()
        
# end of class functions
            

# main loop
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TempService = QtWidgets.QMainWindow()
    ui = Ui_TempService()
    ui.setupUi(TempService)
    TempService.show()

    # timer for resyncing app
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.setTemp)
    timer.start(10000)
    
    sys.exit(app.exec_())
