function solution(A, B) {
    let result = 0;
    let idx = 0;
    A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
    
    for (let i = 0; i < A.length; i++) {
        if (A[idx] < B[i]) {
            result += 1;
            idx += 1;
        }
    }
    return result;
}