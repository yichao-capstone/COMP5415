import streamlit as st

import streamlit as st
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="🎥 Digital Video Introduction", layout="wide")
st.title("🎥 Introduction to Digital Video")

# ------------------------
# Sidebar Controls
# ------------------------
st.sidebar.header("🎛️ Video Settings")
frame_rate = st.sidebar.slider("Frame Rate (FPS)", 1, 60, 10)
duration = st.sidebar.slider("Duration (Seconds)", 1, 10, 3)
resolution = st.sidebar.selectbox("Resolution", ["64x64", "128x128", "256x256"], index=1)
color_mode = st.sidebar.selectbox("Color Mode", ["RGB", "Grayscale"])
###
# ------------------------
# Config
# ------------------------
width, height = map(int, resolution.split('x'))
total_frames = frame_rate * duration

# ------------------------
# Generate Synthetic Video Frames
# ------------------------
def generate_frame(i, width, height, color_mode):
    """Generate synthetic frame: animated RGB pattern or grayscale"""
    x = np.linspace(0, 2 * np.pi, width)
    y = np.linspace(0, 2 * np.pi, height)
    X, Y = np.meshgrid(x, y)

    pattern = np.sin(X + i / 5.0) * np.cos(Y + i / 7.0)

    if color_mode == "Grayscale":
        grayscale = ((pattern + 1) / 2 * 255).astype(np.uint8)
        img = Image.fromarray(grayscale, mode="L")
    else:
        r = ((np.sin(X + i / 5.0) + 1) / 2 * 255).astype(np.uint8)
        g = ((np.cos(Y + i / 6.0) + 1) / 2 * 255).astype(np.uint8)
        b = ((np.sin(X + Y + i / 10.0) + 1) / 2 * 255).astype(np.uint8)
        rgb = np.stack([r, g, b], axis=-1)
        img = Image.fromarray(rgb, mode="RGB")

    return img

# ------------------------
# Explanation Panel
# ------------------------
st.markdown("## 🧠 What is Digital Video?")
st.markdown("""
Digital video is a sequence of images (frames) shown rapidly to create motion illusion.

- **Frame Rate (FPS)**: How many images are shown per second (e.g. 24 FPS = cinematic)
- **Resolution**: Number of pixels per frame (width × height)
- **Color Mode**:
    - RGB = full color (Red, Green, Blue)
    - Grayscale = black & white (1 channel)
- Videos are essentially **3D arrays**: `(frames, height, width, channels)`
""")

# ------------------------
# Video Simulation (Animated Frames)
# ------------------------
st.markdown("## ▶️ Simulated Video Playback")

video_area = st.empty()

for i in range(total_frames):
    frame = generate_frame(i, width, height, color_mode)
    video_area.image(frame, caption=f"Frame {i+1}/{total_frames}")
    time.sleep(1.0 / frame_rate)

# ------------------------
# Show Single Frame Details
# ------------------------
st.markdown("## 🖼️ Frame Details")

frame_index = st.slider("Inspect Frame", 0, total_frames - 1, 0)
selected_frame = generate_frame(frame_index, width, height, color_mode)
st.image(selected_frame, caption=f"Frame {frame_index + 1}")

np_frame = np.array(selected_frame)
st.write(f"**Resolution:** {np_frame.shape[0]} × {np_frame.shape[1]}")
st.write(f"**Color Channels:** {np_frame.shape[2] if len(np_frame.shape) == 3 else 1}")
st.write("**Pixel Data Sample (Top-Left 5×5):**")
if len(np_frame.shape) == 3:  # RGB
    rgb_values = np_frame[:5, :5]
    display_array = np.empty((5, 5), dtype=object)
    for i in range(5):
        for j in range(5):
            pixel = rgb_values[i, j]
            # Convert each channel to native int
            display_array[i, j] = str(tuple(int(x) for x in pixel))
    st.table(display_array)
else:  # Grayscale
    st.table(np_frame[:5, :5])

# ------------------------
# Optional: Download a Frame
# ------------------------
buffer = np_frame
img = Image.fromarray(buffer)
st.download_button("⬇️ Download This Frame", data=img.tobytes(), file_name=f"frame_{frame_index+1}.bmp", mime="image/bmp")





st.title("🎥 How to Set Up a Green Screen Studio")
st.markdown("Welcome to your beginner-friendly guide on creating a professional green screen setup at home or in the studio!")

st.header("🧰 What You'll Need")
st.markdown("""
To build a green screen studio, you'll need the following equipment:

- ✅ Green screen backdrop (fabric or collapsible)
- ✅ Lighting kit (softboxes or LED panels)
- ✅ Camera or smartphone with a tripod
- ✅ Video editing or streaming software (e.g., OBS, Adobe Premiere, Final Cut)
- ✅ Room with space and controlled lighting
""")

# Optional placeholder image
#st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Green_screen_example.jpg/640px-Green_screen_example.jpg", caption="Example green screen setup",)

st.header("🔧 Step-by-Step Setup Guide")

with st.expander("Step 1: Choose the Right Space"):
    st.markdown("""
    Pick a room with minimal natural light to control lighting. Ensure the wall or area behind you is wide and tall enough for the green screen.
    """)

with st.expander("Step 2: Set Up the Green Screen"):
    st.markdown("""
    - Hang or stretch the green fabric tightly to remove wrinkles.
    - Avoid folds or shadows on the screen.
    - You can also use a portable green screen stand.
    """)

with st.expander("Step 3: Lighting the Scene"):
    st.markdown("""
    - Light the green screen evenly from both sides.
    - Use soft, diffused lights (like softboxes).
    - Avoid casting shadows on the screen.
    """)

with st.expander("Step 4: Position the Camera"):
    st.markdown("""
    - Place your camera on a tripod for stability.
    - Ensure you're well-lit separately from the background.
    - Maintain enough distance from the screen to avoid shadows or green spill.
    """)

with st.expander("Step 5: Use Software to Apply Chroma Key"):
    st.markdown("""
    - Use OBS Studio, Premiere Pro, or similar software to remove the green background (chroma key).
    - Adjust threshold and spill settings to fine-tune.
    """)

st.header("💡 Tips for Best Results")
st.markdown("""
- Wear clothing that doesn't contain green.
- Use high-resolution cameras for cleaner keying.
- Keep the subject at least 3–4 feet from the screen.
- Iron or steam the green screen to remove wrinkles.
""")

st.success("You're now ready to build your own green screen studio! 🎬")




