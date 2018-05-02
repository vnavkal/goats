#!/usr/bin/env bash

set -e

SOURCE_URL="https://stream-us1-charlie.dropcam.com/nexus_aac/34f0486df1e74532bd4b0da5e2612870/chunklist_w219577946.m3u8"

while getopts ":o:l:" opt; do
    case $opt in
        o) output_dir="$OPTARG"
           ;;
        l) log_path="$OPTARG"
           ;;
        \?) echo "Invalid option -$OPTARG" >&2
            ;;
    esac
done

ffmpeg \
    -i $SOURCE_URL \
    -safe 0 \
    -vcodec libx264 \
    -crf 25 \
    -pix_fmt yuv420p \
    -f stream_segment \
    -segment_format mpegts \
    -segment_time 60 \
    -reset_timestamps 1 \
    -strftime 1 \
    "$output_dir"goat_%s.mp4 \
    2> $log_path
