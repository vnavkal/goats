#!/usr/bin/env bash

ffmpeg -i https://stream-us1-charlie.dropcam.com/nexus_aac/34f0486df1e74532bd4b0da5e2612870/chunklist_w219577946.m3u8 -safe 0 -vcodec libx264 -crf 25 -pix_fmt yuv420p goats.mp4
