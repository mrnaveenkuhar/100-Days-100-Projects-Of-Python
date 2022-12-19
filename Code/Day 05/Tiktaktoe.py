import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a grid layout to hold the buttons
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the buttons and add them to the grid layout
        self.buttons = []
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                button = QPushButton('', self)
                grid.addWidget(button, i, j)
                self.buttons[i].append(button)

        # Set the button click event handler
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(self.buttonClicked)

        # Create a label to display the game status
        self.label = QLabel('X\'s turn')
        grid.addWidget(self.label, 3, 0, 1, 3)

        # Set the window properties
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tic Tac Toe')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        # Update the button text and the game status label
        if sender.text() == '' and self.label.text()[0] == 'X':
            sender.setText('X')
            self.label.setText('O\'s turn')
        elif sender.text() == '' and self.label.text()[0] == 'O':
            sender.setText('O')
            self.label.setText('X\'s turn')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())
