#!/usr/bin/env python
# coding: utf-8

# In[20]:


# NAME: KOLAWOLE INIOLUWA ENOCH 
# MATRICULATION NUMBER: VUG/CSC/22/6970
# COURSE TITLE: CSC 333 Computational science and Numeriacal Methods 
# Lab Assignment 1


# In[24]:


#Number 1
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE 
            Z = 3x_A + 4x_B
SUBJECT TO

            2x_A + 3x_B ≤ 12
            x_A + 2x_B ≤ 8
            x_A ≥ 0, x_B ≥ 0 (non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 10, 400)

# Constraint 1: 2x_A + 3x_B ≤ 12 → x_B = (12 - 2x_A) / 3
y1 = (12 - 2 * x_A) / 3

# Constraint 2: x_A + 2x_B ≤ 8 → x_B = (8 - x_A) / 2
y2 = (8 - x_A) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 12 / 3),  # Intersection with y-axis for y1
    (8, 0),  # Intersection with x-axis for y2
    (6, 0)  # Intersection of y1 and the x-axis
]

# Calculate the profit Z = 3x_A + 4x_B at each corner point
profits = [3 * x + 4 * y for x, y in corner_points]
optimal_index = np.argmax(profits)
optimal_point = corner_points[optimal_index]
optimal_profit = profits[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$2x_A + 3x_B \leq 12$', color='blue')
plt.plot(x_A, y2, label=r'$x_A + 2x_B \leq 8$', color='green')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, Z={optimal_profit}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('$x_A$')
plt.ylabel('$x_B$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method with Optimal Solution')

plt.show()


# In[22]:


#Number 2
import numpy as np
import matplotlib.pyplot as plt

"""
MINIMIZE
            C = 2x_X + 5x_Y
SUBJECT TO

            x_X + 2x_Y ≥ 6  (Labor constraint)
            2x_X + x_Y ≥ 5  (Material constraint)
            x_X ≥ 0, x_Y ≥ 0 (non-negativity constraints)
"""

# Define the constraints
x_X = np.linspace(0, 4, 400)  # Adjust range for better visibility

# Constraint 1: x_X + 2x_Y ≥ 6 → x_Y = (6 - x_X) / 2
y1 = (6 - x_X) / 2

# Constraint 2: 2x_X + x_Y ≥ 5 → x_Y = 5 - 2 * x_X
y2 = 5 - 2 * x_X

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (2.5, 0),  # Intersection with x-axis for y2
    (0, 3),  # Intersection with y-axis for y1
    (2, 2),  # Intersection of y1 and y2
]

# Calculate the cost C = 2x_X + 5x_Y at each corner point
costs = [2 * x + 5 * y for x, y in corner_points]
optimal_index = np.argmin(costs)  # Minimization
optimal_point = corner_points[optimal_index]
optimal_cost = costs[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_X, y1, label=r'$x_X + 2x_Y \geq 6$', color='blue')
plt.plot(x_X, y2, label=r'$2x_X + x_Y \geq 5$', color='green')

# Shade the feasible region
plt.fill_between(x_X, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')


# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, C={optimal_cost}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.xlabel('$x_X$')
plt.ylabel('$x_Y$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Minimizing Cost')

plt.show()


# In[ ]:


#Number 3
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            P = 5x_A + 4x_B
SUBJECT TO

            2x_A + x_B ≤ 20  (Labor constraint)
            3x_A + 2x_B ≤ 30  (Material constraint)
            x_A + 2x_B ≤ 18  (Machine time constraint)
            x_A ≥ 0, x_B ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 20, 400)  # Adjust range for visibility

# Constraint 1: 2x_A + x_B ≤ 20 → x_B = 20 - 2x_A
y1 = 20 - 2 * x_A

# Constraint 2: 3x_A + 2x_B ≤ 30 → x_B = (30 - 3x_A) / 2
y2 = (30 - 3 * x_A) / 2

