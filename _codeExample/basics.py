# -*- coding: utf-8 -*-
# 파일의 문자 인코딩 선언방법

import sys
#sys모듈(파일)을 불러옴

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from A.B import C : A폴더의 B파일의 C클래스, 변수를 불러옴

class MainDialog(QDialog): #QDialog를 상속받는 MainDialog를 선언
    def __init__(self):
        QDialog.__init__(self, None)

        self.setFixedSize(300, 200)
        #창크기 조절(가로px, 세로px), Fixed이므로 크기가 고정되어 조절 불가능
        self.lineEdit = QLineEdit(self)
        #QLineEdit = 사용자가 글을 쓸 수 있는 인풋위젯
        self.pushButton = QPushButton(self)
        #QPushButton = 유저가 누를 수 있는 버튼 위젯

app = QApplication(sys.argv)
#QApplication() : 기본적으로 프로그램을 실행시키는 역할
main_dialog = MainDialog()
main_dialog.show()
#show() : dialog(창)을 띄우는 메서드(함수)
app.exec_()
#exec_() : 프로그램을 이벤트루프로 진입시키는 메서드 -> 없으면 실행눌러도 창이 켜졌다가 훅 꺼짐
#이벤트루프 : 프로그램을 무한루프 안에서 계속 실행시키고 프로그램에서 벌어지는 이벤트를 받아 처리함.