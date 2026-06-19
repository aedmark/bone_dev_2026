# Domain 02: The Mind (Memory & Topology)

> **Forge Document Hierarchy:** Constitution > Conventions > Glossary > **Architecture Domain Docs** > Engineering Plan
>
> **Domain Scope:** This document covers the cognitive structures of BoneAmanita, primarily residing in the `brain/` (`akashic.py`, `mind.py`, `ann.py`) and `spores/` (`memory.py`) directories. 

## 1. Specification

The Mind in BoneAmanita does not treat memory as a flat database. It treats memory as a biological topology—a weighted graph of concepts, synapses, and vectors. 

The `HippocampalCache` (`ann.py`) acts as the immediate short-term buffer, encoding recent interactions into vectors using SHA-256 hashing for cryptographic stability. 

As interactions age, they sink into the `MemoryCore` (`spores/memory.py`). When the engine needs to recall information, it performs "Subconscious Dredging" to find relevant topological nodes. However, because infinite memory leads to graph collapse, the engine actively runs defragmentation (`run_defragmentation` in `mind.py`) and pruning protocols (`cannibalize`). Weak nodes are permanently amputated (Constitution Article 8) to conserve ATP and processing cycles.

Simultaneously, the engine maintains a continuous biological `ChemicalState` (`mind.py`) tracking Dopamine, Cortisol, Adrenaline, and Serotonin. These floats are updated continuously in a high-frequency `homeostasis` tick loop, subtly coloring the context retrieval process [OQ-1].

---

## 2. Decided

### [DEC-01] Zero-Allocation Chemical Homeostasis
**Decision:** The chemical constants map (`_HOMEOSTASIS_MAP`) used to calculate the decay and growth of neurotransmitters is strictly defined as a class-level tuple, completely outside the `homeostasis()` function loop.
**WHY:** The homeostasis function ticks continuously throughout a cycle. Allocating a list of tuples inside the function forces the Python garbage collector to create and destroy the array on every tick, causing massive GC thrash.
**WHY NOT:** Declaring variables locally inside the function makes the code slightly more readable, but readability cannot come at the cost of high-frequency GC freezing.

### [DEC-02] O(N) Subconscious Dredging
**Decision:** When dredging the memory core for relevant nodes, the system must strictly use `np.argpartition` instead of `np.argsort` to find the top $K$ memories. 
**WHY:** The memory graph scales massively. `np.argsort` has a time complexity of $O(N \log N)$ because it sorts the entire array. `np.argpartition` runs in $O(N)$ time by only guaranteeing the top $K$ elements are separated, which is all the Akashic record needs.
**WHY NOT:** `np.argsort` is the standard ecosystem default for array sorting, but it will catastrophically bottleneck the Geodesic Orchestrator as the memory graph grows.

### [DEC-03] Trusting the Graph Types During Defragmentation
**Decision:** During `run_defragmentation`, dictionary nodes are accessed using native Python `.get()` methods rather than the engine's global `safe_get` try/except abstraction wrapper.
**WHY:** The `memory_system.graph` is strictly typed and mathematically guaranteed to contain dictionaries at this stage. Applying paranoid abstraction wrappers over secure native types ("paranoia drift") introduces an immense function-call abstraction tax during deep graph traversal.
**WHY NOT:** Using `safe_get` everywhere prevents `KeyError` crashes. But applying it to a guaranteed structure is redundant and slow.

### [DEC-04] Cryptographic Memory Hygiene
**Decision:** `HippocampalCache` hashes vectors using SHA-256 instead of MD5. 
**WHY:** MD5 is computationally compromised and can lead to collision states in dense neural topologies, accidentally fusing unrelated topological nodes. 
**WHY NOT:** MD5 is slightly faster, but corrupted memory graphs require a total Genesis reset to fix. 

---

## 3. Open Questions

### [OQ-1] Chemical Influence on Memory Retrieval
**Status:** `Discovery: Phase 2`
**Question:** Currently, neurotransmitters exist and track homeostasis. But how heavily should they influence actual `MemoryCore` dredging? Should high Cortisol actively suppress the retrieval of positive or lateral topological nodes, forcing a "tunnel vision" recall?

### [OQ-2] Shadow Archival Thresholds
**Status:** `Backlog`
**Question:** Article 8 mandates that "load-bearing context or highly polarized nodes" are granted shadow-archival status instead of being deleted. What is the exact mathematical threshold (e.g., mass > 50, resonance > 0.9) that promotes a node from "noise" to "shadow archive"?