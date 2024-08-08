import simpy
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
NUM_PEDESTRIANS = 10  # Number of pedestrians
ARRIVAL_INTERVAL = 5  # Average time between pedestrian arrivals
WALKING_TIME = (1, 3)  # Range of walking time (min, max) between points
CROSSWALK_TIME = (1, 2)  # Range of time to wait at crosswalk (min, max)
SIMULATION_TIME = 50  # Total simulation time
GREEN_LIGHT_DURATION = 10  # Duration of the green light
RED_LIGHT_DURATION = 5  # Duration of the red light

# # Data for visualization
# pedestrian_positions = []

class TrafficLight:
    def __init__(self, env):
        self.env = env
        self.color = 'GREEN'
        self.green = env.event()  # Event to signal the green light
        self.process = env.process(self.run())

    def run(self):
        while True:
            self.color = 'GREEN'
            self.green.succeed()  # Signal the green light
            self.green = self.env.event()  # Reset the event for the next green phase
            yield self.env.timeout(GREEN_LIGHT_DURATION)

            self.color = 'RED'
            yield self.env.timeout(RED_LIGHT_DURATION)

def pedestrian(env, name, light):
    """Simulates a pedestrian's movement through the system."""
    print(f'{name} starts walking at {env.now:.2f}')
    start_time = env.now
    pedestrian_positions.append((start_time, name, 0))
    
    # Walk to crosswalk
    walking_time = random.uniform(*WALKING_TIME)
    yield env.timeout(walking_time)
    reach_crosswalk_time = env.now
    pedestrian_positions.append((reach_crosswalk_time, name, 1))
    print(f'{name} reaches crosswalk at {env.now:.2f}')
    
    # Wait at crosswalk if light is red
    if light.color == 'RED':
        print(f'{name} waits at crosswalk at {env.now:.2f}')
        yield light.green  # Wait for the green light
    
    cross_time = env.now
    pedestrian_positions.append((cross_time, name, 2))
    print(f'{name} crosses at {env.now:.2f}')
    
    # Continue walking
    walking_time = random.uniform(*WALKING_TIME)
    yield env.timeout(walking_time)
    finish_time = env.now
    pedestrian_positions.append((finish_time, name, 3))
    print(f'{name} finishes walking at {env.now:.2f}')

def pedestrian_generator(env, light):
    """Generates pedestrians at random intervals."""
    for i in range(NUM_PEDESTRIANS):
        yield env.timeout(random.expovariate(1.0 / ARRIVAL_INTERVAL))
        env.process(pedestrian(env, f'Pedestrian {i+1}', light))

# Simulate the pedestrian traffic
def simulate_pedestrian_traffic():
    global pedestrian_positions
    pedestrian_positions = []
    env = simpy.Environment()
    light = TrafficLight(env)
    env.process(pedestrian_generator(env, light))
    env.run(until=SIMULATION_TIME)
    return pd.DataFrame(pedestrian_positions, columns=["Time", "Pedestrian", "Event"])

# if __name__ == "__main__":
#     df = simulate_pedestrian_traffic()
#     print("Simulation Results")
#     print(df)

#     # Plot the simulation results
#     fig, ax = plt.subplots()
#     lines = {name: ax.plot([], [], label=name)[0] for name in df["Pedestrian"].unique()}

#     def init():
#         for line in lines.values():
#             line.set_data([], [])
#         return lines.values()

#     def update(frame):
#         for name, line in lines.items():
#             times = df[df["Pedestrian"] == name]["Time"]
#             events = df[df["Pedestrian"] == name]["Event"]
#             mask = times <= frame
#             line.set_data(times[mask], events[mask])
#         return lines.values()

#     ani = animation.FuncAnimation(fig, update, frames=range(int(df["Time"].max()) + 1), init_func=init, blit=True, repeat=False)
#     ax.set_xlabel("Time")
#     ax.set_ylabel("Event")
#     ax.set_yticks([0, 1, 2, 3])
#     ax.set_yticklabels(["Start", "Reach Crosswalk", "Cross", "Finish"])
#     ax.legend(title="Pedestrian")
#     plt.show()
