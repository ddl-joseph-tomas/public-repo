def run_job(success=True):
    if success:
        print("Job works!")
    else:
        print("Job doesn't work.")

# Example usage:
run_job(True)   # prints: Job works!
run_job(False)  # prints: Job doesn't work.
