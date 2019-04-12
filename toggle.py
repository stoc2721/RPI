from PyQt5 import QtCore, QtGui, QtWidgets
## Our Code
from PyQt5.QtWidgets import QMessageBox


import RPi.GPIO as GPIO
from gpiozero import LED

## Toggle Stuff

GPIO.setmode(GPIO.BCM)
led = LED(23)

def ledToggle():
    if led.is_lit:
        led.off()
        
    else:
        led.on()
        
##
        
## Slider Stuff
led_pin=23
GPIO.setup(led_pin, GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(100)
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(75, 75, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setGeometry(QtCore.QRect(400,25,25,200))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        #self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit.setGeometry(QtCore.QRect(380,220,101,22)
        #font=QtGui.QFont()
        #font.setPointSize(10)
        #self.lineEdit.setFont(font)
        #self.lineEdit.setObject("lineEdit")
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar= QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Toggle LED"))
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)
        
    def sliderMov(self):
        value = self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
    



        
        
import sys
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

