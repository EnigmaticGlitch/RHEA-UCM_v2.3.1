# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ®  2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: C:/Users/south/Documents/Theories/ZADEIAN_Sentinel_RHEA-UCM_v2.3║
# ║ ⌬   /rhea_ucm/utils/logging_setup.py                                    ║
# ║ ⌬ Description: Logging                                                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import os
import logging
from datetime import datetime


def get_log_dir(base="logs", session_prefix="RTS"):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = os.path.join(base, f"{session_prefix}_{now}")
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def setup_logger(name, log_dir, logfile=None):
    if not logfile:
        logfile = name
    full_path = os.path.join(log_dir, f"{logfile}.log")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(full_path, encoding="utf-8")
        fh.setFormatter(logging.Formatter("[%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
        logger.addHandler(fh)
    return logger


def initialize_global_logging():
    """
    Initializes global logging to a timestamped interpreter log.
    Used when running Zadeian-RHEA_Sentinel.py directly.
    """
    base_log_dir = "logs"
    os.makedirs(base_log_dir, exist_ok=True)
    log_file = os.path.join(base_log_dir, f"interpreter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s [%(levelname)s] %(message)s",
        level=logging.INFO
    )
    logging.info("🌐 Global logging initialized by initialize_global_logging().")