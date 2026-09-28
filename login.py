#load libraries
import sys
from PyQt5.QtWidgets import  *


#first page / main window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()


                                   # Uİ PART( DESİGN / FRONTEND )

        #create our widgets
        username       =   QLineEdit(self)                  #username input area
        username.setPlaceholderText(" NAME ")
        password       =   QLineEdit(self)                  #password input area
        password.setPlaceholderText(" PASSWORD ")
        login          =   QPushButton("LOGİN",self)        #login button
        create_account =   QLabel("Create Account",self)    #clickable text create account
        exit_button    =   QPushButton(" EXİT ",self)       #exit from program

        #set position and size of interface widgets
        username.setGeometry       (300, 136, 200, 30)
        password.setGeometry       (300, 168, 200, 30)
        login.setGeometry          (300, 200, 200, 30)
        create_account.setGeometry (355, 230,  90, 10)
        exit_button.setGeometry    (720, 568,  80, 30)

        #set color to our interface widgets(buttons anda labels),I cant able to set color only background of window
        username.setStyleSheet       ("background-color:none;")
        password.setStyleSheet       ("background-color:none;")
        login.setStyleSheet          ("background-color:none;")
        create_account.setStyleSheet ("color:black;")
        exit_button.setStyleSheet    ("background-color:#ad4040;")

                                    #BACKGROUND PART ( BACKEND )

        #create_accaunt event
        create_account.mousePressEvent=self.new_account

        #exit_button event
        exit_button.clicked.connect(self.exit)


                                       #FUNCTİONS
    def new_account(self,event):
        stack.setCurrentWidget(create_w)
        stack.setWindowTitle(" CREATE ACCOUNT ")

    def exit(self):
        stack.close()



                                          # SETTİNG WİNDOW

#second page / second(sett)
class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()

                                 # Uİ PART( DESİGN / FRONTEND )

        #create ui widgets
        name           =   QLineEdit(self)
        name.setPlaceholderText(" NAME ")
        password       =   QLineEdit(self)
        password.setPlaceholderText(" PASSWORD ")
        create_button  =   QPushButton("CREATE",self)

        back           =   QPushButton(" BACK ",self) #back to log in window

        #set color and size for widgets
        name.setStyleSheet          ("background-color:none;")
        password.setStyleSheet      ("background-color:none;")
        create_button.setStyleSheet ("background-color:none;")
        back.setStyleSheet          ("background-color:none;")

        name.setGeometry            (1, 1,  200, 30)
        password.setGeometry        (1, 32, 200, 30)
        create_button.setGeometry   (1, 62, 200, 30)
        back.setGeometry            (720, 1, 80, 30)


                                        #BACKGROUND PART( BACKEND )
        back.clicked.connect(self.back_window)





                                         #FUNCTİONS

    def back_window(self):
        stack.setCurrentWidget(login_w)
        stack.setWindowTitle("MAİN WİNDOW")


app=QApplication(sys.argv)

# create instance of Main and Settings window for using it in stack
login_w=LoginWindow()
create_w=CreateWindow()

# add windows to stack
stack=QStackedWidget()
stack.addWidget(login_w)
stack.addWidget(create_w)

# set main window to the first page / set window title(name) to current page
stack.setCurrentWidget(login_w)
stack.setWindowTitle("MAİN WİNDOW")

# set background color for main window
stack.setStyleSheet("background-color:#829982;")
stack.setFixedSize(800,600)

stack.show()

#dont close while program run
sys.exit(app.exec_())