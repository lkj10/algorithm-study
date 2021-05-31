function solution(board, moves) {
  let result = 0;
  let stack = [];
  moves.forEach((pos)=>{
      for(let i=0; i<board.length; i++) {
          if(board[i][pos-1] !== 0) {
              let top = stack.length -1;
              let tmp = board[i][pos-1];
              board[i][pos-1] = 0;
              if(stack[top] === tmp) {
                  stack.pop();
                  result += 2;
              } else stack.push(tmp);
              break;
          }
      }
  })

  return result;
}