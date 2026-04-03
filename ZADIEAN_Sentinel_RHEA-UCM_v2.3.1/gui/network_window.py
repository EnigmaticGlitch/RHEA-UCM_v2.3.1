# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /gui/network_window.py                                          ║
# ║ ⌬ Description: Real-Time Network Monitor · Entropy Summary Pipeline     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk, messagebox
import threading

from rhea_ucm.utils.network_scan import NetworkAnalyzer
from rhea_ucm.utils.graphing import GraphingTools
from rhea_ucm.utils.logging_setup import get_log_dir
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

class NetworkWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ZADEIAN Sentinel - Network Monitor [Ψ→Δ→Net→Reg]")
        self.geometry("1000x650")
        self.configure(bg="#030303")
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.packet_data = []
        self.max_packets_display = 50
        self.scan_active = threading.Event()
        self.after_id = None

        self.log_dir = get_log_dir(base="logs/network", session_prefix="NetScan")
        self.graph_tools = GraphingTools(log_dir=self.log_dir)
        self.analyzer = NetworkAnalyzer(self._enqueue_packet, self.log_dir)

        # ══════════[ Background Glyph Watermark Canvas ]══════════
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

        # GUI Header
        ttk.Label(self, text="Network Activity Monitor [Packet Summaries]",
                  font=("Helvetica", 18), background="#030303", foreground="#00BFFF").pack(pady=10)

        self.packet_listbox = tk.Listbox(self, width=120, height=20,
                                         bg="#1A1A1A", fg="lime")
        self.packet_listbox.pack(pady=10)

        button_frame = tk.Frame(self, bg="#030303")
        button_frame.pack(pady=10)

        btn_cfg = {
            "width": 24,
            "font": ("Helvetica", 10, "bold"),
            "relief": "raised",
            "padx": 5,
            "pady": 4
        }

        self.start_button = tk.Button(button_frame, text="⚡ Start Scan",
                                      command=self._start_scan, bg="#242424", fg="#00BFFF", **btn_cfg)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="🛑 Stop Scan",
                                     command=self._stop_scan, bg="#242424", fg="#FF5F5F", **btn_cfg)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.plot_button = tk.Button(button_frame, text="📈 Plot Network Activity",
                                     command=self._schedule_plot, bg="#242424", fg="#00FF88", **btn_cfg)
        self.plot_button.grid(row=0, column=2, padx=5)

        self.quit_button = tk.Button(button_frame, text="🔒 Quit",
                                     command=self._on_close, bg="#242424", fg="#FFCC00", **btn_cfg)
        self.quit_button.grid(row=0, column=3, padx=5)

        glyph_log("adaptive", "NetworkWindow initialized.", glyph="♻")
        print(get_footer())

    def _start_scan(self):
        if self.scan_active.is_set():
            messagebox.showinfo("Scan Already Running", "Please stop the current scan before starting a new one.")
            return
        try:
            self.packet_data.clear()
            self.scan_active.set()
            self.analyzer.start_scan()
            self._poll_packets()
            glyph_log("signal", "Network scan started (live feed enabled).", glyph="Ψ")
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))
            glyph_log("fatal", f"Start scan failure: {e}", glyph="💥")

    def _stop_scan(self):
        if not self.scan_active.is_set():
            return
        try:
            self.scan_active.clear()
            self.analyzer.stop_scan()
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
            glyph_log("trust_loss", "Network scan halted by user.", glyph="⸸")
        except Exception as e:
            glyph_log("anomaly", f"Stop scan failure: {e}", glyph="☣")

    def _on_close(self):
        self._stop_scan()
        self.destroy()
        glyph_log("signal", "Network window closed cleanly.", glyph="✖")

    def _enqueue_packet(self, packet_summary):
        try:
            display_text = (
                f"[Src: {packet_summary.get('src', '?')}] → [Dst: {packet_summary.get('dst', '?')}] "
                f"| VPN: {'Yes' if packet_summary.get('vpn') else 'No'} "
                f"| Match: {'⚠' if packet_summary.get('match') else '✔'} "
                f"| {packet_summary.get('proto', 'N/A')}"
            )
            self.packet_data.append(display_text)
            if len(self.packet_data) > self.max_packets_display:
                self.packet_data.pop(0)
        except Exception as e:
            glyph_log("anomaly", f"Failed to enqueue packet: {e}", glyph="☣")

    def _poll_packets(self):
        try:
            self.analyzer.process_pending_packets()
            self._update_display()
        except Exception as e:
            glyph_log("anomaly", f"Polling error: {e}", glyph="☣")

        if self.scan_active.is_set():
            self.after_id = self.after(500, self._poll_packets)

    def _update_display(self):
        self.packet_listbox.delete(0, tk.END)
        for summary in self.packet_data:
            self.packet_listbox.insert(tk.END, summary)

    def _schedule_plot(self):
        if not self.packet_data or len(self.packet_data) < 2:
            glyph_log("anomaly", "Plot aborted: insufficient Ψ packet data.", glyph="☣")
            return
        self.after(100, self._run_plot)

    def _run_plot(self):
        try:
            self.graph_tools.plot_network_activity(packet_data=self.packet_data)
            glyph_log("bayesian", "Network activity chart generated.", glyph="⧊")
        except Exception as e:
            with open("crash_report.txt", "w") as f:
                f.write(f"Network plot crash: {str(e)}\n")
            glyph_log("fatal", f"Plot failed: {str(e)}", glyph="💥")
