"""Reusable helpers"""

from __future__ import annotations

from datetime import date, datetime
import re
from typing import Iterable


def clean_column_name(name: object) -> str:
    """Convert a column label to lowercase ``snake_case``.
    """
    cleaned = re.sub(r"[^a-z0-9]+", "_", str(name).strip().lower())
    return cleaned.strip("_")


def clean_column_names(names: Iterable[object]) -> list[str]:
    """Return column labels converted to lowercase ``snake_case``."""
    return [clean_column_name(name) for name in names]


def parse_date(value: str | date | datetime, format: str | None = None) -> date:
    """Parse a value into a :class:`datetime.date`.

    String values use ISO 8601 by default (for example, ``2026-08-17``).
    Supply ``format`` for other representations, such as ``%m/%d/%Y``.

    Raises:
        TypeError: If ``value`` is not a string, date, or datetime.
        ValueError: If a string cannot be parsed with the requested format.
    """
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        raise TypeError("value must be a string, date, or datetime")

    text = value.strip()
    if format is not None:
        return datetime.strptime(text, format).date()
    return date.fromisoformat(text)
