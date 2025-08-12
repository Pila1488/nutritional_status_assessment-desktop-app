import sys
from PyQt5 import QtWidgets


import menu
import body_mass_index
import norm_calories
import evaluation_bju


class Function_1(QtWidgets.QMainWindow, body_mass_index.Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.change_wind1)
        self.pushButton.clicked.connect(self.func)
        self.ret_menu = None

    def change_wind1(self):
        self.close()
        self.ret_menu = Menu()
        self.ret_menu.show()

    def func(self):
        self.textBrowser.clear()
        mass = str(self.LineEdit.text())
        grow = str(self.LineEdit_2.text())
        mass = mass.replace(',', '.')
        grow = grow.replace(',', '.')

        try:
            grow = float(grow)
            mass = float(mass)
            if grow <= 0 or mass <= 0:
                self.textBrowser.append('Введите свой рост или массу корректно!')
                return 0
        except ValueError:
            self.textBrowser.append('Введите свой рост или массу корректно!')
            return 0

        res = mass / (grow ** 2)
        self.textBrowser.append('Вывод: ')
        self.textBrowser.append(str(round(res, 1)))

        msg = "Недостаточный вес!"
        if 18.5 <= res < 25:
            msg = 'Нормальный вес!'
        elif 25 <= res < 30:
            msg = 'Избыточный вес!'
        elif 30 <= res < 35:
            msg = 'Ожирение 1 степени!'
        elif 35 <= res < 40:
            msg = 'Ожирение 2 степени!'
        elif res >= 40:
            msg = 'Ожирение 3 степени!'

        self.textBrowser.append(msg)
        self.textBrowser.append('Диапазон значений индекса для нормального веса:' + 'от 18.5 до 25')
        self.textBrowser.show()

class Function_2(QtWidgets.QMainWindow, norm_calories.Ui_Dialog2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.change_wind2)
        self.pushButton.clicked.connect(self.func2)
        self.ret_menu = None

    def change_wind2(self):
        self.close()
        self.ret_menu = Menu()
        self.ret_menu.show()

    def func2(self):
        self.textBrowser.clear()
        mass = self.LineEdit.text()
        grow = self.LineEdit_2.text()
        age = self.LineEdit_3.text()
        gender = self.LineEdit_4.text()
        group = self.LineEdit14.text()
        mass = mass.replace(',', '.')
        grow = grow.replace(',', '.')
        age = age.replace(',', '.')
        is_error = False

        if gender != 'ж' and gender != 'м':
            self.textBrowser.append('Введите свой пол корректно!')
            is_error = True
        try:
            grow = float(grow)
            if grow <= 0 or grow >= 3:
                self.textBrowser.append('Введите свой рост корректно!')
                is_error = True
        except ValueError:
            self.textBrowser.append('Введите свой рост корректно!')
            is_error = True

        try:
            age = float(age)
            if age <= 0:
                self.textBrowser.append('Введите свой возраст корректно!')
                is_error = True
        except ValueError:
            self.textBrowser.append('Введите свой возраст корректно!')
            is_error = True

        try:
            mass = float(mass)
            if mass <= 0:
                self.textBrowser.append('Введите свою массу корректно!')
                is_error = True
        except ValueError:
            self.textBrowser.append('Введите свою массу корректно!')
            is_error = True

        try:
            group = int(group)
            if group not in [1, 2, 3, 4]:
                self.textBrowser.append('Введите номер своей группы интенсивности труда корректно!')
                is_error = True
        except ValueError:
            self.textBrowser.append('Введите номер своей группы интенсивности труда корректно!')
            is_error = True


        if is_error:
            return 0
        vvo = (9.99 * mass) + (6.25 * grow * 100) - (4.92 * age)

        if gender == 'ж':
            vvo -= 161

        elif gender == 'м':
             vvo += 5


        if group == 1:
            res = vvo * 1.4
        if group == 2:
            res = vvo * 1.6
        if group == 3:
            res = vvo * 1.9
        if group == 4:
            res = vvo * 2.2

        self.textBrowser.append('Вам нужно потреблять'+ ' ' + str(round(res,1)) + ' ' + 'ккал в день')
        self.textBrowser.show()

