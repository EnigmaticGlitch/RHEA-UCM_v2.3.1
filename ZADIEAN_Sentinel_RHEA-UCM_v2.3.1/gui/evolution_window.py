# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /gui/evolution_window.py                                        ║
# ║ ⌬ Description: Self-Adaptive Evolution Monitor (Ψ→Δ→🧠→Reg)              ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk
import threading
import random
import os

from rhea_ucm.utils.behavioral import BehavioralMonitor
from rhea_ucm.utils.intrusion_detection import IntrusionDetection
from rhea_ucm.utils.graphing import GraphingTools
from rhea_ucm.utils.logging_setup import get_log_dir
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

class EvolutionWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ZADEIAN Sentinel - Evolution Monitor 🧬")
        self.geometry("1000x650")
        self.configure(bg="#030303")

        self.log_dir = get_log_dir(base="logs/graphs")
        self.graph_tools = GraphingTools(self.log_dir)
        self.behavior_monitor = BehavioralMonitor(log_dir=self.log_dir)
        self.intrusion_detector = IntrusionDetection()
        self.entropy_values = []
        self.threat_values = []
        self.entity_threat_index = {}
        self.entropy_spike_markers = []
        self.entropic_glyphs = []
        self.running = False
        self.after_id = None

        # ══════════[ Background Glyph Canvas Watermark ]══════════
        self.bg_canvas = tk.Canvas(self, width=1000, height=650, bg="#030303", highlightthickness=0)
        self.bg_canvas.place(x=-350, y=-30, relwidth=1, relheight=1)

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

        ttk.Label(self, text="System Evolution Monitor [Self-Adaptation]",
                  font=("Helvetica", 18), background="#030303", foreground="#00BFFF").pack(pady=10)

        control_frame = tk.Frame(self, bg="#030303")
        control_frame.pack(pady=10)

        btn_cfg = {
            "width": 24,
            "font": ("Helvetica", 10, "bold"),
            "relief": "raised",
            "padx": 5,
            "pady": 4
        }

        tk.Button(control_frame, text="⚡ Start Evolution Scan",
                  command=self.start_evolution_scan, bg="#242424", fg="#00BFFF", **btn_cfg).grid(row=0, column=0, padx=5)

        tk.Button(control_frame, text="🛑 Stop",
                  command=self.stop_evolution_scan, bg="#242424", fg="#FF5F5F", **btn_cfg).grid(row=0, column=1, padx=5)

        tk.Button(control_frame, text="📈 Plot Evolution",
                  command=self.plot_current, bg="#242424", fg="#00FF88", **btn_cfg).grid(row=0, column=2, padx=5)

        tk.Button(control_frame, text="🔒 Quit Window",
                  command=self.safe_quit, bg="#242424", fg="#FFCC00", **btn_cfg).grid(row=0, column=3, padx=5)

        self.output_box = tk.Text(self, height=15, width=100, bg="#1A1A1A", fg="lime")
        self.output_box.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.safe_quit)
        glyph_log("adaptive", "Evolution Window Initialized.", glyph="♻")
        print(get_footer())

    def start_evolution_scan(self):
        if not self.running:
            self.running = True
            self.run_evolution_analysis()
            glyph_log("signal", "Evolution monitoring started.", glyph="Ψ")

    def stop_evolution_scan(self):
        self.running = False
        if self.after_id:
            try:
                self.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None
        glyph_log("trust_loss", "Evolution monitoring stopped by user.", glyph="⸸")

    def run_evolution_analysis(self):
        if not self.running or not self.winfo_exists():
            return

        try:
            entity_id = f"entity_{random.randint(1, 10)}"
            action_type = f"action_{random.randint(1, 5)}"
            self.behavior_monitor.record_action(entity_id, action_type)

            entropy = self.behavior_monitor.compute_behavioral_entropy(entity_id)
            threat = self.intrusion_detector.score_threat_level()
            self.entity_threat_index[entity_id] = threat

            glyph = (
                "☣" if entropy > 1.0 else
                "⸸" if entropy > 0.6 else
                "♇" if entropy > 0.3 else
                "Δ"
            )

            self.entropy_values.append(entropy)
            self.threat_values.append(threat)
            self.entropic_glyphs.append(glyph)

            if len(self.entropy_values) >= 3:
                recent_avg = sum(self.entropy_values[-3:]) / 3
                if entropy > 1.5 * recent_avg:
                    self.entropy_spike_markers.append(len(self.entropy_values) - 1)

            self.output_box.insert(
                tk.END,
                f"[{glyph}] {entity_id} → Δ: {entropy:.4f} | ☣: {threat:.4f}\n"
            )
            self.output_box.see(tk.END)
        except Exception as e:
            glyph_log("anomaly", f"Evolution loop error: {e}", glyph="☣")

        if self.running and self.winfo_exists():
            self.after_id = self.after(1000, self.run_evolution_analysis)

    def plot_current(self):
        if not self.entropy_values or not self.threat_values:
            glyph_log("anomaly", "Plot aborted. No data collected yet.", glyph="☣")
            return

        def _plot_thread():
            output_path = os.path.join(self.log_dir, "evolution_entropy_threat_plot.png")
            self.graph_tools.plot_entropy_threat(
                self.entropy_values,
                self.threat_values,
                entity_scores=self.entity_threat_index,
                entropy_spikes=self.entropy_spike_markers,
                glyphs=self.entropic_glyphs,
                output_file=output_path
            )
            glyph_log("bayesian", f"Evolution graph saved to {output_path}", glyph="⧊")

        threading.Thread(target=_plot_thread, daemon=True).start()

    def safe_quit(self):
        self.stop_evolution_scan()
        try:
            if self.winfo_exists():
                self.destroy()
                glyph_log("trust_loss", "Evolution Monitor window closed safely.", glyph="⸸")
        except Exception as e:
            glyph_log("anomaly", f"Safe quit error: {e}", glyph="☣")