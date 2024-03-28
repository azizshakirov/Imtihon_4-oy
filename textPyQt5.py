'''
PyQineeditga bir nechta gap yoziladi va sizning vazifangiz 2-labelda barcha sozlarni chiqaring
vt5 orqali 3ta label, 1ta lineedit va 1ta button yarating. 1-labelmi nomini"Input".
1-la 3-labelda esa gaplarni chiqaring
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Sozlar va Gaplar')
        self.setGeometry(100, 100, 300, 200)
        
        self.label_input = QLabel('Input:', self)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton('Chiqarish', self)
        self.button.clicked.connect(self.print_words_and_sentences)
        
        self.label_words = QLabel('Sozlar:', self)
        self.label_sentences = QLabel('Gaplar:', self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_input)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.button)
        vbox.addWidget(self.label_words)
        vbox.addWidget(self.label_sentences)
        
        self.setLayout(vbox)
        
    def print_words_and_sentences(self):
        input_text = self.line_edit.text()
        words = input_text.split()
        sentences = input_text.split('.')
        
        words_output = ", ".join(words)
        sentences_output = ""
        for sentence in sentences:
            if sentence.strip():
                sentences_output += sentence.strip() + ".\n"
        
        self.label_words.setText('Sozlar: ' + words_output)
        self.label_sentences.setText('Gaplar: ' + sentences_output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

