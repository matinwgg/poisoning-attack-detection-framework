from __future__ import annotations
import numpy as np

def robust_zscore(matrix: np.ndarray, threshold: float = 3.0) -> np.ndarray:
    x=np.asarray(matrix,dtype=float)
    if x.ndim != 2 or x.shape[0] < 2: raise ValueError('expected at least two client updates')
    med=np.median(x,axis=0); mad=np.median(np.abs(x-med),axis=0); scale=1.4826*np.maximum(mad,1e-12)
    scores=np.max(np.abs((x-med)/scale),axis=1)
    return scores > threshold

def label_flip(labels: np.ndarray, classes: int) -> np.ndarray:
    if classes < 2: raise ValueError('at least two classes')
    y=np.asarray(labels).copy(); return (y+1)%classes
