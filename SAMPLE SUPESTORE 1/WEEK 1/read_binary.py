"""
read_bigbasket_binary_logs.py
-----------------------------
Reads back one BigBasket binary partition file and decodes it into
human-readable log lines. This demonstrates that the .bin files contain
structured, recoverable log data rather than random binary bytes.

Usage:
    python read_bigbasket_binary_logs.py partitions/bigbasket-orders_ERROR.bin
"""

import struct
import sys

# Log level encoding
LEVEL_CODE = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
CODE_LEVEL = {v: k for k, v in LEVEL_CODE.items()}


def read_records(filepath):
    """Read and decode all log records from a binary partition file."""

    with open(filepath, "rb") as f:
        data = f.read()

    offset = 0
    records = []

    while offset < len(data):

        # First 4 bytes indicate the length of the record
        (record_len,) = struct.unpack_from("!I", data, offset)
        offset += 4

        # Extract the complete record
        record_bytes = data[offset:offset + record_len]
        offset += record_len

        # Decode header
        # 19s -> Timestamp
        # B   -> Log level
        # H   -> Service name length
        ts_bytes, level_byte, service_len = struct.unpack_from(
            "!19sBH", record_bytes, 0
        )

        pos = 19 + 1 + 2

        # Decode service name
        service = record_bytes[pos:pos + service_len].decode("utf-8")
        pos += service_len

        # Decode message length
        (message_len,) = struct.unpack_from("!H", record_bytes, pos)
        pos += 2

        # Decode log message
        message = record_bytes[pos:pos + message_len].decode("utf-8")

        records.append(
            {
                "timestamp": ts_bytes.decode("ascii").strip(),
                "level": CODE_LEVEL[level_byte],
                "service": service,
                "message": message,
            }
        )

    return records


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python read_bigbasket_binary_logs.py <path-to-.bin-file>")
        sys.exit(1)

    filepath = sys.argv[1]

    records = read_records(filepath)

    print(f"\nFound {len(records)} log records in {filepath}:\n")

    for r in records:
        print(
            f"{r['timestamp']} | "
            f"{r['level']} | "
            f"{r['service']} | "
            f"{r['message']}"
        )
        