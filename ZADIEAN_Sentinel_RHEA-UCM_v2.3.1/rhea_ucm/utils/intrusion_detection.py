# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/intrusion_detection.py                          ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404             ║
# ║ ⌬ Description: Symbolic Intrusion Detection Engine & Threat Scoring     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import logging
import random

from rhea_ucm.utils.adaptive_behavior_engine import AdaptiveBehaviorEngine
from rhea_ucm.utils.behavioral import HeuristicScanner
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.utils.logging_setup import setup_logger

class IntrusionDetection:
    def __init__(self, log_dir="logs", delta_weight=0.3, trust_weight=0.4, bayes_weight=0.3):
        self.logger = setup_logger("intrusion_detection", log_dir)
        self.engine = AdaptiveBehaviorEngine(log_dir)
        self.heuristic = HeuristicScanner()
        self.entities = {}
        self.weights = {
            "delta": delta_weight,
            "trust": trust_weight,
            "bayes": bayes_weight
        }
        self.logger.info("🧠 Intrusion Detection Engine Initialized")
        glyph_log("phase_lock", "Intrusion Detection Engine Loaded", glyph="♇")

    def analyze_packet(self, packet_id: str, entropy_val: float, glyph: str = "☢"):
        try:
            delta = self.engine.delta(entropy_val)
            bayes_score = self.engine.bayes(entropy_val)
            trust_score = self.heuristic.scan_entity(packet_id, entropy_val, delta, glyph)

            threat_score = (
                delta * self.weights["delta"] +
                (1 - trust_score) * self.weights["trust"] +
                (1 - bayes_score) * self.weights["bayes"]
            )

            self.entities[packet_id] = threat_score
            self.engine.adaptive_learning(threat_score)

            glyph_log("entropy", f"[{packet_id}] Δ={delta:.3f}", "Δ")
            glyph_log("bayesian", f"[{packet_id}] P={bayes_score:.3f}", "⧊")
            glyph_log("adaptive", f"[{packet_id}] Trust={trust_score:.3f}", "⚖")

            if threat_score > 0.8:
                glyph_log("anomaly", f"[{packet_id}] ☣ THREAT DETECTED: Score={threat_score:.3f}", "☣")
            elif threat_score > 0.6:
                glyph_log("trust_loss", f"[{packet_id}] ⸸ Suspicious Activity: Score={threat_score:.3f}", "⸸")
            else:
                glyph_log("trust_gain", f"[{packet_id}] ✓ Benign Activity: Score={threat_score:.3f}", "⚖")

            return threat_score

        except Exception as e:
            glyph_log("fatal", f"[{packet_id}] Intrusion scan failed: {e}", "✖")
            self.logger.exception("Intrusion scan exception")
            return 0.0

    def scan_batch(self, batch_data):
        """Accepts list of (packet_id, entropy_value, glyph) tuples"""
        for packet_id, entropy_val, glyph in batch_data:
            self.analyze_packet(packet_id, entropy_val, glyph)

    def detect_intrusion(self):
        """Returns dict of {entity: threat_score}"""
        return self.entities

    def score_threat_level(self):
        """Returns global system-wide threat index"""
        scores = list(self.entities.values())
        return round(sum(scores) / len(scores), 4) if scores else 0.0

# ════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    from rhea_ucm.utils.logging_setup import get_log_dir
    log_dir = get_log_dir()
    ids = IntrusionDetection(log_dir)
    test_data = [
        ("pkt_Ψ001", random.uniform(0.2, 0.9), "♇"),
        ("pkt_Δ002", random.uniform(0.3, 0.85), "☣"),
        ("pkt_Φ003", random.uniform(0.1, 0.7), "⧊")
    ]
    ids.scan_batch(test_data)
    print(get_footer())
