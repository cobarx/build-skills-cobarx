"""Draw a bar chart of monthly signups from a CSV file and save it as a PNG.

Usage: python3 scripts/plot_signups.py <signups.csv> <out.png>

The CSV has a header row and two columns, month and signups. Months are drawn left to right in
file order, one bar each. The PNG is 640x360, written with the standard library only.
"""

import csv
import struct
import sys
import zlib

WIDTH, HEIGHT = 640, 360
MARGIN = 20
BACKGROUND = (255, 255, 255)
BAR = (52, 101, 164)
AXIS = (0, 0, 0)


def read_signups(path):
    with open(path, newline="") as f:
        return [(row["month"], int(row["signups"])) for row in csv.DictReader(f)]


def draw(rows):
    """Return the image as a list of pixel rows, y = 0 at the baseline."""
    pixels = [[BACKGROUND] * WIDTH for _ in range(HEIGHT)]
    for x in range(MARGIN, WIDTH - MARGIN):
        pixels[MARGIN][x] = AXIS
    peak = max(count for _, count in rows)
    slot = (WIDTH - 2 * MARGIN) // len(rows)
    for i, (_, count) in enumerate(rows):
        bar_height = round(count / peak * (HEIGHT - 2 * MARGIN - 1))
        left = MARGIN + i * slot + slot // 6
        right = MARGIN + (i + 1) * slot - slot // 6
        for y in range(MARGIN + 1, MARGIN + 1 + bar_height):
            for x in range(left, right):
                pixels[y][x] = BAR
    return pixels


def write_png(path, pixels):
    def chunk(kind, data):
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    raw = b"".join(b"\x00" + bytes(c for px in row for c in px) for row in pixels)
    header = struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", header))
        f.write(chunk(b"IDAT", zlib.compress(raw, 9)))
        f.write(chunk(b"IEND", b""))


def main(src, out):
    # draw() puts the baseline at row 0, and a PNG's row 0 is the top: flip before writing.
    write_png(out, draw(read_signups(src))[::-1])
    print(f"wrote {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
