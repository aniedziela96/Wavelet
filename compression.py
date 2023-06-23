import pywt
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import wave
import sounddevice as sd

samplerate, data = wavfile.read('dataset/kobietamniebije.wav')

t = np.arange(len(data)) / float(samplerate)
np.arange(len(data))

sd.wait()
sd.play(data, samplerate)
sd.wait()

data = data / max(data) # normalization 

coeffs = pywt.wavedec(data, 'bior6.8', 'per')

epsilon = 0.01
k = 0
for i in range(1, len(coeffs)):
    for j in range(len(coeffs[i])):
        if abs(coeffs[i][j]) < epsilon:
            coeffs[i][j] = 0
            k += 1

print(k/len(data))

compressed = pywt.waverec(coeffs, 'bior6.8', 'per')


# cA, cD = pywt.dwt(data, 'bior6.8', 'per')
# wavfile.write('sounds/samplecD.wav', samplerate, cD)
# wavfile.write('sounds/samplecA.wav', samplerate, cA)

# new = pywt.idwt(cA, cD, "bior6.8", 'per')
# wavfile.write('sounds/sample.wav', samplerate, new)

sd.wait()
sd.play(compressed, samplerate)
sd.wait()

v = [-1, 0, 1]
v = [1, 0]
