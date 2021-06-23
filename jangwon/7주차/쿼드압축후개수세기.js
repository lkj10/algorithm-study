function solution(arr) {
  const aux = (rs, re, cs, ce) => {
    if (rs === re) {
      return String(arr[rs][cs]);
    }

    const rowMid = Math.floor((rs + re) / 2);
    const colMid = Math.floor((cs + ce) / 2);

    const leftUpper = aux(rs, rowMid, cs, colMid);
    const rightUpper = aux(rowMid + 1, re, cs, colMid);
    const leftLower = aux(rs, rowMid, colMid + 1, ce);
    const rightLower = aux(rowMid + 1, re, colMid + 1, ce);

    const result = leftUpper + rightUpper + leftLower + rightLower;
    if (result === '0000' || result === '1111') return leftUpper;
    else return result;
  };

  const compressed = aux(0, arr.length - 1, 0, arr.length - 1);
  const numOfOne = compressed.split('').filter((c) => c === '1').length;
  return [compressed.length - numOfOne, numOfOne];
}

function solution(arr) {
    const answer = [0, 0];
    const n = arr.length;
    
    const aux = (x, y, n) => {
        const init = arr[x][y];
        for(let i = x; i < x + n; i++) {
            for (let j = y; j < y + n; j++) {
                if (arr[i][j] !== init) {
                    const div = parseInt(n / 2);
                    aux(x, y, div);
                    aux(x, y + div, div);
                    aux(x + div, y, div);
                    aux(x + div, y + div, div);
                    return;
                }
            }
        }
        answer[init] += 1;
    }
    
    aux(0, 0, n);
    return answer;    
}