def fixed_window(arr, k):
    window_sum = sum(arr[:k])  # Khởi tạo window đầu tiên
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Slide: bỏ phần tử đầu, thêm phần tử mới
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
