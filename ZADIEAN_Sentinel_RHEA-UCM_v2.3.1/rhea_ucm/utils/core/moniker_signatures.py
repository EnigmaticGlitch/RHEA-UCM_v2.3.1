# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/core/moniker_signatures.py                      ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Symbolic Moniker Core · Glyph Logging Engine             ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import logging
import os
from datetime import datetime

# ════════════════════════════════════════════════════════════════════════
# GLYPHSET — Symbol Definitions for Entropy, Trust, and Recursive States
# ════════════════════════════════════════════════════════════════════════

GLYPHSET = {
    "entropy": "Δ",
    "trust_gain": "⚖",
    "trust_loss": "⸸",
    "anomaly": "☣",
    "signal": "Ψ",
    "emergent": "🧠",
    "phase_lock": "♇",
    "regulation": "⟳",
    "adaptive": "♻",
    "recursive": "⌬",
    "bayesian": "⧊",
    "pluto_lock": "♇🜨",
    "fatal": "💥",
    "termination": "☯"
}

# ════════════════════════════════════════════════════════════════════════
# GLOBAL LOGGER INITIALIZATION
# ════════════════════════════════════════════════════════════════════════

LOG_PATH = "logs/interpreter.log"
os.makedirs("logs", exist_ok=True)

global_logger = logging.getLogger("interpreter")
global_logger.setLevel(logging.INFO)

if not global_logger.handlers:
    fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
    formatter = logging.Formatter("[%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    global_logger.addHandler(fh)

# ════════════════════════════════════════════════════════════════════════
# LOGGING WRAPPER — Glyph-Based Logger
# ════════════════════════════════════════════════════════════════════════

def glyph_log(event_type: str, message: str, glyph: str = None, phase: str = ""):
    """Log with symbolic prefix and glyph to console and file"""
    symbol = GLYPHSET.get(event_type, glyph or "?")
    timestamp = datetime.now().strftime("%H:%M:%S")
    full_message = f"{timestamp} :: [{symbol}] ({event_type.upper()}) {message} {phase}".strip()

    # Terminal echo
    print(full_message)

    # File log echo
    try:
        global_logger.info(f"[{symbol}] ({event_type.upper()}) {message}")
    except Exception:
        pass

# ════════════════════════════════════════════════════════════════════════
# SIGNATURE BLOCK — Footer Moniker
# ════════════════════════════════════════════════════════════════════════

def get_footer():
    return (
        "\n"
        "█████████® 2025 PAUL M. ROE / ENIGMATICGLITCH ███████████████████████████\n"
        "█ LICENSED TIER: ZADEIAN-SOVEREIGN | PAT. PEND. #63/796,404               █\n"
        "█ SYMBOLIC INTERFACE ACTIVE | SFI · RUM · PMR · UWC · ADO               █\n"
        "█ ♇🧙‍♂️♏ Trust is not given. It is oscillated into being.               █\n"
        "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
    )

# ════════════════════════════════════════════════════════════════════════
# SELF-TEST
# ════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    glyph_log("entropy", "Entropy spike detected at runtime", glyph="Δ")
    glyph_log("phase_lock", "Phase-lock initialized successfully", glyph="♇")
    print(get_footer())