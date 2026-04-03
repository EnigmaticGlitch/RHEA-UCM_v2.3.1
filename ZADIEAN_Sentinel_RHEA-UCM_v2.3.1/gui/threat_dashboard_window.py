# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1                                          ║
# ║ ⌬ File: /gui/threat_dashboard_window.py                                 ║
# ║ ⌬ Description: Live Threat Monitoring Dashboard with Recursive Overlay  ║
# ║ ⌬ Glyphset: ♇🧠⧊Δ⇌ · Patent: US 63/796,404                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

class ThreatDashboardWindow(tk.Toplevel):
    def __init__(self, parent, sentinel_manager):
        super().__init__(parent)
        self.title("🧠 ZADEIAN Threat Dashboard · PMR Overlay")
        self.geometry("960x720")
        self.configure(bg="#000000")
        self.sentinel = sentinel_manager
        self.running = True
        self.after_id = None

        
        # ══════════[ Background Glyph Watermark Canvas ]══════════
        self.bg_canvas = tk.Canvas(self, width=2440, height=1980, bg="#000000", highlightthickness=0)
        self.bg_canvas.place(x=-150, y=0, relwidth=1, relheight=1)

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
            980, 690,
            text=ascii_stamp,
            fill="#2e5411",
            font=("Courier New", 9),
            anchor="se",
            justify="right",
            tags="watermark"
        )
        self.bg_canvas.tag_lower("watermark")

        # ════════════════[ Entity Table View ]════════════════
        self.entity_label = ttk.Label(self, text="⇌ Entity Threat Index Monitor ⇌", font=("Segoe UI", 12, "bold"))
        self.entity_label.pack(pady=5)

        self.entity_table = ttk.Treeview(self, columns=("Entity ID", "Threat Score"), show="headings", height=12)
        self.entity_table.heading("Entity ID", text="Entity ID")
        self.entity_table.heading("Threat Score", text="⚠️ Threat Score")
        self.entity_table.pack(pady=5, fill="x")

        # ════════════════[ Live Graph View ]══════════════════
        self.figure, self.ax = plt.subplots(figsize=(8.5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(pady=5)

        # ════════════════[ Controls ]═════════════════════════
        self.refresh_button = ttk.Button(self, text="⟳ Manual Refresh", command=self.refresh_dashboard)
        self.refresh_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.safe_close)
        self.refresh_dashboard()
        self.auto_refresh()
        glyph_log("adaptive", "Threat Dashboard Window initialized", glyph="♇")
        print(get_footer())

    def refresh_dashboard(self):
        if not self.winfo_exists():
            return
        try:
            self.refresh_table()
            self.refresh_graph()
        except Exception as e:
            glyph_log("anomaly", f"Dashboard refresh error: {e}", glyph="☣")

    def refresh_table(self):
        try:
            for item in self.entity_table.get_children():
                self.entity_table.delete(item)
            for entity_id, threat_score in self.sentinel.active_entities.items():
                self.entity_table.insert("", tk.END, values=(entity_id, f"{threat_score:.4f}"))
        except Exception as e:
            glyph_log("anomaly", f"Table refresh error: {e}", glyph="☣")

    def refresh_graph(self):
        try:
            self.ax.clear()
            entity_ids = list(self.sentinel.active_entities.keys())
            threat_scores = list(self.sentinel.active_entities.values())
            self.ax.bar(entity_ids, threat_scores, color="#00BCD4")
            self.ax.set_title("🧬 Emergent Threat Scores")
            self.ax.set_xlabel("Entity ID")
            self.ax.set_ylabel("Trust Entropy Score (Δ⇌)")
            self.ax.set_ylim(0, 1.0)
            self.ax.tick_params(axis='x', rotation=30)
            self.ax.grid(True, linestyle="--", alpha=0.3)
            self.canvas.draw()
        except Exception as e:
            glyph_log("anomaly", f"Graph refresh error: {e}", glyph="☣")

    def auto_refresh(self):
        if not self.running or not self.winfo_exists():
            return
        try:
            from random import uniform
            for entity in self.sentinel.active_entities.keys():
                simulated = uniform(0.0, 1.0)
                self.sentinel.active_entities[entity] = simulated
                glyph_log("adaptive", f"⇌ Auto-Update {entity} → {simulated:.4f}", glyph="Δ")
            self.refresh_dashboard()
        except Exception as e:
            glyph_log("fatal", f"Auto-refresh error: {e}", glyph="💥")
        finally:
            self.after_id = self.after(6000, self.auto_refresh)

    def safe_close(self):
        self.running = False
        if self.after_id:
            try:
                self.after_cancel(self.after_id)
            except Exception:
                pass
        self.destroy()
        glyph_log("termination", "Threat Dashboard closed", glyph="⧊")