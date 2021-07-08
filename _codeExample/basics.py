# -*- coding: utf-8 -*-
# 파일의 문자 인코딩 선언방법

import sys
#sys모듈(파일)을 불러옴

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from A.B import C : A폴더의 B파일의 C클래스, 변수를 불러옴
from PyQt5 import uic

CalUI = '../_uiFiles/calculator.ui'

class MainDialog(QDialog): #QDialog를 상속받는 MainDialog를 선언
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        #lambda함수 : 코드 한 줄로 함수를 만드는 애
        # 버튼.clicked.connect(함수) : 버튼을 클릭했을 때 해당 함수를 실행
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))

    def NumClicked(self, state, button): #함수선언
        #button : 버튼에 적힌 글자
        exist_line_text = self.q_lineEdit.text()
        #lineEdit에 적힌 문자가 누적되어야하므로 변수에 저장

        now_num_text = button.text()
        #버튼에 적혀있는 글자 가져오기 : .text()
        # #버튼의 숫자 변수에 저장

        self.q_lineEdit.setText(exist_line_text + now_num_text)
        #qlineEdit.setText(문자열) : lineEdit에 해당 문자열'만' 적는 메서드

app = QApplication(sys.argv)
#QApplication() : 기본적으로 프로그램을 실행시키는 역할
main_dialog = MainDialog()
main_dialog.show()
#show() : dialog(창)을 띄우는 메서드(함수)
app.exec_()
#exec_() : 프로그램을 이벤트루프로 진입시키는 메서드 -> 없으면 실행눌러도 창이 켜졌다가 훅 꺼짐
#이벤트루프 : 프로그램을 무한루프 안에서 계속 실행시키고 프로그램에서 벌어지는 이벤트를 받아 처리함.
