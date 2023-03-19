# 221RDB014 Mihails Ruhļa 13. grupa

def parallel_processing(n, m, data):
    output = []
    next = [(0, i) for i in range(n)]
    for work in data:
        min_index = 0
        for i in range(1, n):
            if next[i][0] < next[min_index][0]:
                min_index = i
        thread, st = next[min_index]
        output.append((thread, st))
        next[min_index] = (st + work, thread)
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
