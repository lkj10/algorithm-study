// DFS 풀이 
let result = Infinity;
let check = [];

const diff = (word1, word2) => {
    let diffNumber = 0;
    for (let i = 0; i< word1.length; i++) {
        if (word1[i] !== word2[i]) diffNumber += 1;
    }
    
    return diffNumber === 1 ? true : false;
};

const dfs = (begin, target, words, depth, check) => {
  if (begin == target && result > depth) {
    result = depth;
    return;
  } else {
      for (let i = 0; i < words.length; i++) {
        if (!check[i] && diff(begin, words[i])) {
          depth += 1;
          check[i] = true;
          dfs(words[i], target, words, depth, check);
          check[i] = false;
          depth -= 1;
        }
     }
  }
};

const solution = (begin, target, words) => {
    // 예외 처리
    if (!words.includes(target)) return 0;
    
    // 방문 함수 생성
    words.forEach((_, idx) => check[idx] = false);
    dfs(begin, target, words, 0, check);
    return result === Infinity ? 0 : result;
};