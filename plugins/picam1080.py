# ---------------- User Configuration Settings for speed-cam.py ---------------------------------
#         Ver 7.0 speed-cam.py picam1080 Stream Variable Configuration Settings

#######################################
#    speed-cam.py plugin settings
#          EXPERIMENTAL
#######################################

# Calibration Settings
# ===================
cal_obj_px = 620       # Length of a calibration object in pixels
cal_obj_mm = 4330.0    # Length of the calibration object in millimetres

# Crop Area for motion detection Tracking
# =======================================
x_left  = 660          # Exclude event if x less than this px position Default=25
x_right = 1260         # Exclude event if x greater than this px position Default=295
y_upper = 340          # Exclude event if y less that this value default=100
y_lower = 740          # Exclude event if y greater than this value default=175

# Motion Event Settings
# ---------------------
SPEED_MPH = False      # Set the speed conversion  kph=False  mph=True
track_len_trig = 100   # Default=100 Length of track to trigger speed photo
track_timeout = 1      # Number of seconds to wait after track End (prevents dual tracking)
event_timeout = 2      # Number of seconds to wait for next motion event before starting new track

# Camera Settings
# ---------------
WEBCAM = False        # default = False False=PiCamera True=USB WebCamera

# Pi Camera Settings
# ------------------
CAMERA_WIDTH = 1920    # default = 1920 Image stream width for opencv motion scanning (quad core)
CAMERA_HEIGHT = 1088   # default = 1088 Image stream height for opencv motion scanning (quad core)
CAMERA_FRAMERATE = 15  # default = 15 framerate for video stream max for V2 can be higher

# Camera Image Settings
# ---------------------
image_font_size = 20          # Default = 20 Font text height in px for text on images
image_bigger = 1              # Default = 1 Resize saved speed image by value

# ---------------------------------------------- End of User Variables -----------------------------------------------------
