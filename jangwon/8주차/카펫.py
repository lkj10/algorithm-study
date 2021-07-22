def solution(brown, yellow):
    space = brown + yellow
    
    # 약수 
    for i in range(brown, 0, -1):
        w = i
        h = space / i
        target = (w - 2) * (h - 2)
        
        if target == yellow:
            return [w, h]