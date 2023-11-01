import argparse
from fetchtube.core import download_video, download_audio, get_qualities, display_qualities
from pathlib import Path

DOWNLOADS_PATH = str(Path.home() / "Downloads")
FETCH_VERSION = "0.0.1"

def main():
    parser = argparse.ArgumentParser(description="Fetch - YouTube Video and Audio Downloader")

    parser.add_argument("url", help="URL of the YouTube video to download")
    parser.add_argument("-o", "--output", help="Specify the output directory for downloaded files")
    parser.add_argument("-v", "--video", action="store_true", help="Download video")
    parser.add_argument("-a", "--audio", action="store_true", help="Download audio")
    parser.add_argument("-q", "--quality", help="Preferred quality (e.g., '1080p' or '128kbps')")
    parser.add_argument("-l", "--list-qualities", action="store_true", help="List available video and audio qualities")
    parser.add_argument("--oauth", action="store_true", help="Use OAuth for authentication")

    args = parser.parse_args()

    if args.list_qualities:
        qualities = get_qualities(args.url)
        if qualities:
            display_qualities(qualities)
    else:
        output_path = args.output if args.output else DOWNLOADS_PATH  # Use Downloads folder if no output directory is provided

        if args.video:
            preferred_quality = args.quality if args.quality else "1080p"
            oauth = args.oauth if args.oauth else False
            download_video(args.url, output_path, preferred_quality, oauth=oauth)
        elif args.audio:
            preferred_quality = args.quality if args.quality else "128kbps"
            oauth = args.oauth if args.oauth else False
            download_audio(args.url, output_path, preferred_quality, oauth=oauth)


if __name__ == "__main__":
    main()