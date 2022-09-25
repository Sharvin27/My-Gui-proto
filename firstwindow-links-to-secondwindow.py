import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()


        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("TEAM VAAYUSHASTRA")
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setStyleSheet("background-color:black")

        # to set the image to the screen
        # self.labels = QLabel(self)
        # self.image1 = QPixmap("logo.jpg")
        # self.labels.setPixmap(self.image1)
        # self.labels.move(660, 200)

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(800, 280, 400, 400)
        self.btn1.setStyleSheet("background-color:black")

        #to set the icon for button and the resize the icon
        self.btn1.setIcon(QIcon("logo.jpg"))
        self.btn1.setIconSize(QSize(400, 400))
        self.btn1.animateClick(1500)
        self.btn1.clicked.connect(self.showSecondWindow)


    def showSecondWindow(self):
        self.sw = SecondWindow()
        self.sw.show()


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.start = False
        self.n=0
        self.yup=False
        

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("TEAM VAAYUSHASTRA")
        self.setWindowIcon(QIcon('logo.jpg'))

        self.label_a = QLabel(self)
        self.label_a.setGeometry(290, 100, 100, 500)

        self.transform1 = 0
        self.transform2 = 0
        self.transform3 = 0

        self.i = 0
        self.j = 0
        self.k = 0

        self.angle1 = 0
        self.angle2 = 0
        self.angle3 = 0

        # self.setStyleSheet("background-color:lightblue")

        # to add image in the window -> import QLabel class from QtWidgets; create an object of QLabel class
        # and object of QPixmap class

        # image 1

        self.label1 = QLabel(self)
        self.pixmap1 = QPixmap('img.png')
        self.label1.setPixmap(self.pixmap1)
        self.label1.move(70, 120)
        self.label1.resize(500, 500)
        # self.label1.setAlignment(Qt.AlignVCenter)
        # self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setAlignment(Qt.AlignCenter)

        # self.pixmap = self.pixmap.scaled(32, 32)
        # self.label.resize(self.pixmap.width(), self.pixmap.height())

        # image 2
        self.label2 = QLabel(self)
        self.pixmap2 = QPixmap('image.png')
        self.label2.setPixmap(self.pixmap2)
        self.label2.move(670, 150)
        self.label2.resize(500, 500)
        # self.label2.setAlignment(Qt.AlignVCenter)
        # self.label2.setAlignment(Qt.AlignHCenter) #to rotate around the centre
        # both these had shortcomings of the plane shifting of its center towards the bottom
        self.label2.setAlignment(Qt.AlignCenter)

        # image 3
        self.label3 = QLabel(self)
        self.pixmap3 = QPixmap("images.png")
        self.label3.setPixmap(self.pixmap3)
        self.label3.move(1290, 190)
        self.label3.resize(500, 500)
        # self.label3.setAlignment(Qt.AlignVCenter)
        # self.label3.setAlignment(Qt.AlignHCenter)
        self.label3.setAlignment(Qt.AlignCenter)

        # button1
        self.btn1 = QPushButton(self)
        self.btn1.setText("Enter")
        self.btn1.setFont(QFont("Helvetica", 18))

        # input box for button1
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(260, 600)
        self.textbox1.resize(100, 40)
        # placeholer text for input box and its font
        self.textbox1.setPlaceholderText("Enter angle")
        self.textbox1.setFont(QFont("Helvetica", 10))
        self.btn1.setGeometry(260, 660, 100, 50)
        self.btn1.clicked.connect(self.rotate1)

        # button2
        self.btn2 = QPushButton(self)
        self.btn2.setText("Enter")
        self.btn2.setFont(QFont("Helvetica", 18))  # to change the font within the box you need PyQt5.QtGui

        # input box for button2
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(870, 600)
        self.textbox2.resize(100, 40)
        # placeholer text for input box and its font
        self.textbox2.setPlaceholderText("Enter angle")
        self.textbox2.setFont(QFont("Helvetica", 10))

        self.btn2.setGeometry(870, 660, 100, 50)
        self.btn2.clicked.connect(self.rotate2)

        # button3
        self.btn3 = QPushButton(self)
        self.btn3.setText("Enter")

        # input box for button3
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(1470, 600)
        self.textbox3.resize(100, 40)
        # placeholer text for input box and its font
        self.textbox3.setPlaceholderText("Enter angle")
        self.textbox3.setFont(QFont("Helvetica", 10))

        self.btn3.setFont(QFont("Helvetica", 18))
        self.btn3.setGeometry(1470, 660, 100, 50)
        self.btn3.clicked.connect(self.rotate3)

        # it was initial task to increment text in button
        # def text_button1(self):
        #     self.i = self.i+10
        #     self.btn1.setText(str(self.i))
        #
        # def text_button2(self):
        #     self.j = self.j+10
        #     self.btn2.setText(str(self.j))
        #
        # def text_button3(self):
        #     self.k = self.k+10
        #     self.btn3.setText(str(self.k))


        self.timer()


    def rotate1(self):
        # for text from the input box
        offset = self.angle1
        if (self.textbox1.text())[1:].isdigit():
            self.angle1 = int(self.textbox1.text())

        if int(self.angle1) >= 0:
            self.transform1 = QTransform().rotate(self.angle1 - offset)
        else:
            self.angle1 = 360 - abs(int(self.angle1))
            self.transform1 = QTransform().rotate(self.angle1 - offset)

        self.pixmap1 = self.pixmap1.transformed(self.transform1, Qt.SmoothTransformation)
        self.label1.setPixmap(self.pixmap1)

    def rotate2(self):
        offset = self.angle2
        if (self.textbox2.text())[1:].isdigit():
            self.angle2 = int(self.textbox2.text())

        if int(self.angle2) >= 0:
            self.transform2 = QTransform().rotate(self.angle2 - offset)
        else:
            self.angle2 = 360 - abs(int(self.angle2))
            self.transform2 = QTransform().rotate(self.angle2 - offset)

        transform2 = QTransform().rotate(self.angle2 - offset)
        self.pixmap2 = self.pixmap2.transformed(transform2, Qt.SmoothTransformation)
        self.label2.setPixmap(self.pixmap2)

    def rotate3(self):
        offset = self.angle3
        if (self.textbox3.text())[1:].isdigit():
            self.angle3 = int(self.textbox3.text())

        if int(self.angle3) >= 0:
            self.transform3 = QTransform().rotate(self.angle3 - offset)
        else:
            self.angle3 = 360 - abs(self.angle3)
            self.transform3 = QTransform().rotate(self.angle3 - offset)

        transform3 = QTransform().rotate(self.angle3 - offset)
        self.pixmap3 = self.pixmap3.transformed(transform3, Qt.SmoothTransformation)
        self.label3.setPixmap(self.pixmap3)



    def timer(self):

        #all the elements required for displaying timer -> start, reset, push, display

        self.time = QLabel(self)
        self.time.setGeometry(1650, 50, 200, 50)
        self.time.setStyleSheet("background-color:white")
        self.time.setStyleSheet("border:5px")
        self.time.setText("0.0")
        self.time.setFont(QFont("Times", 15))
        self.time.setAlignment(Qt.AlignCenter)

        self.start = QPushButton("Start",self)
        self.start.setGeometry(1600, 110, 100, 50)
        self.start.setFont(QFont("Helvetica",15))
        self.start.clicked.connect(self.start_action)

        self.pause = QPushButton("Pause", self)
        self.pause.setGeometry(1700, 110, 100, 50)
        self.pause.setFont(QFont("Helvetica", 15))
        self.pause.clicked.connect(self.pause_action)

        self.reset = QPushButton("Reset", self)
        self.reset.setGeometry(1800, 110, 100, 50)
        self.reset.setFont(QFont("Helvetica", 15))
        self.reset.clicked.connect(self.reset_action)


    def start_timer(self):
        #displays the timer in the label
        self.timer = QTimer(self)   #to create a timer object
        self.timer.timeout.connect(self.showTime)   #adding action to timer
        # 'timeout' is the only signal of QTimer class
        (self.timer).start(1000)   #update the timer every tenth second (100 milliseconds = 10 seconds)

    def showTime(self):  #This is a function thats is called by line 247 every second due to line 249

        if  self.start and self.yup:
            self.count=0
        
        elif self.start and not self.yup:
            self.count += 1
            self.pause.setText("Pause")
            self.n +=1

            while self.count>=1000:
                self.start = False
                self.time.setText("Completed")
                break
            # if self.count >= 10:
            #     self.start = False
            #     self.time.setText("Completed!")

        if self.start:
            text = str(self.count/10)+' s'
            #(self.count/10) gives you seconds and milliseconds
            #(self.count) gives you just integer seconds

            self.time.setText(text)


    def start_action(self):
        self.start = True
        self.yup=False
        self.start_timer()

    def pause_action(self):
        
        if self.n % 2 != 0:
            self.start=False
            self.n-=1
            self.pause.setText("Resume")

        else:
            self.start=True
            self.n+=1
            self.pause.setText("Pause")

    def reset_action(self):
        self.start = True
        self.yup = True




app = QApplication([])

window = MainWindow()
window.show()

app.exec_()
