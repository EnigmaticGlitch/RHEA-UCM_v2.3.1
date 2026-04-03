# ╔════════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1 — Signature Checker Module                  ║
# ║ ⌬ File: /rhea_ucm/utils/signature_checker.py                               ║
# ║ ⌬ Features: JSONL-Based Trust/Blacklist with SHA Confidence Digests       ║
# ║ ⌬ Author: EnigmaticGlitch ♇🧙‍♂️♏ · © 2025 · All Rights Reserved           ║
# ╚════════════════════════════════════════════════════════════════════════════╝

import os
import hashlib
import json
from rhea_ucm.utils.core.moniker_signatures import glyph_log

DEFAULT_SIGNATURE_FILE = os.path.join("logs", "NetworkScan", "net_signatures.json")

class SignatureChecker:
    def __init__(self, path=DEFAULT_SIGNATURE_FILE):
        self.signature_path = path
        self.signatures = set()
        self._ensure_signature_file()
        self._load_signatures()

    def _ensure_signature_file(self):
        folder = os.path.dirname(self.signature_path)
        os.makedirs(folder, exist_ok=True)
        if not os.path.isfile(self.signature_path):
            with open(self.signature_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)
            glyph_log("init", f"Created new signature file → {self.signature_path}", glyph="♻")

    def _load_signatures(self):
        try:
            with open(self.signature_path, "r", encoding="utf-8") as f:
                hashes = json.load(f)
                if isinstance(hashes, list):
                    self.signatures = set(hashes)
                    glyph_log("trust", f"Loaded {len(hashes)} known hashes", glyph="✔")
        except Exception as e:
            glyph_log("anomaly", f"Failed to load signatures: {e}", glyph="☣")
            self.signatures = set()

    def _save_signatures(self):
        try:
            with open(self.signature_path, "w", encoding="utf-8") as f:
                json.dump(sorted(self.signatures), f, indent=2)
            glyph_log("adaptive", f"Saved {len(self.signatures)} signatures", glyph="💾")
        except Exception as e:
            glyph_log("fatal", f"Signature save failure: {e}", glyph="💥")

    def check_signature(self, raw_bytes: bytes) -> bool:
        digest = hashlib.sha256(raw_bytes).hexdigest()
        return digest in self.signatures

    def add_signature(self, raw_bytes: bytes):
        digest = hashlib.sha256(raw_bytes).hexdigest()
        if digest not in self.signatures:
            self.signatures.add(digest)
            self._save_signatures()
            glyph_log("trust_gain", f"New signature added: {digest[:12]}...", glyph="⚠")

    @staticmethod
    def hash_variants(raw_bytes: bytes) -> dict:
        return {
            "md5": hashlib.md5(raw_bytes).hexdigest(),
            "sha1": hashlib.sha1(raw_bytes).hexdigest(),
            "sha256": hashlib.sha256(raw_bytes).hexdigest()
        }

    @classmethod
    def from_bytes(cls, raw_bytes: bytes, path=DEFAULT_SIGNATURE_FILE):
        checker = cls(path)
        return checker.check_signature(raw_bytes)
