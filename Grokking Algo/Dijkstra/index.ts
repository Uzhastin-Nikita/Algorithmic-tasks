type Graph = { [key: string]: { [key: string]: number } };

export const dijkstra = (
  graph: Graph,
  startNode: string
): { [key: string]: number } => {
  const distances: { [key: string]: number } = {};
  const visited: { [key: string]: boolean } = {};
  const queue: { node: string; distance: number }[] = [];

  for (const node in graph) {
    distances[node] = Infinity;
    visited[node] = false;
  }

  distances[startNode] = 0;
  queue.push({ node: startNode, distance: 0 });

  while (queue.length > 0) {
    const { node, distance } = queue.shift()!;
    visited[node] = true;

    for (const neighbor in graph[node]) {
      if (!visited[neighbor]) {
        const newDistance = distance + graph[node][neighbor];

        if (newDistance < distance[neighbor]) {
          distance[neighbor] = newDistance;
          queue.push({ node: neighbor, distance: newDistance });
        }
      }
    }
    queue.sort((a, b) => a.distance - b.distance);
  }

  return distances;
};
