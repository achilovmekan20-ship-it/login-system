#load libraries
import sqlite3
import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import QTimer




#first page / main window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()



                                   # Uİ PART( DESİGN / FRONTEND )

        #create our widgets
        self.username       =   QLineEdit(self)                  #username input area
        self.username.setPlaceholderText(" NAME ")
        self.password       =   QLineEdit(self)                  #password input area
        self.password.setPlaceholderText(" PASSWORD ")
        login          =   QPushButton("LOGİN",self)             #login button
        create_account =   QLabel("Create Account",self)         #clickable text create account
        exit_button    =   QPushButton(" EXİT ",self)            #exit from program

        #set position and size of interface widgets
        self.username.setGeometry       (300, 136, 200, 30)
        self.password.setGeometry       (300, 168, 200, 30)
        login.setGeometry               (300, 200, 200, 30)
        create_account.setGeometry      (355, 230,  90, 10)
        exit_button.setGeometry         (720, 568,  80, 30)

        #set color to our interface widgets(buttons anda labels)
        self.username.setStyleSheet       ("background-color:none;")
        self.password.setStyleSheet       ("background-color:none;")
        login.setStyleSheet               ("background-color:none;")
        create_account.setStyleSheet      ("color:black;")
        exit_button.setStyleSheet         ("background-color:#ad4040;")

                                    #BACKGROUND PART ( BACKEND )

        #create_accaunt event
        create_account.mousePressEvent=self.new_account

        #exit_button event
        exit_button.clicked.connect(self.exit)

        # if log in successful goto main window
        login.clicked.connect(self.log_success)


                                       #FUNCTİONS
    def new_account(self,event):
        Stack.setCurrentWidget(create_w)
        Stack.setWindowTitle(" CREATE ACCOUNT ")

    def log_success(self):

        name = self.username.text()
        password = self.password.text()

        db = sqlite3.connect("users.db")
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE name = ? AND password = ?",
            (name, password)
        )

        user = cursor.fetchone()

        db.close()

        if user:
            from main import stack as main_stack
            main_stack.show()
            Stack.close()

        else:

            if len(name)==0 and len(password)==0:
                self.username.setStyleSheet("background-color:red;")
                self.username.setPlaceholderText("PLEASE FİLL EMPTY ZONES! ")
                QTimer.singleShot(5000, lambda: self.username.setStyleSheet("background-color:none;"))
                QTimer.singleShot(5000, lambda: self.username.setPlaceholderText(" NAME "))
                self.password.setStyleSheet("background-color:red;")
                self.password.setPlaceholderText("PLEASE FİLL EMPTY ZONES! ")
                QTimer.singleShot(5000, lambda: self.password.setStyleSheet("background-color:none;"))
                QTimer.singleShot(5000, lambda: self.password.setPlaceholderText(" PASSWORD "))

            elif len(name)==0:
                self.username.setStyleSheet("background-color:red;")
                self.username.setPlaceholderText("PLEASE FİLL EMPTY ZONES! ")
                QTimer.singleShot(5000,lambda :self.username.setStyleSheet("background-color:none;"))
                QTimer.singleShot(5000, lambda: self.username.setPlaceholderText(" NAME "))

            elif len(password)==0:
                self.password.setStyleSheet("background-color:red;")
                self.password.setPlaceholderText("PLEASE FİLL EMPTY ZONES! ")
                QTimer.singleShot(5000, lambda: self.password.setStyleSheet("background-color:none;"))
                QTimer.singleShot(5000, lambda: self.password.setPlaceholderText(" PASSWORD "))


    def exit(self):
        Stack.close()
        QApplication.quit()





                                          # CREATE ACCOUNT WİNDOW

