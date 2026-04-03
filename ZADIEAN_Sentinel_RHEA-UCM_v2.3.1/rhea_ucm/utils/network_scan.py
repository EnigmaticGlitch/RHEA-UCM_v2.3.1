# ╔════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1 — Network Packet Scanner               ║
# ║ ⌬ File: /rhea_ucm/utils/network_scan.py                               ║
# ║ ⌬ Features: Signature Analysis + WHOIS/VPN + JSONL Logging            ║
# ║ ⌬ Author: EnigmaticGlitch · © 2025 · All Rights Reserved             ║
# ╚════════════════════════════════════════════════════════════════════════╝

import os
import queue
import json
import time
import threading
import logging
import scapy.all as scapy
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from rhea_ucm.utils.signature_checker import SignatureChecker
from rhea_ucm.utils.logging_setup import setup_logger
from rhea_ucm.utils.thread_governor import ThreadGovernor

MAX_LOG_MB = 512

class NetworkAnalyzer:
    def __init__(self, packet_callback, log_dir):
        self.logger = setup_logger("network_scan", log_dir)
        self.packet_callback = packet_callback
        self.packet_queue = queue.Queue()
        self._stop_event = threading.Event()
        self._lock = threading.RLock()

        self.scan_dir = os.path.join(log_dir, "network")
        self.signature_file = os.path.join(self.scan_dir, "net_signatures.txt")
        self.log_base = os.path.join(self.scan_dir, "net_scan_logs")
        self.vpn_cache = {}

        self.sig_checker = SignatureChecker(path=self.signature_file)

        self._executor = ThreadPoolExecutor(max_workers=6)
        self._sniff_thread = None

        self.thread_governor = ThreadGovernor(adjust_function=self.set_thread_count)

        self.ensure_env()
        self.logger.info("🌐 NetworkAnalyzer initialized")

    def ensure_env(self):
        os.makedirs(self.scan_dir, exist_ok=True)
        if not os.path.exists(self.signature_file):
            with open(self.signature_file, "w") as f:
                f.write("# Placeholder for network signature hex patterns\n")

    def get_active_log_path(self):
        idx = 0
        while True:
            log_path = f"{self.log_base}_{idx}.jsonl"
            if not os.path.exists(log_path) or os.path.getsize(log_path) < MAX_LOG_MB * 1024 * 1024:
                return log_path
            idx += 1

    def log_entry(self, entry: dict):
        path = self.get_active_log_path()
        entry["timestamp"] = datetime.now().isoformat()
        try:
            with open(path, "a", encoding="utf-8") as f:
                json.dump(entry, f)
                f.write("\n")
        except Exception as e:
            self.logger.error(f"[✖ LOGGING ERROR] Failed to log entry: {e} | Entry: {entry}")

    def is_vpn_ip(self, ip):
        if ip.startswith(("192.168.", "10.", "172.")):
            return False
        if ip in self.vpn_cache:
            return self.vpn_cache[ip]
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
            data = response.json()
            vpn_status = (
                data.get("proxy", False)
                or data.get("hosting", False)
                or "VPN" in data.get("org", "").upper()
            )
            self.vpn_cache[ip] = vpn_status
            return vpn_status
        except Exception as e:
            self.logger.warning(f"[WHOIS] VPN check failed for {ip}: {e}")
            return False

    def start_scan(self, iface=None):
        with self._lock:
            if self._sniff_thread and self._sniff_thread.is_alive():
                raise RuntimeError("Scan already running.")
            self._stop_event.clear()
            self._sniff_thread = threading.Thread(target=self.sniff_packets, args=(iface,), daemon=True)
            self._sniff_thread.start()
            self.logger.info("[RTS] Packet sniffing started.")

    def stop_scan(self):
        with self._lock:
            self._stop_event.set()
            self.logger.info("[RTS] Packet sniffing requested to stop.")
            self.join_sniff_thread()
            self.thread_governor.stop()

    def join_sniff_thread(self):
        if self._sniff_thread and self._sniff_thread.is_alive():
            self._sniff_thread.join(timeout=2)
            self.logger.info("[RTS] Packet sniffing thread joined.")
        self._executor.shutdown(wait=False)

    def set_thread_count(self, thread_count):
        self.logger.info(f"[🧠 Governor] Adjusting thread pool → {thread_count}")
        try:
            self._executor.shutdown(wait=True)
        except Exception:
            pass
        self._executor = ThreadPoolExecutor(max_workers=thread_count)

    def sniff_packets(self, iface):
        def process(packet):
            if self._stop_event.is_set():
                return
            if not packet.haslayer(scapy.IP):
                return
            try:
                ip_layer = packet[scapy.IP]
                raw_bytes = bytes(packet)
                summary = {
                    "src": ip_layer.src,
                    "dst": ip_layer.dst,
                    "vpn": self.is_vpn_ip(ip_layer.src),
                    "match": self.sig_checker.check_signature(raw_bytes),
                    "proto": packet.summary(),
                    "length": len(raw_bytes)
                }
                self.packet_queue.put(summary)
                self.log_entry(summary)

                if summary["vpn"] or summary["match"]:
                    self.logger.warning(
                        f"[⚠️ DETECTED] Src: {summary['src']} | VPN: {summary['vpn']} | Match: {summary['match']}"
                    )
            except Exception as e:
                self.logger.error(f"[✖] Packet processing failed: {e}")

        while not self._stop_event.is_set():
            try:
                scapy.sniff(
                    iface=iface,
                    prn=process,
                    store=False,
                    filter="ip",
                    timeout=1
                )
            except Exception as e:
                self.logger.error(f"[✖] Sniffing error: {e}")
                break

    def process_pending_packets(self):
        packets = []
        while not self.packet_queue.empty():
            try:
                packets.append(self.packet_queue.get_nowait())
            except queue.Empty:
                break
        if packets:
            for pkt in packets:
                self._executor.submit(self.packet_callback, pkt)