# Monte-Carlo Simulation for pi

# install numpy if you don't have it already
# command: pip install numpy
import numpy as np
import turtle as trtl

# Visualize the Monte Carlo simulation using turtle graphics
# Set up the turtle screen
screen = trtl.Screen()
screen.title("Monte Carlo Simulation for Pi")
screen.setup(width=600, height=600) 

# Set up the turtle
trtl.speed(0)
trtl.hideturtle()

# Draw the unit circle
trtl.penup()
trtl.goto(0, -300)  # Move to the bottom of the circle
trtl.pendown()
trtl.circle(300)  # Draw the unit circle with radius 300

# Function to calculate pi using Monte Carlo method
def calculate_pi(numSamples):
    # Initialize counter for points within the circle
    insideCircle = 0

    # Run numSamples iterations of simulation
    for samples in range(numSamples):
       
        #get random coordinates in 2x2 square
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)

        # Visualize the point
        trtl.penup()
        trtl.goto(x * 300, y * 300)  # Scale to fit the drawn circle
        trtl.pendown()
        if x**2 + y**2 <= 1:
            trtl.dot(5, "green")  # Point is inside the circle
        else:
            trtl.dot(5, "red")    # Point is outside the circle

        # Check if point is within unit circle using the pythagorean theorem
        if x**2 + y**2 <= 1:
            insideCircle += 1

    # Calculate pi by using the ratio of the 2x2 square area and the unit circle area
    # Area of square = 4, area of circle = pi * 1^2 = pi
    # Therefore, pi = 4 * (insideCircle/numSamples)
    pi = 4 * (insideCircle/numSamples)

    return pi

# Get user input for number of iterations and print calculated value of pi
numIterations = input("Enter the number of iterations to run: ")
print(calculate_pi(int(numIterations)))

screen.mainloop()