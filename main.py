import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Função para simular o sistema com controlador PID
def simulate_pid(Kp, Ki, Kd, t, plant):
    # Controlador PID: Gc(s) = Kp + Ki/s + Kd*s
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])  # Forma: Kd*s + Kp + Ki/s
    # Sistema em malha fechada
    sys_cl = ctrl.feedback(pid * plant, 1)
    # Resposta ao degrau
    t, y = ctrl.step_response(sys_cl, T=t)
    return y

# Função para calcular métricas (overshoot, tempo de acomodação)
def calculate_metrics(t, y, setpoint=1.0):
    # Overshoot (%)
    max_value = np.max(y)
    overshoot = ((max_value - setpoint) / setpoint) * 100 if max_value > setpoint else 0

    # Tempo de acomodação (tempo para y ficar dentro de ±2% do setpoint)
    tolerance = 0.02 * setpoint
    settling_time = t[-1]
    for i in range(len(y)):
        if np.all(np.abs(y[i:] - setpoint) <= tolerance):
            settling_time = t[i]
            break

    return overshoot, settling_time

# Configurações do sistema
t = np.linspace(0, 10, 1000)  # Vetor de tempo
plant = ctrl.TransferFunction([1], [1, 2, 1])  # Planta exemplo: 1/(s^2 + 2s + 1)

# Valores de teste para Kp, Ki, Kd
kp_values = [1, 5, 10]  # Três valores de Kp
ki_values = [0, 0.5, 1]  # Três valores de Ki
kd_values = [0, 0.1, 0.5]  # Três valores de Kd

# Configuração dos gráficos
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.suptitle('Análise do Controlador PID: Efeito de Kp, Ki e Kd', fontsize=16)

# Parâmetros base
Kp_base, Ki_base, Kd_base = 5, 0.5, 0.1

# Plot 1: Variação de Kp
for Kp in kp_values:
    y = simulate_pid(Kp, Ki_base, Kd_base, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[0, 0].plot(t, y, label=f'Kp={Kp}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[0, 0].set_title('Variação de Kp (Ki={:.1f}, Kd={:.1f})'.format(Ki_base, Kd_base))
axs[0, 0].set_xlabel('Tempo (s)')
axs[0, 0].set_ylabel('Saída')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Plot 2: Variação de Ki
for Ki in ki_values:
    y = simulate_pid(Kp_base, Ki, Kd_base, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[0, 1].plot(t, y, label=f'Ki={Ki}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[0, 1].set_title('Variação de Ki (Kp={:.1f}, Kd={:.1f})'.format(Kp_base, Kd_base))
axs[0, 1].set_xlabel('Tempo (s)')
axs[0, 1].set_ylabel('Saída')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Plot 3: Variação de Kd
for Kd in kd_values:
    y = simulate_pid(Kp_base, Ki_base, Kd, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[1, 0].plot(t, y, label=f'Kd={Kd}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[1, 0].set_title('Variação de Kd (Kp={:.1f}, Ki={:.1f})'.format(Kp_base, Ki_base))
axs[1, 0].set_xlabel('Tempo (s)')
axs[1, 0].set_ylabel('Saída')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Plot 4: Kp baixo, variação de Ki
for Ki in ki_values:
    y = simulate_pid(kp_values[0], Ki, Kd_base, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[1, 1].plot(t, y, label=f'Ki={Ki}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[1, 1].set_title('Variação de Ki com Kp baixo ({:.1f})'.format(kp_values[0]))
axs[1, 1].set_xlabel('Tempo (s)')
axs[1, 1].set_ylabel('Saída')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Plot 5: Kp alto, variação de Kd
for Kd in kd_values:
    y = simulate_pid(kp_values[2], Ki_base, Kd, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[2, 0].plot(t, y, label=f'Kd={Kd}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[2, 0].set_title('Variação de Kd com Kp alto ({:.1f})'.format(kp_values[2]))
axs[2, 0].set_xlabel('Tempo (s)')
axs[2, 0].set_ylabel('Saída')
axs[2, 0].legend()
axs[2, 0].grid(True)

# Plot 6: Ki alto, variação de Kd
for Kd in kd_values:
    y = simulate_pid(Kp_base, ki_values[2], Kd, t, plant)
    overshoot, settling_time = calculate_metrics(t, y)
    axs[2, 1].plot(t, y, label=f'Kd={Kd}, OS={overshoot:.2f}%, Ts={settling_time:.2f}s')
axs[2, 1].set_title('Variação de Kd com Ki alto ({:.1f})'.format(ki_values[2]))
axs[2, 1].set_xlabel('Tempo (s)')
axs[2, 1].set_ylabel('Saída')
axs[2, 1].legend()
axs[2, 1].grid(True)

# Ajustar layout e exibir
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
