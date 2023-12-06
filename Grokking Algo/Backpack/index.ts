interface Item {
  weight: number;
  value: number;
}

function knapsackGreedy(items: Item[], capacity: number): number {
  const sortedItems = items.sort(
    (a, b) => b.value / b.weight - a.value / a.weight
  );

  let currentWeight = 0;
  let totalValue = 0;

  for (const item of sortedItems) {
    if (currentWeight + item.weight <= capacity) {
      currentWeight += item.weight;
      totalValue += item.value;
    } else {
      const remainingCapacity = capacity - currentWeight;
      totalValue += (remainingCapacity / item.weight) * item.value;
      break;
    }
  }

  return totalValue;
}
