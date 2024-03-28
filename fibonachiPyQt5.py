import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


def calculate_fibonacci():
    input_value = int(line_edit.text())
    fib_sequence = fibonacci(input_value)
    fib_label.setText(f"Fibbonachi sonlari: {fib_sequence}")


app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()

input_label = QLabel("Input:")
line_edit = QLineEdit()
fib_button = QPushButton("Fibonacci hisoblash")
fib_label = QLabel()

fib_button.clicked.connect(calculate_fibonacci)

layout.addWidget(input_label)
layout.addWidget(line_edit)
layout.addWidget(fib_button)
layout.addWidget(fib_label)

window.setLayout(layout)
window.show()

sys.exit(app.exec())