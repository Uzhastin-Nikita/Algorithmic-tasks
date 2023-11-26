import { binarySearch } from "./index";
import '@types/jest'

describe('binarySearch', () => {
  it('finds an element in the middle of the array', () => {
    const sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const target = 5;
    expect(binarySearch(sortedList, target)).toBe(4);
  });

  it('finds an element at the beginning of the array', () => {
    const sortedList = [10, 20, 30, 40, 50];
    const target = 10;
    expect(binarySearch(sortedList, target)).toBe(0);
  });

  it('finds an element at the end of the array', () => {
    const sortedList = [10, 20, 30, 40, 50];
    const target = 50;
    expect(binarySearch(sortedList, target)).toBe(4);
  });

  it('does not find a missing element', () => {
    const sortedList = [1, 2, 3, 4, 5];
    const target = 10;
    expect(binarySearch(sortedList, target)).toBe(-1);
  });

  it('handles an empty array', () => {
    const sortedList = [];
    const target = 10;
    expect(binarySearch(sortedList, target)).toBe(-1);
  });
});
