import threading
from .error_utils import ErrorReporter

class TimerBase:
    def __init__(self, callback, interval):
        self.callback = callback
        self.interval = interval
        self.timer = None
        self.is_active = False
        self._lock = threading.RLock()
    
    def start(self):
        with self._lock:
            if not self.is_active:
                self.is_active = True
                self._schedule_callback()
    
    def stop(self):
        with self._lock:
            if self.timer:
                self.timer.cancel()
            self.is_active = False
    
    def _schedule_callback(self):
        with self._lock:
            if self.is_active:
                self.timer = threading.Timer(self.interval, self._execute_and_reschedule)
                self.timer.daemon = True
                self.timer.start()
    
    def _execute_and_reschedule(self):
        try:
            self.callback()
        except Exception as e:
            ErrorReporter.report_error("Timer callback", e)
        self._schedule_callback()