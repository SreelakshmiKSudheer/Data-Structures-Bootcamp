    {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Sets\n",
    "A **set** is an unordered collection of unique elements. Sets are mutable and support mathematical set operations such as union, intersection, difference, and more.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Creating Sets\n",
    "You can create a set using curly braces `{}` or the `set()` constructor.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({1, 2, 3, 4}, {3, 4, 5, 6}, set())"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set1 = {1, 2, 3, 4}\n",
    "set2 = set([3, 4, 5, 6])\n",
    "empty_set = set()  # Note: {} creates an empty dict, not a set\n",
    "\n",
    "set1, set2, empty_set\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Adding and Removing Elements\n",
    "- Use `.add()` to add an element.\n",
    "- Use `.remove()` to remove an element (raises error if not present).\n",
    "- Use `.discard()` to remove an element (does not raise error if absent).\n",
    "- Use `.pop()` to remove and return an arbitrary element.\n",
    "- Use `.clear()` to remove all elements.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, {3, 4}, set())"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = {1, 2, 3}\n",
    "s.add(4)          # Add 4\n",
    "s.remove(2)       # Remove 2\n",
    "s.discard(5)      # Try to discard 5 (no error)\n",
    "popped = s.pop()  # Remove and return an arbitrary element\n",
    "s_before_clear = s.copy()\n",
    "s.clear()         # Clear all elements\n",
    "\n",
    "popped, s_before_clear, s\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Union\n",
    "Combine elements from both sets, removing duplicates.\n",
    "- Operator: `|`\n",
    "- Method: `.union()`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({1, 2, 3, 4, 5}, {1, 2, 3, 4, 5})"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2, 3}\n",
    "B = {3, 4, 5}\n",
    "union_op = A | B\n",
    "union_method = A.union(B)\n",
    "union_op, union_method\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Intersection\n",
    "Elements common to both sets.\n",
    "- Operator: `&`\n",
    "- Method: `.intersection()`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({2, 3}, {2, 3})"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2, 3}\n",
    "B = {2, 3, 4}\n",
    "inter_op = A & B\n",
    "inter_method = A.intersection(B)\n",
    "inter_op, inter_method\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Difference\n",
    "Elements in one set but not the other.\n",
    "- Operator: `-`\n",
    "- Method: `.difference()`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({1, 2}, {1, 2})"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2, 3, 4}\n",
    "B = {3, 4, 5}\n",
    "diff_op = A - B\n",
    "diff_method = A.difference(B)\n",
    "diff_op, diff_method\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Symmetric Difference\n",
    "Elements in either set, but not in both.\n",
    "- Operator: `^`\n",
    "- Method: `.symmetric_difference()`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({1, 4}, {1, 4})"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2, 3}\n",
    "B = {2, 3, 4}\n",
    "sym_diff_op = A ^ B\n",
    "sym_diff_method = A.symmetric_difference(B)\n",
    "sym_diff_op, sym_diff_method\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Subset and Superset\n",
    "- `.issubset()` checks if all elements of one set are in another.\n",
    "- `.issuperset()` checks if one set contains all elements of another.\n",
    "- Operators: `<=` for subset, `>=` for superset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(True, True, True, True)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2}\n",
    "B = {1, 2, 3, 4}\n",
    "is_subset_method = A.issubset(B)\n",
    "is_superset_method = B.issuperset(A)\n",
    "is_subset_op = (A <= B)\n",
    "is_superset_op = (B >= A)\n",
    "is_subset_method, is_superset_method, is_subset_op, is_superset_op\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Disjoint Sets\n",
    "Two sets are disjoint if they have no elements in common.\n",
    "- Method: `.isdisjoint()`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(True, False)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = {1, 2}\n",
    "B = {3, 4}\n",
    "C = {2, 3}\n",
    "A.isdisjoint(B), A.isdisjoint(C)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Clearing a Set\n",
    "Use `.clear()` to remove all elements from a set.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = {1, 2, 3}\n",
    "s.clear()\n",
    "s\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Updating Sets In-Place\n",
    "These methods modify the set itself:\n",
    "- `.update()` — add multiple elements from another set or iterable\n",
    "- `.intersection_update()` — keep only elements found in another set\n",
    "- `.difference_update()` — remove elements found in another set\n",
    "- `.symmetric_difference_update()` — keep elements found in either set but not both\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4}, {1, 3, 6})"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = {1, 2, 3}\n",
    "s.update([3, 4, 5])\n",
    "after_update = s.copy()\n",
    "\n",
    "s.intersection_update({2, 3, 4})\n",
    "after_intersection_update = s.copy()\n",
    "\n",
    "s.difference_update({2})\n",
    "after_difference_update = s.copy()\n",
    "\n",
    "s.symmetric_difference_update({1, 4, 6})\n",
    "after_sym_diff_update = s\n",
    "\n",
    "after_update, after_intersection_update, after_difference_update, after_sym_diff_update\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}