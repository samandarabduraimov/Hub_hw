if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
runner_up_arr = sorted(set(arr))[-2]

# Print the runner-up score
print(runner_up_arr)