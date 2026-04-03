# benchmark/benchmark_graphs.py

import matplotlib.pyplot as plt

def plot_pulse_speed(times):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(times)), times, label="✪ Ψ Pulse Speed — (Signal generation speed benchmark)", color='blue')
    plt.xlabel("Iterations")
    plt.ylabel("Computation Time (seconds)")
    plt.title("ZADEIAN Sentinel Benchmark: Ψ Pulse Generation Speed")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_entropy_reaction_speed(times):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(times)), times, label="⚡ ∆ Entropy Reaction Speed — (Entropy adaptation speed benchmark)", color='orange')
    plt.xlabel("Iterations")
    plt.ylabel("Computation Time (seconds)")
    plt.title("ZADEIAN Sentinel Benchmark: ∆ Entropy Reaction Speed")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_regulation_speed(times):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(times)), times, label="🌬️ Regulation Speed — (Homeostatic adjustment speed benchmark)", color='green')
    plt.xlabel("Iterations")
    plt.ylabel("Computation Time (seconds)")
    plt.title("ZADEIAN Sentinel Benchmark: Regulation Adjustment Speed")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def describe_graphs():
    descriptions = {
        "✪ Ψ Pulse Speed": "Measures the time to generate new Ψ signals (system pulse events).",
        "⚡ ∆ Entropy Reaction Speed": "Measures the reaction time to entropy disturbances.",
        "🌬️ Regulation Speed": "Measures the time to stabilize after disturbances."
    }
    return descriptions