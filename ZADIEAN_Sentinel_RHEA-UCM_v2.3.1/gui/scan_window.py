# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1                                          ║
# ║ ⌬ File: /gui/scan_window.py                                             ║
# ║ ⌬ Tier: Sovereign · Glyphset: ΨΔ⚖⧊⸸🧠♻                               ║
# ║ ⌬ Description: Visual File Scanner GUI · Anomaly Trust Overlay Engine   ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import queue
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

from rhea_ucm.interpreter import RHEAInterpreter
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

class ScanWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("🔍 ZADEIAN Sentinel · Scan Chamber [Ψ→Δ→⚖]")
        self.geometry("1000x720")
        self.configure(bg="#030303")
        self.protocol("WM_DELETE_WINDOW", self.safe_quit)

        # ══════════[ Background Glyph Watermark Canvas ]══════════
        self.bg_canvas = tk.Canvas(self, width=1000, height=720, bg="#030303", highlightthickness=0)
        self.bg_canvas.place(x=-275, y=375, relwidth=1, relheight=1)

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

        self.rhea = RHEAInterpreter()
        self.queue = queue.Queue()
        self.scan_thread = None
        self.scanning = threading.Event()

        ttk.Label(self, text="📂 File Scanner (Entropy-Regulation Overlay)", font=("Helvetica", 17)).pack(pady=15)
        ttk.Button(self, text="🧭 Select Folder", command=self.choose_folder).pack(pady=10)

        self.textbox = tk.Text(self, height=16, width=110, bg="#1A1A1A", fg="white")
        self.textbox.pack(pady=10)

        self.fig, self.ax = plt.subplots(figsize=(8, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(pady=10)

        self.results = []
        self.after(100, self.poll_queue)
        glyph_log("adaptive", "ScanWindow [Ψ→Δ→Reg→🧠] initialized", glyph="♻")
        print(get_footer())

    def choose_folder(self):
        if self.scanning.is_set():
            messagebox.showinfo("Scan In Progress", "🌀 Please wait for current scan to finish.")
            return
        folder_path = filedialog.askdirectory()
        if not folder_path:
            messagebox.showwarning("⚠ No Folder", "You must select a valid folder to begin scan.")
            glyph_log("trust_loss", "Scan aborted — no folder chosen.", glyph="⸸")
            return
        glyph_log("signal", f"Target directory selected: {folder_path}", glyph="Ψ")
        self.start_scan_thread(folder_path)

    def start_scan_thread(self, folder_path):
        self.results.clear()
        self.textbox.delete("1.0", tk.END)
        self.scanning.set()
        self.scan_thread = threading.Thread(target=self.scan_folder, args=(folder_path,), daemon=True)
        self.scan_thread.start()

    def scan_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if not self.scanning.is_set():
                break
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                        hashes = self.rhea.compute_hashes(content)
                        psi_val = self.rhea.psi()
                        delta_val = self.rhea.bayes(len(content) % 100 / 100)
                        reg_val = self.rhea.reg(delta_val)
                        emergent_val = self.rhea.emergent_behavior()

                        self.results.append((filename, reg_val))

                        log_msg = (
                            f"📄 {filename} | Ψ={psi_val:.4f} | Δ→⚖={reg_val:.4f} | 🧠={emergent_val:.4f}"
                        )
                        self.queue.put(("log", log_msg))
                        glyph_log("entropy", log_msg, glyph="Δ")

                except Exception as e:
                    err_msg = f"☣ Error scanning {filename}: {e}"
                    self.queue.put(("log", err_msg))
                    glyph_log("anomaly", err_msg, glyph="☣")

        self.queue.put(("done", None))

    def poll_queue(self):
        try:
            while True:
                kind, data = self.queue.get_nowait()
                if kind == "log":
                    self.textbox.insert(tk.END, data + "\n")
                    self.textbox.see(tk.END)
                elif kind == "done":
                    self.plot_results()
                    self.scanning.clear()
        except queue.Empty:
            pass
        self.after(100, self.poll_queue)

    def plot_results(self):
        self.ax.clear()
        if not self.results:
            self.ax.set_title("⚠ No Files Processed")
            self.canvas.draw()
            return

        files = [r[0] for r in self.results]
        scores = [r[1] for r in self.results]

        self.ax.barh(files, scores, color="cyan")
        self.ax.set_title("📊 File Anomaly Scores [Ψ→Δ→⚖]")
        self.ax.set_xlabel("Entropy-Regulated Score")
        self.ax.set_xlim(0, 1.1)
        self.ax.grid(True)
        self.fig.tight_layout()
        self.canvas.draw()
        glyph_log("bayesian", "📈 Scan results plotted", glyph="⧊")

        try:
            os.makedirs("logs/graphs", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"logs/graphs/Scan_Overlay_{timestamp}.png"
            self.fig.savefig(filename, dpi=300, bbox_inches="tight")
            glyph_log("recursive", f"📁 Plot saved to {filename}", glyph="🧠")
        except Exception as e:
            glyph_log("anomaly", f"Failed to save scan graph: {e}", glyph="☣")

    def safe_quit(self):
        self.scanning.clear()
        if self.scan_thread and self.scan_thread.is_alive():
            self.scan_thread.join(timeout=1.5)
        self.destroy()
        glyph_log("trust_loss", "🛑 ScanWindow closed", glyph="⸸")