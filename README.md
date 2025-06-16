---
````markdown
# 🎯 PID Controller Simulation with Step Response Analysis

## 📘 Overview

This project presents a **numerical simulation and analysis** of a PID (Proportional–Integral–Derivative) controller applied to a second-order plant. It aims to visualize the impact of the parameters **Kp**, **Ki**, and **Kd** on the system's step response.

The simulation is performed using Python with scientific libraries, and generates **six comparative plots** showing how each PID parameter affects the system behavior — including **overshoot (%)** and **settling time (Ts)**.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/92/PID_Response_Analysis.png" width="600" alt="PID step response (illustrative)">
</p>

---

## ⚙️ System Model

The plant used in this simulation is a **second-order system** represented by the transfer function:

\[
G(s) = \frac{1}{s^2 + 2s + 1}
\]

The PID controller is implemented in the **parallel form**:

\[
G_c(s) = K_p + \frac{K_i}{s} + K_d \cdot s
\]

The **closed-loop system** is constructed using **unit negative feedback**.

---

## 📊 Plot Analysis

The simulation generates six subplots that explore the step response under the following conditions:

1. **Variation of Kp** (fixed Ki and Kd)
2. **Variation of Ki** (fixed Kp and Kd)
3. **Variation of Kd** (fixed Kp and Ki)
4. **Variation of Ki** with low Kp
5. **Variation of Kd** with high Kp
6. **Variation of Kd** with high Ki

Each plot includes:
- Step response curve
- Overshoot (%)
- Settling time (s)

---

## 🧩 Dependencies

This project requires the following Python libraries:

| Library         | Version     | Purpose                                      |
|----------------|-------------|----------------------------------------------|
| `numpy`        | 1.21.0      | Numerical computations [Harris et al., 2020] |
| `matplotlib`   | 3.4.2       | Plotting and visualization [Hunter, 2007]    |
| `control`      | 0.9.0       | Control system modeling [Murray et al., 2021]|

---

## 🚀 How to Run

### In Google Colab:

```python
!pip install numpy==1.21.0
!pip install matplotlib==3.4.2
!pip install control==0.9.0
````

Then copy the contents of `main.py` into a code cell and run.

---

### In Local Environment (e.g., Jupyter Notebook):

Use the terminal or Jupyter:

```bash
pip install numpy==1.21.0
pip install matplotlib==3.4.2
pip install control==0.9.0
```

Then run the script using:

```bash
python main.py
```

---

## 🧪 Customization

You can adapt the simulation easily:

* **Plant:** Modify `plant = ctrl.TransferFunction([1], [1, 2, 1])` to test other systems.
* **PID Parameters:** Change the lists `kp_values`, `ki_values`, `kd_values`.
* **Simulation Time:** Adjust `t = np.linspace(0, 10, 1000)` to simulate longer or shorter responses.

---

## 📂 Code Structure

| File        | Description                                |
| ----------- | ------------------------------------------ |
| `main.py`   | Main simulation script with plotting logic |
| `README.md` | Project documentation                      |

### Main Functions:

* `simulate_pid()`: Computes closed-loop step response for given Kp, Ki, Kd.
* `calculate_metrics()`: Computes overshoot and settling time from step response.

---

## 📚 References

* Harris, C. R., et al. (2020). *Array programming with NumPy*. Nature, **585**, 357–362.
* Hunter, J. D. (2007). *Matplotlib: A 2D graphics environment*. Computing in Science & Engineering, **9**(3), 90–95.
* Murray, R. M., et al. (2021). *Python Control Systems Library*. [Online Documentation](https://python-control.readthedocs.io)

---

## 📌 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

> *“Simulation brings insight. Understanding PID behavior numerically is a foundation for building real-world control systems with confidence.”*


