# 📚 Python Algorithm Project

Welcome to the Python Algorithm Project! This repository contains a collection of algorithms implemented in Python, organized alphabetically by topic. Whether you're studying algorithms or just want to explore efficient solutions, this project provides an extensive library to learn from! 🎉

## 🌟 Project Structure

Each algorithm is implemented in its own Python file, and the code is organized alphabetically. This way, you can easily navigate and find algorithms based on their first letter.

## 📋 Table of Contents

- **A** 📐 Algorithms starting with "A"
- **B** 📊 Algorithms starting with "B"
- **C** 🎲 Algorithms starting with "C"
- **D** 📏 Algorithms starting with "D"
- **...** (and so on)
- **T** 🔢 Algorithms starting with "T"
  - [two_sum](#-two_sum)

---

### T 🔢

#### two_sum

The `two_sum` algorithm takes an array and a target value and finds two numbers within the array that add up to the target. It offers both a brute-force solution and a hash-map-based optimized solution.

```python
def two_sum(arr, target):
    count = {}
    for i in range(len(arr)):
        needed_val = target - arr[i]
        if needed_val in count:
            return [count[needed_val], i]
        count[arr[i]] = i
    return -1
```
