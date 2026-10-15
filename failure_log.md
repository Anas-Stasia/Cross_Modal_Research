# Failure Log and Research Limitations

This log records issues described in the paper. It does not invent failed software runs; the paper does not include a run-by-run debugging log.

| ID | Issue / observation | Evidence in paper | Interpretation |
|---|---|---|---|
| F-01 | MDS does not meaningfully predict engagement | Spearman rho: plays 0.036; likes 0.037; comments 0.014; shares -0.015 | Treat as a substantive null finding, not automatically as experiment failure. |
| F-02 | MDS effect disappears under controls | Log-plays coefficient 0.003, p = .951; R² = 0.316 | Do not claim MDS predicts engagement. |
| F-03 | Trained and PCA measures agree weakly | rho = 0.027, p = .057 | Potential construct-validity limitation. |
| F-04 | Encoders are unimodal | Independently trained text/audio/visual encoders | Retrieval success does not prove human-valid divergence. |
| F-05 | Sampling is narrow | Five-day Explore-page snapshot | Limited generalizability. |
| F-06 | Engagement is a snapshot | One scrape per video after deduplication | Cannot model engagement trajectories reliably. |
| F-07 | PCA baseline fits PCA on the full sample | Stated in paper | Possible held-out information leakage; retain for exact comparison and report train-only PCA separately as an improvement. |
| F-08 | Captions may be hashtag-driven | Discussed in paper | Score may not reflect meaningful contradiction. |

## Implementation run log
No implementation failures or debugging traces are supplied in the paper. Add observed failures below rather than guessing.

| Date / run ID | Environment/configuration | Failure or deviation | Evidence | Resolution |
|---|---|---|---|---|
| To be completed | Not specified | No run-by-run log included in source paper | Not available | Record each reproduction run |

For future runs, record timestamp, code revision, dataset version/split, library versions, hardware, expected and observed behavior, traceback/metrics, suspected cause, fix attempted, outcome, and impact on comparability.
