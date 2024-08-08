Pedestrian Traffic Simulation

Overview
This project simulates pedestrian movement through a crosswalk, incorporating a traffic light system that alternates between red and green. The simulation tracks pedestrians as they walk, wait at the crosswalk, cross the road, and finish their journey.

Features
Traffic Light System: Simulates a traffic light alternating between red and green. Pedestrians wait at the crosswalk if the light is red.
Randomized Pedestrian Behavior: Pedestrians have random arrival times and varying walking speeds, simulating real-life behavior.
Real-time Visualization: An animated plot visualizes the pedestrian movements through the different stages of their journey.

Code Structure
TrafficLight Class: Manages the state of the traffic light (green/red) and signals to pedestrians when they can cross.
Pedestrian Function: Simulates the behavior of a pedestrian, including walking, waiting at the crosswalk, crossing, and finishing.
Pedestrian Generator: Generates pedestrians at random intervals to simulate continuous pedestrian traffic.
Simulation Function: Runs the entire simulation and returns the data for visualization.
Visualization: The simulation results are visualized using matplotlib.animation.FuncAnimation, showing the progression of each pedestrian.

Customization
Number of Pedestrians: Modify the NUM_PEDESTRIANS variable to simulate more or fewer pedestrians.
Traffic Light Timing: Adjust GREEN_LIGHT_DURATION and RED_LIGHT_DURATION to change how long the traffic light stays green or red.
Simulation Time: Change SIMULATION_TIME to simulate for a longer or shorter period.
