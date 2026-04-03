# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1                                          ║
# ║ ⌬ File: /gui/security_center_window.py                                  ║
# ║ ⌬ Description: GUI Trust Center & Symbolic Signature Quarantine Engine  ║
# ║ ⌬ Glyphset: ⚖Ψ⧊⸸♻ · Patent: US 63/796,404                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from rhea_ucm.utils.core.moniker_signatures import glyph_log

class SecurityCenterWindow(tk.Toplevel):
    def __init__(self, parent, sentinel_manager):
        super().__init__(parent)
        self.title("⚖ ZADEIAN Security Trust Center · Signature Control")
        self.geometry("820x640")
        self.configure(bg="#030303")
        self.sentinel = sentinel_manager

        # ══════════[ Background Glyph Canvas Watermark ]══════════
        self.bg_canvas = tk.Canvas(self, width=820, height=640, bg="#030303", highlightthickness=0)
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
            810, 10,
            text=ascii_stamp,
            fill="#2e5411",
            font=("Courier New", 8),
            anchor="ne",
            justify="right",
            tags="watermark"
        )
        self.bg_canvas.tag_lower("watermark")

        # ════════════════[ UI Controls ]════════════════
        ttk.Label(self, text="Selected File:", background="#030303", foreground="#00BFFF").pack(pady=(10, 3))
        self.file_entry = ttk.Entry(self, width=80)
        self.file_entry.pack(pady=3)

        btn_cfg = {
            "width": 22,
            "font": ("Helvetica", 10, "bold"),
            "relief": "raised",
            "bg": "#242424",
            "padx": 5,
            "pady": 4
        }

        tk.Button(self, text="📁 Browse File", command=self.browse_file,
                  fg="#00BFFF", **btn_cfg).pack(pady=2)
        tk.Button(self, text="🔍 Check Signature", command=self.check_signature,
                  fg="#00FF88", **btn_cfg).pack(pady=2)
        tk.Button(self, text="⚖ Trust File", command=self.trust_file,
                  fg="#33FF33", **btn_cfg).pack(pady=2)
        tk.Button(self, text="⸸ Quarantine File", command=self.quarantine_file,
                  fg="#FF5F5F", **btn_cfg).pack(pady=2)
        tk.Button(self, text="♻ Refresh Lists", command=self.refresh_tables,
                  fg="#FFCC00", **btn_cfg).pack(pady=8)

        # ════════════════[ Trusted Tree ]═══════════════
        ttk.Label(self, text="🧬 Trusted Signatures:", background="#030303", foreground="#33FF33").pack(pady=(5, 1))
        self.trusted_tree = tk.Listbox(self, height=6, bg="#d9d9d9", fg="#000000", font=("Courier New", 9))
        self.trusted_tree.pack(pady=1, fill="x", padx=20)

        # ════════════════[ Blacklist Tree ]═════════════
        ttk.Label(self, text="☣ Blacklisted Signatures:", background="#030303", foreground="#FF4444").pack(pady=(10, 1))
        self.blacklist_tree = tk.Listbox(self, height=6, bg="#d9d9d9", fg="#000000", font=("Courier New", 9))
        self.blacklist_tree.pack(pady=1, fill="x", padx=20)

        self.refresh_tables()
        glyph_log("trust_gain", "🧠 Security Center Initialized", glyph="⚖")

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            glyph_log("signal", f"File selected: {file_path}", glyph="Ψ")

    def check_signature(self):
        file_path = self.file_entry.get()
        if not os.path.isfile(file_path):
            messagebox.showerror("Error", "Invalid file selected.")
            glyph_log("anomaly", f"Invalid path attempted: {file_path}", glyph="☣")
            return
        result = self.sentinel.check_file_signature(file_path)
        msg = (
            f"Trusted: {len(result['trusted'])}\n"
            f"Blacklisted: {len(result['blacklisted'])}\n"
            f"Status: {result['status']}"
        )
        messagebox.showinfo("Scan Result", msg)
        glyph_log("bayesian", f"Scan ⧊ → {msg.replace(chr(10), ' | ')}", glyph="⧊")

    def trust_file(self):
        file_path = self.file_entry.get()
        if os.path.isfile(file_path):
            self.sentinel.update_signature_trust(file_path, good=True)
            self.refresh_tables()
            glyph_log("trust_gain", f"🧠 Trusted file: {file_path}", glyph="⚖")

    def quarantine_file(self):
        file_path = self.file_entry.get()
        if os.path.isfile(file_path):
            self.sentinel.update_signature_trust(file_path, good=False)
            self.refresh_tables()
            glyph_log("trust_loss", f"☣ Quarantined file: {file_path}", glyph="⸸")

    def refresh_tables(self):
        self.trusted_tree.delete(0, tk.END)
        self.blacklist_tree.delete(0, tk.END)

        for h in self.sentinel.signature_checker.trusted:
            self.trusted_tree.insert(tk.END, h)
        for h in self.sentinel.signature_checker.blacklist:
            self.blacklist_tree.insert(tk.END, h)

        glyph_log("adaptive", "♻ Signature tables refreshed", glyph="♻")