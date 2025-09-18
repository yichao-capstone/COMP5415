import streamlit as st
import numpy as np
import soundfile as sf
import io
from scipy.signal import resample
from scipy.fft import fft, fftfreq
import plotly.graph_objects as go


st.title("🎧 Digital Audio")

# ------------------------
# Sidebar Controls
# ------------------------
st.sidebar.header("🎛️ Controls")

waveform_type = st.sidebar.selectbox("Waveform", ["Sine", "Square", "Sawtooth", "Triangle"])
frequency = st.sidebar.slider("Frequency (Hz)", 100, 2000, 440)
duration = st.sidebar.slider("Duration (s)", 0.5, 3.0, 1.0, 0.1)
sample_rate = st.sidebar.selectbox("Sample Rate (Hz)", [8000, 16000, 22050, 44100, 48000], index=3)
bit_depth = st.sidebar.selectbox("Bit Depth (conceptual)", [8, 16, 24, 32], index=1)
pitch_semitones = st.sidebar.slider("Pitch Shift (Semitones)", -12, 12, 0)

# ------------------------
# Waveform Generators
# ------------------------
def generate_waveform(wave_type, freq, duration, sr):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    if wave_type == "Sine":
        y = np.sin(2 * np.pi * freq * t)
    elif wave_type == "Square":
        y = np.sign(np.sin(2 * np.pi * freq * t))
    elif wave_type == "Sawtooth":
        y = 2 * (t * freq - np.floor(t * freq + 0.5))
    elif wave_type == "Triangle":
        y = 2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
    return t, y

def shift_pitch(signal, semitones, sr):
    factor = 2 ** (semitones / 12)
    new_len = int(len(signal) / factor)
    return resample(signal, new_len)

# ------------------------
# Generate Original Waveform
# ------------------------
t, y_original = generate_waveform(waveform_type, frequency, duration, sample_rate)
y_original = 0.5 * y_original  # Normalize

# Apply pitch shift
y_shifted = shift_pitch(y_original, pitch_semitones, sample_rate)

# ------------------------
# Display Conceptual Info
# ------------------------
st.markdown("## 🧠 Digital Audio Concepts")
st.markdown("""
**Digital Audio** represents sound with samples.  
- **Sample Rate:** How often audio is sampled per second  
- **Bit Depth:** How precise each sample is  
- **Waveform:** Shape of the sound wave  
- **Pitch Shift:** Changing playback rate to raise/lower pitch  
""")

# ------------------------
# Audio Players
# ------------------------
st.markdown("## 🎧 Listen to Audio")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Original Tone**")
    buffer1 = io.BytesIO()
    sf.write(buffer1, y_original, sample_rate, format="WAV")
    buffer1.seek(0)
    st.audio(buffer1, format="audio/wav")
with col2:
    st.markdown(f"**Pitch Shifted Tone ({pitch_semitones:+} semitones)**")
    buffer2 = io.BytesIO()
    sf.write(buffer2, y_shifted, sample_rate, format="WAV")
    buffer2.seek(0)
    st.audio(buffer2, format="audio/wav")

# ------------------------
# Time-Domain Waveform Plot
# ------------------------
st.markdown("## 📈 Waveform Comparison")

plot_len = int(sample_rate * 0.03)  # show first 30 ms
fig_wave = go.Figure()
fig_wave.add_trace(go.Scatter(x=t[:plot_len], y=y_original[:plot_len], name="Original", line=dict(color="blue")))
t_shifted = np.linspace(0, len(y_shifted) / sample_rate, len(y_shifted))
fig_wave.add_trace(go.Scatter(x=t_shifted[:plot_len], y=y_shifted[:plot_len], name="Shifted", line=dict(color="red")))
fig_wave.update_layout(xaxis_title="Time (s)", yaxis_title="Amplitude", height=300)
st.plotly_chart(fig_wave, use_container_width=True)

# ------------------------
# Frequency Spectrum Plot
# ------------------------
st.markdown("## 🔬 Frequency Spectrum (FFT)")

def compute_fft(signal, sr):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sr)
    xf = xf[:N // 2]
    yf = 2.0 / N * np.abs(yf[:N // 2])
    yf_db = 20 * np.log10(yf + 1e-10)
    return xf, yf_db

xf1, yf1 = compute_fft(y_original, sample_rate)
xf2, yf2 = compute_fft(y_shifted, sample_rate)

fig_fft = go.Figure()
fig_fft.add_trace(go.Scatter(x=xf1, y=yf1, name="Original", line=dict(color="blue")))
fig_fft.add_trace(go.Scatter(x=xf2, y=yf2, name="Shifted", line=dict(color="red")))
fig_fft.update_layout(xaxis_title="Frequency (Hz)", yaxis_title="Magnitude (dB)", height=350, xaxis_range=[0, 5000])
st.plotly_chart(fig_fft, use_container_width=True)

# ------------------------
# Download Buttons
# ------------------------
st.markdown("## 💾 Download Audio")

col3, col4 = st.columns(2)
with col3:
    st.download_button("⬇️ Download Original", buffer1, file_name="original.wav", mime="audio/wav")
with col4:
    st.download_button("⬇️ Download Shifted", buffer2, file_name="shifted.wav", mime="audio/wav")
