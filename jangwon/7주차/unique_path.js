// https://leetcode.com/problems/unique-paths/

// brute force // timeout
const uniquePaths = (m, n) => {
    return helper(m, n, 1, 1);
};

const helper = (m, n, row, col) => {
    if(row === m && col === n) return 1;
    if(row > m || col > n) return 0;
    
    const pathsRight = helper(m, n, row, col + 1);
    const pathsDown = helper(m, n, row + 1, col);
    
    return pathsRight + pathsDown;
};



// memoization // optimization
const uniquePaths = (m, n) => {
  const memo = Array.from({ length: m + 1 }, () => Array.from({ length: n + 1 }, () => -1));
  return helper(m, n, 1, 1, memo);
};

const helper = (m, n, row, col, memo) => {
    if(row === m && col === n) return 1;
    if(row > m || col > n) return 0;
    
    if(memo[row][col] === -1) {
    
        const pathsRight = helper(m, n, row, col + 1, memo);
        const pathsDown = helper(m, n, row + 1, col, memo);
        
        console.log(pathsRight, pathsDown)
        memo[row][col] = pathsRight + pathsDown;
    }
    
    return memo[row][col];
};