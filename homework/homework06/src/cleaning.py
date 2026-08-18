"""
Reusable pandas functions for cleaning tabular data.
"""

from collections.abc import Iterable

import pandas as pd


def fill_missing_median(
    df: pd.DataFrame, columns: Iterable[str]
) -> pd.DataFrame:
    """
    Return a copy with missing values filled by each column's median.
    """
    cleaned = df.copy()
    for column in columns:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    return cleaned


def drop_missing(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Return a copy without columns exceeding a missing-value threshold.
    """
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    missing_fraction = df.isna().mean()
    columns_to_keep = missing_fraction[missing_fraction <= threshold].index
    return df.loc[:, columns_to_keep].copy()


def normalize_data(
    df: pd.DataFrame, columns: Iterable[str]
) -> pd.DataFrame:
    """
    Return a copy with selected numeric columns scaled from 0 to 1.
    """
    normalized = df.copy()
    for col in columns:
        min_val = normalized[col].min()
        max_val = normalized[col].max()
        normalized[col] = (normalized[col] - min_val) / (max_val - min_val) if max_val != min_val else 0

    return normalized