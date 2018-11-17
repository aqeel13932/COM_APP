import socket
import alsaaudio
import wave
import _thread as thread
from time import sleep
# record
CHUNK = 1024 # 512
CHANNELS = 1
RATE = 20000
device = 'default'

# Set input stream (send_stream)
send_stream= alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)
send_stream.setchannels(CHANNELS)
send_stream.setrate(RATE)
send_stream.setformat(alsaaudio.PCM_FORMAT_S16_LE)
send_stream.setperiodsize(CHUNK)
# Set attributes: Mono, 44100 Hz, 16 bit little endian samples
# Set output stream (receive_stream)
out= alsaaudio.PCM(alsaaudio.PCM_PLAYBACK,device=device)
out.setchannels(CHANNELS)
out.setrate(RATE)
out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
out.setperiodsize(CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("138.68.67.116", 50000))
print("Voice chat running")
def receive_data():
    while True:
        try:
            data = s.recv(1024)
            out.write(data)
        except:
            pass


def send_data():
    while True:
        try:
            l,data = send_stream.read()
            if l:
                s.sendall(data)
                sleep(0.001)
                
        except:
            pass

thread.start_new_thread(receive_data, ())
thread.start_new_thread(send_data, ())

while True:
    pass
