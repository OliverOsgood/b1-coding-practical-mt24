# Import relevant modules
from uuv_mission.control import controller
from uuv_mission.dynamic import Submarine, ClosedLoop, Mission


sub = Submarine()
# Instantiate your controller (depending on your implementation)
closed_loop = ClosedLoop(sub, controller)
mission = Mission.from_csv(r"C:\Users\Oxfordium\OneDrive - Nexus365\Documents\Engineering\Third Year\B1\Mini Project 1\b1-coding-practical-mt24\data\mission.csv") # You must implement this method in the Mission class

trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)
