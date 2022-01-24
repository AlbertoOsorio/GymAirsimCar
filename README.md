#### Requirements
This script is designed to work with AirSim's Car simulator, but the project is build to run on skoods[https://github.com/skoods-org/Welcome], wich is a program that is build on top of AirSim, so the requirements you must comply are the following:
- Installing Skoods
	- Note: AirSim's current version is newer than the one you must have for the actual installation of skoods. You must install "airsim==1.5.0"
- OpenAI's Gym
- Stable-Baselines3

#### Installation

To successfully run this code you must install the needed requirements, to do this run the next commands (I recomend you to use a conda enviroment):
`pip install gym`

`pip install stable-baselines3[extra]`

*Remember that you must install skoods first*

#### Usage and Configuration
Once you have installed the requirements all you need to do to start the reinforcment learning agent is start the simulator and running the main python script by:
`python dqn_car.py`

A "DeepRacer like" approach to the configuration of your agent would be the following:

##### Reward function:
- You can edit it by changing the function called _compute_reward that is located at airgym/envs/car_env

##### Action space:
- You also can edit this in the same file (airgym/envs/car_env). To change your actions you must edit the function called _do_action and the parameter setted here:
`self.action_space = spaces.Discrete(6)`

	Where 6 is the number you must change and the number you must put in it is the number of possible actions that are present on the _do_action function.

##### Hyperparameters:
- You can edit hyperparameters by changing the model declaration on the file dqn_car.py
The full list of posible hyperparameters depends on the type of model you are using, read full documentation on stable-baselines3's documentation [https://stable-baselines3.readthedocs.io/en/master/]
