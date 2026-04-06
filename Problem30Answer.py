from collections import deque
def floodFill(self, image, sr, sc, color):
        """
        Performs a flood fill on a 2D image starting from (sr, sc).
        Changes the color of the starting pixel and all connected pixels of the same color to the new color.
        Uses Breadth-First Search (BFS) for traversal.
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # If the starting pixel already has the new color, no need to proceed
        if image[sr][sc] == color:
            return image

        # Direction vectors for traversing up, down, right, and left
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()  # Initialize a queue for BFS
        oldColor = image[sr][sc]  # Store the original color to be replaced
        q.append((sr, sc))  # Start BFS from the given starting pixel

        # Change the color of the starting pixel to the new color
        image[sr][sc] = color

        # Perform BFS to fill all connected pixels of the same color
        while q:
            x, y = q.popleft()  # Get the next pixel to process

            # Traverse all 4 possible directions from the current pixel
            for dx, dy in dir:
                nx = x + dx  # Calculate new x-coordinate
                ny = y + dy  # Calculate new y-coordinate

                # Check if the new coordinates are within bounds and match the old color
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == oldColor:
                    image[nx][ny] = color  # Change color to the new color
                    q.append((nx, ny))  # Add the pixel to the queue for further processing

        # Return the modified image after flood fill
        return image