# MPV Configuration with Motion Interpolation

This repository contains a complete MPV configuration setup with motion interpolation capabilities using VapourSynth. The configuration includes optimized settings for NVIDIA GPUs and VLC-like keybindings.

## Features

- **Motion Interpolation**: Two VapourSynth scripts for smooth video playback
  - Basic motion interpolation (`motioninterpolation.vpy`)
  - Enhanced motion interpolation (`motioninterpolation_enhanced.vpy`) - more demanding but higher quality
- **VLC-like Keybindings**: Familiar controls for VLC users
- **NVIDIA GPU Optimization**: Optimized settings for NVIDIA graphics cards
- **Portable Configuration**: Easy to set up and use

## Installation Guide

### Prerequisites

- Windows operating system
- NVIDIA GPU (recommended, but should work with other GPUs)

### Step 1: Download MPV

1. Download MPV Windows builds by shinchiro from: https://github.com/shinchiro/mpv-winbuild-cmake/releases
   - Choose a build that includes VapourSynth compilation
   - This is essential for motion interpolation functionality

### Step 2: Install MPV

1. Create a folder named `mpv` where you want to install MPV (e.g., `C:\Program Files\mpv`)
2. Extract the MPV build to the `mpv` folder you created
3. Run `updated.bat` and let it finish completely

### Step 3: Install VapourSynth

1. Download VapourSynth from: https://github.com/vapoursynth/vapoursynth/releases
2. Download the PowerShell version (currently `Install-Portable-VapourSynth-R72.ps1`)
3. Copy the PowerShell script to your MPV folder
4. Run the script - it will download all dependencies and Python for VapourSynth in a new folder called `vapoursynth-portable`

### Step 4: Install Motion Tools Plugin

1. Download from: https://github.com/dubhater/vapoursynth-mvtools/releases
2. Copy the DLL file to `vapoursynth-portable/vs-plugins` folder

### Step 5: Set Up Configuration

1. Create a `portable_config` folder in your MPV directory
2. Copy the motion interpolation scripts from this repository to `mpv/portable_config/scripts/`
3. Optionally, copy `input.conf` and `mpv.conf` from this repository to your `portable_config` folder
   - `input.conf`: VLC-like keybindings
   - `mpv.conf`: Optimized settings (primarily for NVIDIA GPU)

### Step 6: Configure Motion Interpolation

Add these lines to your `input.conf`:

```
KP4 vf toggle vapoursynth=~~/scripts/motioninterpolation.vpy
KP5 vf toggle vapoursynth=~~/scripts/motioninterpolation_enhanced.vpy
```

This enables:
- **Numpad 4**: Activates basic motion interpolation
- **Numpad 5**: Activates enhanced motion interpolation (more demanding, better quality)

### Step 7: Final Setup

**Important**: 
1. Go to the `vapoursynth-portable` folder
2. Select all files
3. Cut and move them up one folder level (to where `mpv.exe` is located)
4. then delete the vapoursynth-portable, make sure you copied all the files to where mpv.exe is.

## Usage

1. Run any video file (ideally 1080p or less and under 60fps for best results)
2. Press **Numpad 4** for basic motion interpolation
3. Press **Numpad 5** for enhanced motion interpolation
4. Press the same key again to toggle off

### Video Requirements

- **Resolution**: 1080p or lower recommended
- **Frame Rate**: Less than 60fps (motion interpolation won't apply to 60fps+ videos)
- You can modify the scripts to change these requirements

## Configuration Files

### `input.conf`
- VLC-like keybindings for familiar controls
- Motion interpolation toggles on Numpad 4 and 5

### `mpv.conf`
- Optimized settings primarily for NVIDIA GPUs
- Should work with other GPUs but may need testing and adjustment

### Scripts
- `motioninterpolation.vpy`: Basic motion interpolation script
- `motioninterpolation_enhanced.vpy`: Enhanced version with better quality but higher resource usage

## Troubleshooting

- If motion interpolation doesn't work, ensure VapourSynth is properly installed
- Check that the DLL files are in the correct location
- Verify the directory structure is clean (all VapourSynth files should be in the same folder as `mpv.exe`)
- For non-NVIDIA GPUs, you may need to adjust settings in `mpv.conf`

## Customization

You can modify the motion interpolation scripts to:
- Change frame rate requirements
- Adjust interpolation quality settings
- Modify video resolution limits
- Add additional filters or effects

## License

See [LICENSE](LICENSE) file for details.