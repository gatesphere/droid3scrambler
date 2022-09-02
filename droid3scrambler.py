#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:gatesphere.20220901122505.2: * @file droid3scrambler.py
#@@first
#@@language python
#@@tabwidth -2

#@+<< imports >>
#@+node:gatesphere.20220901122646.1: ** << imports >>
import random
from mido import Message, MetaMessage, MidiFile, MidiTrack
#@-<< imports >>
#@+<< declarations >>
#@+node:gatesphere.20220901122650.1: ** << declarations >>
CHANNEL = 0 # all messages should occur on channel 0
TICK = 2 # all message should happen 2 ticks apart

CC_KEYS = {
  # Control
  'VIP':     16,
  'TYP':     20,
  'CUT':     21,
  'WID':     22,
  'ARP':     23,
  'STP':     24,
  'BIT':     25,
  'CHANNEL': 120,

  # DCO1
  'DCO1WAV': 26,
  'DCO1PW':  27,
  'DCO1OFF': 28,
  'DCO1AMP': 29,
  'DCO1OCT': 30,
  'DCO1FRQ': 31,

  # DCO2
  'DCO2WAV': 102,
  'DCO2PW':  103,
  'DCO2OFF': 104,
  'DCO2AMP': 105,
  'DCO2OCT': 106,
  'DCO2FRQ': 107,

  # EN1
  'EN1A':    108,
  'EN1LV':   109,
  'EN1D':    110,
  'EN1S':    111,
  'EN1R':    112,
  'EN1OFF':  113,

  # EN2
  'EN2A':    114,
  'EN2LV':   115,
  'EN2D':    116,
  'EN2S':    117,
  'EN2R':    118,
  'EN2OFF':  119
}

MATRIX_CONTROLLERS = [ 'En1', 'En2', 'DC1', 'DC2',
                       'Pb',  'Pb2', 'Mod', 'Vel',
                       'V1G', 'Gat', 'Aft', 'KF',
                       'KF2', 'Hld', 'Exp', 'Bth' ]

#@-<< declarations >>

#@+others
#@+node:gatesphere.20220901122700.1: ** main
def main():
  # setup -- generate ID and set seed, and start a midi track
  inst_id = random.randint(0,10000000000)
  random.seed(inst_id)
  mid = MidiFile()
  track = MidiTrack()
  mid.tracks.append(track)
  print(f'Instrument ID: {inst_id}')

  # generate contents
  generate_bits(track)
  generate_filt(track)
  generate_dco1(track)
  generate_dco2(track)
  generate_en1(track)
  generate_en2(track)

  # finish up the track
  track.append(MetaMessage('end_of_track', time=TICK))
  fname = f'{inst_id}.mid'
  mid.save(fname)
  print(f'Instrument saved as: {fname}')
#@+node:gatesphere.20220901211426.1: ** generate_dco
def generate_dco(track, key):
  print(f'=== {key} ===')

  # waveform (0-31, matrix)
  generate_value_matrix(f'{key}WAV', track, maximum=31)

  # octave (0-63)
  generate_value(f'{key}OCT', track, maximum=63)

  # pw/off/amp/frq all 0-255,matrix
  for k in ['PW', 'OFF', 'AMP', 'FRQ']:
    kv = f'{key}{k}'
    generate_value_matrix(kv, track)
#@+node:gatesphere.20220901211433.1: *3* generate_dco1
def generate_dco1(track):
  return generate_dco(track, 'DCO1')
#@+node:gatesphere.20220901211438.1: *3* generate_dco2
def generate_dco2(track):
  return generate_dco(track, 'DCO2')
#@+node:gatesphere.20220901211556.1: ** generate_en
def generate_en(track, key):
  print(f'=== {key} ===')

  # a/lv/d/s/r are all 0-255
  for k in ['A', 'LV', 'D', 'S', 'R']:
    vk = f'{key}{k}'
    generate_value(vk, track)

  # offset can be a matrix or 0-255
  k =  f'{key}OFF'
  generate_value_matrix(k, track)
#@+node:gatesphere.20220901211600.1: *3* generate_en1
def generate_en1(track):
  return generate_en(track, 'EN1')
#@+node:gatesphere.20220901211603.1: *3* generate_en2
def generate_en2(track):
  return generate_en(track, 'EN2')
#@+node:gatesphere.20220901211722.1: ** generate_bits
def generate_bits(track):
  generate_value('BIT', track, binout=True)
#@+node:gatesphere.20220901211742.1: ** generate_filt
def generate_filt(track):
  # typ
  generate_value('TYP', track, binout=True)

  # cut, wid, arp
  for k in ['CUT', 'WID', 'ARP']:
    generate_value_matrix(k, track)

  # stp
  generate_value('STP', track, maximum=7)
#@+node:gatesphere.20220901211918.1: ** generate_cc
def generate_cc(cc_key, val):
  out = []
  mode = 1
  if val >= 128:
    mode = 2
    val -= 128
  out.append(Message('control_change', channel=CHANNEL, control=CC_KEYS['VIP'], value=mode, time=TICK))
  out.append(Message('control_change', channel=CHANNEL, control=CC_KEYS[cc_key], value=val, time=TICK))
  return out
#@+node:gatesphere.20220901211948.1: ** generate_cc_matrix
def generate_cc_matrix(cc_key, val):
  out = []
  mode = 3
  out.append(Message('control_change', channel=CHANNEL, control=CC_KEYS['VIP'], value=mode, time=TICK))
  out.append(Message('control_change', channel=CHANNEL, control=CC_KEYS[cc_key], value=val, time=TICK))
  return out
#@+node:gatesphere.20220902081104.1: ** generate_value
def generate_value(key, track, minimum=0, maximum=255, binout=False):
  val = random.randint(minimum, maximum)
  track.extend(generate_cc(key, val))
  if binout:
    # binary output for BITS and Typ
    print(f'{key}: {bin(val)[2:].rjust(8,"0")} ({val})')
  else:
    print(f'{key}: {val}')
#@+node:gatesphere.20220902081107.1: ** generate_value_matrix
def generate_value_matrix(key, track, minimum=0, maximum=255):
  if random.randint(0,1) == 1:
    # matrix value
    dest = random.randint(0,15)
    val = MATRIX_CONTROLLERS[dest]
    track.extend(generate_cc_matrix(key, dest))
    print(f'{key}: {val}')
  else:
    # normal value
    generate_value(key, track, minimum=minimum, maximum=maximum)
#@-others

if __name__=='__main__':
  main()
#@-leo
