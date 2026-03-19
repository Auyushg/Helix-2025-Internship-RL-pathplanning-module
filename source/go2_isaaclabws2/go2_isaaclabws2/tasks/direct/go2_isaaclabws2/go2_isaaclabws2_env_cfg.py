# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# SPDX-License-Identifier: BSD-3-Clause


from isaaclab.envs import DirectRLEnvCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass
import gymnasium as gym
import numpy as np
from isaaclab.assets import ArticulationCfg
from isaaclab_assets.robots.unitree import UNITREE_GO2_CFG
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sensors.ray_caster import RayCasterCfg, patterns
from isaaclab.utils import configclass
from isaaclab.sensors import RayCaster, RayCasterCfg, patterns
from isaaclab.utils import configclass
from isaaclab.sensors import SensorBaseCfg
from isaaclab.assets import ArticulationCfg, AssetBaseCfg
from isaaclab.sensors import CameraCfg, ContactSensorCfg
import isaaclab.sim as sim_utils
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from .go2scenecfg import Go2SceneCfg
import torch

threshhold = int(500/3) * 1000
path_planning_threshold = 500

obstacle_phase = True

WAYPOINTS = [
    (0.79, 10.26),
    (0.79, 15.27),
    (1.47, 24.61),
    (-0.36, 28.25),
    (-2.37, 23.12),
    (-1.54, 16.10),   # enter from right
    (-2.24, 17.50),   # curve up-left
    (-2.74, 18.50),   # continue up-left  
    (-3.74, 20.50),   # across the top
    (-4.26, 24.30),
    (-6.36, 26.97),
    (-7.67, 14.98),
    (-7.83, 8.86),
    (-10.55, 6.76),
    (-13.02, 9.86),
    (-13.02, 24.71),
    (-15.18, 26.97),
    (-17.06, 24.71),
    (-16.50, 7.80),
    (-16.8, 6.6),
    (-17.0, 5.8),
    (-17.06, 5.06),
    (-18.81, 5.06),
    (-18.81, 24.71),
    (-20.53, 26.97),
    (-22.67, 24.71),
    (-22.67, 7.61),
    (-11.35, 3.32),
    (0, 0),
]

WAYPOINT_RADII = [
    1.0,  # wp 0
    1.0,  # wp 1
    1.0,  # wp 2
    1.0,  # wp 3
    1.0,  # wp 4
    1.5,  # wp 5
    1.5,  # wp 6 - tight corridor, larger radius
    1.5,  # wp 0
    1.0,  # wp 1
    1.0,  # wp 2
    1.0,  # wp 3
    1.0,  # wp 4
    1.0,  # wp 12
    1.0,  # wp 2
    1.0,  # wp 3
    1.0,  # wp 4
    1.0,  # wp 16
    2.0,  # wp 17 - tight corridor, larger radius
    1.0,  # wp 2
    1.0,  # wp 3
    1.0,  # wp 4
    1.0,  # wp 21
    1.0,  # wp 22
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
]
    
@configclass
class Go2Isaaclabws2EnvCfg(DirectRLEnvCfg):

    scene: Go2SceneCfg = Go2SceneCfg()
    
    # sensors
    decimation = 4
    sim = SimulationCfg(dt=1/120, render_interval=decimation)
    episode_length_s = 20.0

    action_space = 12
    observation_space = 46
    state_space = 0
    
    # velocity limits
    max_lin_vel = 0.4
    max_yaw_rate = 0.5

    collision_dist = 0.35
    max_joint_angle = 0.1



