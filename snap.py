#!/usr/bin/env python3

from sys import argv
from camera import Camera, get_timestamp_filename
from datetime import datetime

def resolve_file_name(arguments):
  if len(arguments) == 2:
    return arguments[1]
  else:
    return get_timestamp_filename() 

if len(argv) > 2:
  exit("Too many arguments. Halting")

camera = Camera()
camera.take_picture(resolve_file_name(argv))


