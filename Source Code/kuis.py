import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QInputDialog
from PyQt5 import QtWidgets
from classKuis import ResultWindow


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kuis dari Database')
        self.setGeometry(100, 100, 400, 300)

        self.question_label = QLabel()
        self.option_a = QRadioButton()
        self.option_b = QRadioButton()
        self.option_c = QRadioButton()
        self.submit_button = QPushButton('Submit')

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.option_a)
        layout.addWidget(self.option_b)
        layout.addWidget(self.option_c)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.submit_button.clicked.connect(self.check_answer)

        self.current_question = 0
        self.correct_answers = 0
        self.total_questions = 0
        self.participant_id = None

        self.masukkan_id()
        self.load_question()

    def masukkan_id(self):
        while True:
            participant, ok_pressed = QInputDialog.getText(
                self, 'Masukkan ID Peserta', 'ID Peserta:')
            if ok_pressed:
                self.participant_id = participant
                if self.cek_peserta() and not self.repeat_test():
                    break
                else:
                    QMessageBox.warning(
                        self, 'ID Peserta Tidak Valid', 'ID Peserta tidak ditemukan atau Anda sudah melakukan kuis. Masukkan ID Peserta yang valid.')
            else:
                sys.close()

    def cek_peserta(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        participant_id = self.participant_id

        cursor.execute(
            "SELECT COUNT(*) FROM status_kuis WHERE id_pendaftaran = %s", (participant_id,))
        count = cursor.fetchone()[0]

        conn.close()

        return count > 0

    def repeat_test(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        participant_id = self.participant_id

        cursor.execute(
            "SELECT COUNT(*) FROM hasil_kuis WHERE id_pendaftaran = %s", (participant_id,))
        count = cursor.fetchone()[0]

        conn.close()

        return count > 0

    def load_question(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ppdb'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pertanyaan")
        questions = cursor.fetchall()
        self.total_questions = len(questions)

        if self.current_question < self.total_questions:
            question, question_score = questions[self.current_question][1], questions[self.current_question][5]
            self.question_label.setText(question)
            self.option_a.setText(questions[self.current_question][2])
            self.option_b.setText(questions[self.current_question][3])
            self.option_c.setText(questions[self.current_question][4])
            self.question_score = question_score
            self.correct_answer = questions[self.current_question][6]
        else:
            self.show_result()

        conn.close()

    def check_answer(self):
        answer = ''
        if self.option_a.isChecked():
            answer = self.option_a.text()
        elif self.option_b.isChecked():
            answer = self.option_b.text()
        elif self.option_c.isChecked():
            answer = self.option_c.text()

        correct_answer = self.correct_answer
        question_score = self.question_score

        if answer == correct_answer:
            self.correct_answers += question_score

        self.current_question += 1

        if self.current_question == self.total_questions:
            self.show_result()
        else:
            self.clear_selection()
            self.load_question()

    def clear_selection(self):
        self.option_a.setChecked(False)
        self.option_b.setChecked(False)
        self.option_c.setChecked(False)

    def show_result(self):
        result_text = f'Hasil: {self.correct_answers} dari {
            self.total_questions} pertanyaan benar.\n\n'
        result_text += f'ID Peserta: {self.participant_id}\n'
        result_text += f'Skor Akhir: {self.correct_answers}\n'

        self.result_window = ResultWindow(
            result_text, self.participant_id, self.correct_answers)
        self.result_window.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = QuizApp()
    ui.show()
    sys.exit(app.exec_())
