import time
from functools import wraps

class RateLimiter:
    """Simple rate limiter to avoid API limits"""
    
    def __init__(self, max_calls_per_minute=10):
        self.max_calls_per_minute = max_calls_per_minute
        self.calls = []
        
    def wait_if_needed(self):
        """Wait if we've made too many calls in the last minute"""
        now = time.time()
        
        # Remove calls older than 1 minute
        self.calls = [call_time for call_time in self.calls if now - call_time < 60]
        
        # If we've made too many calls, wait
        if len(self.calls) >= self.max_calls_per_minute:
            sleep_time = 60 - (now - self.calls[0]) + 1  # Wait until oldest call is > 1 minute old
            print(f"Rate limit reached. Waiting {sleep_time:.1f} seconds...")
            time.sleep(sleep_time)
            
        # Record this call
        self.calls.append(now)

def rate_limited(max_calls_per_minute=10):
    """Decorator to rate limit function calls"""
    limiter = RateLimiter(max_calls_per_minute)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            limiter.wait_if_needed()
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage example:
# @rate_limited(max_calls_per_minute=5)
# def api_call():
#     # Your API call here
#     pass