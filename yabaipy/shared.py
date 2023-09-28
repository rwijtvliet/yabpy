"""Shared functions."""

import subprocess


def run_command(command: str) -> str:
    """Run command in subprocess, returning the result if successful."""
    result = subprocess.run(
        command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        raise ValueError(result.stderr.decode("utf-8"))
    return result.stdout.decode("utf-8")
