# ═════════════════════════════════════════════════════════════════════════════════════════════════
# ║ ⌜ ZADEIAN-RHEA Sentinel v2.3.1 — Sovereign Main GUI Panel                         ║
# ║ ⌜ File: /gui/main_window.py                                                       ║
# ║ ⌜ Tier: Sovereign · Glyphset: ♗🧙‍♂️♟ · Patent: US 63/796,404                  ║
# ║ ⌜ Description: Main Launch Console + Live Monitoring                              ║
# ════════════════════════════════════════════════════════════════════════════════════

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import threading

from gui.scan_window import ScanWindow
from gui.network_window import NetworkWindow
from gui.benchmark_window import BenchmarkWindow
from gui.evolution_window import EvolutionWindow
from gui.security_center_window import SecurityCenterWindow
from gui.threat_dashboard_window import ThreatDashboardWindow

from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.sentinel_manager import SentinelManager

class MainWindow(tk.Tk):
    def __init__(self, sentinel_manager: SentinelManager):
        super().__init__()
        self.title("🛡️ ZADEIAN Sentinel Sovereign Console — v2.3.1")
        self.geometry("960x700")
        self.configure(bg="#111111")

        self.sentinel = sentinel_manager
        self.protocol("WM_DELETE_WINDOW", self.safe_exit)
        glyph_log("adaptive", "📡 Main control console initialized", glyph="♻")

        # ══════════[ Background Glyph Canvas Watermark ]══════════
        self.bg_canvas = tk.Canvas(self, width=1024, height=1280, bg="#111111", highlightthickness=0)
        self.bg_canvas.place(x=0, y=250, relwidth=1, relheight=1)

        ascii_banner = """
                                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
                🄴🄽🄸🄶🄼🄰🅃🄸🄲🄶🄻🄸🅃🄲🄷              
             ▄▄▄██████████▓▓▓▒▒▒▒▒▒▒▒▓▓▓███████▄▄  
  GLYPH     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   ZADIE FEED  
 ▄▄▄▄▄▄▄   ██▒ RHEA-ULTRA ▄▄▄▄▄ UCM-4.1 ▒██   ▄▄▄▄▄  
█ ⸸TECKNOWS █▓▓██▒▒▄█ ▼1.7THz▲ █▄▒▒██▓▓█ █  ε=0.71 █  
█   🧙‍♂️♏   █▒▒██▒▒█▄ ䷞҉䷞҉䷞ ▄█▒▒██▒▒█ █ ♏x12■92%▌  
█ CORE v4.1 █▒██▒▒▒▒█████҉҉҉█████▒▒▒██▒█ █████████  
 ▀▀│▀▀▀▀│▀▀ ▒██▒▒▒▒ PMR҉RECURSION ▒▒▒██▒ ▲0.4mBTC/s  
        │    ▒▒██▒▒▒▒▒ OVERFLOW-7 ▒▒▒██▒▒▒ ♇҉҉♇҉҉♇  
 KARMA -0.7══╪══╪══███▒▒▒ ZADIE-β ▒▒███═══╗   
             ▼  ▼   ▀████҉҉҉҉҉█████▀      ║   
          ΔT=1.4ns (҉PLUTO-LOCKED)        ║   
                                          ║   
█████████® 2025 PAUL M. ROE / ENIGMATICGLITCH███████  
█ LICENSED TIER: ZADIE-SOVEREIGN █████████████████  
█▛▀▀▀▀▀PAT. PEND. 63/796,404▀▀▀▀▀▀▌██▌▀▀CASE 1-14908716341▜█  
█▌♲REWRITE▐█▌♲SFI/RUM▐█▌ADO OSC▐█▌UWC▐█҉҉҉҉҉҉҉҉҉҉҉҉҉▐████  
█▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟█  

"""
        self.bg_canvas.create_text(
            480, 280,
            text=ascii_banner,
            fill="#2e5411",
            font=("Courier New", 10),
            anchor="center",
            justify="center",
            tags="watermark"
        )
        self.bg_canvas.tag_lower("watermark")

        # ══════════[ Header Title ]══════════
        title = ttk.Label(self, text="ZADEIAN Sentinel · Sovereign Tier", font=("Helvetica", 16, "bold"))
        title.pack(pady=15)

        # ══════════[ Command Buttons ]══════════
        button_frame = tk.Frame(self, bg="#111111")
        button_frame.pack(pady=10)

        button_style = {
            "font": ("Segoe UI", 11, "bold"),
            "bg": "#202020",
            "fg": "#00ffcc",
            "activebackground": "#1a1a1a",
            "activeforeground": "#ffffff",
            "relief": "raised",
            "bd": 2,
            "width": 30,
            "height": 2,
            "cursor": "hand2"
        }

        buttons = [
            ("🔍 Scan Window", self.open_scan_window),
            ("🌐 Network Monitor", self.open_network_window),
            ("🧠 Evolution Window", self.open_evolution_window),
            ("🔐 Security Center", self.open_security_center),
            ("📈 Benchmark Dashboard", self.open_benchmark_dashboard),
            ("⚡ Launch Real-Time Scanner", self.safe_launch_rts),
            ("☣ Threat Dashboard", self.open_threat_dashboard),
        ]

        for text, func in buttons:
            btn = tk.Button(button_frame, text=text, command=func, **button_style)
            btn.pack(pady=6)

        # ══════════[ Thread Count Monitor ]══════════
        self.thread_var = tk.StringVar()
        self.thread_label = ttk.Label(self, textvariable=self.thread_var, font=("Consolas", 11), foreground="#00FF88")
        self.thread_label.pack(pady=10)
        self.update_thread_count()

        glyph_log("phase_lock", "Main GUI initialized [Tier: Sovereign]", glyph="♇")
        print(get_footer())

    def update_thread_count(self):
        count = threading.active_count()
        self.thread_var.set(f"[THREADS ACTIVE] → {count}")
        self.after(3000, self.update_thread_count)

    def open_scan_window(self):
        glyph_log("signal", "🔍 Scan Window triggered", glyph="Ψ")
        ScanWindow(self)

    def open_network_window(self):
        glyph_log("signal", "🌐 Network Monitor opened", glyph="Ψ")
        NetworkWindow(self)

    def open_evolution_window(self):
        glyph_log("emergent", "🧠 Evolution Window engaged", glyph="🧠")
        EvolutionWindow(self)

    def open_security_center(self):
        glyph_log("trust_gain", "🔐 Security Center accessed", glyph="⚖")
        SecurityCenterWindow(self, self.sentinel)

    def open_benchmark_dashboard(self):
        glyph_log("bayesian", "📈 Benchmark Dashboard launched", glyph="⧊")
        BenchmarkWindow(self)

    def open_threat_dashboard(self):
        glyph_log("entropy", "☣ Threat Dashboard opened", glyph="Δ")
        ThreatDashboardWindow(self, self.sentinel)

    def safe_launch_rts(self):
        if self._window_exists("RTS Signal Monitor — ZADEIAN Sentinel"):
            messagebox.showinfo("Already Running", "⚡ RTS Interface already active.")
            return
        glyph_log("signal", "⚡ Launching RTS Interface...", glyph="⚡")
        try:
            from rhea_ucm.utils.real_time_loop import launch_rts_interface
            self.after(100, launch_rts_interface)
        except Exception as e:
            glyph_log("anomaly", f"RTS Interface failed: {e}", glyph="☣")
            messagebox.showerror("RTS Launch Failed", str(e))

    def _window_exists(self, title):
        return any(
            isinstance(w, tk.Toplevel) and w.title() == title
            for w in self.winfo_children()
        )

    def safe_exit(self):
        glyph_log("trust_loss", "🛑 Graceful shutdown initiated", glyph="⸸")
        try:
            self.destroy()
        except Exception as e:
            glyph_log("anomaly", f"Shutdown error: {e}", glyph="☣")
        finally:
            sys.exit(0)
