# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/adaptive_behavior_engine.py                     ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Full Recursive Adaptive Behavioral Model Engine           ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import math
import random
import hashlib
import logging
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.utils.logging_setup import setup_logger

class AdaptiveBehaviorEngine:
    def __init__(self, log_dir="logs"):
        self.logger = setup_logger("adaptive_behavior_engine", log_dir)
        self.memory_log = []
        self.entropy_log = []
        self.learning_rate = 0.05
        self.target_mean = 0.8
        self.hash_memory = {"md5": set(), "sha1": set(), "sha256": set()}

        glyph_log("phase_lock", "Adaptive Engine Initialized", glyph="♇")
        self.logger.info(get_footer())

    def bayes(self, value, mu=0.5, sigma=0.15):
        z = (value - mu) / (sigma or 1e-6)
        likelihood = math.exp(-0.5 * z ** 2)
        glyph_log("bayesian", f"Bayes Eval: {value:.4f} → {likelihood:.4f}", glyph="⧊")
        self.logger.info(f"Bayesian Evaluation: Input={value:.4f}, Likelihood={likelihood:.4f}")
        return likelihood

    def delta(self, new_value):
        delta_val = abs(new_value - self.memory_log[-1]) if self.memory_log else 0.0
        self.memory_log.append(new_value)
        self.entropy_log.append(delta_val)
        glyph_log("entropy", f"Δ Entropy: {delta_val:.4f}", glyph="Δ")
        self.logger.info(f"Entropy Delta: {delta_val:.4f}")
        return delta_val

    def regulate(self, value):
        adjusted = value + (self.target_mean - value) * 0.4
        glyph_log("regulation", f"Regulate: Raw={value:.4f} → Adjusted={adjusted:.4f}", glyph="⟳")
        self.logger.info(f"Regulation Applied: Raw={value:.4f}, Adjusted={adjusted:.4f}")
        return adjusted

    def emergent(self):
        window = self.memory_log[-5:] if len(self.memory_log) >= 5 else self.memory_log
        if not window:
            return 0.0
        emergent_val = sum(window) / len(window)
        glyph_log("emergent", f"🧠 Emergent Value={emergent_val:.4f}", glyph="🧠")
        self.logger.info(f"Emergence Computed: Value={emergent_val:.4f}")
        return emergent_val

    def adaptive_learning(self, score):
        error = self.target_mean - score
        self.learning_rate += 0.02 * error
        self.learning_rate = min(max(self.learning_rate, 0.01), 1.0)
        glyph_log("adaptive", f"Learn: ΔRate={self.learning_rate:.4f}, Error={error:.4f}", glyph="♻")
        self.logger.info(f"Learning Updated: Rate={self.learning_rate:.4f}, Error={error:.4f}")

    def compute_hashes(self, data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        hashes = {
            'md5': hashlib.md5(data).hexdigest(),
            'sha1': hashlib.sha1(data).hexdigest(),
            'sha256': hashlib.sha256(data).hexdigest()
        }
        glyph_log("signal", f"Hashes: MD5={hashes['md5'][:6]}…", glyph="Ψ")
        self.logger.info(f"Hashes Computed: MD5={hashes['md5']} SHA1={hashes['sha1']} SHA256={hashes['sha256']}")
        return hashes

# Test Block
if __name__ == "__main__":
    engine = AdaptiveBehaviorEngine()
    val = random.random()
    d = engine.delta(val)
    b = engine.bayes(val)
    r = engine.regulate(val)
    e = engine.emergent()
    engine.adaptive_learning(b)