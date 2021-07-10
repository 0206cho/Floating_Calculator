# -*- coding: utf-8 -*-
# 파일의 문자 인코딩 선언방법

import sys, UI
# sys모듈(파일)을 불러옴

import PyQt5
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from A.B import C : A폴더의 B파일의 C클래스, 변수를 불러옴

class MainDialog(QDialog, UI.Ui_Dialog):  # QDialog를 상속받는 MainDialog를 선언
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setupUi(self)

        self.setWindowTitle('계산기')

        self.num_pushButton_1.clicked.connect(
            lambda state, button=self.num_pushButton_1: self.NumClicked(state, button))
        # lambda함수 : 코드 한 줄로 함수를 만드는 애
        # 버튼.clicked.connect(함수) : 버튼을 클릭했을 때 해당 함수를 실행
        self.num_pushButton_2.clicked.connect(
            lambda state, button=self.num_pushButton_2: self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(
            lambda state, button=self.num_pushButton_3: self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(
            lambda state, button=self.num_pushButton_4: self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(
            lambda state, button=self.num_pushButton_5: self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(
            lambda state, button=self.num_pushButton_6: self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(
            lambda state, button=self.num_pushButton_7: self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(
            lambda state, button=self.num_pushButton_8: self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(
            lambda state, button=self.num_pushButton_9: self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(
            lambda state, button=self.num_pushButton_0: self.NumClicked(state, button))

        self.sing_pushButton_1.clicked.connect(
            lambda state, button=self.sing_pushButton_1: self.NumClicked(state, button))  # '/'
        self.sing_pushButton_2.clicked.connect(
            lambda state, button=self.sing_pushButton_2: self.NumClicked(state, button))  # '*'
        self.sing_pushButton_3.clicked.connect(
            lambda state, button=self.sing_pushButton_3: self.NumClicked(state, button))  # '-'
        self.sing_pushButton_4.clicked.connect(
            lambda state, button=self.sing_pushButton_4: self.NumClicked(state, button))  # '+'

        self.p_open_pushButton.clicked.connect(
            lambda state, button=self.p_open_pushButton: self.NumClicked(state, button))  # '('
        self.p_close_pushButton.clicked.connect(
            lambda state, button=self.p_close_pushButton: self.NumClicked(state, button))  # ')'
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton: self.NumClicked(state, button))
        self.per_pushButton.clicked.connect(
            lambda state, button=self.per_pushButton: self.NumClicked(state, button))  # % = *0.01

        self.p_open_pushButton_2.clicked.connect(
            lambda state, button=self.p_open_pushButton_2: self.NumClicked(state, button))  # '<'
        self.p_close_pushButton_2.clicked.connect(
            lambda state, button=self.p_close_pushButton_2: self.NumClicked(state, button))  # '>'
        self.and_pushButton.clicked.connect(
            lambda state, button=self.and_pushButton: self.NumClicked(state, button))  # '&'
        self.or_pushButton.clicked.connect(
            lambda state, button=self.or_pushButton: self.NumClicked(state, button))  # '|'

        self.result_pushButton.clicked.connect(self.MakeResult)  # '='
        self.reset_pushButton.clicked.connect(self.Reset)  # 'C'
        self.del_pushButton.clicked.connect(self.Delete)  # 'del'

        self.del_pushButton.setStyleSheet(
            '''
              QPushButton{image:url(../image/delete.jpg); border:0px;}
              QPushButton:hover{image:url(../image/delete_red.jpg); border:0px;}
             ''')
        # 1: del버튼의 이미지와 경계선 없앰 2: 마우스 올릴 때의 이미지
        # python에서 따옴표 3개문자열 = 이스케이프 문자없이 줄바꿈가능, 보기 편함

        self.and_pushButton.setStyleSheet(
            '''
              QPushButton{image:url(../image/andButton.png);}
             ''')

    def NumClicked(self, state, button):  # 함수선언
        if button == self.per_pushButton:
            now_num_text = '*0.01'
            print(math.sqrt(now_num_text))
            # 변수 now_num_text - per_버튼일 경우 변수값이 *0.01이 되어야 함
        # elif button == self.root_pushButton:
        #     root = pow(float
        #     now_num_text = pow(float(now_num_text)
        #     print(now_num_text)

        else:
            now_num_text = button.text()

        # button : 버튼에 적힌 글자
        exist_line_text = self.q_lineEdit.text()
        # lineEdit에 적힌 문자가 누적되어야하므로 변수에 저장

        # now_num_text = button.text() -> 위 if문이 들어가면서 이 코드는 삭제
        # 버튼에 적혀있는 글자 가져오기 : .text()
        # #버튼의 숫자 변수에 저장

        self.q_lineEdit.setText(exist_line_text + now_num_text)
        # qlineEdit.setText(문자열) : lineEdit에 해당 문자열'만' 적는 메서드

    def MakeResult(self):  # 수식 계산하는 역할
        try:
            result = eval(self.q_lineEdit.text())
            # eval : 문자열의 수식을 계산, q_lineEdit에 있는 글자들을 계산]
            self.a_lineEdit.setText(str(result))
            # setText메서드 안에는 문자열형식만 들어갈 수 있음 -> str(변수) : 변수의 형식을 문자열로 반환
            # print(type(result)) #타입확인

        # except:
        # pass
        # pass : 함수가 실행돼도 동작하지 않음 -> 에러 안 난척,,ㅎ
        # 계산기의 버튼을 말도 안되게 누르면 원랜 실행창 중지됨

        except Exception as e:  # 어떤 에러가 뜨는지 확인 가능
            print(e)

    def Reset(self):
        self.q_lineEdit.clear()
        # .clear() : lineEdit을 초기화
        self.a_lineEdit.setText(str('0'))
        # 리셋버튼 누르면 결과창은 0으로 변함

    def Delete(self):
        # 원래 있던 거 보전하면서 뒤에 있는 문자만 하나씩 지우기
        exist_line_text = self.q_lineEdit.text()

        # 문자슬라이싱 = 문자열을 인덱싱을 이용해 잘라주는 기능
        exist_line_text = exist_line_text[:-1]  # = exist_line_text에 인덱스 -1인 가장 마지막에 전힌 문자만 뺸 문자열
        self.q_lineEdit.setText(exist_line_text)


app = QApplication(sys.argv)
# QApplication() : 기본적으로 프로그램을 실행시키는 역할
main_dialog = MainDialog()
main_dialog.show()
# show() : dialog(창)을 띄우는 메서드(함수)
app.exec_()
# exec_() : 프로그램을 이벤트루프로 진입시키는 메서드 -> 없으면 실행눌러도 창이 켜졌다가 훅 꺼짐
# 이벤트루프 : 프로그램을 무한루프 안에서 계속 실행시키고 프로그램에서 벌어지는 이벤트를 받아 처리함.