# Constraint 3: x_A + 2x_B ≤ 18 → x_B = (18 - x_A) / 2
y3 = (18 - x_A) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 10),  # Intersection with y-axis for y1
    (6, 8),  # Intersection of y2 and y3
    (9, 0),  # Intersection with x-axis for y3
    (10, 0),  # Intersection with x-axis for y1
]

# Calculate the profit P = 5x_A + 4x_B at each corner point
profits = [5 * x + 4 * y for x, y in corner_points]
optimal_index = np.argmax(profits)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_profit = profits[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$2x_A + x_B \leq 20$', color='blue')
plt.plot(x_A, y2, label=r'$3x_A + 2x_B \leq 30$', color='green')
plt.plot(x_A, y3, label=r'$x_A + 2x_B \leq 18$', color='purple')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, P={optimal_profit}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel('$x_A$ (Product A)')
plt.ylabel('$x_B$ (Product B)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Profit')

plt.show()


# In[26]:


#Number 4
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            P = 5x_A + 4x_B
SUBJECT TO

            2x_A + x_B ≤ 20  (Labor constraint)
            3x_A + 2x_B ≤ 30  (Material constraint)
            x_A + 2x_B ≤ 18  (Machine time constraint)
            x_A ≥ 0, x_B ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 20, 400)  # Adjust range for visibility

# Constraint 1: 2x_A + x_B ≤ 20 → x_B = 20 - 2x_A
y1 = 20 - 2 * x_A

# Constraint 2: 3x_A + 2x_B ≤ 30 → x_B = (30 - 3x_A) / 2
y2 = (30 - 3 * x_A) / 2

# Constraint 3: x_A + 2x_B ≤ 18 → x_B = (18 - x_A) / 2
y3 = (18 - x_A) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 10),  # Intersection with y-axis for y1
    (6, 8),  # Intersection of y2 and y3
    (9, 0),  # Intersection with x-axis for y3
    (10, 0),  # Intersection with x-axis for y1
]

# Calculate the profit P = 5x_A + 4x_B at each corner point
profits = [5 * x + 4 * y for x, y in corner_points]
optimal_index = np.argmax(profits)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_profit = profits[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$2x_A + x_B \leq 20$', color='blue')
plt.plot(x_A, y2, label=r'$3x_A + 2x_B \leq 30$', color='green')
plt.plot(x_A, y3, label=r'$x_A + 2x_B \leq 18$', color='purple')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, P={optimal_profit}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel('$x_A$ (Product A)')
plt.ylabel('$x_B$ (Product B)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Profit')

plt.show()


# In[ ]:


#Number 5
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            R = 4x_A + 5x_B
SUBJECT TO

            x_A + 2x_B ≤ 20  (Advertising budget constraint)
            x_A + 2x_B ≤ 15  (Production capacity constraint)
            x_A ≥ 0, x_B ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 20, 400)  # Adjust range for visibility

# Constraint 1: x_A + 2x_B ≤ 20 → x_B = (20 - x_A) / 2
y1 = (20 - x_A) / 2

# Constraint 2: x_A + 2x_B ≤ 15 → x_B = (15 - x_A) / 2
y2 = (15 - x_A) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 7.5),  # Intersection with y-axis for y2
    (10, 5),  # Intersection of y1 and y2
    (20, 0),  # Intersection with x-axis for y1
]

# Calculate the revenue R = 4x_A + 5x_B at each corner point
revenues = [4 * x + 5 * y for x, y in corner_points]
optimal_index = np.argmax(revenues)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_revenue = revenues[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$x_A + 2x_B \leq 20$', color='blue')
plt.plot(x_A, y2, label=r'$x_A + 2x_B \leq 15$', color='green')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, R={optimal_revenue}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 22)
plt.ylim(0, 12)
plt.xlabel('$x_A$ (Product A)')
plt.ylabel('$x_B$ (Product B)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Revenue')

plt.show()


# In[ ]:


