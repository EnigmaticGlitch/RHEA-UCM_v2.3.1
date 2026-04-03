# RHEA-UCM_v2.3.1
Before Sentinel became Sentinel

*Scans Network and Files*

Python3

How to use: 
Download entire RHEA-UCM_V2.3.1 folder.
Open CMD
Navigate to Root Dir in CMD
BASH: python Zadeian-RHEA_Sentinel.py


ZADIEAN Sentinel RHEA-UCM v2.3.1

Comprehensive Software Review

Executive Summary

ZADIEAN Sentinel RHEA-UCM (Recursive Heuristic Entropy-Adaptation with Unified Cognitive Mechanism) v2.3.1 is a sophisticated Python-based cybersecurity monitoring and threat detection framework developed by Paul M. Roe (EnigmaticGlitch). The software represents a novel approach to intrusion detection and behavioral analysis, incorporating mathematical models from signal processing, Bayesian inference, and entropy theory. It operates under U.S. Patent Pending #63/796,404 and is designated as "Sovereign Tier" software.

The system functions as a real-time network security monitor with adaptive behavioral analysis, utilizing symbolic computation and recursive self-reflection mechanisms to detect, analyze, and respond to potential security threats across network environments.

1. System Architecture Overview

1.1 High-Level Architecture

The software follows a modular, multi-tiered architecture consisting of the following primary layers:

┌─────────────────────────────────────────────────────────────────┐
│                    GUI Layer (tkinter-based)                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │  Main    │ │ Network  │ │  Threat  │ │Benchmark │           │
│  │  Window  │ │  Window  │ │Dashboard │ │  Window  │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
├─────────────────────────────────────────────────────────────────┤
│                    Sentinel Manager Layer                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              SentinelManager (Core Orchestrator)          │  │
│  └──────────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│                    RHEA-UCM Core Layer                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │  RHEA        │ │  Adaptive    │ │   Self       │           │
│  │ Interpreter  │ │  Behavior    │ │ Reflection   │           │
│  │              │ │  Engine      │ │              │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
├─────────────────────────────────────────────────────────────────┤
│                    Utility & Detection Layer                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │  Behavioral  │ │  Intrusion   │ │   Network    │           │
│  │  Monitor     │ │  Detection   │ │  Analyzer    │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │  Signature   │ │   Thread     │ │  Graphing    │           │
│  │  Checker     │ │  Governor    │ │   Tools      │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘

1.2 Core Components Breakdown

1.2.1 SentinelManager (rhea_ucm/sentinel_manager.py)

The central orchestration class that coordinates all subsystems:

- Initialization: Sets up logging, initializes all sub-components

- System Lifecycle: Manages startup, shutdown, and system state

- Threat Coordination: Aggregates threat scores from multiple detection vectors

- Alert Management: Raises alerts when threat thresholds are exceeded

1.2.2 RHEAInterpreter (rhea_ucm/interpreter.py)

The mathematical computation engine implementing the core RHEA algorithms:

- Psi (Ψ) Signal Generation: Random pulse generation using PyTorch (CUDA-enabled)

- Bayesian Likelihood: Probabilistic scoring with Gaussian distribution

- Delta (Δ) Entropy: Change detection and tracking

- Phi (Φ) Regulation: Oscillation smoothing toward target mean

- Hash Computation: MD5, SHA1, SHA256 cryptographic hashing

1.2.3 AdaptiveBehaviorEngine (rhea_ucm/utils/adaptive_behavior_engine.py)

A recursive adaptive system that implements:

- Bayesian Evaluation: Gaussian likelihood computation

- Entropy Delta Tracking: Change detection with historical logging

- Regulation Mechanism: Self-adjusting toward target equilibrium

- Emergent Behavior Detection: Pattern recognition across temporal windows

- Adaptive Learning Rate: Dynamic rate adjustment based on error signals

1.2.4 BehavioralMonitor (rhea_ucm/utils/behavioral.py)

Entity behavior tracking and pattern analysis:

- Action Logging: Records entity activities with timestamps

- Pattern Analysis: Calculates behavioral diversity scores

