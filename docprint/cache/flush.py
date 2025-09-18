from ..config.constants import CACHE_FLUSH_INTERVAL
from ..utils.timer_base import TimerBase

class FlushController:
    def __init__(self, cache_manager):
        self.cache_manager = cache_manager
        self.timer_base = TimerBase(self._flush_callback, CACHE_FLUSH_INTERVAL)
    
    def start_timer(self):
        self.timer_base.start()
    
    def stop_timer(self):
        self.timer_base.stop()
    
    def _flush_callback(self):
        if self.cache_manager:
            self.cache_manager.flush()