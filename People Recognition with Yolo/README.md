# Live People Counter (YOLO)

Counts people in a live video stream — **no recording required**. Frames
are processed in memory and discarded immediately.

Two numbers are tracked:

- **Instant count** — how many people are visible in the current frame
- **Cumulative count** — how many *unique* people have been seen since the
  program started (based on tracker IDs, so the same person isn't
  double-counted frame-to-frame)

## How it works

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) (`yolov8n.pt`
  by default) detects people in each frame
- The built-in tracker (ByteTrack, via `model.track()`) assigns persistent
  IDs across frames
- Instant count = number of detections in the current frame
- Cumulative count = size of the set of all track IDs ever seen

## Requirements

- Python 3.9+
- A camera source: USB webcam, RTSP/IP camera stream, or a video file (for
  testing)

## Setup

```bash
git clone <this-repo-url>
cd <this-repo>

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

pip install -r requirements.txt
```

The YOLO model weights (`yolov8n.pt`, ~6 MB) download automatically on first
run.

## Running

All settings are read from environment variables, so the same script works
unchanged on a laptop, in a container, or on a cloud VM.

| Variable          | Default     | Description                                              |
|-------------------|-------------|-----------------------------------------------------------|
| `SOURCE`          | `0`         | Webcam index, RTSP/HTTP URL, or video file path           |
| `MODEL_NAME`      | `yolov8n.pt`| YOLO weights (`yolov8n/s/m/l/x.pt` — bigger = more accurate, slower) |
| `CONF_THRESHOLD`  | `0.4`       | Minimum detection confidence to count as a person         |
| `SHOW_WINDOW`     | `true`      | Show a live annotated window (`false` for headless/cloud) |
| `PRINT_EVERY_N`   | `30`        | How often (in frames) to print stats to the console       |

### Examples

**Local webcam, with display window:**
```bash
python people_counter.py
```

**IP camera (RTSP), headless — e.g. on a cloud VM with no display:**
```bash
SOURCE="rtsp://user:pass@192.168.1.50/stream1" SHOW_WINDOW=false \\
    python people_counter.py
```

**Test against a video file:**
```bash
SOURCE="/path/to/video.mp4" python people_counter.py
```

**Higher accuracy (needs a GPU for real-time performance):**
```bash
MODEL_NAME="yolov8s.pt" python people_counter.py
```

## Where to run it

GitHub itself only stores the code — it doesn't run a live video loop.
Pick a runtime based on where your camera lives:

- **Local PC / mini-PC near the camera** — simplest, lowest latency, no
  ongoing cost. Good if the camera is on your local network.
- **Cloud VM** (AWS/GCP/DigitalOcean/etc.) — good if the camera already
  streams over the internet (RTSP/HTTP), or you want remote access. Add a
  GPU instance if you switch to `yolov8s`/`yolov8m` for better accuracy.
- **Edge device** (Raspberry Pi, NVIDIA Jetson) — purpose-built, low power,
  sits next to the camera permanently.

The script doesn't change between these — only `SOURCE` and your
environment variables do.

## Known limitations

- The cumulative count relies on tracking. If a person is fully occluded for
  a long time or leaves and re-enters the frame later, they may be assigned
  a new track ID and counted again. For accurate footfall counting (people
  *entering* an area), a line-crossing / zone-based approach is more
  reliable than "all unique IDs ever seen" — extend `people_counter.py` if
  you need this.
- RTSP streams over the public internet should be secured (VPN, auth,
  firewall rules) — don't expose camera credentials in plain URLs in
  committed code. Use environment variables or a `.env` file (already
  excluded via `.gitignore`).
