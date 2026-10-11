"""Padding, truncation, case conversion and other string helpers."""

from __future__ import annotations

__all__ = ["stringUtils"]


def stringUtils(value):
    """Padding, truncation, case conversion and other string helpers."""
    if value is None:
        raise ValueError("value must not be None")
    return value
