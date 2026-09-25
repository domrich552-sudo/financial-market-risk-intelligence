"""Chronological validation helpers."""

from sklearn.model_selection import TimeSeriesSplit

def chronological_splits(n_splits=5):
    return TimeSeriesSplit(n_splits=n_splits)
