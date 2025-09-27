# Monte-Carlo Simulation for pi

# install numpy if you don't have it already
# command: pip install numpy
import numpy as np

# Function to calculate pi using Monte Carlo method
def calculate_pi(numSamples):
    # Initialize counter for points within the circle
    insideCircle = 0

    # Run numSamples iterations of simulation
    for samples in range(numSamples):
       
        #get random coordinates in 2x2 square
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)

        # Check if point is within unit circle using the pythagorean theorem
        if x**2 + y**2 <= 1:
            insideCircle += 1

    # Calculate pi by using the ratio of the 2x2 square area and the unit circle area
    pi = 4 * (insideCircle/numSamples)

    return pi

# Get user input for number of iterations and print calculated value of pi
numIterations = input("Enter the number of iterations to run: ")
print(calculate_pi(int(numIterations))) 
