# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                      ║
# ║ ⌬ File: C:/Users/south/Documents/Theories/ZADEIAN_Sentinel_RHEA-UCM_v2.2║
# ║ ⌬        /rhea_ucm/utils/self_reflection.py                              ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404             ║
# ║ ⌬ Description: Symbolic Self-Reflection & System Diagnostics             ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import threading
import time
import logging

from rhea_ucm.utils.adaptive_behavior_engine import AdaptiveBehaviorEngine
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

logging.basicConfig(
    filename="logs/self_reflection.log",
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

class SelfReflection:
    def __init__(self, engine: AdaptiveBehaviorEngine, audit_interval: int = 300):
        self.engine = engine
        self.audit_interval = audit_interval
        self.running = False
        self.thread = threading.Thread(target=self._reflect, daemon=True)

    def start(self):
        self.running = True
        self.thread.start()
        glyph_log("phase_lock", "Self-Reflection Module Activated", "♇")

    def stop(self):
        self.running = False
        glyph_log("trust_loss", "Self-Reflection Module Halted", "⸸")

    def _reflect(self):
        while self.running:
            time.sleep(self.audit_interval)

            last_entropy = self.engine.entropy_log[-5:] if self.engine.entropy_log else []
            emergence = self.engine.emergent()
            high_threats = sum(1 for e in self.engine.entropy_log if e > 0.75)
            rate = self.engine.learning_rate

            glyph_log("entropy", f"Last 5 Δ Entropy: {last_entropy}", "Δ")
            glyph_log("emergent", f"Emergence Score: {emergence:.4f}", "🧠")
            glyph_log("anomaly", f"⚠ High Entropy Entities: {high_threats}", "☣")
            glyph_log("adaptive", f"Learning Rate: {rate:.4f}", "♻")

            glyph_log("phase_lock", "Audit Cycle Complete — Awaiting next phase...", "♇")
            logging.info(get_footer())

# Optional test
if __name__ == "__main__":
    engine = AdaptiveBehaviorEngine()
    engine.delta(0.61)
    engine.delta(0.79)
    engine.delta(0.45)
    engine.adaptive_learning(0.66)

    reflection = SelfReflection(engine, audit_interval=5)
    reflection.start()
    time.sleep(10)
    reflection.stop()