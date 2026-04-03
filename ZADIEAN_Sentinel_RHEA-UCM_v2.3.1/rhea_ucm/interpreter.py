# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: C:/Users/south/Documents/Theories/ZADEIAN_Sentinel_RHEA-UCM_v2.3║
# ║ ⌬     /rhea_ucm/utils/interpreter.py                                    ║
# ║ ⌬ Description: RHEA-UCM 3.8.1 Interpreter (Signal-Entropy-Adaptation Core)║
# ╚══════════════════════════════════════════════════════════════════════════╝

import math
import torch
import hashlib
from rhea_ucm.utils.logging_setup import setup_logger
from rhea_ucm.utils.core.moniker_signatures import glyph_log

class RHEAInterpreter:
    def __init__(self, log_dir="logs"):
        self.logger = setup_logger("interpreter", log_dir)
        self.entropy_log = []
        self.memory_log = []
        self.hash_library = {'md5': set(), 'sha1': set(), 'sha256': set()}
        self.learning_rate = 0.05
        self.target_mean = 0.8
        glyph_log("adaptive", "🧠 Interpreter Initialized", glyph="♇")
        self.logger.info("Interpreter Core Initialized")

    def psi(self):
        """Ψ Signal - Random pulse generator"""
        device = "cuda" if torch.cuda.is_available() else "cpu"
        pulse = torch.rand(1, device=device).item()
        self.logger.info(f"[Ψ] Pulse Generated: {pulse:.5f} on {device}")
        return pulse

    def bayes(self, value, mu=0.5, sigma=0.15):
        """Bayesian Likelihood - Probabilistic scoring"""
        if sigma == 0:
            sigma = 1e-6
        z = (value - mu) / sigma
        likelihood = math.exp(-0.5 * z ** 2)
        self.logger.info(f"[Bayes] value={value:.5f}, mu={mu}, sigma={sigma}, likelihood={likelihood:.5f}")
        return likelihood

    def delta(self, new_value):
        """Δ Entropy - Change detection"""
        delta_val = abs(new_value - self.memory_log[-1]) if self.memory_log else 0.0
        self.entropy_log.append(delta_val)
        self.memory_log.append(new_value)
        self.logger.info(f"[Δ] Entropy Change: {delta_val:.5f}")
        return delta_val

    def reg(self, value):
        """Φ Regulation - Smooth oscillation toward mean"""
        adjusted = value + (self.target_mean - value) * 0.4
        self.logger.info(f"[Reg] Raw={value:.5f}, Adjusted={adjusted:.5f}")
        return adjusted

    def compute_hashes(self, content):
        """Hash Computation - MD5, SHA1, SHA256"""
        if isinstance(content, str):
            content = content.encode("utf-8")
        hashes = {
            "md5": hashlib.md5(content).hexdigest(),
            "sha1": hashlib.sha1(content).hexdigest(),
            "sha256": hashlib.sha256(content).hexdigest()
        }
        self.logger.info(f"[Hashes] {hashes}")
        return hashes

    def adaptive_learning(self, score):
        """Learning Rate Adaptation - Adjust based on performance"""
        error = self.target_mean - score
        self.learning_rate += 0.02 * error
        self.learning_rate = max(0.01, min(self.learning_rate, 1.0))
        self.logger.info(f"[Learning Rate] Updated: {self.learning_rate:.5f} (error={error:.5f})")

    def emergent_behavior(self):
        """🧬 Emergent Pattern - Average of last 5 events"""
        if not self.memory_log:
            return 0.0
        window = self.memory_log[-5:] if len(self.memory_log) >= 5 else self.memory_log
        emergent_val = sum(window) / len(window)
        self.logger.info(f"[Emergence] Last 5 Avg: {emergent_val:.5f}")
        return emergent_val

    def emergent_structure(self):
        """🧬 Structure Recognition - Latent average pattern"""
        if not self.memory_log:
            return 0.0
        recent = self.memory_log[-5:]
        average = sum(recent) / len(recent)
        self.logger.info(f"[Structure] Memory Score: {average:.5f}")
        return average