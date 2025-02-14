if __name__ == '__main__':
    n = int(input())
    arr = list (map(int, input().split()))


sorted_arr = list(set(sorted(arr)))

second_largest = sorted_arr[-2]

print(second_largest)