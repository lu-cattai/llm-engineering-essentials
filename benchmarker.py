import time
import psutil
import os
import functools

def profile_performance(func):
    """
    Decorator to monitor latency and memory footprint (RSS).
    Used to validate performance gains in C++/Python refactoring.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        
        # Baseline memory usage
        mem_before = process.memory_info().rss / 1024 / 1024
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        # Post-execution metrics
        end_time = time.perf_counter()
        mem_after = process.memory_info().rss / 1024 / 1024
        
        print("-" * 40)
        print(f"📊 PERFORMANCE REPORT: {func.__name__}")
        print(f"⏱️ Latency (Total): {end_time - start_time:.4f} seconds")
        print(f"🧠 Memory Delta: {mem_after - mem_before:.2f} MB")
        print(f"📍 Peak RSS Usage: {mem_after:.2f} MB")
        print("-" * 40)
        return result
    return wrapper

@profile_performance
def simulate_inference_pipeline():
    print("Simulating weights loading and model inference...")
    # Stress test: allocation of 1M elements
    stress_buffer = [x for x in range(1000000)] 
    time.sleep(0.8)
    return "Inference Logic Executed"

if __name__ == "__main__":
    simulate_inference_pipeline()