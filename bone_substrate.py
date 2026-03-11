"""bone_substrate.py"""
import os
from typing import List, Dict
from bone_types import Prisma

class TheSubstrate:
    """
    The Physical Hands of the machine.
    Allows the system to write files directly to the host OS.
    """
    def __init__(self, events_ref):
        self.events = events_ref
        self.pending_writes: List[Dict[str, str]] = []

    def queue_write(self, path: str, content: str):
        self.pending_writes.append({"path": path, "content": content})

    def execute_writes(self, stamina_pool: float) -> tuple[List[str], float]:
        logs = []
        cost = 0.0

        # Ensure a directory exists for output to keep the root clean
        if not os.path.exists("output"):
            os.makedirs("output")

        for write in self.pending_writes:
            # Prevent directory traversal attacks by forcing it to the output folder
            safe_name = os.path.basename(write["path"])
            safe_path = os.path.join("output", safe_name)

            content = write["content"]
            size = len(content)
            write_cost = size * 0.02 # 2 stamina per 100 characters

            if stamina_pool - cost < write_cost:
                logs.append(f"{Prisma.RED}SUBSTRATE FAULT: Insufficient stamina to forge {safe_name}.{Prisma.RST}")
                continue

            try:
                with open(safe_path, "w", encoding="utf-8") as f:
                    f.write(content)
                cost += write_cost
                logs.append(f"{Prisma.GRN}SUBSTRATE: Physically forged {safe_path} ({size} bytes).{Prisma.RST}")
            except Exception as e:
                logs.append(f"{Prisma.RED}SUBSTRATE FAULT: Write failed - {e}{Prisma.RST}")

        self.pending_writes.clear()
        return logs, cost