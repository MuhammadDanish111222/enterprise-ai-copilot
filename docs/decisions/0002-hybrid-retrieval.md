# ADR 0002: Hybrid Retrieval with Dense Search, BM25, and RRF

## Status

Proposed

## Date

2026-07-02

## Context

The current system has semantic retrieval using embeddings and Qdrant.

This is useful, but dense retrieval alone is not enough for production RAG.

Dense retrieval can fail when the question contains:

- Exact product names
- Policy names
- Error codes
- SKUs
- IDs
- Rare terms
- Version numbers
- Names
- Short exact-match queries

Sparse retrieval is better for exact token matching.

The target RAG system should support both:

```text
Dense retrieval
Sparse retrieval
```

Then both result lists should be fused into one ranked list.

## Decision

We will implement hybrid retrieval using:

```text
Dense retrieval: Qdrant vector search
Sparse retrieval: BM25
Fusion: Reciprocal Rank Fusion
```

The first hybrid strategy name will be:

```text
hybrid_dense_bm25_rrf_v1
```

## Why RRF

RRF is simple, explainable, and strong for combining ranked result lists.

It does not require score normalization between dense and sparse systems.

The formula:

```text
score = sum(1 / (k + rank))
```

Default `k`:

```text
60
```

## Planned Flow

```text
User query
  |
  v
Embed query
  |
  v
Search Qdrant dense index
  |
  v
Search BM25 sparse index
  |
  v
Fuse results with RRF
  |
  v
Return ranked chunks with debug scores
```

## Planned Response Fields

Each result should include:

```text
chunk_id
text
fused_score
dense_rank
dense_score
sparse_rank
sparse_score
metadata
```

## Planned API

```text
POST /v1/retrieval/hybrid-search
```

## Planned Request

```json
{
  "query": "What is the refund policy?",
  "top_k": 5,
  "filters": {
    "access_level": "public"
  }
}
```

## Planned Response

```json
{
  "query": "What is the refund policy?",
  "top_k": 5,
  "strategy": "hybrid_dense_bm25_rrf_v1",
  "results": [
    {
      "chunk_id": "example-chunk-id",
      "text": "example chunk text",
      "fused_score": 0.0327,
      "dense_rank": 1,
      "dense_score": 0.84,
      "sparse_rank": 3,
      "sparse_score": 4.21,
      "metadata": {}
    }
  ]
}
```

## Implementation Plan

### Step 1: Sparse Retrieval Schema

Create schemas for:

```text
SparseSearchResult
HybridSearchResult
HybridSearchRequest
HybridSearchResponse
```

### Step 2: BM25 Store

Create a BM25 store that can:

```text
index chunks
search chunks
return ranked sparse results
```

### Step 3: RRF Utility

Create utility:

```text
reciprocal_rank_fusion
```

Inputs:

```text
dense_results
sparse_results
top_k
rrf_k
```

Output:

```text
fused ranked results
```

### Step 4: Hybrid Retriever

Create service:

```text
HybridRetriever
```

Responsibilities:

```text
run dense search
run sparse search
fuse results
return debug metadata
```

### Step 5: API Endpoint

Add:

```text
POST /v1/retrieval/hybrid-search
```

## Acceptance Criteria

Hybrid retrieval is complete when:

* Semantic search still works
* BM25 sparse search works
* Hybrid search works
* RRF combines dense and sparse results
* Result includes fused score
* Result includes dense rank and sparse rank
* Result includes retrieval strategy
* Result includes enough metadata for debugging
* Basic tests exist for RRF fusion

## Consequences

### Positive

* Better retrieval quality
* Better exact-match handling
* Better debugging
* Better foundation for citation accuracy
* Closer to production RAG architecture

### Negative

* More indexing complexity
* BM25 index must be kept in sync with chunks
* More metadata needs to be managed

## Status

Proposed for Phase 1C.
