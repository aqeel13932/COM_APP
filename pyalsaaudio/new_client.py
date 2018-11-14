import socket
import alsaaudio
import wave
import _thread as thread

# record
CHUNK = 1024 # 512
CHANNELS = 1
RATE = 20000
device = 'default'

receive_stream= alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)
send_stream= alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device)

# Set attributes: Mono, 44100 Hz, 16 bit little endian samples
send_stream.setchannels(CHANNELS)
receive_stream.setchannels(CHANNELS)
send_stream.setrate(RATE)
receive_stream.setrate(RATE)
send_stream.setformat(alsaaudio.PCM_FORMAT_S16_LE)
receive_stream.setformat(alsaaudio.PCM_FORMAT_S16_LE)
send_stream.setperiodsize(CHUNK)
receive_stream.setperiodsize(CHUNK)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("138.68.67.116", 50000))
print("Voice chat running")
def receive_data():
    while True:
        try:
            data = s.recv(1024)
            print(data)
            receive_stream.write(data)
        except:
            pass


def send_data():
    while True:
        try:
            l,data = send_stream.read(CHUNK)
            if l:
                s.sendall(data)
        except:
            pass

thread.start_new_thread(receive_data, ())
thread.start_new_thread(send_data, ())

while True:
    pass
