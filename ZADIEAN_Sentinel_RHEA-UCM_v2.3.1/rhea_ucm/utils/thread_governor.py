# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ ⌬ ZADEIAN-RHEA Sentinel v2.3.1                                          ║
# ║ ⌬ File: /rhea_ucm/utils/thread_governor.py                              ║
# ║ ⌬ Description: Dynamic Thread Governor — Scales Threads via GPU Load   ║
# ║ ⌬ Author: EnigmaticGlitch · © 2025 · All Rights Reserved               ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import threading
import time
import logging

try:
    import pynvml
    pynvml.nvmlInit()
    GPU_AVAILABLE = True
except Exception:
    GPU_AVAILABLE = False


class ThreadGovernor:
    def __init__(self, max_threads=10, min_threads=1, safe_load=70, adjust_function=None):
        self.logger = logging.getLogger("ThreadGovernor")
        self.max_threads = max_threads
        self.min_threads = min_threads
        self.safe_load = safe_load
        self.adjust_function = adjust_function
        self.current_threads = min_threads
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._govern_loop, daemon=True)
        self._thread.start()

    def _get_gpu_utilization(self):
        if not GPU_AVAILABLE:
            raise RuntimeError("GPU metrics unavailable")
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            util = pynvml.nvmlDeviceGetUtilizationRates(handle)
            return util.gpu  # in percent
        except Exception as e:
            self.logger.warning(f"[✖ GPU] Utilization fetch error: {e}")
            return None

    def _govern_loop(self):
        while not self._stop_event.is_set():
            try:
                if GPU_AVAILABLE:
                    gpu_load = self._get_gpu_utilization()
                    if gpu_load is not None:
                        ideal = int((1 - gpu_load / 100) * self.max_threads)
                        ideal = max(self.min_threads, min(ideal, self.max_threads))
                        if ideal != self.current_threads:
                            self.logger.info(f"[🧠 THREAD GOV] GPU Load: {gpu_load}% → Threads: {ideal}")
                            self.current_threads = ideal
                            if self.adjust_function:
                                self.adjust_function(ideal)
                    else:
                        self.current_threads = self.min_threads
                else:
                    self.logger.warning("[☣] GPU metrics unavailable — defaulting to static threads")
                    self.current_threads = self.min_threads
            except Exception as e:
                self.logger.error(f"[✖ GOVERNOR] Error: {e}")
                self.current_threads = self.min_threads
            time.sleep(5)

    def get_thread_count(self):
        return self.current_threads

    def stop(self):
        self._stop_event.set()
        self._thread.join(timeout=2)


# Optional test mode
if __name__ == "__main__":
    def mock_adjust(n): print(f"[Mock] Adjusted to {n} threads")
    gov = ThreadGovernor(adjust_function=mock_adjust)
    try:
        for _ in range(10):
            print(f"Current threads: {gov.get_thread_count()}")
            time.sleep(2)
    finally:
        gov.stop()