#Number 6
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            P = 8x_P1 + 7x_P2
SUBJECT TO

            3x_P1 + 4x_P2 ≤ 12  (Labor hours constraint)
            2x_P1 + x_P2 ≤ 6    (Capital constraint)
            x_P1 ≥ 0, x_P2 ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_P1 = np.linspace(0, 6, 400)  # Adjust range for visibility

# Constraint 1: 3x_P1 + 4x_P2 ≤ 12 → x_P2 = (12 - 3x_P1) / 4
y1 = (12 - 3 * x_P1) / 4

# Constraint 2: 2x_P1 + x_P2 ≤ 6 → x_P2 = 6 - 2x_P1
y2 = 6 - 2 * x_P1

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 3),  # Intersection with y-axis for y2
    (4, 0),  # Intersection with x-axis for y2
    (2, 1.5),  # Intersection of y1 and y2
]

# Calculate the profit P = 8x_P1 + 7x_P2 at each corner point
profits = [8 * x + 7 * y for x, y in corner_points]
optimal_index = np.argmax(profits)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_profit = profits[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_P1, y1, label=r'$3x_P1 + 4x_P2 \leq 12$', color='blue')
plt.plot(x_P1, y2, label=r'$2x_P1 + x_P2 \leq 6$', color='green')

# Shade the feasible region
plt.fill_between(x_P1, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, P={optimal_profit}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 5)
plt.ylim(0, 4)
plt.xlabel('$x_{P1}$ (Units of Project P1)')
plt.ylabel('$x_{P2}$ (Units of Project P2)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Profit')

plt.show()


# In[ ]:


#Number 7
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            P = 5x_C + 3x_V
SUBJECT TO

            x_C + 2x_V ≤ 8  (Baking time constraint)
            3x_C + 2x_V ≤ 12 (Flour constraint)
            x_C ≥ 0, x_V ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_C = np.linspace(0, 8, 400)  # Adjust range for visibility

# Constraint 1: x_C + 2x_V ≤ 8 → x_V = (8 - x_C) / 2
y1 = (8 - x_C) / 2

# Constraint 2: 3x_C + 2x_V ≤ 12 → x_V = (12 - 3x_C) / 2
y2 = (12 - 3 * x_C) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 4),  # Intersection with y-axis for y2
    (4, 2),  # Intersection of y1 and y2
    (8, 0),  # Intersection with x-axis for y1
]

# Calculate the profit P = 5x_C + 3x_V at each corner point
profits = [5 * x + 3 * y for x, y in corner_points]
optimal_index = np.argmax(profits)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_profit = profits[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_C, y1, label=r'$x_C + 2x_V \leq 8$', color='blue')
plt.plot(x_C, y2, label=r'$3x_C + 2x_V \leq 12$', color='green')

# Shade the feasible region
plt.fill_between(x_C, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, P={optimal_profit}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 10)
plt.ylim(0, 5)
plt.xlabel('$x_C$ (Chocolate Cakes)')
plt.ylabel('$x_V$ (Vanilla Cakes)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Profit')

plt.show()


# In[ ]:


#Number 8
import numpy as np
import matplotlib.pyplot as plt

