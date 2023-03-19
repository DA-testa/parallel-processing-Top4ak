# 221RDB014 Mihails Ruhļa 13. grupa

def parallel_processing(num_threads, num_jobs, job_times):
    output = []
    thread_finish_times = [0] * num_threads
    for job_idx in range(num_jobs):
        earliest_finish_time = thread_finish_times[0]
        earliest_finish_thread = 0
        for thread_idx in range(1, num_threads):
            if thread_finish_times[thread_idx] < earliest_finish_time:
                earliest_finish_time = thread_finish_times[thread_idx]
                earliest_finish_thread = thread_idx
        output.append((earliest_finish_thread, earliest_finish_time))
        thread_finish_times[earliest_finish_thread] += job_times[job_idx]
        
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
