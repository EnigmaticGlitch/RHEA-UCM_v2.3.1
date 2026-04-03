# benchmark/benchmark_runner.py

import time
from rhea_ucm.interpreter import RHEAInterpreter

class BenchmarkRunner:
    def __init__(self):
        self.rhea = RHEAInterpreter()

    def benchmark_pulse_speed(self, iterations=1000):
        """
        Benchmark how fast RHEA can generate Ψ pulses.
        Returns list of computation times (seconds).
        """
        times = []
        for _ in range(iterations):
            start = time.perf_counter()
            self.rhea.psi()
            end = time.perf_counter()
            elapsed = end - start
            times.append(elapsed)
        return times

    def benchmark_entropy_reaction(self, iterations=1000):
        """
        Benchmark how fast RHEA can react to ∆ entropy changes.
        Returns list of computation times (seconds).
        """
        times = []
        for _ in range(iterations):
            value = self.rhea.psi()
            start = time.perf_counter()
            self.rhea.delta(value)
            end = time.perf_counter()
            elapsed = end - start
            times.append(elapsed)
        return times

    def benchmark_regulation_speed(self, iterations=1000):
        """
        Benchmark how fast RHEA can perform regulation.
        Returns list of computation times (seconds).
        """
        times = []
        for _ in range(iterations):
            value = self.rhea.psi()
            start = time.perf_counter()
            self.rhea.reg(value)
            end = time.perf_counter()
            elapsed = end - start
            times.append(elapsed)
        return times

    def describe_benchmarks(self):
        """
        Provide user-friendly descriptions for each benchmark.
        """
        descriptions = {
            "Ψ Pulse Speed": "✪ Measures how fast the system generates new Ψ signals (pulse events).",
            "∆ Entropy Reaction Speed": "⚡ Measures how fast the system reacts to entropy changes (self-stabilization).",
            "Regulation Speed": "🌬️ Measures how quickly homeostatic corrections are applied."
        }
        return descriptions
