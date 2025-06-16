**PID Controller Simulation with Step Response Analysis**

Description
This project implements a simulation of a PID (Proportional, Integral, Derivative) controller applied to a second-order plant to analyze the impact of the parameters Kp, Ki, and Kd on the system's step response. The code, contained in main.py, generates six plots displaying the system's response for various combinations of Kp, Ki, and Kd, including metrics such as overshoot (%) and settling time (Ts). The plant used is a second-order transfer function, represented by 1/(s² + 2s + 1) .
The plots analyze:

Variation of Kp with fixed Ki and Kd.
Variation of Ki with fixed Kp and Kd.
Variation of Kd with fixed Kp and Ki.
Variation of Ki with low Kp.
Variation of Kd with high Kp.
Variation of Kd with high Ki.

Dependencies
The code relies on the following Python libraries:

NumPy (version 1.21.0 recommended): For mathematical operations and array manipulation [HARRIS et al., 2020].
Matplotlib (version 3.4.2 recommended): For graphical visualization of results [HUNTER, 2007].
Python Control Systems Library (version 0.9.0 recommended): For simulation and analysis of linear control systems [MURRAY et al., 2021].

Installation in Google Colab
In Google Colab, install the required libraries with the following commands:
!pip install numpy==1.21.0
!pip install matplotlib==3.4.2
!pip install control==0.9.0

Installation in Local Environment (Jupyter Notebook)
In a local environment, install the libraries with:
pip install numpy==1.21.0
pip install matplotlib==3.4.2
pip install control==0.9.0

Note: The specified versions are recommended for consistency with the cited references. Newer versions may be used, but compatibility should be verified.
How to Use

Set Up the Environment:

In Google Colab, run the installation commands above if needed.
In a local environment, ensure the libraries are installed in the correct Python environment.


Run the Code:

Copy the contents of main.py into a Google Colab cell or a Jupyter Notebook, or run it directly as a Python script.
Execute the code. It will generate a figure with six subplots showing the step response for different Kp, Ki, and Kd values, along with overshoot and settling time metrics.


Customization:

Plant: Modify the plant's transfer function in the code (plant = ctrl.TransferFunction([1], [1, 2, 1])) to simulate other systems.
PID Parameters: Adjust kp_values, ki_values, and kd_values to test different configurations.
Time Range: Change the time vector (t = np.linspace(0, 10, 1000)) to adjust the simulation duration.


Visualization:

The plots are generated automatically upon running the code. Each plot includes legends with Kp, Ki, Kd values, overshoot (%), and settling time (s).



Code Structure

simulate_pid: Function that simulates the closed-loop system with a PID controller and returns the step response.
calculate_metrics: Calculates overshoot (%) and settling time (Ts) based on the step response.
Main Script: Configures the system, defines test parameters, and generates six plots with varying PID parameters.

References

Harris, C. R., et al. (2020). Array programming with NumPy. Nature, 585, 357–362.
Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95.
Murray, R. M., et al. (2021). Python Control Systems Library. Available at: https://python-control.readthedocs.io.

