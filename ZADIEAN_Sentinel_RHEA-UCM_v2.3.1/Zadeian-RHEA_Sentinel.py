# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel Sovereign Console — Launcher                     ║
# ║ ⌬ File: Zadeian-RHEA_Sentinel.py                                         ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Entry Point for PMR-Based Adaptive Security Framework     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import sys
import os
import platform
from gui.main_window import MainWindow
from rhea_ucm.sentinel_manager import SentinelManager
from rhea_ucm.utils.logging_setup import initialize_global_logging
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

def check_python_version():
    if sys.version_info < (3, 8):
        sys.exit("⛔ Python 3.8+ is required to run ZADEIAN-RHEA Sentinel.")

def check_working_dir():
    if not os.path.exists("rhea_ucm"):
        sys.exit("⛔ Error: Run this script from the project root containing 'rhea_ucm/'.")

if __name__ == "__main__":
    check_python_version()
    check_working_dir()

    glyph_log("phase_lock", f"🛡️ Launching ZADEIAN-RHEA Sentinel v2.3.1 on {platform.system()}", glyph="♇")
    initialize_global_logging()

    sentinel_manager = SentinelManager()
    sentinel_manager.start_system()

    app = MainWindow(sentinel_manager)
    app.mainloop()

    glyph_log("termination", "🧠 Sentinel GUI shutdown complete.", glyph="☯")
    print(get_footer())