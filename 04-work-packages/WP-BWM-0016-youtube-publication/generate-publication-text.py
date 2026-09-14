#!/usr/bin/env python3
"""Generate the retained transcript and WebVTT from approved narration data."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def timestamp(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{milliseconds:03d}"


def sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text.strip()) if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("content", type=Path)
    parser.add_argument("timeline", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    content = json.loads(args.content.read_text())
    timeline = json.loads(args.timeline.read_text())
    content_by_id = {section["id"]: section for section in content["sections"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)

    transcript = [
        "# The Biblical WorldModel — The Story",
        "",
        "Language: English (`en`)",
        "",
        "Source: https://worldmodel.thinxai.net/the-story/",
        "",
        "Transcript for the approved revision-3 full-length narrated video.",
        "",
    ]
    vtt = ["WEBVTT", ""]

    cursor = 0.0
    cue = 1
    for timed in timeline["sections"]:
        section = content_by_id[timed["id"]]
        narration = section["narration"].strip()
        transcript.extend([f"## {section['text']}", "", narration, ""])

        parts = sentences(narration)
        spoken_seconds = timed["narrationFrames"] / timeline["fps"]
        weights = [max(1, len(re.findall(r"\w+", part))) for part in parts]
        total_weight = sum(weights)
        part_start = cursor
        for index, (part, weight) in enumerate(zip(parts, weights)):
            part_end = cursor + spoken_seconds if index == len(parts) - 1 else part_start + spoken_seconds * weight / total_weight
            vtt.extend([str(cue), f"{timestamp(part_start)} --> {timestamp(part_end)}", part, ""])
            part_start = part_end
            cue += 1
        cursor += timed["durationInFrames"] / timeline["fps"]

    (args.output_dir / "transcript.md").write_text("\n".join(transcript).rstrip() + "\n")
    (args.output_dir / "captions.vtt").write_text("\n".join(vtt).rstrip() + "\n")


if __name__ == "__main__":
    main()
