#!/usr/bin/env python3
import argparse
import sys

import yt_dlp


QUALITY_PRESETS = {
    # Best effort at or below 480p
    "low": "bestvideo*[height<=480]+bestaudio/best[height<=480]",
    # Best effort at or below 720p
    "medium": "bestvideo*[height<=720]+bestaudio/best[height<=720]",
    # Best available quality
    "high": "bestvideo*+bestaudio/best",
}


def build_ydl_opts(quality: str) -> dict:
    return {
        "format": QUALITY_PRESETS[quality],
        # Put videos into a folder named after the playlist.
        # If playlist_index exists, prefix the filename with it.
        "outtmpl": {
            "default": "%(playlist)s/%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
        },
        "noplaylist": False,
        "ignoreerrors": True,   # skip unavailable/private videos instead of aborting all
        "continuedl": True,     # resume partial downloads when possible
        "quiet": False,
        "no_warnings": False,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="download.py",
        description="Download an entire YouTube playlist with a quality preset.",
        usage="python download.py <link> <low|medium|high>",
    )
    parser.add_argument("link", help="YouTube playlist link")
    parser.add_argument("quality", choices=QUALITY_PRESETS.keys(), help="Quality preset")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        with yt_dlp.YoutubeDL(build_ydl_opts(args.quality)) as ydl:
            result = ydl.download([args.link])
            return int(bool(result))
    except KeyboardInterrupt:
        print("\nDownload cancelled by user.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