- Entropy Computation: Shannon entropy for action distribution

- Threat Indexing: Combined behavioral threat assessment

- HeuristicScanner: Trust scoring with glyph-based evaluation

1.2.5 IntrusionDetection (rhea_ucm/utils/intrusion_detection.py)

Primary threat detection engine:

- Multi-vector Analysis: Combines delta, trust, and Bayesian scores

- Weighted Scoring: Configurable weights for different detection methods

- Batch Processing: Supports multiple packet analysis

- Threat Classification: Categorizes threats (benign, suspicious, critical)

1.2.6 NetworkAnalyzer (rhea_ucm/utils/network_scan.py)

Real-time network packet capture and analysis:

- Packet Sniffing: Uses Scapy for network traffic capture

- VPN Detection: IP-API integration for VPN/proxy detection

- Signature Matching: Hash-based packet signature verification

- JSONL Logging: Structured log output for network events

- Thread Pool Management: Concurrent packet processing

2. Novel Algorithms and Approaches

2.1 RHEA Mathematical Framework

The software implements a proprietary mathematical framework defined as:

2.1.1 Psi (Ψ) Signal - Entropy Pulse Generation

def psi(self):
    """Ψ Signal - Random pulse generator"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pulse = torch.rand(1, device=device).item()
    return pulse

This generates random entropy pulses used as the foundation for all downstream calculations. The CUDA acceleration enables high-throughput signal generation.

2.1.2 Bayesian Likelihood Function

def bayes(self, value, mu=0.5, sigma=0.15):
    """Bayesian Likelihood - Probabilistic scoring"""
    z = (value - mu) / sigma
    likelihood = math.exp(-0.5 * z ** 2)
    return likelihood

Implements a Gaussian likelihood function for probability evaluation. The default parameters (μ=0.5, σ=0.15) create a centered distribution with controlled sensitivity.

2.1.3 Delta (Δ) Entropy - Change Detection

def delta(self, new_value):
    """Δ Entropy - Change detection"""
    delta_val = abs(new_value - self.memory_log[-1]) if self.memory_log else 0.0
    self.entropy_log.append(delta_val)
    self.memory_log.append(new_value)
    return delta_val

Tracks temporal changes in signal values, maintaining a historical log for trend analysis.

2.1.4 Phi (Φ) Regulation - Homeostatic Correction

def reg(self, value):
    """Φ Regulation - Smooth oscillation toward mean"""
    adjusted = value + (self.target_mean - value) * 0.4
    return adjusted

Implements a dampening mechanism that gradually adjusts values toward a target equilibrium (default 0.8), simulating homeostatic regulation.

2.2 Emergent Behavior Detection

def emergent_behavior(self):
    """🧬 Emergent Pattern - Average of last 5 events"""
    if not self.memory_log:
        return 0.0
    window = self.memory_log[-5:] if len(self.memory_log) >= 5 else self.memory_log
    emergent_val = sum(window) / len(window)
    return emergent_val

This rolling window approach detects emergent patterns by analyzing recent signal history, enabling the system to identify trends and anomalies.

2.3 Adaptive Learning Rate

def adaptive_learning(self, score):
    """Learning Rate Adaptation - Adjust based on performance"""
    error = self.target_mean - score
    self.learning_rate += 0.02 * error
    self.learning_rate = max(0.01, min(self.learning_rate, 1.0))

Dynamically adjusts the learning rate based on deviation from target performance, bounded between 0.01 and 1.0.

2.4 Symbolic Glyph-Based Logging System

A novel approach to system state representation using Unicode glyphs:

GLYPHSET = {
    "entropy": "Δ",
    "trust_gain": "⚖",
    "trust_loss": "⸘",
    "anomaly": "☣",
    "signal": "Ψ",
    "emergent": "🧠",
    "phase_lock": "♊",
    "regulation": "⟳",
    "adaptive": "♻",
    "recursive": "⌬",
    "bayesian": "⧊",
    "pluto_lock": "♊🌀",
    "fatal": "💥",
    "termination": "☯"
}

This symbolic representation provides immediate visual categorization of system events and states.

2.5 Multi-Vector Threat Scoring

threat_score = (
    delta * self.weights["delta"] +
    (1 - trust_score) * self.weights["trust"] +
    (1 - bayes_score) * self.weights["bayes"]
)

Combines three independent metrics with configurable weights (default: delta=0.3, trust=0.4, bayes=0.3) to produce a composite threat score.

2.6 Heuristic Trust Model

GLYPH_WHITELIST = {"♻", "☯", "⌬", "⚡", "🧠", "♊", "䶘", "☣"}

def scan_entity(self, entity_id, signal_entropy, delta, glyph):
    score = self.entity_scores.get(entity_id, 0.5)

    if glyph in GLYPH_WHITELIST:
        score += 0.05
    else:
        score -= TRUST_DECAY_RATE * delta

    score = min(max(score, 0.0), 1.0)
    self.entity_scores[entity_id] = score
    return score

A trust scoring system that incorporates symbolic classification alongside numerical metrics.

3. User-Facing Features

3.1 Main Console (MainWindow)

The primary user interface provides:

- Navigation Hub: Central access point for all subsystems

- Thread Monitoring: Real-time active thread count display

- ASCII Art Watermark: Visual branding with system identification

- Dark Theme Interface: Professional cybersecurity aesthetic (#111111 background)

Accessible Modules:

- Scan Window - File/system scanning interface

- Network Monitor - Real-time network activity visualization

- Evolution Window - Behavioral evolution tracking

- Security Center - Security configuration and controls

- Benchmark Dashboard - Performance metrics

- Real-Time Scanner - Live signal monitoring

- Threat Dashboard - Active threat visualization

3.2 Threat Dashboard

Real-time threat monitoring interface featuring:

- Entity Table: Lists all tracked entities with threat scores

- Live Graph: Bar chart visualization of threat scores

- Auto-Refresh: Configurable automatic updates (default: 6 seconds)

- Manual Refresh: On-demand data update capability

3.3 Real-Time Signal Monitor (RTS)

Live signal visualization showing:

- Ψ Signal Plot: Random pulse visualization (cyan)

- Δ Entropy Plot: Entropy change tracking (orange)

- Φ Regulation Plot: Regulation adjustment visualization (magenta)

- Graph Export: Save visualization to PNG files

3.4 Network Monitor

Network analysis interface providing:

- Packet Capture Statistics: Live traffic analysis

- VPN Detection Alerts: Warnings for detected VPN/proxy connections

- Signature Match Alerts: Known threat pattern notifications

3.5 Benchmark Dashboard

Performance testing interface for:

- Pulse Speed Benchmark: Measures Ψ signal generation rate

- Entropy Reaction Benchmark: Measures Δ response time

- Regulation Speed Benchmark: Measures Φ adjustment speed

3.6 Security Center

Administrative interface for:

- Signature Management: Trust/blacklist file operations

- Signature Checking: File verification against known hashes

- Cache Management: Clear signature caches

4. Intrinsic and Inherent Capabilities

4.1 Self-Reflection Engine

class SelfReflection:
    def _reflect(self):
        while self.running:
            time.sleep(self.audit_interval)

            last_entropy = self.engine.entropy_log[-5:] if self.engine.entropy_log else []
            emergence = self.engine.emergent()
            high_threats = sum(1 for e in self.engine.entropy_log if e > 0.75)
            rate = self.engine.learning_rate

The system includes a recursive self-monitoring capability that:

- Runs periodic audits (default: 300-second intervals)

- Analyzes entropy trends

- Evaluates emergence patterns

- Tracks learning rate evolution

- Generates diagnostic reports

4.2 Dynamic Thread Governance

class ThreadGovernor:
    def _govern_loop(self):
        while not self._stop_event.is_set():
            if GPU_AVAILABLE:
                gpu_load = self._get_gpu_utilization()
                ideal = int((1 - gpu_load / 100) * self.max_threads)
                ideal = max(self.min_threads, min(ideal, self.max_threads))
                if ideal != self.current_threads:
                    self.adjust_function(ideal)

Adaptive thread pool management that:

- Monitors GPU utilization (via NVML)

- Dynamically adjusts worker thread count

- Maintains system stability under varying loads

- Falls back to static configuration if GPU unavailable

4.3 Behavioral Pattern Recognition

def analyze_patterns(self, entity_id):
    self.prune_old(entity_id)
    recent_actions = [a for (_, a) in self.action_log[entity_id]]

    if not recent_actions:
        return 0.0

    pattern_score = len(set(recent_actions)) / len(recent_actions)
    score = 1.0 - pattern_score
    return score

Analyzes entity behavior to detect:

- Action diversity (low diversity = suspicious repetition)

- Temporal patterns within configurable windows

- Behavioral anomalies through entropy analysis

4.4 Shannon Entropy Computation

def compute_behavioral_entropy(self, entity_id):
    counts = defaultdict(int)
    for _, action in self.action_log[entity_id]:
        counts[action] += 1

    total = sum(counts.values())
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
    return entropy

Implements information-theoretic entropy for behavioral analysis, measuring the unpredictability of entity actions.

4.5 Cryptographic Hash Verification

Multi-algorithm hash computation:

- MD5: 128-bit hash for quick identification

- SHA-1: 160-bit hash for compatibility

- SHA-256: 256-bit hash for security applications

Signature database supports:

- Known-good (trusted) signatures

- Known-bad (blacklisted) signatures

- Real-time packet signature matching

4.6 VPN and Proxy Detection

def is_vpn_ip(self, ip):
    if ip.startswith(("192.168.", "10.", "172.")):
        return False
    response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
    data = response.json()
    vpn_status = (
        data.get("proxy", False)
        or data.get("hosting", False)
        or "VPN" in data.get("org", "").upper()
    )
    return vpn_status

External API integration for IP analysis:

- Detects VPN connections

- Identifies proxy servers

- Recognizes hosting infrastructure

4.7 Structured Logging System

Multi-layered logging architecture:

- Session-based Directories: Timestamped log folders

- Component-specific Logs: Separate files per subsystem

- JSONL Format: Structured, parseable network logs

- JSON Signature Database: Persistent hash storage

5. Configuration and Customization

5.1 Threat Scoring Weights (config/intrusion_config.yaml)

threat_scoring:
  delta_weight: 0.3      # Weight of behavioral entropy shift Δ
  trust_weight: 0.4      # Weight of symbolic trust loss ⚖
  bayes_weight: 0.3      # Weight of Bayesian abnormality ⧊

Allows customization of the multi-vector threat scoring algorithm.

5.2 Alert Thresholds

self.alert_threshold = 0.75  # Configurable in SentinelManager

Threshold for triggering threat alerts (range: 0.0-1.0).

5.3 Learning Parameters

- Learning Rate: Initial 0.05, adaptive range 0.01-1.0

- Target Mean: Default 0.8 for regulation target

- Window Size: Default 60 seconds for behavioral analysis

- Audit Interval: Default 300 seconds for self-reflection

5.4 Thread Pool Configuration

- Max Threads: Default 10

- Min Threads: Default 1

- Safe Load Threshold: Default 70% GPU utilization

6. Dependencies and Requirements

6.1 Python Requirements

torch          # Deep learning framework for CUDA-accelerated computation
numpy          # Numerical computing library
matplotlib     # Visualization and plotting
scapy          # Network packet manipulation
customtkinter  # Enhanced tkinter widgets

6.2 System Requirements

- Python Version: 3.8+ (enforced at startup)

- GPU Support: Optional CUDA acceleration via PyTorch

- NVIDIA Management: Optional NVML for GPU monitoring

- Administrative Privileges: Required for network packet capture

7. Logging and Monitoring

7.1 Log Directory Structure

logs/
├── Sentinel_[timestamp]/
│   ├── sentinel_manager.log
│   ├── behavioral.log
│   ├── intrusion_detection.log
│   ├── adaptive_behavior_engine.log
│   ├── network_scan.log
│   └── network/
│       ├── net_scan_logs_[n].jsonl
│       └── net_signatures.txt
├── real_time/
│   └── RTS_[timestamp]/
│       └── graphing.log
├── graphs/
│   └── [various PNG outputs]
└── NetworkScan/
    └── net_signatures.json

7.2 Log Format

Standard Log Entry:

[YYYY-MM-DD HH:MM:SS] [GLYPH] (EVENT_TYPE) Message

JSONL Network Log Entry:

{
    "src": "192.168.1.1",
    "dst": "10.0.0.1",
    "vpn": false,
    "match": false,
    "proto": "IP / TCP 192.168.1.1:54321 > 10.0.0.1:80 S",
    "length": 64,
    "timestamp": "2025-05-05T12:34:56.789"
}

7.3 Graphing Outputs

- Entropy-Trust Plots: Comparison of Δ entropy and trust scores

- Network Activity Plots: Packet length visualization

- Entropy-Threat Plots: Combined threat assessment visualization

- Scan Overlay Images: Visual representation of scan results

8. Security Considerations

8.1 Data Protection

- All hashes stored locally (no external transmission)

- VPN detection uses external API with timeout limits

- No persistent storage of captured packet contents

8.2 Access Control

- Single-user desktop application model

- No built-in authentication mechanism

- Relies on OS-level access controls

8.3 Network Capture

- Requires administrative/root privileges

- Captures IP-layer traffic only

- Configurable network interface selection

9. Patent and Licensing

The software is protected under:

- U.S. Patent Pending: #63/796,404

- License Tier: ZADIE-SOVEREIGN

- Copyright: © 2025 Paul M. Roe / EnigmaticGlitch

- Trademark Indicators: SFI, RUM, PMR, UWC, ADO

The codebase includes proprietary symbolic interfaces and recursive mechanisms that are subject to intellectual property protection.

10. Technical Assessment Summary

10.1 Strengths

- Novel Mathematical Framework: The RHEA system introduces unique approaches to signal processing and entropy-based threat detection.

- Adaptive Architecture: Self-adjusting learning rates and thread governance enable responsive operation under varying loads.

- Multi-Vector Analysis: Combining Bayesian, entropy, and trust-based scoring provides robust threat assessment.

- Modular Design: Clean separation of concerns allows for component-level updates and testing.

- Real-Time Capabilities: Live monitoring and visualization support immediate threat response.

- CUDA Acceleration: Optional GPU support enables high-throughput signal generation.

- Comprehensive Logging: Structured logs support forensic analysis and compliance requirements.

10.2 Architectural Observations

- Mathematical Foundation: The system is built on principles from:

- Information Theory (Shannon entropy)

- Bayesian Statistics (likelihood functions)

- Signal Processing (wave-like regulation)

- Control Theory (homeostatic mechanisms)

- Recursive Design: Multiple feedback loops enable self-correction:

- Entropy tracking → Learning rate adjustment

- Threat scoring → Alert generation → Behavioral update

- Self-reflection → System diagnostic → Parameter tuning

- Symbolic Computation: The glyph-based state representation provides:

- Rapid visual identification

- Categorical event classification

- Stenographic capability in logs

10.3 Potential Applications

- Network Security Operations Centers (SOCs)

- Intrusion Detection Systems (IDS)

- Behavioral Analytics Platforms

- Security Research and Development

- Threat Intelligence Gathering

- Anomaly Detection Systems

11. Conclusion

ZADIEAN Sentinel RHEA-UCM v2.3.1 represents an innovative approach to cybersecurity monitoring, combining mathematical rigor with practical threat detection capabilities. The software's unique RHEA framework introduces concepts from signal processing and control theory into the security domain, while its modular architecture supports extensibility and maintenance.

The system's adaptive mechanisms—learning rate adjustment, thread governance, and self-reflection—enable autonomous operation with minimal manual intervention. Its multi-vector threat scoring provides a balanced approach to risk assessment that can be tuned to specific operational requirements.

As a patent-pending technology, the software represents intellectual property with potential commercial applications in enterprise security, managed security services, and cybersecurity research domains.

Document Generated: Analysis of ZADIEAN Sentinel RHEA-UCM v2.3.1 Review Coverage: Architecture, Algorithms, Features, Capabilities, Configuration Reference: U.S. Patent Pending #63/796,404
