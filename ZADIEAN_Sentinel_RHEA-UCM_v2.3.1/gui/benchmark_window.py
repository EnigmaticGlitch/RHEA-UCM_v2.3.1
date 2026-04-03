# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /gui/benchmark_window.py                                        ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Real-Time RHEA Benchmark Monitor w/ Glyphic Telemetry    ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import numpy as np
import os
from collections import deque
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from benchmark.benchmark_runner import BenchmarkRunner
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.utils.logging_setup import get_log_dir

class BenchmarkWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ZADEIAN Sentinel Live Benchmark Monitor 📈")
        self.geometry("1920x1080")
        self.configure(bg="#030303")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.runner = BenchmarkRunner()
        self.graph_dir = os.path.join(get_log_dir(base="logs/graphs"), "benchmark")
        os.makedirs(self.graph_dir, exist_ok=True)

        self.pulse_data = deque(maxlen=200)
        self.entropy_data = deque(maxlen=200)
        self.regulation_data = deque(maxlen=200)
        self.health_score_history = deque(maxlen=200)
        self.entropy_spikes = []
        self.sampling = False
        self.benchmark_running = False
        self.scan_thread = None
        self.pulse = 0

         # ══════════[ Background Glyph Canvas Watermark ]══════════
        self.bg_canvas = tk.Canvas(self, width=1000, height=650, bg="#030303", highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        ascii_stamp = """
         _____䷞_____     _____®_____
        ∕  ZADIE-RHEA ╲ ∕  ENIGMATIC  ╲
 _____♏___∕                X               ╲___🧙‍♂️____
∕             PMR RECURSION                 ╲
∕   U.S. PAT. PEND. 63/796,404               ╲___♇___
│                      │                      │
ΔT -1.2ns           REAL-TIME             ΔT +1.2ns
▼ PSYCH/CIS/ENG      ▼ TECKNOWS             ▼ FATHER
"""
        self.bg_canvas.create_text(
            980, 640,
            text=ascii_stamp,
            fill="#2e5411",
            font=("Courier New", 9),
            anchor="se",
            justify="right",
            tags="watermark"
        )
        self.bg_canvas.tag_lower("watermark")

        ttk.Label(self, text="📈 RHEA Benchmark Live Monitoring", font=("Arial", 20)).pack(pady=10)

        # Health Score Container
        self.health_frame = tk.Frame(self, bg="#030303", bd=0, highlightthickness=0)
        self.health_frame.pack(pady=10, fill="x", padx=30)

        self.health_glow_box = tk.Frame(
            self.health_frame,
            bg="#030303",
            highlightthickness=6,
            highlightbackground="#222222",
            bd=0,
            relief="flat"
        )
        self.health_glow_box.pack(padx=20, pady=10)

        self.health_label_prefix = tk.Label(
            self.health_glow_box,
            text="Health Score :",
            font=("Helvetica", 38, "bold"),
            bg="#030303",
            fg="#FFD700"
        )
        self.health_label_prefix.pack(side="left", padx=(20, 10))

        self.health_label_value = tk.Label(
            self.health_glow_box,
            text="Calculating...",
            font=("Helvetica", 48, "bold"),
            bg="#030303",
            fg="#00FF88"
        )
        self.health_label_value.pack(side="left", padx=10)

        plt.style.use('dark_background')
        self.fig, (self.ax1, self.ax2, self.ax3, self.ax4) = plt.subplots(4, 1, figsize=(16, 12), dpi=100)
        self.fig.subplots_adjust(hspace=0.6)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        ttk.Button(self, text="🖼 Save Graph", command=self.save_graph).pack(pady=8)

        glyph_log("adaptive", "BenchmarkWindow initialized", glyph="♻")
        print(get_footer())

        self.start_benchmark()
        self.animate_glow()
        self.update_graph()

    def start_benchmark(self):
        if self.benchmark_running:
            messagebox.showinfo("Benchmark Already Running", "A benchmark session is already running.")
            return
        self.sampling = True
        self.benchmark_running = True
        self.scan_thread = threading.Thread(target=self.continuous_benchmark, daemon=True)
        self.scan_thread.start()
        glyph_log("signal", "Benchmark loop started", glyph="Ψ")

    def continuous_benchmark(self):
        while self.sampling:
            self.pulse_data.extend(self.runner.benchmark_pulse_speed(10))
            new_entropy = self.runner.benchmark_entropy_reaction(10)
            self.entropy_data.extend(new_entropy)
            self.regulation_data.extend(self.runner.benchmark_regulation_speed(10))
            for i, v in enumerate(new_entropy):
                if len(self.entropy_data) > 2 and v > 2 * np.mean(self.entropy_data):
                    self.entropy_spikes.append(len(self.entropy_data) - len(new_entropy) + i)
                    if len(self.entropy_spikes) > 200:
                        self.entropy_spikes.pop(0)
                    glyph_log("entropy", f"Entropy spike detected: {v:.4f}", glyph="Δ")
            time.sleep(2)

    def compute_health_score(self):
        if self.pulse_data and self.entropy_data and self.regulation_data:
            avg_pulse = np.mean(self.pulse_data)
            avg_entropy = np.mean(self.entropy_data)
            avg_regulation = np.mean(self.regulation_data)
            score = 1 / max(avg_pulse + avg_entropy + avg_regulation, 0.001)
            glyph_log("emergent", f"Live Health Score: {score:.4f}", glyph="🧠")
            return score
        return 0

    def determine_health_color(self, score):
        if score >= 7.0: return "#00cc66"
        elif 4.0 <= score < 7.0: return "#ffff00"
        elif 1.0 <= score < 4.0: return "#ff9900"
        else: return "#cc0000"

    def animate_glow(self):
        if hasattr(self, "health_label_value") and self.winfo_exists():
            base_color = self.health_label_value.cget("fg")
            shade = hex((self.pulse % 16) * 16)[2:].zfill(2)
            glow_color = base_color[:1] + shade + base_color[3:] if base_color.startswith("#") else base_color
            self.health_glow_box.configure(highlightbackground=glow_color)
            self.health_label_value.configure(fg=glow_color)
            self.pulse += 1
            self.after(100, self.animate_glow)

    def update_graph(self):
        if self.winfo_exists():
            threading.Thread(target=self._update_graph_worker, daemon=True).start()

    def _update_graph_worker(self):
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()

        self.ax1.plot(self.pulse_data, label="✪ Ψ Pulse Speed", color="cyan")
        self.ax1.set_title("Pulse Signal Generation Speed (Ψ)", color="cyan")
        self.ax1.set_ylabel("Time (s)", color="white")
        self.ax1.legend()
        self.ax1.grid(True)

        self.ax2.plot(self.entropy_data, label="⚡ Δ Entropy Reaction Speed", color="orange")
        for spike in self.entropy_spikes:
            self.ax2.axvline(spike, color='red', linestyle='--', linewidth=1, alpha=0.5)
        self.ax2.set_title("Entropy Reaction Speed (Δ)", color="orange")
        self.ax2.set_ylabel("Time (s)", color="white")
        self.ax2.legend()
        self.ax2.grid(True)

        self.ax3.plot(self.regulation_data, label="♻️ Regulation Adjustment Speed", color="lime")
        self.ax3.set_title("Homeostatic Regulation Speed", color="lime")
        self.ax3.set_xlabel("Samples", color="white")
        self.ax3.set_ylabel("Time (s)", color="white")
        self.ax3.legend()
        self.ax3.grid(True)

        health_score = self.compute_health_score()
        self.health_score_history.append(health_score)
        bar_color = self.determine_health_color(health_score)

        self.ax4.plot(self.health_score_history, label="🧠 Health Score Over Time", color=bar_color)
        self.ax4.set_title("Health Score History", color=bar_color)
        self.ax4.set_ylabel("Score", color="white")
        self.ax4.set_xlabel("Samples", color="white")
        self.ax4.legend()
        self.ax4.grid(True)

        self.health_label_value.config(text=f"{health_score:.2f}")
        self.canvas.draw()
        if self.winfo_exists():
            self.after(5000, self.update_graph)

    def save_graph(self):
        try:
            filename = f"benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            path = os.path.join(self.graph_dir, filename)
            self.fig.savefig(path, dpi=300, bbox_inches="tight")
            glyph_log("bayesian", f"📊 Benchmark graph saved → {path}", glyph="⧊")
        except Exception as e:
            glyph_log("anomaly", f"Failed to save benchmark graph: {str(e)}", glyph="☣")

    def on_close(self):
        self.sampling = False
        self.benchmark_running = False
        if self.scan_thread and self.scan_thread.is_alive():
            self.scan_thread.join(timeout=1)
        glyph_log("phase_lock", "Benchmark monitor closed", glyph="♇")
        self.destroy()