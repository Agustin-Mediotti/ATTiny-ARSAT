import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import sys

def process_audio(filename):
    # Load audio file
    y, sr = librosa.load(filename, sr=None)

    # Generate the spectrogram
    S = np.abs(librosa.stft(y))
    frequencies = librosa.fft_frequencies(sr=sr)
    times = librosa.frames_to_time(np.arange(S.shape[1]), sr=sr)

    # Identify peaks in the spectrogram
    peak_frequencies = []
    peak_durations = []

    prev_peak = None
    duration = 0

    for i in range(S.shape[1]):
        spectrum = S[:, i]
        peak_indices, _ = find_peaks(spectrum, height=np.max(spectrum) * 0.5)  # Detect peaks
        if peak_indices.size > 0:
            peak_freq = frequencies[peak_indices[0]]
            if prev_peak is None:
                prev_peak = peak_freq
            if peak_freq == prev_peak:
                duration += 1
            else:
                peak_frequencies.append(prev_peak)
                peak_durations.append(duration * librosa.frames_to_time(1, sr=sr))
                prev_peak = peak_freq
                duration = 1
        else:
            if prev_peak is not None:
                peak_frequencies.append(prev_peak)
                peak_durations.append(duration * librosa.frames_to_time(1, sr=sr))
                prev_peak = None
                duration = 0

    # Add the last frequency and duration if they exist
    if prev_peak is not None:
        peak_frequencies.append(prev_peak)
        peak_durations.append(duration * librosa.frames_to_time(1, sr=sr))

    # Convert durations to milliseconds and ensure they are within the uint8_t range
    peak_durations_ms = [int(d * 1000) for d in peak_durations]
    peak_durations_ms = [min(d, 255) for d in peak_durations_ms]  # Limit to 255 ms

    # Save frequencies to a file
    with open('frequencies.h', 'w') as f:
        f.write("const uint16_t frequencies[] PROGMEM = {")
        f.write(", ".join(f"{int(freq)}" for freq in peak_frequencies))
        f.write("};\n")

    # Save durations to a file
    with open('durations.h', 'w') as f:
        f.write("const uint8_t durations[] PROGMEM = {")
        f.write(", ".join(f"{d}" for d in peak_durations_ms))
        f.write("};\n")

    # Save the spectrogram as an image
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), sr=sr, x_axis='time', y_axis='log')
    plt.scatter(times[:len(peak_frequencies)], peak_frequencies, color='red')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram and detected peaks')
    plt.savefig('spectrogram_and_peaks.png')
    plt.close()  # Close figure to free memory

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sstv_to_freq.py <audio_file.wav>")
        sys.exit(1)

    audio_file = sys.argv[1]
    process_audio(audio_file)
