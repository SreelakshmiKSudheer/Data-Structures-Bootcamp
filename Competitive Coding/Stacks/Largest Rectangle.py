def largestRectangle(heights):
    """
    Calculates the area of the largest rectangle that can be formed in a histogram.
    Args:
        heights (List[int]): A list of non-negative integers representing the heights of histogram bars.
    Returns:
        int: The area of the largest rectangle that can be formed within the histogram.
    Example:
        >>> largestRectangle([2, 1, 5, 6, 2, 3])
        10
    Notes:
        - The function uses a stack-based approach to efficiently compute the largest rectangle area in O(n) time.
        - The input list is modified by appending a zero at the end to ensure all bars are processed.
    """
    # Write your code here
    stack = []  # Stack to store indices of histogram bars
    maxArea = 0  # Variable to keep track of the maximum area found
    heights = heights + [0]  # Create a copy of the list and append a zero to process all bars in the histogram

    for i, h in enumerate(heights):  # Iterate through each bar in the histogram
        # While the current bar is lower than the bar at the stack's top
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]  # Pop the top and get its height
            # Calculate the width of the rectangle
            width = i if not stack else i - stack[-1] - 1
            # Update maxArea if the current area is larger
            maxArea = max(maxArea, height * width)
        stack.append(i)  # Push current index to the stack

    return maxArea  # Return the largest rectangle area found