


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow
import instaloader
import sys,os
import urllib.request


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)



class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 40, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 40, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 90, 631, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_detail = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_detail.setGeometry(QtCore.QRect(450, 130, 221, 401))
        self.groupBox_detail.setObjectName("groupBox_detail")
        self.label_full_name = QtWidgets.QLabel(self.groupBox_detail)
        self.label_full_name.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label_full_name.setObjectName("label_full_name")
        self.label_3 = QtWidgets.QLabel(self.groupBox_detail)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_detail)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_detail)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 55, 16))
        self.label_5.setObjectName("label_5")
        self.full_name_edit = QtWidgets.QLineEdit(self.groupBox_detail)
        self.full_name_edit.setGeometry(QtCore.QRect(20, 50, 181, 22))
        self.full_name_edit.setObjectName("full_name_edit")
        self.followers_edit = QtWidgets.QLineEdit(self.groupBox_detail)
        self.followers_edit.setGeometry(QtCore.QRect(20, 100, 181, 22))
        self.followers_edit.setObjectName("followers_edit")
        self.followings_edit = QtWidgets.QLineEdit(self.groupBox_detail)
        self.followings_edit.setGeometry(QtCore.QRect(20, 150, 181, 22))
        self.followings_edit.setObjectName("followings_edit")
        self.bio_edit = QtWidgets.QTextEdit(self.groupBox_detail)
        self.bio_edit.setGeometry(QtCore.QRect(20, 200, 181, 151))
        self.bio_edit.setReadOnly(True)
        self.bio_edit.setObjectName("bio_edit")
        self.saveBtn = QtWidgets.QPushButton(self.groupBox_detail)
        self.saveBtn.setGeometry(QtCore.QRect(20, 360, 181, 31))
        self.saveBtn.setObjectName("saveBtn")
        self.groupBox_pic = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_pic.setGeometry(QtCore.QRect(50, 130, 391, 401))
        self.groupBox_pic.setObjectName("groupBox_pic")
        self.photo = QtWidgets.QLabel(self.groupBox_pic)
        self.photo.setGeometry(QtCore.QRect(20, 30, 350, 350))
        self.photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photo.setText("")
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        ### my customation
        MainWindow.setFixedSize(714,566)
        MainWindow.setWindowIcon(QtGui.QIcon(resource_path('./assets/icon.ico')))
        MainWindow.setWindowTitle("Get Data from Instagram")
        self.pushButton.clicked.connect(self.start)
        self.saveBtn.clicked.connect(self.save)
        self.full_name_edit.setReadOnly(True)
        self.followers_edit.setReadOnly(True)
        self.followings_edit.setReadOnly(True)
        self.bio_edit.setReadOnly(True)
        self.groupBox_detail.setEnabled(False)
        self.groupBox_pic.setEnabled(False)
        self.lineEdit.returnPressed.connect(self.pushButton.click)

        
    def start(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        user= self.lineEdit.text()
        if user =="":
            self.progressBar.setValue(0)
            QApplication.restoreOverrideCursor()
            return
        self.progressBar.setValue(10)

        loader = instaloader.Instaloader()
        self.progressBar.setValue(20)
        try:
            profile = instaloader.Profile.from_username(loader.context, user)
            profile_pic = profile.profile_pic_url
            self.progressBar.setValue(50)
        except:
            QApplication.restoreOverrideCursor()
            return

        import urllib.request

        print('Beginning file download with urllib2...')

        url = profile_pic
        self.progressBar.setValue(60)

        self.full_name_edit.setText(profile.full_name)
        self.followers_edit.setText(str(profile.followers))
        self.followings_edit.setText(str(profile.followees))
        self.bio_edit.setText(profile.biography)
        self.groupBox_detail.setEnabled(True)
        self.progressBar.setValue(80)


        if os.path.isfile(resource_path('./temp.jpg')):
            os.remove(resource_path('./temp.jpg'))

        try:
            urllib.request.urlretrieve(url, resource_path('./temp.jpg'))
            self.photo.setPixmap(QtGui.QPixmap(resource_path('./temp.jpg')))
            self.groupBox_pic.setEnabled(True)
            self.progressBar.setValue(90)

        except:
            QApplication.restoreOverrideCursor()
            return
        
        if os.path.isfile(resource_path('./temp.jpg')):
            os.remove(resource_path('./temp.jpg'))
            self.progressBar.setValue(100)
            QApplication.restoreOverrideCursor()

    def save(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        user= self.lineEdit.text()
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, user)
        profile_pic = profile.profile_pic_url
        url = profile_pic
        save_path = user+'.jpg'
        urllib.request.urlretrieve(url, os.path.abspath(save_path))


        QApplication.restoreOverrideCursor()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter username:"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.groupBox_detail.setTitle(_translate("MainWindow", "Details"))
        self.label_full_name.setText(_translate("MainWindow", "full name:"))
        self.label_3.setText(_translate("MainWindow", "Followers:"))
        self.label_4.setText(_translate("MainWindow", "Followings::"))
        self.label_5.setText(_translate("MainWindow", "Biography"))
        self.saveBtn.setText(_translate("MainWindow", "Save Picture"))
        self.groupBox_pic.setTitle(_translate("MainWindow", "Profile Picture"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
