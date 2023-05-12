# Banker's Algorithm

This program implements the banker's algorithm for deadlock prevention. It allows the user to input the total number of resources, available resources, current allocation, and maximum need. It also allows the user to enter that a particular process requests a certain number of a particular resource. The program uses the banker's algorithm to determine whether or not to grant the request. The program contains a graphical user interface (GUI) to show the steps of the algorithm.

## Requirements

This program requires the following:

- Python 3
- PyQt5

## How to use

To use this program, follow these steps:

1. Install Python 3 and PyQt5 if not already installed.

2. Run the program by executing the `main.py` file.

3. Input the total number of resources, available resources, current allocation, and maximum need.

4. Enter the request for a particular process.

5. Click on the "Run Algorithm" button to run the banker's algorithm.

6. The program will display the result of the algorithm in the output box.

## How it works

The program uses the banker's algorithm to determine whether or not to grant a request for resources. The algorithm works by simulating the allocation of the requested resources and then checking if the system is in a safe state. If the system is in a safe state, the resources are allocated; otherwise, the request is denied.

The program first calculates the need matrix by subtracting the current allocation from the maximum need. It then checks if the request exceeds the available resources and if the request exceeds the need of the process. If either of these conditions is true, the request is denied. If the request is valid, the program simulates the allocation of the request by subtracting the requested resources from the available resources, adding the requested resources to the current allocation, and subtracting the requested resources from the need matrix. The program then runs the safety algorithm to check if the system is in a safe state. The safety algorithm works by simulating the allocation of resources to each process and checking if the system is still in a safe state after each allocation. If the system is in a safe state, the request is granted; otherwise, the request is denied.

## GUI

The program contains a graphical user interface (GUI) that allows the user to input the required values and view the output of the algorithm. The GUI is created using the PyQt5 library. The GUI consists of several input fields for the total number of resources, available resources, current allocation, maximum need, and request. The program also contains a "Run Algorithm" button and an output box that displays the result of the algorithm. When the user clicks on the "Run Algorithm" button, the program runs the algorithm and displays the result in the output box.

![Python 3 10 12_05_2023 1_54_20 PM](https://github.com/Marise-Medhat/banker-s-algorithm/assets/133333482/2d5dc5e8-9e50-44d8-91c8-5a15e140afed)
![Python 3 10 12_05_2023 1_55_39 PM](https://github.com/Marise-Medhat/banker-s-algorithm/assets/133333482/74efbbf9-f4e1-4ae7-a66d-83850360acc7)
