import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# --- Graph A: Threat Detection Accuracy ---
# Simulated data: false positive rates and detection sensitivity.
rhea_fp = np.random.uniform(0.01, 0.05, 10)             # RHEA false positive rates
rhea_sens = np.linspace(0.90, 0.98, 10)                 # RHEA detection sensitivities

comp_fp = np.random.uniform(0.05, 0.10, 10)             # Competitor false positive rates
comp_sens = np.linspace(0.85, 0.95, 10)                 # Competitor detection sensitivities

# --- Graph B: Real-Time Processing Speed ---
rhea_latency = np.random.normal(15, 3, 10)              # RHEA processing latency (ms)
comp_latency = np.random.normal(25, 4, 10)              # Competitor processing latency (ms)

# --- Graph C: Entropy-Driven Anomaly Detection ---
time_points = np.arange(0, 10)
rhea_resilience = np.random.uniform(0.7, 0.9, 10)       # RHEA resilience scores
comp_resilience = np.random.uniform(0.5, 0.8, 10)       # Competitor resilience scores

# --- Graph D: Adaptive Security Performance ---
rhea_evolution = np.linspace(1.0, 1.5, 10) + np.random.uniform(0, 0.2, 10)
comp_evolution = np.linspace(0.8, 1.2, 10) + np.random.uniform(0, 0.2, 10)

# --- Plotting the Benchmark Comparison ---
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("RHEA Sentinel vs. Competitor Benchmark Metrics", fontsize=16)

# Graph A: Threat Detection Accuracy
axs[0, 0].plot(rhea_fp, rhea_sens, marker='o', label="RHEA", color='green', linewidth=2)
axs[0, 0].plot(comp_fp, comp_sens, marker='s', label="Competitor", color='red', linewidth=2)
axs[0, 0].set_title("Threat Detection Accuracy")
axs[0, 0].set_xlabel("False Positive Rate")
axs[0, 0].set_ylabel("Detection Sensitivity")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Graph B: Real-Time Processing Speed
indices = np.arange(10)
bar_width = 0.35
axs[0, 1].bar(indices - bar_width/2, rhea_latency, width=bar_width, label="RHEA", color='blue')
axs[0, 1].bar(indices + bar_width/2, comp_latency, width=bar_width, label="Competitor", color='orange')
axs[0, 1].set_title("Real-Time Processing Speed (ms)")
axs[0, 1].set_xlabel("Test Run")
axs[0, 1].set_ylabel("Latency (ms)")
axs[0, 1].legend()
axs[0, 1].grid(True)

# Graph C: Entropy-Driven Anomaly Detection
axs[1, 0].plot(time_points, rhea_resilience, marker='o', label="RHEA", color='purple', linewidth=2)
axs[1, 0].plot(time_points, comp_resilience, marker='s', label="Competitor", color='brown', linewidth=2)
axs[1, 0].set_title("Entropy-Driven Anomaly Detection (Resilience)")
axs[1, 0].set_xlabel("Time Point")
axs[1, 0].set_ylabel("Resilience Score")
axs[1, 0].legend()
axs[1, 0].grid(True)

# Graph D: Adaptive Security Performance
axs[1, 1].plot(rhea_evolution, marker='o', linestyle='-', label="RHEA", color='cyan', linewidth=2)
axs[1, 1].plot(comp_evolution, marker='s', linestyle='--', label="Competitor", color='magenta', linewidth=2)
axs[1, 1].set_title("Adaptive Security Performance")
axs[1, 1].set_xlabel("Test Run")
axs[1, 1].set_ylabel("Evolution Speed")
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
