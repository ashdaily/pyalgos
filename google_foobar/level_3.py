def solution(start, length):
    ids = [i for i in range(start, start+(length**2))]
    matrix = []
    for idx, value in enumerate(ids):
        if (idx+1)%length == 0:
            batch = ids[idx-length+1:idx+1]
            matrix.append(batch)
    
    max_idx = length - 1
    result = None
    for arr_idx, arr in enumerate(matrix):
        for element_idx, element in enumerate(arr):
            if element_idx <= max_idx:
                if result is None:
                    result = element
                else:
                    result ^= element
        max_idx -= 1
    return result