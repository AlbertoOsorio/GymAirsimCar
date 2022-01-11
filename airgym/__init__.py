from gym.envs.registration import register

register(
    id="airsim-car-sample-v0", entry_point="airgym.envs:AirSimCarEnv",
)