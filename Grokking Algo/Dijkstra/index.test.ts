import { dijkstra } from "./index";
import "@types/jest";

describe("Dijkstra's Algorithm", () => {
  test("should find the shortest distances in a simple graph", () => {
    // Arrange
    const graph = {
      A: { B: 1, C: 4 },
      B: { A: 1, C: 2, D: 5 },
      C: { A: 4, B: 2, D: 1 },
      D: { B: 5, C: 1 },
    };

    // Act
    const result = dijkstra(graph, "A");

    // Assert
    expect(result).toEqual({
      A: 0,
      B: 1,
      C: 3,
      D: 4,
    });
  });

  test("should handle an empty graph", () => {
    // Arrange
    const graph = {};

    // Act
    const result = dijkstra(graph, "A");

    // Assert
    expect(result).toEqual({});
  });

  test("should handle a graph with a single node", () => {
    // Arrange
    const graph = { A: {} };

    // Act
    const result = dijkstra(graph, "A");

    // Assert
    expect(result).toEqual({ A: 0 });
  });
});