"""
MINIMIZE
            C = 6x_X + 7x_Y
SUBJECT TO

            3x_X + 4x_Y ≤ 18  (Fuel constraint)
            2x_X + x_Y ≤ 10   (Driver time constraint)
            x_X ≥ 0, x_Y ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_X = np.linspace(0, 10, 400)  # Adjust range for visibility

# Constraint 1: 3x_X + 4x_Y ≤ 18 → x_Y = (18 - 3x_X) / 4
y1 = (18 - 3 * x_X) / 4

# Constraint 2: 2x_X + x_Y ≤ 10 → x_Y = 10 - 2x_X
y2 = 10 - 2 * x_X

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 4.5),  # Intersection with y-axis for y1
    (3, 4),  # Intersection of y1 and y2
    (5, 0),  # Intersection with x-axis for y2
]

# Calculate the cost C = 6x_X + 7x_Y at each corner point
costs = [6 * x + 7 * y for x, y in corner_points]
optimal_index = np.argmin(costs)  # Minimization
optimal_point = corner_points[optimal_index]
optimal_cost = costs[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_X, y1, label=r'$3x_X + 4x_Y \leq 18$', color='blue')
plt.plot(x_X, y2, label=r'$2x_X + x_Y \leq 10$', color='green')

# Shade the feasible region
plt.fill_between(x_X, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, C=${optimal_cost}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 6)
plt.ylim(0, 5)
plt.xlabel('$x_X$ (Trips by Vehicle X)')
plt.ylabel('$x_Y$ (Trips by Vehicle Y)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Minimizing Cost')

plt.show()


# In[ ]:


#Number 9
import numpy as np
import matplotlib.pyplot as plt

"""
MINIMIZE
            C = 6x_X + 7x_Y
SUBJECT TO

            3x_X + 4x_Y ≤ 18  (Fuel constraint)
            2x_X + x_Y ≤ 10   (Driver time constraint)
            x_X ≥ 0, x_Y ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_X = np.linspace(0, 10, 400)  # Adjust range for visibility

# Constraint 1: 3x_X + 4x_Y ≤ 18 → x_Y = (18 - 3x_X) / 4
y1 = (18 - 3 * x_X) / 4

# Constraint 2: 2x_X + x_Y ≤ 10 → x_Y = 10 - 2x_X
y2 = 10 - 2 * x_X

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 4.5),  # Intersection with y-axis for y1
    (3, 4),  # Intersection of y1 and y2
    (5, 0),  # Intersection with x-axis for y2
]

# Calculate the cost C = 6x_X + 7x_Y at each corner point
costs = [6 * x + 7 * y for x, y in corner_points]
optimal_index = np.argmin(costs)  # Minimization
optimal_point = corner_points[optimal_index]
optimal_cost = costs[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_X, y1, label=r'$3x_X + 4x_Y \leq 18$', color='blue')
plt.plot(x_X, y2, label=r'$2x_X + x_Y \leq 10$', color='green')

# Shade the feasible region
plt.fill_between(x_X, np.minimum(y1, y2), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.2, point[1] + 0.2, f"({point[0]}, {point[1]})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, C=${optimal_cost}")
plt.text(optimal_point[0] + 0.2, optimal_point[1] + 0.2, f"Optimal\n({optimal_point[0]}, {optimal_point[1]})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 6)
plt.ylim(0, 5)
plt.xlabel('$x_X$ (Trips by Vehicle X)')
plt.ylabel('$x_Y$ (Trips by Vehicle Y)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Minimizing Cost')

plt.show()


# In[ ]:


#Number 10
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            R = 500000x_A + 400000x_B
SUBJECT TO

            4000x_A + 3000x_B ≤ 5000   (Television budget constraint)
            2000x_A + 2500x_B ≤ 4500   (Print media budget constraint)
            1000x_A + 1500x_B ≤ 3000   (Social media budget constraint)
            x_A ≥ 0, x_B ≥ 0           (Non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 2, 400)  # Adjust range for visibility

# Constraint 1: 4000x_A + 3000x_B ≤ 5000 → x_B = (5000 - 4000x_A) / 3000
y1 = (5000 - 4000 * x_A) / 3000

# Constraint 2: 2000x_A + 2500x_B ≤ 4500 → x_B = (4500 - 2000x_A) / 2500
y2 = (4500 - 2000 * x_A) / 2500

# Constraint 3: 1000x_A + 1500x_B ≤ 3000 → x_B = (3000 - 1000x_A) / 1500
y3 = (3000 - 1000 * x_A) / 1500

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 1),  # Intersection with y-axis for y3
    (0.75, 0.5),  # Intersection of y1 and y2
    (1, 0),  # Intersection with x-axis for y3
]

