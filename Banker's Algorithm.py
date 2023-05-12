import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QTextEdit, QPushButton

class BankersAlgorithm(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Create labels for each input field
        self.total_label = QLabel('Total Resources:')
        self.available_label = QLabel('Available Resources:')
        self.current_label = QLabel('Current Allocation:')
        self.maximum_label = QLabel('Maximum Need:')
        self.request_label = QLabel('Request:')

        # Create text boxes for each input field
        self.total_input = QLineEdit()
        self.available_input = QLineEdit()
        self.current_input = QTextEdit()
        self.maximum_input = QTextEdit()
        self.request_input = QLineEdit()

        # Create the 'Run Algorithm' button
        self.run_button = QPushButton('Run Algorithm', self)
        self.run_button.clicked.connect(self.run_algorithm)

        # Create the output box for displaying the results of the algorithm
        self.output_box = QTextEdit()

        # Create the grid layout for the GUI
        grid = QGridLayout()
        grid.setSpacing(10)

        # Add the labels and text boxes to the grid layout
        grid.addWidget(self.total_label, 1, 0)
        grid.addWidget(self.total_input, 1, 1)

        grid.addWidget(self.available_label, 2, 0)
        grid.addWidget(self.available_input, 2, 1)

        grid.addWidget(self.current_label, 3, 0)
        grid.addWidget(self.current_input, 3, 1)

        grid.addWidget(self.maximum_label, 4, 0)
        grid.addWidget(self.maximum_input, 4, 1)

        grid.addWidget(self.request_label, 5, 0)
        grid.addWidget(self.request_input, 5, 1)

        grid.addWidget(self.run_button, 6, 1)

        grid.addWidget(self.output_box, 7, 0, 1, 2)

        self.setLayout(grid)

        # Connect the "Run Algorithm" button to the run_algorithm method
        self.run_button.clicked.connect(self.run_algorithm)

        # Set the size and title of the GUI
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Banker\'s Algorithm')
        self.show()
    def run_algorithm(self):

        # Get the input values from the text boxes
        total = list(map(int, self.total_input.text().split()))
        available = list(map(int, self.available_input.text().split()))
        current = []
        for line in self.current_input.toPlainText().split('\n'):
            current.append(list(map(int, line.split())))
        maximum = []
        for line in self.maximum_input.toPlainText().split('\n'):
            maximum.append(list(map(int, line.split())))
        request = list(map(int, self.request_input.text().split()))

        # Calculate the need matrix
        need = []
        for i in range(len(current)):
            need.append([])
            for j in range(len(total)):
                need[i].append(maximum[i][j] - current[i][j])

        # Run the banker's algorithm
        result = self.bankers_algorithm(total, available, current, maximum, need, request)

        # Display the results in the output box
        if result:
            self.output_box.setText('Request granted!\n')
        else:
            self.output_box.setText('Request denied!\n')

    def bankers_algorithm(self, total, available, current, maximum, need, request):

        # Check if the request exceeds the available resources
        for i in range(len(total)):
            if request[i] > available[i]:
                return False

        # Check if the request exceeds the need of the process
        for i in range(len(total)):
            if request[i] > need[0][i]:
                return False

        # Simulate the allocation of the request
        for i in range(len(total)):
            available[i] -= request[i]
            current[0][i] += request[i]
            need[0][i] -= request[i]

        # Run the safety algorithm to check if the system is in a safe state
        return self.safety_algorithm(total, available, current, need)

    def safety_algorithm(self, total, available, current, need):

        # Initialize the work and finish vectors
        work = available.copy()
        finish = [False] * len(current)

        # Loop through the processes until all have been allocated
        while False in finish:
            # Find a process that can be allocated resources
            for i in range(len(current)):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(len(total))):
                    # Allocate resources to the process
                    for j in range(len(total)):
                        work[j] += current[i][j]
                    finish[i] = True
                    break
            else:
                # No process can be allocated resources
                return False

        # All processes have been allocated
        return True
if __name__ == "__main__":
    app = QApplication(sys.argv)
    bankers_algorithm = BankersAlgorithm()
    sys.exit(app.exec_())
