# Modular Arithmetic

#### In this post I'll keep some useful notes and scripts that can be used to solve problems regarding Modular Arithmetic

## Greatest Common Divisor

> CryptoHack

The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers $(a, b)$.

For $a = 12, b = 8$ we can calculate the divisors of $a$: $\{1, 2, 3, 4, 6, 12\}$ and the divisor of $b$: $\{1, 2, 4, 8\}$. Comparing these two we see that $gcd(a,b) = 4$

> GeeksForGeeks

![image](https://github.com/user-attachments/assets/79b14d76-f84f-4241-ab0d-007a30dfed19)

**Basic Euclidean Algorithm for GCD:** 
The algorithm is based on the below facts. 

- If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
- Now instead of subtraction, if we divide the larger number, the algorithm stops when we find the remainder 0.

```python
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
```

