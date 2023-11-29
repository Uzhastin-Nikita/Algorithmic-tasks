export const factorial = (x) => {
    if (x === 0 || x === 1) {
        return x;
    } else {
        return x * factorial(x-1)
    }
}
