export const sum = (arr, index = 0) => {
  if (index === arr.length) {
    return 0;
  } else {
    return arr[index] + sum(arr, index + 1);
  }
};
