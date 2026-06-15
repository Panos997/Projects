"""
Live People Counter (no recording required)
=============================================

Reads a live video stream (webcam, RTSP/IP camera, or video file), runs
YOLO person detection + tracking on each frame, and reports:

  - INSTANT COUNT: number of people visible in the current frame
  - CUMULATIVE COUNT: number of *unique* people seen since the program
    started (based on tracker IDs, so the same person isn't double-counted
    across consecutive frames)

No video is saved to disk. Frames are processed in memory and discarded.

Configuration is read from environment variables (with sensible defaults),
so the same script runs unchanged on a laptop, in Docker, or on a cloud VM -
only the environment differs.

Environment variables:
    SOURCE            Camera index, RTSP/HTTP URL, or video file path.
                       Default: "0" (first webcam)
    MODEL_NAME         YOLO weights file. Default: "yolov8n.pt"
    CONF_THRESHOLD      Detection confidence threshold. Default: "0.4"
    SHOW_WINDOW        "true"/"false" - show a live OpenCV window.
                       Default: "true". Set "false" for headless/cloud use.
    PRINT_EVERY_N      Console stats print interval (frames). Default: "30"

Examples:
    # Local webcam, with display window
    python people_counter.py

    # IP camera RTSP stream, headless (e.g. cloud VM)
    SOURCE="rtsp://user:pass@192.168.1.50/stream1" SHOW_WINDOW=false \\
        python people_counter.py

    # Test against a video file
    SOURCE="/path/to/video.mp4" python people_counter.py
"""

import os
import time

import cv2
from ultralytics import YOLO

# In the COCO dataset (used by default YOLO weights), class 0 = "person"
PERSON_CLASS_ID = 0


def _env_bool(name, default):
    return os.environ.get(name, str(default)).strip().lower() in ("1", "true", "yes", "on")


def _env_source(name, default):
    """Camera index (int) if numeric, otherwise treat as a path/URL string."""
    value = os.environ.get(name, default)
    return int(value) if str(value).isdigit() else value


def load_config():
    return {
        "source": _env_source("SOURCE", "0"),
        "model_name": os.environ.get("MODEL_NAME", "yolov8n.pt"),
        "conf_threshold": float(os.environ.get("CONF_THRESHOLD", "0.4")),
        "show_window": _env_bool("SHOW_WINDOW", True),
        "print_every_n": int(os.environ.get("PRINT_EVERY_N", "30")),
    }


def main():
    cfg = load_config()
    model = YOLO(cfg["model_name"])

    cap = cv2.VideoCapture(cfg["source"])
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {cfg['source']!r}")

    unique_ids_seen = set()
    frame_idx = 0
    start_time = time.time()

    print(f"Config: {cfg}")
    print("Starting live people counting. Press 'q' to quit (if window shown).")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Stream ended or frame not received - stopping.")
                break

            frame_idx += 1

            # Run detection + tracking in one call. persist=True keeps track
            # IDs consistent across frames within this session.
            results = model.track(
                frame,
                persist=True,
                classes=[PERSON_CLASS_ID],
                conf=cfg["conf_threshold"],
                verbose=False,
            )

            result = results[0]
            instant_count = 0

            if result.boxes is not None and len(result.boxes) > 0:
                instant_count = len(result.boxes)

                # Track IDs may be None for the first frame(s) before the
                # tracker has assigned an ID
                if result.boxes.id is not None:
                    for track_id in result.boxes.id.int().tolist():
                        unique_ids_seen.add(track_id)

            cumulative_count = len(unique_ids_seen)

            # --- Console reporting ---
            if frame_idx % cfg["print_every_n"] == 0:
                elapsed = time.time() - start_time
                fps = frame_idx / elapsed if elapsed > 0 else 0
                print(
                    f"[frame {frame_idx}] "
                    f"instant_count={instant_count} | "
                    f"cumulative_unique={cumulative_count} | "
                    f"fps={fps:.1f}"
                )

            # --- Optional live display ---
            if cfg["show_window"]:
                annotated = result.plot()  # draws boxes + track IDs
                overlay_text = (
                    f"In frame: {instant_count}  |  "
                    f"Total unique seen: {cumulative_count}"
                )
                cv2.putText(
                    annotated, overlay_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
                )
                cv2.imshow("Live People Counter", annotated)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    print("Quit requested.")
                    break

    finally:
        cap.release()
        if cfg["show_window"]:
            cv2.destroyAllWindows()

        print("\n--- Final summary ---")
        print(f"Frames processed: {frame_idx}")
        print(f"Unique people seen (cumulative): {len(unique_ids_seen)}")


if __name__ == "__main__":
    main()
