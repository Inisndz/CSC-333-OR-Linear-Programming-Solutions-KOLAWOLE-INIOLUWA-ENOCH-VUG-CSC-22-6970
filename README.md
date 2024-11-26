# CSC-333-OR-Linear-Programming-Solutions-KOLAWOLE-INIOLUWA-ENOCH-VUG-CSC-22-6970
An Assignment repo for CSC 333 
Detailed Description of the Project
This project involves solving various linear programming (LP) problems, each with different real-world applications, using Python. The problems aim to optimize specific objectives (either maximizing or minimizing) subject to constraints. Linear programming (LP) is a mathematical method used for optimization in which a linear objective function is maximized or minimized subject to linear equality or inequality constraints.

The specific problem here involves maximizing the total revenue for a school cafeteria that offers two types of meals, Meal A and Meal B, subject to ingredient and availability constraints. The objective is to maximize the revenue generated from selling these meals.

Problem Statement
Objective:
Maximize the total revenue from selling two types of meals (A and B) in a school cafeteria.

Meal A requires:
2 units of meat,
3 units of vegetables,
1 unit of rice.
Meal B requires:
4 units of meat,
2 units of vegetables,
2 units of rice.
The cafeteria has:

30 units of meat,
24 units of vegetables,
20 units of rice.
The revenue from each meal is:

$6 per Meal A,
$5 per Meal B.
Goal: Maximize the total revenue, given these constraints.

Objective of the LP Problem
The main objective of this LP problem is to maximize the total revenue. The revenue is represented by the following objective function:



(No negative number of meals(non negativity constraint )).
Steps Taken to Solve the Problem
Define the Constraints: We first defined the constraints as mathematical equations. These constraints describe the availability of ingredients (meat, vegetables, and rice) for meal production.

Graph the Constraints: Using Python's matplotlib library, we plotted the constraints to visually identify the feasible region. This region is the area where all constraints are satisfied. Each constraint was plotted as a line (inequality), and the region satisfying all inequalities was shaded.

Identify Corner Points: In linear programming, the optimal solution lies at one of the corner points of the feasible region. We found the corner points by solving the system of equations formed by the intersections of the constraints.

Evaluate the Objective Function at Corner Points: The revenue function 
𝑅
=
6
𝑥
𝐴
+
5
𝑥
𝐵
R=6x 
A
​
 +5x 
B
​
  was evaluated at each corner point to identify the point that gives the maximum revenue.

Select the Optimal Solution: The corner point that provided the highest revenue was selected as the optimal solution.

Python Code
Below is the Python code used to solve this problem.

python
Copy code
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
Instructions on How to Run the Python Code
Install Required Libraries: Before running the code, ensure you have the necessary Python libraries installed. You can install them using pip:

bash
Copy code
pip install numpy matplotlib
Run the Code: Copy the code into a Python script file (e.g., meal_planning.py). You can run the script using a Python interpreter:

bash
Copy code
python meal_planning.py
Understand the Output:

The code will generate a plot displaying the feasible region for the LP problem and the corner points.
The plot will also highlight the optimal point, which gives the maximum revenue.
The corner points and the optimal solution will be labeled, along with the calculated total revenue at each corner point.
Conclusion
This project demonstrates how linear programming can be applied to maximize revenue while respecting resource constraints. By using Python and matplotlib, we can visually solve LP problems and identify optimal solutions.
