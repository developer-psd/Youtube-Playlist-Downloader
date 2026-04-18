# YouTube Playlist Downloader

A simple Python script for downloading an entire YouTube playlist from a playlist link using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

## Features

- Downloads all videos from a YouTube playlist
- Supports three quality presets:
  - `low` → best available up to 480p
  - `medium` → best available up to 720p
  - `high` → best available quality
- Saves videos into a folder named after the playlist
- Prefixes filenames with playlist index when available
- Skips unavailable/private videos instead of stopping the whole playlist
- Resumes partial downloads when possible

## Requirements

- Python 3.8+
- `yt-dlp`
- `ffmpeg` (optional but strongly recommended for merging best video + audio streams)

## Usage
python download.py <playlist_link> <low|medium|high>

## Installation

Clone the repo and install dependencies:

```bash
pip install -r requirements.txt

