#load libraries
import sys

from PyQt5.QtWidgets import  *



#first page / main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

                                   # Uİ PART( DESİGN / FRONTEND )

        #create widgets
        self.setting_button  = QPushButton     ("SETTİNGS",self)

        #set a size and position to widgets
        self.setting_button.setGeometry        (730,1,70,30)

        #set a color widgets
        self.setting_button.setStyleSheet      ("background-color:#569c8f;")


                                    #BACKGROUND WORK ( BACKEND )

        #set a process to setting button
        self.setting_button.clicked.connect(self.change_window)





                                    # FUNCTIONS / EVENT
        # change window function
    def change_window(self):
            stack.setCurrentWidget(setting_w)
            stack.setWindowTitle("SETTİNG")



#second page / second(sett)
class SettingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_w=main_w #we need this for changing color button from main window

                                     # Uİ PART( DESİGN / FRONTEND )
        #ui theme changer
        self.dark     = QRadioButton("DARK",   self)
        self.normal   = QRadioButton("NORMAL", self)
        self.white    = QRadioButton("WHİTE",  self)
        self.back     = QPushButton("BACK",self)
        self.back.setStyleSheet("background-color:#569c8f;") #when window opens first the button color will change
        self.log_out       = QPushButton("LOG OUT",self) #log out and goto login window
        self.log_out.setStyleSheet("background-color:#569c8f;")
        self.exit          = QPushButton("EXİT",self)    #close the program
        self.exit.setStyleSheet("background-color:#ad4040;")


        #set position and size of widgets
        self.dark.setGeometry        (1, 1, 80, 10)
        self.normal.setGeometry      (1, 19, 80, 10)
        self.white.setGeometry       (1, 39, 80, 10)
        self.back.setGeometry        (730, 1, 70, 30)
        self.log_out.setGeometry     (730, 545, 70, 30)
        self.exit.setGeometry        (730, 575, 70, 30)



                                        # BACKGROUND PART ( BACKEND )

        #set event to theme checkbox
        self.dark.clicked.connect(lambda:self.theme("DARK"))
        self.normal.clicked.connect(lambda:self.theme("NORMAL"))
        self.white.clicked.connect(lambda:self.theme("WHİTE"))
        self.back.clicked.connect(self.change_window)

        self.log_out.clicked.connect(self.logout)           #log out and goto login page
        self.exit.clicked.connect(lambda:stack.close())      #close program (break)


                                        #FUNCTİONS

        #change theme color function
    def theme(self,mod):
        if mod=="DARK":
            stack.setStyleSheet("background-color:#141313;")
            self.dark.setStyleSheet("color:#26a80f;")
            self.normal.setStyleSheet("color:#26a80f;")
            self.white.setStyleSheet("color:#26a80f;")
            self.back.setStyleSheet("color:black;""background-color:#26a80f;")
            self.main_w.setting_button.setStyleSheet("background-color:#26a80f;")
            self.log_out.setStyleSheet("background-color:#26a80f;")

        elif mod=="NORMAL":
            stack.setStyleSheet("background-color:#829982;")
            self.dark.setStyleSheet("color:black;")
            self.normal.setStyleSheet("color:black;")
            self.white.setStyleSheet("color:black;")
            self.back.setStyleSheet("color:black;""background-color:#569c8f;")
            self.main_w.setting_button.setStyleSheet("background-color:#569c8f;")
            self.log_out.setStyleSheet("background-color:#569c8f;")

        elif mod=="WHİTE":
            stack.setStyleSheet("background-color:none;")
            self.dark.setStyleSheet("color:black;")
            self.normal.setStyleSheet("color:black;")
            self.white.setStyleSheet("color:black;")
            self.back.setStyleSheet("color:black;""background-color:none;")
            self.main_w.setting_button.setStyleSheet("background-color:none;")
            self.log_out.setStyleSheet("background-color:none;")

        #change window into main
    def change_window(self):
            stack.setCurrentWidget(main_w)
            stack.setWindowTitle("MAİN WİNDOW")

        #logout back to log in window
    def logout(self):
        from login import Stack as logging_out_stack  #import login page for run
        logging_out_stack.show()
        stack.close()




stack=QStackedWidget()

# create instance of Main and Settings window for using it in stack
main_w=MainWindow()
setting_w=SettingWindow()

# add windows to stack
stack.addWidget(main_w)
stack.addWidget(setting_w)

# set main window to the first page / set window title(name) to current page
stack.setCurrentWidget(main_w)
stack.setWindowTitle("MAİN WİNDOW")

# set background color for main window
stack.setStyleSheet("background-color:#829982;")
stack.setFixedSize(800,600)

stack.show()

if __name__=="__main__":
 sys.exit(app.exec_())