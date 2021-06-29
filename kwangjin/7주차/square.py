def solution(w,h):
    
    def GCD(x, y):
        return y if x % y == 0 else GCD(y, x % y)
    
    return w * h - (w + h - GCD(w, h))