#second page / second(sett)
class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()

                                 # Uİ PART( DESİGN / FRONTEND )

        #create ui widgets
        self.name           =  QLineEdit  (self)
        self.name.setPlaceholderText      (" NAME ")
        self.password       =  QLineEdit  (self)
        self.password.setPlaceholderText  (" PASSWORD ")
        create_button  =   QPushButton    ("CREATE",self)

        back           =   QPushButton    (" BACK ",self) #back to log in window

        #set color and size for widgets
        self.name.setStyleSheet           ("background-color:none;")
        self.password.setStyleSheet       ("background-color:none;")
        create_button.setStyleSheet       ("background-color:none;")
        back.setStyleSheet                ("background-color:none;")

        self.name.setGeometry             (1, 1,  200, 30)
        self.password.setGeometry         (1, 32, 200, 30)
        create_button.setGeometry         (1, 62, 200, 30)
        back.setGeometry                  (720, 1, 80, 30)


                                        #PRESS EVENTS / BACKGROUND PART( BACKEND )
        create_button.clicked.connect(self.create_account)

        back.clicked.connect(self.back_window)


                                         # DATABASE

    def create_account(self):

        name = self.name.text()
        password = self.password.text()

        if len(name) == 0 and len(password) == 0:                                            #İF BOTH OF BOXES EMPTY REMİND İT TO USER(for 5s turns in to red)
            self.name.setStyleSheet("background-color:red;")
            self.name.setPlaceholderText("PLEASE ENTER NAME! ")
            QTimer.singleShot(5000, lambda: self.name.setStyleSheet("background-color:none;"))
            QTimer.singleShot(5000, lambda: self.name.setPlaceholderText(" NAME "))
            self.password.setStyleSheet("background-color:red;")
            self.password.setPlaceholderText("PLEASE ENTER PASSWORD! ")
            QTimer.singleShot(5000, lambda: self.password.setStyleSheet("background-color:none;"))
            QTimer.singleShot(5000, lambda: self.password.setPlaceholderText(" PASSWORD "))
                                                                                            #İF ONLY NAME EMPTY REMİND TO USER (for 5s turns in to red)
        elif len(name) == 0:
            self.name.setStyleSheet("background-color:red;")
            self.name.setPlaceholderText("PLEASE ENTER NAME! ")
            QTimer.singleShot(5000, lambda: self.name.setStyleSheet("background-color:none;"))
            QTimer.singleShot(5000, lambda: self.name.setPlaceholderText(" NAME "))
                                                                                             # İF ONLY PASSWORD EMPTY REMİND TO USER (for 5s turns in to red)
        elif len(password) == 0:
            self.password.setStyleSheet("background-color:red;")
            self.password.setPlaceholderText("PLEASE ENTER PASSWORD! ")
            QTimer.singleShot(5000, lambda: self.password.setStyleSheet("background-color:none;"))
            QTimer.singleShot(5000, lambda: self.password.setPlaceholderText(" PASSWORD "))

        else:
            import sqlite3

            db = sqlite3.connect("users.db")
            cursor = db.cursor()

            try:
                cursor.execute(
                    "INSERT INTO users (name, password) VALUES (?, ?)",
                    (name, password)
                )

                db.commit()

                self.name.setStyleSheet("background-color:green;")
                self.password.setStyleSheet("background-color:green;")
                QTimer.singleShot(10000, lambda: self.name.setStyleSheet("background-color:none;"))
                QTimer.singleShot(10000, lambda: self.password.setStyleSheet("background-color:none;"))


            except sqlite3.IntegrityError:
                print("this account is exists")






                                         #FUNCTİONS

    def back_window(self):
        Stack.setCurrentWidget(login_w)
        Stack.setWindowTitle("MAİN WİNDOW")


app=QApplication(sys.argv)


# create instance of Main and Settings window for using it in stack
login_w=LoginWindow()
create_w=CreateWindow()

# add windows to stack
Stack=QStackedWidget()
Stack.addWidget(login_w)
Stack.addWidget(create_w)

# set main window to the first page / set window title(name) to current page
Stack.setCurrentWidget(login_w)
Stack.setWindowTitle("MAİN WİNDOW")

# set background color for main window
Stack.setStyleSheet("background-color:#829982;")
Stack.setFixedSize(800,600)
Stack.show()

if __name__ == "__main__":
 #dont close while program run
 sys.exit(app.exec_())