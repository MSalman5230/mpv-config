import sys
import vapoursynth as vs

# Write debug info to file
with open('C:/Apps/mpv/debug_output.txt', 'w') as f:
    f.write("=== VAPOURSYNTH DEBUG ===\n")
    f.write(f"Python executable: {sys.executable}\n")
    f.write(f"Python version: {sys.version}\n")
    f.write(f"Python path: {sys.path}\n")
    f.write(f"Available globals: {list(globals().keys())}\n")
    
    try:
        core = vs.core
        f.write(f"VapourSynth core: {core}\n")
        f.write(f"VapourSynth version: {core.version()}\n")
        
        # Check if video_in exists
        if 'video_in' in globals():
            f.write(f"video_in found: {video_in}\n")
            f.write(f"video_in type: {type(video_in)}\n")
            clip = video_in
            f.write(f"Clip format: {clip.format}\n")
            f.write(f"Clip dimensions: {clip.width}x{clip.height}\n")
            clip.set_output()
            f.write("SUCCESS: Script completed\n")
        else:
            f.write("ERROR: video_in not in globals\n")
            
    except Exception as e:
        f.write(f"EXCEPTION: {str(e)}\n")
        f.write(f"Exception type: {type(e)}\n")
        import traceback
        f.write(f"Traceback: {traceback.format_exc()}\n")
        raise
