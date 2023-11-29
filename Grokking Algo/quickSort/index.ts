const quickSort = (arr) => {
  if (arr.length < 2) {
    return arr;
  }

  const pivot = arr[0];
  const { less, greater } = partition(arr.slice(1), pivot);

  return [...quickSort(less), pivot, ...quickSort(greater)];
};

const partition = (arr, pivot) => {
  return {
    less: arr.filter((element) => element <= pivot),
    greater: arr.filter((element) => element > pivot),
  };
};
