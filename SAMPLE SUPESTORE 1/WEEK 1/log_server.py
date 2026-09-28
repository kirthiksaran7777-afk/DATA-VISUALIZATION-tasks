"""
log_server_simulator.py
------------------------
Pretends to be 3 "high-velocity" BigBasket warehouse servers
(BigBasket-Chennai, BigBasket-Bangalore, BigBasket-Mumbai).

Each server is a tiny TCP server that, once a client (our harvester daemon)
connects, continuously streams log lines at random intervals.

Run this FIRST in its own terminal and leave it running.
"""

import socket
import threading
import random
import time
from datetime import datetime

# Simulated BigBasket warehouse servers
BRANCHES = [
    ("bigbasket-chennai", 9001),
    ("bigbasket-bangalore", 9002),
    ("bigbasket-mumbai", 9003),
]

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]

# Sample log messages for BigBasket
MESSAGE_TEMPLATES = {
    "INFO": [
        "Order#{oid} placed successfully",
        "Order#{oid} packed at warehouse",
        "Order#{oid} dispatched for delivery",
        "Inventory updated for Product#{oid}",
        "Customer payment received for Order#{oid}",
    ],

    "WARNING": [
        "Low stock detected for Product#{oid}",
        "Delivery delayed for Order#{oid}",
        "Warehouse processing slower than expected for Order#{oid}",
        "High demand detected for Product#{oid}",
    ],

    "ERROR": [
        "Payment failed for Order#{oid}",
        "Order#{oid} cancelled due to out-of-stock items",
        "Inventory synchronization failed for Product#{oid}",
        "Delivery partner unavailable for Order#{oid}",
    ],

    "DEBUG": [
        "Cache miss while fetching Product#{oid}",
        "Retrying database update for Order#{oid}",
        "Warehouse inventory refresh triggered for Product#{oid}",
    ],
}


def build_log_line(branch_name):
    """Build one well-formed BigBasket log line."""
    level = random.choice(LEVELS)
    oid = random.randint(1000, 9999)
    message = random.choice(MESSAGE_TEMPLATES[level]).format(oid=oid)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{timestamp} | {level} | {branch_name} | {message}\n"


def handle_client(conn, branch_name):
    """Continuously stream logs until the client disconnects."""
    print(f"[{branch_name}] Harvester connected. Streaming logs...")

    try:
        while True:
            line = build_log_line(branch_name)
            conn.sendall(line.encode("utf-8"))

            # Random interval simulates high-volume log generation
            time.sleep(random.uniform(0.05, 0.4))

            # Occasionally send a corrupted line to test regex validation
            if random.random() < 0.05:
                conn.sendall(b"CORRUPTED_LINE_NO_STRUCTURE_HERE\n")

    except (BrokenPipeError, ConnectionResetError):
        print(f"[{branch_name}] Harvester disconnected.")

    finally:
        conn.close()


def run_branch_server(branch_name, port):
    """Run one simulated warehouse log server."""

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_sock.bind(("127.0.0.1", port))
    server_sock.listen(1)

    print(f"[{branch_name}] Listening on port {port}...")

    while True:
        conn, addr = server_sock.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(conn, branch_name),
            daemon=True,
        )

        client_thread.start()


if __name__ == "__main__":

    threads = []

    for name, port in BRANCHES:
        t = threading.Thread(
            target=run_branch_server,
            args=(name, port),
            daemon=True,
        )
        t.start()
        threads.append(t)

    print("\nAll simulated BigBasket warehouse servers are running.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nShutting down BigBasket log simulator.")