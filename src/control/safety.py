import threading
import time

class EmergencyStopHandler:
    def __init__(self, callback):
        self.triggered = False
        self.callback = callback
        self._monitor_thread = None
        self._running = False

    def trigger(self):
        self.triggered = True
        if self.callback:
            self.callback()
            
    def reset(self):
        self.triggered = False

    def start_hardware_monitor(self):
        # Stub for GPIO hardware interrupt monitoring
        self._running = True
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()

    def stop_hardware_monitor(self):
        self._running = False

    def _monitor_loop(self):
        while self._running:
            # Poll hardware pin here (stub)
            time.sleep(0.1)