class Function_3(QtWidgets.QMainWindow, evaluation_bju.Ui_Dialog3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.change_wind4)
        self.pushButton.clicked.connect(self.func3)
        self.ret_menu = None

    def change_wind4(self):
        self.close()
        self.ret_menu = Menu()
        self.ret_menu.show()

    def func3(self):
        self.textBrowser.clear()
        vvo = self.LineEdit.text()
        my_b = self.LineEdit_2.text()
        my_j = self.LineEdit_3.text()
        my_u = self.LineEdit_4.text()
        if vvo != '':
            try:
                vvo = float(vvo)
                if vvo <= 0:
                    self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                    return 0
            except ValueError:
                self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                return 0
        if my_b != '':
            try:
                my_b = float(my_b)
                if my_b <= 0:
                    self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                    return 0
            except ValueError:
                self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                return 0
        if my_j != '':
            try:
                my_j = float(my_j)
                if my_j <= 0:
                    self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                    return 0
            except ValueError:
                self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                return 0
        if my_u != '':
            try:
                my_u = float(my_u)
                if my_u <= 0:
                    self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                    return 0
            except ValueError:
                self.textBrowser.append('Введите свою норму ежедневного потребления калорий(Величина основного обмена(ВОО))/белков/жиров/углеводов корректно!')
                return 0
        if vvo != '':
            b = (vvo / 7.7) / 4
            j = ((vvo*2.3)/7.7) / 9
            u = ((vvo*4.4)/7.7) / 4

            self.textBrowser.append('Вам нужно потреблять каждый день примерно ' + str(round(b)) + ' г белков, ' + str(round(j)) + ' г жиров, ' + str(round(u)) + ' г углеводов.' )
            if my_b == '':
                self.textBrowser.append('')
            if my_b != '':
                if b > my_b:
                    otkl_b = b / my_b
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_b,2)) + ' раз меньше, чем вам нужно белков.')
                if b < my_b:
                    otkl_b = my_b / b
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_b,2)) + ' раз больше, чем вам нужно белков.')
                if b == my_b:
                    self.textBrowser.append('Отклонения в потреблении белков нет(совпадает с нормой).')
            if my_j == '':
                self.textBrowser.append('')
            if my_j != '':
                if j > my_j:
                    otkl_j = j / my_j
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_j,2)) + ' раз меньше, чем вам нужно жиров.')
                if j < my_j:
                    otkl_j = my_j / j
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_j,2)) + ' раз больше, чем вам нужно жиров.')
                if j == my_j:
                    self.textBrowser.append('Отклонения в потреблении жиров нет(совпадает с нормой).')
            if my_u == '':
                self.textBrowser.append('')
            if my_u != '':
                if u > my_u:
                    otkl_u = u / my_u
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_u,2)) + ' раз меньше, чем вам нужно углеводов.')
                if u < my_u:
                    otkl_u = my_u / u
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_u,2)) + ' раз больше, чем вам нужно углеводов.')
                if u == my_u:
                    self.textBrowser.append('Отклонения в потреблении углеводов нет(совпадает с нормой).')
            if my_u != '' and my_j != '' and my_b != '':
                my_vvo = my_b + my_j + my_u
                if vvo > my_vvo:
                    otkl_vvo = vvo / my_vvo
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_vvo,2)) + ' раз меньше, чем вам нужно общего количества ккал.')
                if vvo < my_vvo:
                    otkl_vvo = my_vvo / vvo
                    self.textBrowser.append('Вы потребляете в ' + str(round(otkl_vvo,2)) + ' раз больше, чем вам нужно общего количества ккал.')
                if vvo == my_vvo:
                    self.textBrowser.append('Отклонения в потреблении общего количества ккал нет(совпадает с нормой).')


class Menu(QtWidgets.QMainWindow, menu.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.change_wind)
        self.pushButton_2.clicked.connect(self.change_wind2)
        self.pushButton_3.clicked.connect(self.change_wind3)
        self.pushButton_4.clicked.connect(self.ex)
        self.function_window = None

    def change_wind(self):
        self.close()
        self.function_window = Function_1()
        self.function_window.show()

    def change_wind2(self):
        self.close()
        self.function_window = Function_2()
        self.function_window.show()

    def change_wind3(self):
        self.close()
        self.function_window = Function_3()
        self.function_window.show()

    def ex(self):
        exit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()