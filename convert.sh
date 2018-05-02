set -e

while getopts ":i:o:" opt; do
    case $opt in
        i) input_dir="$OPTARG"
           ;;
        o) output_dir="$OPTARG"
           ;;
        \?) echo "Invalid option -$OPTARG" >&2
            ;;
    esac
done

for path in "$input_dir"*.mp4; do
    echo $input_dir"*.mp4"
    echo $path
    filename=$(basename -- "$path")
    filename_noextension="${filename%.*}"
    echo "1"
    echo $input_dir
    echo "2"
    echo $filename_noextension
    echo "3"
    output_dir_thisimage=$output_dir$filename_noextension
    mkdir -p $output_dir_thisimage
    echo $output_dir_thisimage
    ffmpeg \
        -i "$input_dir$filename" \
        -f image2 \
        $output_dir_thisimage/image-%05d.bmp
done
