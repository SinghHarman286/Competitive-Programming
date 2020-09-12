// Colt's Solution

function countUniqueValues(arr) {
  let i = 0;

  for(j = 1; j < arr.length; j++) {
    if(arr[i] !== arr[j]) {
        i++;
        arr[i] == arr[j];
    }
    j++;
  }

  return i+1;
}


function countUniqueValues(arr){
  // add whatever parameters you deem necessary - good luck!
  let first = 0;
  let second = 1;
  let length_arr = arr.length;
  let count = 0;
  
  if(length_arr === 0) {
      return 0;
  }
  
  while(second <= length_arr) {
      if(arr[first] !==  arr[second]) {
          count++;
      }
      first++;
      second++;
  }
  return count;
}