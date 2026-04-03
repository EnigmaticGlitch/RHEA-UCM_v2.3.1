# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/real_time_loop.py                                ║
# ║ ⌬ Description: Real-Time Signal Evolution Loop + GUI Plotting           ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import threading
import time
import os
import sys
import warnings

from rhea_ucm.utils.behavioral import BehavioralMonitor
from rhea_ucm.utils.graphing import GraphingTools
from rhea_ucm.utils.logging_setup import get_log_dir
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

# Suppress Matplotlib Unicode warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


def generate_signals():
    t = time.time()
    psi = np.sin(t) + np.random.normal(0, 0.1)
    delta = abs(np.cos(t)) + np.random.normal(0, 0.05)
    phi = np.sin(t + np.pi / 4) + np.random.normal(0, 0.05)
    health = max(0, 1.0 - abs(psi - phi) * delta)
    return psi, delta, phi, health


def launch_rts_interface():
    def run_gui():
        glyph_log("signal", "Initializing Real-Time Signal Monitor", glyph="⚡")

        log_dir = get_log_dir(base="logs/real_time", session_prefix="RTS")
        monitor = BehavioralMonitor(log_dir=log_dir)
        graph = GraphingTools(log_dir=log_dir)

        root = tk.Tk()
        root.title("RTS Signal Monitor — ZADEIAN Sentinel")
        root.configure(bg="#000000")
        root.geometry("950x700")

        fig, ax = plt.subplots(figsize=(9, 4))
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(pady=10)

        line1, = ax.plot([], [], label="Ψ Signal", color="cyan")
        line2, = ax.plot([], [], label="Δ Entropy", color="orange")
        line3, = ax.plot([], [], label="Φ Regulation", color="magenta")
        ax.set_title("Ψ | Δ | Φ — Real-Time Signal Dynamics")
        ax.set_xlim(0, 100)
        ax.set_ylim(-2, 2)
        ax.legend()
        ax.grid(True)

        data_psi, data_delta, data_phi, data_health = [], [], [], []
        running = [True]

        def update_plot():
            if not running[0] or not root.winfo_exists():
                return
            try:
                psi, delta_val, phi, health = generate_signals()

                monitor.record_action("RTS", "signal_update")
                monitor.engine.delta(psi)
                monitor.engine.adaptive_learning(health)

                data_psi.append(psi)
                data_delta.append(delta_val)
                data_phi.append(phi)
                data_health.append(health)

                if len(data_psi) > 100:
                    data_psi.pop(0)
                    data_delta.pop(0)
                    data_phi.pop(0)
                    data_health.pop(0)

                line1.set_data(range(len(data_psi)), data_psi)
                line2.set_data(range(len(data_delta)), data_delta)
                line3.set_data(range(len(data_phi)), data_phi)
                ax.relim()
                ax.autoscale_view()
                canvas.draw()
            except Exception as e:
                glyph_log("anomaly", f"RTS update error: {e}", glyph="☣")
            finally:
                if root.winfo_exists() and running[0]:
                    root.after(1000, update_plot)

        def save_graph():
            try:
                # Patch: only pass filename — let GraphingTools handle full path
                filename = "RTS_entropy_trust_plot.png"
                output_file = "RTS_entropy_trust_plot.png"
                graph.plot_entropy_trust(
                    entropy_log=monitor.engine.entropy_log,
                    trust_log=data_health,
                    output_file=output_file
                )
                glyph_log("bayesian", f"RTS graph saved successfully to {output_file}", glyph="⧊")
            except Exception as e:
                glyph_log("anomaly", f"Graph save error: {e}", glyph="☣")

        def graceful_exit():
            running[0] = False
            glyph_log("phase_lock", "RTS GUI shutdown initiated", glyph="♇")
            try:
                root.after(250, root.quit)
            except Exception:
                pass

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Save Graph", command=save_graph).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Close Window", command=graceful_exit).pack(side=tk.LEFT, padx=5)

        root.protocol("WM_DELETE_WINDOW", graceful_exit)
        root.after(1000, update_plot)
        glyph_log("adaptive", "RTS Signal Monitor GUI Loop Started", glyph="♻")
        print(get_footer())
        root.mainloop()

        # Cleanup patch: prevent __del__ errors
        try:
            def _safe_del(*args, **kwargs): pass
            tk.Variable.__del__ = _safe_del
            tk.Image.__del__ = _safe_del
        except Exception as e:
            print(f"[DEBUG] Final suppression patch failed: {e}")

        try:
            if root.winfo_exists():
                root.destroy()
        except Exception:
            pass

        glyph_log("termination", "RTS GUI fully terminated", glyph="☯")

    if threading.current_thread() is threading.main_thread():
        run_gui()
    else:
        glyph_log("anomaly", "RTS GUI must be launched from the main thread!", glyph="☣")
        print("[ERROR] RTS interface must be called from main thread. Aborting GUI launch.")