# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ® 2025 Paul M. Roe / EnigmaticGlitch — All Rights Reserved.             ║
# ║ ⌬ ZADEIAN-RHEA Sentinel Iteration_2                                     ║
# ║ ⌬ File: /rhea_ucm/utils/graphing.py                                     ║
# ║ ⌬ Description: Entropy & Trust Diagnostic Graphing + Glyph Watermarks   ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import os
import matplotlib
matplotlib.use("Agg")  # Ensure headless-safe rendering
import matplotlib.pyplot as plt
import logging
import warnings

from rhea_ucm.utils.core.moniker_signatures import glyph_log, get_footer
from rhea_ucm.utils.logging_setup import setup_logger

# Set emoji-safe font for glyph plots
plt.rcParams['font.family'] = 'Segoe UI Emoji'

# Suppress font and glyph warning spam
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


class GraphingTools:
    def __init__(self, log_dir):
        self.logger = setup_logger("graphing", log_dir)
        self.graph_dir = os.path.abspath(os.path.join(log_dir, "..", "graphs"))
        os.makedirs(self.graph_dir, exist_ok=True)

    def _get_output_path(self, filename: str):
        return os.path.join(self.graph_dir, filename)

    def plot_entropy_trust(self, entropy_log, trust_log, output_file="entropy_trust_plot.png"):
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(entropy_log, label="Δ Entropy", color="red", linestyle="--")
            plt.plot(trust_log, label="⚖ Trust", color="blue", linestyle="-")
            plt.title("Δ Entropy vs ⚖ Trust Levels")
            plt.xlabel("Timestep")
            plt.ylabel("Score")
            plt.grid(True)
            plt.legend()
            plt.text(0.98, 0.02, "🧠♇⸸", fontsize=12, ha="right", va="bottom",
                     transform=plt.gca().transAxes, alpha=0.5)
            plt.tight_layout()
            path = self._get_output_path(output_file)
            plt.savefig(path, dpi=300, bbox_inches='tight')
            glyph_log("recursive", f"Graph saved with glyph overlay to {path}", glyph="⌬")
            self.logger.info(get_footer())
        except Exception as e:
            glyph_log("anomaly", f"plot_entropy_trust() error: {str(e)}", glyph="☣")
            self.logger.exception("Graphing error")
        finally:
            plt.close()

    def plot_network_activity(self, packet_data, output_file="network_activity.png"):
        try:
            plt.figure(figsize=(10, 4))
            packet_lengths = [p["length"] for p in packet_data if isinstance(p, dict) and "length" in p]
            indices = list(range(len(packet_lengths)))
            plt.plot(indices, packet_lengths, color="magenta", label="Ψ Packet Signature Lengths")
            plt.title("Ψ Network Activity Over Time")
            plt.xlabel("Packet Index")
            plt.ylabel("Length (bytes)")
            plt.grid(True)
            plt.legend()
            plt.text(0.98, 0.02, "ΨΔ♇", fontsize=12, ha="right", va="bottom",
                     transform=plt.gca().transAxes, alpha=0.5)
            plt.tight_layout()
            path = self._get_output_path(output_file)
            plt.savefig(path, dpi=300, bbox_inches="tight")
            glyph_log("signal", f"Network activity plot saved to {path}", glyph="Ψ")
            self.logger.info(get_footer())
        except Exception as e:
            glyph_log("anomaly", f"plot_network_activity() error: {str(e)}", glyph="☣")
            self.logger.exception("Graphing error")
        finally:
            plt.close()

    def plot_entropy_threat(self,
                            entropy_log,
                            threat_log,
                            entity_scores=None,
                            entropy_spikes=None,
                            glyphs=None,
                            output_file="entropy_threat_plot.png"):
        try:
            import numpy as np

            plt.figure(figsize=(12, 6))
            x = list(range(len(entropy_log)))
            plt.plot(x, entropy_log, label="Δ Entropy", color="#FFA500", linestyle="--", linewidth=2)
            plt.plot(x, threat_log, label="☣ Threat Index", color="#32CD32", linewidth=2)

            if entropy_spikes:
                for spike in entropy_spikes:
                    plt.axvline(x=spike, color="red", linestyle=":", alpha=0.6, linewidth=1)
                    plt.text(spike, max(entropy_log), "⚡", fontsize=10, ha="center", va="bottom", color="red")

            if glyphs:
                for i, g in enumerate(glyphs):
                    if i < len(entropy_log) and i % 3 == 0:
                        plt.text(i, entropy_log[i] + 0.05, g, fontsize=12, alpha=0.6)

            plt.axhspan(0.75, max(max(entropy_log), max(threat_log)), color='red', alpha=0.05)

            if entity_scores:
                for idx, (entity, score) in enumerate(entity_scores.items()):
                    plt.plot(len(entropy_log)-1, score, marker='o', color="magenta", alpha=0.7)
                    plt.text(len(entropy_log)-1 + 0.5, score, f"{entity}: {score:.2f}", fontsize=8, color="magenta")

            plt.title("Δ Entropy vs ☣ Threat Index")
            plt.xlabel("Timestep")
            plt.ylabel("Score")
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.text(0.98, 0.02, "Δ☣🧠", fontsize=12, ha="right", va="bottom",
                     transform=plt.gca().transAxes, alpha=0.4)

            plt.tight_layout()
            path = self._get_output_path(output_file)
            plt.savefig(path, dpi=300, bbox_inches='tight')
            glyph_log("signal", f"Entropy-Threat graph saved with overlays → {path}", glyph="🧠")
            self.logger.info(get_footer())
        except Exception as e:
            glyph_log("anomaly", f"Failed to render plot_entropy_threat(): {str(e)}", glyph="☣")
            self.logger.exception("Graphing error")
        finally:
            plt.close()