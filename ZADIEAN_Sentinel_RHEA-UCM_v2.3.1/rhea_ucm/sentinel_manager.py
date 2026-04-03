# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/sentinel_manager.py                             ║
# ║ ⌬ Tier: Sovereign · Glyphset: ♇🧙‍♂️♏ · Patent: US 63/796,404            ║
# ║ ⌬ Description: Core Sentinel Manager · Signal, Threat, Self-Audit Core  ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import logging
from rhea_ucm.utils.logging_setup import setup_logger, get_log_dir
from rhea_ucm.interpreter import RHEAInterpreter
from rhea_ucm.utils.behavioral import BehavioralMonitor
from rhea_ucm.utils.intrusion_detection import IntrusionDetection
from rhea_ucm.utils.network_scan import NetworkAnalyzer
from rhea_ucm.utils.signature_checker import SignatureChecker
from rhea_ucm.utils.self_reflection import SelfReflection
from rhea_ucm.utils.adaptive_behavior_engine import AdaptiveBehaviorEngine
from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer

class SentinelManager:
    def __init__(self):
        self.log_dir = get_log_dir(base="logs", session_prefix="Sentinel")
        self.logger = setup_logger("sentinel_manager", self.log_dir)

        self.rhea = RHEAInterpreter(log_dir=self.log_dir)
        self.behavior_monitor = BehavioralMonitor(log_dir=self.log_dir)
        self.intrusion_detector = IntrusionDetection(log_dir=self.log_dir)
        self.signature_checker = SignatureChecker()  # ✅ Fixed: removed log_dir
        self.adaptive_engine = AdaptiveBehaviorEngine(log_dir=self.log_dir)
        self.self_reflection_core = SelfReflection(self.adaptive_engine)
        self.network_analyzer = NetworkAnalyzer(self.packet_callback, log_dir=self.log_dir)

        self.active_entities = {}
        self.alert_threshold = 0.75

        glyph_log("phase_lock", "Sentinel Manager Booted", glyph="♇")
        self.logger.info(get_footer())

    def start_system(self):
        self.start_network_scan()
        self.start_self_reflection()
        glyph_log("signal", "System Start-Up Complete", glyph="Ψ")
        self.logger.info(get_footer())

    def start_network_scan(self):
        glyph_log("adaptive", "Network Scan Initialized", glyph="♻")
        self.network_analyzer.start_scan()

    def packet_callback(self, packet_summary):
        src = packet_summary.get("src", "unknown")
        proto = packet_summary.get("proto", "packet_activity")
        entropy_value = self.rhea.psi()

        self.behavior_monitor.record_action(
            src, proto,
            src_ip=src,
            vpn_flag=packet_summary.get("vpn", False),
            sig_match=packet_summary.get("match", False)
        )

        self.intrusion_detector.analyze_packet(src, entropy_value, glyph="☢")
        self.update_threat_scores(src)

    def update_threat_scores(self, entity_id):
        behavior_score = self.behavior_monitor.analyze_patterns(entity_id)
        intrusion_scores = self.intrusion_detector.detect_intrusion()
        intrusion_score = intrusion_scores.get(entity_id, 0.0)
        emergence = self.rhea.emergent_behavior()

        threat_index = (behavior_score + intrusion_score + emergence) / 3.0
        self.active_entities[entity_id] = threat_index

        glyph_log("entropy", f"{entity_id} Δ-TrustIndex = {threat_index:.4f}", glyph="⚖")

        if threat_index >= self.alert_threshold:
            self.raise_alert(entity_id, threat_index)

    def raise_alert(self, entity_id, threat_index):
        self.logger.warning(f"[ALERT] Entity {entity_id} Threat Score: {threat_index:.2f}")
        glyph_log("trust_loss", f"{entity_id} flagged with ⸸ Score={threat_index:.2f}", glyph="⸸")

    def start_self_reflection(self):
        glyph_log("recursive", "Self-Reflection Engine Started", glyph="⌬")
        self.self_reflection_core.start()

    def check_file_signature(self, file_path):
        return {
            "status": self.signature_checker.check_file(file_path),
            "trusted": list(self.signature_checker.trusted),
            "blacklisted": list(self.signature_checker.blacklist)
        }

    def update_signature_trust(self, file_path, good=True):
        if good:
            self.signature_checker.trust(file_path)
        else:
            self.signature_checker.blacklist_file(file_path)

    def clear_signature_cache(self):
        self.signature_checker.clear()

    def log_startup(self):
        glyph_log("adaptive", "System Log Initialized", glyph="♻")

    def shutdown_system(self):
        self.network_analyzer.stop_scan()
        glyph_log("signal", "Shutdown executed. Sentinel offline.", glyph="Ψ")
        self.logger.info(get_footer())

    def get_active_threats(self, threshold=None):
        threshold = threshold if threshold is not None else self.alert_threshold
        return {eid: score for eid, score in self.active_entities.items() if score >= threshold}

    def force_refresh(self):
        for entity in self.active_entities:
            self.update_threat_scores(entity)
