import { factorial } from "./index";
import '@types/jest'

describe('factorial', () => {
    it('factorial with simple number', () => {
        // Arrange
        const x = 0;

        // Act
        const result = factorial(x);

        // Assert
        expect(result).toBe(1)
    }) 
})