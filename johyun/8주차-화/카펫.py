def solution(brown, yellow):
    total = brown + yellow

    for idx in range(1, yellow + 1):
        if yellow % idx == 0:
            y_height = idx  # 노랑이 세로길이
            y_length = yellow // idx
            if brown == (y_length + 2) * (y_height + 2) - yellow:
                print(y_length + 2, y_height + 2)
                return (y_length + 2, y_height + 2)