# Calculate the reach R = 500000x_A + 400000x_B at each corner point
reaches = [500000 * x + 400000 * y for x, y in corner_points]
optimal_index = np.argmax(reaches)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_reach = reaches[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$4000x_A + 3000x_B \leq 5000$', color='blue')
plt.plot(x_A, y2, label=r'$2000x_A + 2500x_B \leq 4500$', color='green')
plt.plot(x_A, y3, label=r'$1000x_A + 1500x_B \leq 3000$', color='purple')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.05, point[1] + 0.05, f"({point[0]:.2f}, {point[1]:.2f})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, R={optimal_reach:,}")
plt.text(optimal_point[0] + 0.05, optimal_point[1] + 0.05, f"Optimal\n({optimal_point[0]:.2f}, {optimal_point[1]:.2f})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel('$x_A$ (Campaign A)')
plt.ylabel('$x_B$ (Campaign B)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Reach')

plt.show()


# In[ ]:


#Number 10
import numpy as np
import matplotlib.pyplot as plt

"""
MAXIMIZE
            R = 6x_A + 5x_B
SUBJECT TO

            2x_A + 4x_B ≤ 30  (Meat constraint)
            3x_A + 2x_B ≤ 24  (Vegetable constraint)
            x_A + 2x_B ≤ 20   (Rice constraint)
            x_A ≥ 0, x_B ≥ 0  (Non-negativity constraints)
"""

# Define the constraints
x_A = np.linspace(0, 20, 400)  # Adjust range for visibility

# Constraint 1: 2x_A + 4x_B ≤ 30 → x_B = (30 - 2x_A) / 4
y1 = (30 - 2 * x_A) / 4

# Constraint 2: 3x_A + 2x_B ≤ 24 → x_B = (24 - 3x_A) / 2
y2 = (24 - 3 * x_A) / 2

# Constraint 3: x_A + 2x_B ≤ 20 → x_B = (20 - x_A) / 2
y3 = (20 - x_A) / 2

# Non-negativity constraints (clip below 0)
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Calculate intersection points (corner points of the feasible region)
corner_points = [
    (0, 0),  # Origin
    (0, 7.5),  # Intersection with y-axis for y1
    (4, 8),  # Intersection of y1 and y2
    (10, 5),  # Intersection of y2 and y3
    (20, 0),  # Intersection with x-axis for y3
]

# Calculate the revenue R = 6x_A + 5x_B at each corner point
revenues = [6 * x + 5 * y for x, y in corner_points]
optimal_index = np.argmax(revenues)  # Maximization
optimal_point = corner_points[optimal_index]
optimal_revenue = revenues[optimal_index]

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x_A, y1, label=r'$2x_A + 4x_B \leq 30$', color='blue')
plt.plot(x_A, y2, label=r'$3x_A + 2x_B \leq 24$', color='green')
plt.plot(x_A, y3, label=r'$x_A + 2x_B \leq 20$', color='purple')

# Shade the feasible region
plt.fill_between(x_A, np.minimum(np.minimum(y1, y2), y3), 0, color='red', alpha=0.3, label='Feasible Region')

# Plot and label corner points
for point in corner_points:
    plt.scatter(*point, color='black', zorder=5)
    plt.text(point[0] + 0.5, point[1] + 0.5, f"({point[0]:.1f}, {point[1]:.1f})", fontsize=10, color='black')

# Highlight the optimal solution
plt.scatter(*optimal_point, color='gold', s=100, zorder=6, label=f"Optimal Point {optimal_point}, R=${optimal_revenue}")
plt.text(optimal_point[0] + 0.5, optimal_point[1] + 0.5, f"Optimal\n({optimal_point[0]:.1f}, {optimal_point[1]:.1f})", 
         fontsize=10, color='gold')

# Labels and legends
plt.xlim(0, 20)
plt.ylim(0, 10)
plt.xlabel('$x_A$ (Meal A)')
plt.ylabel('$x_B$ (Meal B)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Graphical Method for Maximizing Revenue')

plt.show()

