#!/usr/bin/python

import time
from dotstar import Adafruit_DotStar

data_pin   = 23
clock_pin  = 24
strip      = Adafruit_DotStar(0, data_pin, clock_pin)

# Could be BRG or GBR. Figure out later.
# byte 0 is always 0xFF
# Here's the offsets for current (2015+) strips:
rOffset = 2
gOffset = 3
bOffset = 1

# Initialize pins for output
strip.begin()

# Calculate gamma correction table, makes mid-range colors look 'right':
gamma = bytearray(256)
for i in range(256):
  gamma[i] = int(pow(float(i) / 255.0, 2.7) * 255.0 + 0.5)

def rgb_to_data(red, green, blue):
  data = [0xFF, 0x00, 0x00, 0x00]
  data[r_offs] = gamma[red]
  data[g_offs] = gamma[green]
  data[b_offs] = gamma[blue]

print "Displaying..."

solid_time = 1
fade_time = 0.05

print "Off"
strip.show(rgb_to_data(0,0,0))
time.sleep(solid_time)

print "Red"
strip.show(rgb_to_data(255,0,0))
time.sleep(solid_time)

print "Green"
strip.show(rgb_to_data(0,255,0))
time.sleep(solid_time)

print "Blue"
strip.show(rgb_to_data(0,255,0))
time.sleep(solid_time)

print "Off"
strip.show(rgb_to_data(0,255,0))
time.sleep(solid_time)

for color in xrange(3):
  data = [0,0,0]

  for i in xrange(256):
    data[color] = i
    strip.show(rgb_to_data(data[0],data[1],data[2]))
    time.sleep(fade_time)

  for i in xrange(256):
    data[color] = 255-i
    strip.show(rgb_to_data(data[0],data[1],data[2]))
    time.sleep(fade_time)
