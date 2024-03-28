from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


def get_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes


def display_prime_numbers():
    number = int(lineEdit.text())
    primes = get_prime_numbers(number)
    label2.setText(",".join(str(prime) for prime in primes))


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()


label1 = QLabel("Input")
layout.addWidget(label1)


lineEdit = QLineEdit()
layout.addWidget(lineEdit)


button = QPushButton("Calculate")
button.clicked.connect(display_prime_numbers)
layout.addWidget(button)


label2 = QLabel()
layout.addWidget(label2)


window.setLayout(layout)
window.show()
app.exec_()

