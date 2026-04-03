# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/behavioral.py                                   ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Behavioral Pattern Analysis and Entropy Scoring Core     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import logging
import time
import math
from collections import deque, defaultdict

from rhea_ucm.interpreter import RHEAInterpreter
from rhea_ucm.utils.adaptive_behavior_engine import AdaptiveBehaviorEngine
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.utils.logging_setup import setup_logger

# ════════════════════════════════════════════════════════════════════════
# BEHAVIORAL MONITOR
# ════════════════════════════════════════════════════════════════════════

class BehavioralMonitor:
    def __init__(self, log_dir):
        self.logger = setup_logger("behavioral", log_dir)
        self.action_log = defaultdict(deque)
        self.pattern_history = {}
        self.rhea = RHEAInterpreter(log_dir)
        self.engine = AdaptiveBehaviorEngine(log_dir)
        self.window_size = 60  # Time window in seconds
        glyph_log("recursive", "Behavioral Monitor Initialized", glyph="⌬")
        self.logger.info(get_footer())

    def record_action(self, entity_id, action_type, src_ip=None, vpn_flag=False, sig_match=False):
        timestamp = time.time()
        self.action_log[entity_id].append((timestamp, action_type))

        log_msg = f"Action from {entity_id} | Action: {action_type}"
        if src_ip:
            log_msg += f" | IP: {src_ip} | VPN: {vpn_flag} | Signature: {sig_match}"
        glyph_log("signal", log_msg, glyph="Ψ")

    def prune_old(self, entity_id):
        now = time.time()
        self.action_log[entity_id] = deque(
            [(t, a) for (t, a) in self.action_log[entity_id] if now - t < self.window_size],
            maxlen=100
        )

    def analyze_patterns(self, entity_id):
        self.prune_old(entity_id)
        recent_actions = [a for (_, a) in self.action_log[entity_id]]

        if not recent_actions:
            return 0.0

        pattern_score = len(set(recent_actions)) / len(recent_actions)
        score = 1.0 - pattern_score
        glyph_log("adaptive", f"Pattern Score for {entity_id}: {score:.4f}", glyph="♻")
        return score

    def compute_behavioral_entropy(self, entity_id):
        self.prune_old(entity_id)
        counts = defaultdict(int)
        for _, action in self.action_log[entity_id]:
            counts[action] += 1

        total = sum(counts.values())
        if total == 0:
            return 0.0

        entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
        glyph_log("entropy", f"Entropy for {entity_id}: {entropy:.4f}", glyph="Δ")
        return entropy

    def behavioral_threat_index(self, entity_id):
        pattern_score = self.analyze_patterns(entity_id)
        entropy = self.compute_behavioral_entropy(entity_id)
        rhea_score = self.rhea.psi()

        combined = (pattern_score + entropy + rhea_score) / 3.0
        glyph_log("bayesian", f"Threat Index for {entity_id}: {combined:.4f}", glyph="⧊")
        return combined

    def log_behavioral_event(self, entity_id, action, meta={}):
        """Convenience method to safely record action with metadata injection"""
        self.record_action(
            entity_id,
            action,
            src_ip=meta.get("src"),
            vpn_flag=meta.get("vpn", False),
            sig_match=meta.get("match", False)
        )

# ════════════════════════════════════════════════════════════════════════
# HEURISTIC SCANNER (INLINE RESTORE)
# ════════════════════════════════════════════════════════════════════════

TRUST_DECAY_RATE = 0.08

GLYPH_WHITELIST = {
    "♻", "☯", "⌬", "⚛", "🧠", "♇", "䷘", "☣"
}

class HeuristicScanner:
    def __init__(self):
        self.entity_scores = {}

    def scan_entity(self, entity_id, signal_entropy, delta, glyph):
        score = self.entity_scores.get(entity_id, 0.5)

        if glyph in GLYPH_WHITELIST:
            score += 0.05
        else:
            score -= TRUST_DECAY_RATE * delta

        score = min(max(score, 0.0), 1.0)
        self.entity_scores[entity_id] = score
        glyph_log("trust_gain" if score >= 0.5 else "trust_loss", f"Entity {entity_id} trust score: {score:.4f}")
        return score

    def get_trust(self, entity_id):
        return self.entity_scores.get(entity_id, 0.0)

# ════════════════════════════════════════════════════════════════════════
# TEST BLOCK
# ════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    from logging_setup import get_log_dir
    log_dir = get_log_dir()
    monitor = BehavioralMonitor(log_dir)
    monitor.log_behavioral_event("host123", "ping", {"src": "192.168.1.10", "vpn": True, "match": True})
    monitor.log_behavioral_event("host123", "dns_lookup")
    score = monitor.behavioral_threat_index("host123")
    print("Threat Index:", score)

    hs = HeuristicScanner()
    trust = hs.scan_entity("host123", 0.81, 0.07, "☣")
    print("Trust Level:", trust)
    print(get_footer())