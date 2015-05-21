#!/usr/bin/python

import os, zipfile

def generate():
    imageDir = None
    bootloader = None
    radio = None

    for f in os.listdir('./'):
        if f.endswith('.zip') and f.startswith('image'):
            imageDir = f.split('.')[0]
            print 'Unzipping %s ...' % f
            with zipfile.ZipFile(f, 'r') as z:
                z.extractall('./%s/' % imageDir)

    print 'Unzipped Successfully!'

    for f in os.listdir('./'):
        if f.endswith('.img'):
            if f.startswith('bootloader'):
                bootloader = f
            elif f.startswith('radio'):
                radio = f

    print 'Bootloader Detected - %s' % bootloader
    print 'Radio Detected - %s' % radio

    print 'Generating flasher.sh ...'

    commands = open('flasher.sh', 'w')
    commands.write('#!/bin/sh\n\n')
    commands.write('fastboot flash bootloader %s\n' % bootloader)
    commands.write('fastboot reboot-bootloader\n')
    commands.write('sleep 5\n')
    commands.write('fastboot flash radio %s\n' % radio)
    commands.write('fastboot reboot-bootloader\n')
    commands.write('sleep 5\n')
    commands.write('fastboot flash boot %s/boot.img\n' % imageDir)
    commands.write('fastboot flash cache %s/cache.img\n' % imageDir)
    commands.write('fastboot flash system %s/system.img\n' % imageDir)
    commands.write('fastboot flash recovery %s/recovery.img\n' % imageDir)
    commands.write('fastboot reboot\n')
    commands.close()

    os.system('chmod a+x flasher.sh')

    print 'Completed!'

