"""
RIFE Configuration Settings

This file contains all the configurable parameters for the RIFE interpolation script.
Modify these values to customize the behavior according to your needs.
"""

import vapoursynth as vs
from vs_script.target_fps_mode import TargetFpsMode
from vs_script.expensive_clip_mode import ExpensiveClipMode


# =============================================================================
# RIFE Model Settings
# =============================================================================

# The RIFE model to use. Recommended ones are 4.26, 4.25 or 4.25.lite
rife_model = "4.25.lite"

# Interpolation scale
scale = 1

# Produces better results at a decently heavy cost. NOTE: NOT SUPPORTED BY ALL MODELS
ensemble = False


# =============================================================================
# Target FPS Settings
# =============================================================================

# Target FPS mode. Can be TargetFpsMode.fixed_fps(*target_fps*) or TargetFpsMode.fixed_multiplier(*multiplier*)
target_mode = TargetFpsMode.fixed_multiplier(2)

# Disable when source media is above threshold
disable_fps_threshold = 60


# =============================================================================
# Video Output Format Settings
# =============================================================================

# You can change these to better match your display or source media
output_format = vs.YUV420P10
output_colorspace = vs.MATRIX_BT2020_NCL
output_transfer = vs.TRANSFER_BT2020_10
output_primaries = vs.PRIMARIES_BT2020


# =============================================================================
# Resolution and Performance Settings
# =============================================================================

# Resolution threshold for what determines if a clip is "expensive"
# Anything ABOVE this resolution will be considered expensive.
expensive_res_threshold = (3840, 2160)

# How do we handle expensive clips?
expensive_clip_handling = ExpensiveClipMode.DOWNSCALE

# Resolution to downscale to if expensive_clip_handling is "downscale"
downscale_res = (1920, 1080)

# To use scene change detection or not
sc = True
sc_threshold = 0.15

# =============================================================================
# GPU and TensorRT Settings
# =============================================================================

# Which GPU to use
gpu_index = 0

# RGBH is faster, RGBS is more accurate
gpu_format = vs.RGBH

# Uses Nvidia TensorRT framework which is faster.
# It also takes a million years to build an RT engine for each resolution and config, but it is much faster than regular.
tensorrt = True

# Enable for TensorRT debug logging
tensorrt_debug = False

# 0 is min - 5 is max. This will increase the time it takes to build the RT engine
tensorrt_optimization = 3

# Dynamic shapes allows TensorRT to build a single engine for multiple resolutions.
# Meaning that you only have to compile the engine once, and it will work for all resolutions within the min-max range.
# The downside is worse performance and memory usage than static shapes.
# You should set opt_shape to the resolution you will be using most of the time.
tensorrt_static_shape = True

# Min size of dynamic shape
tensorrt_min_shape = [128, 128]

# Optimized size of dynamic shape
tensorrt_opt_shape = [3840, 2160]

# Max size of dynamic shape
tensorrt_max_shape = [
    expensive_res_threshold[0],
    expensive_res_threshold[1],
]


# =============================================================================
# Logging Settings
# =============================================================================

# Log file path. Set to None for no log, or to an output stream to a log file
log = None #open("./rife_log.txt", "w")
