# Import relevant modules
from uuv_mission.control import controller
from uuv_mission.dynamic import Submarine, ClosedLoop, Mission



sub = Submarine()
# Instantiate your controller (depending on your implementation)
closed_loop = ClosedLoop(sub, controller)
mission = Mission.from_csv("data/mission.csv")
trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)
