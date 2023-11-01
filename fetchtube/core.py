import os
from pathlib import Path
from pytube import YouTube

DOWNLOADS_PATH = str(Path.home() / "Downloads")

def find_best_quality(streams, preferred_quality):
    # Sort the streams by quality in descending order
    sorted_streams = sorted(streams, key=lambda s: s.resolution if preferred_quality.isdigit() else s.abr, reverse=True)

    for stream in sorted_streams:
        if (stream.resolution if preferred_quality.isdigit() else stream.abr) <= preferred_quality:
            return stream

    return None


def download_video(url, output_path=DOWNLOADS_PATH, preferred_quality="1080p", oauth=False):
    try:
        yt = YouTube(url, use_oauth=oauth, allow_oauth_cache=oauth)
        available_streams = yt.streams.filter(file_extension='mp4', progressive=True)

        selected_stream = find_best_quality(available_streams, preferred_quality)

        if selected_stream:
            print(f"Downloading '{yt.title}' video in {selected_stream.resolution}...")
            selected_stream.download(output_path)
            print(f"'{yt.title}' video downloaded to {output_path}")
        else:
            print(f"No suitable video stream found for '{yt.title}' video.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def download_audio(url, output_path=DOWNLOADS_PATH, preferred_quality="128kbps", oauth=False):
    try:
        yt = YouTube(url, use_oauth=oauth, allow_oauth_cache=oauth)
        available_streams = yt.streams.filter(only_audio=True, file_extension='mp4')

        selected_stream = find_best_quality(available_streams, preferred_quality)

        if selected_stream:
            print(f"Downloading '{yt.title}' audio in {selected_stream.abr}...")
            file_path = selected_stream.download(output_path)

            base, ext = os.path.splitext(file_path)
            os.rename(file_path, base + '.mp3')

            print(f"'{yt.title}' audio downloaded to {output_path}")
        else:
            print(f"No suitable audio stream found for '{yt.title}' video.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_qualities(url, oauth=False):
    try:
        yt = YouTube(url, use_oauth=oauth, allow_oauth_cache=oauth)
        available_video_streams = yt.streams.filter(file_extension='mp4', progressive=True)
        available_audio_streams = yt.streams.filter(only_audio=True, file_extension='mp4')

        video_qualities = [stream.resolution for stream in available_video_streams]
        audio_qualities = [stream.abr for stream in available_audio_streams]

        return {
            "Video Qualities": video_qualities,
            "Audio Qualities": audio_qualities,
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def display_qualities(qualities):
    if qualities is not None:
        print("Available Video Qualities:")
        for quality in qualities["Video Qualities"]:
            print(f"  - {quality}")

        print("Available Audio Qualities:")
        for quality in qualities["Audio Qualities"]:
            print(f"  - {quality}")
    else:
        print("No qualities available.")

