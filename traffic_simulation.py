import traci

# Start SUMO Simulation
traci.start(["sumo-gui", "-c", "my_config_file.sumocfg"])

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

traci.close()
