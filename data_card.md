# Data Card: A Categorized Multimodal TikTok Dataset

## Identity and source
- **Citation:** Wedel, L. (2023). *A categorized multimodal TikTok dataset* [Data set]. Weizenbaum Institute.
- **DOI:** https://doi.org/10.34669/WI.RD/3
- **Use in this project:** Evaluate whether embedding-based cross-modal semantic divergence relates to engagement.
- **Size:** 5,136 unique videos.

## Contents
| Component | Description |
|---|---|
| Metadata | Plays, likes, comments, shares, follower count, category, advertisement/duet indicators, video IDs, scrape records |
| Text | Precomputed embedding, 512 dimensions |
| Audio | Precomputed embedding, 4,096 dimensions |
| Visual/video | Precomputed embedding, 2,304 dimensions |

The paper states that the videos were collected from TikTok Explore over five days in July and August 2023. Metadata contains 11,242 rows for 5,136 unique videos, with one to five scrapes per video.

## Preparation
1. Align the four files by video ID and check missing/infinite embedding values.
2. Retain the most recent metadata scrape for each video.
3. Apply `log(1 + x)` to plays, likes, comments, shares, and follower counts.
4. For alignment training, split by video 80/20 and calculate z-score standardization statistics on training data only.

The paper does not specify exact file names, file hashes, split seed, or split IDs.

## Intended use
Educational/research analysis of embedding-based cross-modal divergence and observed engagement associations.

## Uses not supported
Do not use this dataset to infer causation, explain TikTok's recommendation algorithm, rank or judge individual creators, or generalize to all TikTok videos without further evidence. Avoid re-identification or linkage to external personal information.

## Limitations and risks
- Explore-page selection may overrepresent content already receiving distribution.
- Five days of collection is not representative of all platform content.
- Engagement is a single-scrape snapshot and mixes together video age and collection timing.
- Independently trained unimodal embeddings may not capture human-perceived semantic correspondence.
- Captions may consist primarily of hashtags rather than descriptions.
- Social media records may encode identifiable or sensitive information even when working with embeddings.

## Access and governance
Use the official dataset source and confirm licensing, terms, and redistribution permission before sharing data or derived records. The paper does not establish that redistribution is unrestricted.
