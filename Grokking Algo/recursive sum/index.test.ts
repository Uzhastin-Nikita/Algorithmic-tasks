
import { sum } from './index'

describe("sum function", () => {
  it("should return 0 for an empty array", () => {
    expect(sum([])).toBe(0);
  });

  it("should return the sum of elements in the array", () => {
    expect(sum([1, 2, 3, 4, 5])).toBe(15);
  });

  it("should handle arrays with negative numbers", () => {
    expect(sum([-1, -2, -3, -4, -5])).toBe(-15);
  });

  it("should return 0 if all elements in the array are 0", () => {
    expect(sum([0, 0, 0, 0, 0])).toBe(0);
  });

  it("should handle arrays with a single element", () => {
    expect(sum([42])).toBe(42);
  });

  it("should handle large arrays", () => {
    const arr = Array.from({ length: 100 }, (_, i) => i + 1);
    expect(sum(arr)).toBe(5050);
  });
});
