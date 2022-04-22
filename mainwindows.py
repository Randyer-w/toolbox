import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
################################################
#######创建主窗口
################################################
class FirstMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('毕业设计工具箱   作者：王浩然')
        self.setFixedSize(400,300)
        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("制作论文展示图")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("制作差分图")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("生成Mask以及训练数据集")
        self.buttonLayout.addWidget(self.pushButton3)

        # self.pushButton3 = QPushButton()
        # self.pushButton3.setText("打开提示框")
        # self.buttonLayout.addWidget(self.pushButton3)



        # 设置中间文本
        self.label = QLabel()
        self.label.setText("毕业答辩")
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        self.Layout.addWidget(self.label)

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)




    # 按钮一：打开主界面
    windowList = []
    def on_pushButton1_clicked(self):
        os.system('python ./scrip/cut_imagetocompare.py')



    # 按钮二：打开对话框
    def on_pushButton2_clicked(self):
        os.system('python ./scrip/get_diffimage.py')



    def on_pushButton3_clicked(self):
        os.system('python ./scrip/koutu.py')



    # 按钮三：打开提示框
    # def on_pushButton3_clicked(self):
    #     QMessageBox.information(self, "提示", "这是information框！")




################################################
#######第二个主界面
################################################
class SecondWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('第二主界面')

        # 设置中间文本
        self.label = QLabel()
        self.label.setText("第二个主界面")
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        self.setCentralWidget(self.label)




    ###### 重写关闭事件，回到第一界面
    windowList = []
    def closeEvent(self, event):
        the_window = FirstMainWindow()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()




################################################
#######对话框
################################################
class TestdemoDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('对话框')

        ### 设置对话框类型
        self.setWindowFlags(Qt.Tool)

################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
