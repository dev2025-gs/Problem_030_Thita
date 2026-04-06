# Flood Fill

🔗 Problem Link: https://thita.ai/problems/flood-fill

---

## 🧠 Problem Description

You are given a 2D grid `image` of size `m x n`, where each cell represents a pixel value. You are also given three integers:

- `sr` (start row)
- `sc` (start column)
- `color` (new color)

Your task is to perform a **flood fill** starting from the pixel at `(sr, sc)`.

### Flood Fill Rules:

1. Change the starting pixel's color to `color`.
2. Recursively (or iteratively) update all **adjacent pixels** (up, down, left, right) that:
   - Have the **same original color** as the starting pixel.
3. Continue this process until no more valid adjacent pixels remain.

Return the modified image.

---

## ✨ Examples

### Example 1

**Input:**

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1
color = 2


**Output:**

[[2,2,2],[2,2,0],[2,0,1]]

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(m * n)`  
  Each pixel in the grid is visited at most once during the traversal.

- **Space Complexity:** `O(m * n)`  
  In the worst case, the recursion stack (DFS) or queue (BFS) can grow to include all pixels.

---

## 🚀 Key Takeaways

- Flood Fill is a classic **graph traversal problem** on a 2D grid.
- Both **DFS** and **BFS** approaches work effectively.
- Always check if the starting pixel already has the target color to avoid unnecessary processing.
- Be careful with boundary conditions to prevent index errors.
- The problem is essentially about finding and updating a **connected component**.

---

## 🏁 Summary

Flood Fill works by exploring all pixels connected to a starting point that share the same value. Using DFS or BFS, we systematically update each valid neighboring pixel until the entire connected region is filled with the new color. This problem is a fundamental example of grid-based traversal and appears frequently in image processing and graph-related tasks.

---

