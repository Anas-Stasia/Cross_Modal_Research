# Model Card: Cross-Modal Alignment and Multimodal Divergence Score

## Model summary
A research model that maps precomputed text, audio, and visual embeddings into a shared space and calculates a per-video Multimodal Divergence Score (MDS). It is not a general-purpose video-understanding model.

## Inputs and outputs
- Text embedding: 512 dimensions
- Audio embedding: 4,096 dimensions
- Visual embedding: 2,304 dimensions
- Each modality is mapped by a two-layer feed-forward projection head to 128 dimensions.

`MDS = 1 - (sim(text, video) + sim(text, audio)) / 2`

Here, `sim` is cosine similarity in the projected space. Lower scores indicate greater caption alignment with audio and visual content under this formula; higher scores indicate greater divergence. Audio–video similarity is also analyzed separately.

## Training and validation
- Contrastive objective: InfoNCE across text–audio, text–video, and audio–video pairs.
- Preprocessing: dimension-wise z-score standardization using training-set statistics.
- Split: 80% train / 20% held-out test, split by video.
- Retrieval evaluation: cosine similarity; the paper reports about 4–4.5% top-1 accuracy versus a 0.1% chance baseline for 1,028 test videos.
- Baseline: random untrained projection heads for retrieval, plus a separate PCA-based divergence measure.

The paper does not specify optimizer, learning rate, batch size, epoch count, random seed, projection layer widths/activations, contrastive temperature, regularization, checkpoint selection, or exact software versions. These must be recovered to reproduce training exactly.

## Reported engagement results
Spearman correlations with log engagement:
- Plays: rho = 0.036, p = .010
- Likes: rho = 0.037, p = .008
- Comments: rho = 0.014, p = .321
- Shares: rho = -0.015, p = .269

With controls for log followers, category, advertisement, and duet status, MDS was not a significant predictor of log plays (coefficient 0.003, p = .951; model R² = 0.316). These are paper-reported results, not independently reproduced results.

## Limitations and intended interpretation
The source embeddings were created by independently trained unimodal encoders. Good retrieval performance does not establish that the MDS matches human judgments of semantic mismatch. The trained MDS and PCA baseline agree weakly (rho = 0.027, p = .057). Results apply to the analyzed sample and are associational.

Do not use the score to rank creators, moderate content, infer intent, or make consequential decisions. Treat it as an experimental measurement proxy, not a human-equivalent understanding of coherence.

## Release requirements
Any checkpoint release should include code, configuration, software/hardware versions, split procedure or IDs, preprocessing statistics, checkpoint-selection details, retrieval evaluation, statistical-analysis scripts, and a record of deviations. The paper does not identify a public checkpoint.
