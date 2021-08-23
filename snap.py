#!/usr/bin/env python3

from sys import argv
from picamera import PiCamera
from datetime import datetime

def resolve_file_name(arguments):
  if len(arguments) == 2:
    return arguments[1]
  else:
    current_date = datetime.now()
    return current_date.strftime('%Y-%m-%d') + '.jpg'


if len(argv) > 2:
  exit("Too many arguments. Halting")

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.awb_mode='incandescent'

camera.capture(resolve_file_name(argv))
