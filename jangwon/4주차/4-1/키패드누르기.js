function solution(numbers, hand) {
  let answer = "";

  const location = (pos,num,lhand,rhand,hand) => {
      const lD = Math.abs(pos[lhand][0] - pos[num][0]) + Math.abs(pos[lhand][1] - pos[num][1]);
      const rD = Math.abs(pos[rhand][0] - pos[num][0]) + Math.abs(pos[rhand][1] - pos[num][1]);

      if(lD === rD) return hand === 'left' ? 'L' : 'R';
      return lD < rD ? 'L' : 'R';
  }

  const pos = {
      1:[0,0], 2: [0,1], 3: [0,2],
      4:[1,0], 5: [1,1], 6: [1,2],
      7:[2,0], 8: [2,1], 9: [2,2],
      '*': [3, 0], 0: [3, 1], '#': [3, 2]
  }

  let lhand = "*";
  let rhand = "#";

  for (let num of numbers){
      if (num % 3 === 1){
          answer += 'L';
          lhand = num;
      }

      else if (num !==0 && num % 3 === 0){
          answer += 'R';
          rhand = num;
      }
      else{
          answer += location(pos,num, lhand, rhand, hand)
          answer[answer.length-1] === 'L'? lhand = num : rhand = num;
      }
  }
  return answer
}