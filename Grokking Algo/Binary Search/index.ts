export const binarySearch = (list, item) => {
    const NOT_FOUND = -1;
  
    let low = 0;
    let high = list.length - 1;
    let mid, guess;
  
    while (low <= high) {
      mid = Math.floor((low + high) / 2);
      guess = list[mid];
  
      if (guess === item) {
        return mid;
      } else if (guess > item) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
  
    return NOT_FOUND;
  };
  