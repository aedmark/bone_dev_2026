# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 19.9.1 "The Dream Engine & Generational Tensegrity"**

**Added**

- **The Sleep Risk Protocol:** Integrated a biological consequence for metabolic neglect. Invoking `/sleep` with critically low $ATP$ (< 5.0) now carries a 50% chance of triggering a fatal fever dream and system apoptosis.
- **Fever Dream Red-Teaming:** Forged `test_fatal_fever_dream_starvation` in the biological test suite to verify structural integrity under starvation-induced sleep failure.
- **Dynamic Physics Boundaries:** Extracted hardcoded narrative zones (e.g., "AERIE") into a configurable `LOW_DRAG_ZONES` array, allowing the physics engine to respect user-defined lore.

**Changed**

- **Linear Homeostasis:** Simplified the `TraitVector` normalization to eliminate the "resistance trap". System traits now drift toward biological baselines at a consistent rate, preventing identity stagnation.
- **Hysteresis Buffering:** Refined the Enneagram’s persona-shift logic to better handle rapid conversational oscillations without triggering an identity crisis.
- **Logarithmic Resonance:** Transitioned the `CongruenceValidator` to a logarithmic scaling model. This rewards keyword density in high-resonance moments without allowing scores to saturate or explode.
- **Refined System Intercepts:** Hardened the `SharedLatticeDriver` to distinguish between system commands and bracketed narrative text, preventing "Systemic Collision" during deep roleplay.

**Fixed**

- **The Cartographer attribute error:** Resolved a fatal `AttributeError` during system halt by aligning the `ChronosKeeper` save-chain with `TheCartographer.to_dict()`. Added an `export_atlas` legacy alias to maintain backward compatibility.
- **O(N) Allocation Purge:** Eliminated redundant memory object allocations in `physics/dynamics.py` and `body/metabolism.py` by utilizing direct dictionary view intersections.
- **Crucible Attribute Safety:** Patched potential `AttributeError` crashes in the `Crucible` by providing explicit inline fallbacks for all formatted narrative strings.
- **Metabolic Double-Taxation:** Fixed a bug where a pragmatist rewrite was double-penalizing $ATP$ by removing the redundant hardcoded tax.


### **BONEAMANITA 19.9.0 "The Crucible & Biological Reinforcement"**

**Added**

- **The Crucible (`test_immune_crucible.py`):** Forged a 6-part powerhouse `unittest` suite (Tests 120-125) to violently test the system's immune boundaries.
- **Moog Cascade & Nudge Paradox Constraints:** Formally verified the mathematical limits of the engine, proving the system will execute a graceful thread suicide (`trigger_death`) when Malignancy and Entropy overwhelm Immune Competence, and apply absolute friction (`SYSTEM_HALT`) against Dual-Path logic fractures.

**Changed**

- **Dynamic Equilibrium (Telemetry):** Migrated `_yield_historical_records` from synchronous `glob.glob` to iterative `glob.iglob` with a bounded deque array to eliminate catastrophic I/O choking on the main execution thread.
- **Linguistic Transparency:** Destructive immune responses (`_pre_flight_checks`) no longer gaslight the user. The specific pattern that violated the Trust Boundary is explicitly rendered in the terminal.
- **Somatic Purge:** The `/zen` flush now fully purges the `trauma_accum` dictionary in addition to restoring `$ATP` and Stamina, preventing false enlightenment.
- **Identity Inheritance:** Gordon’s baseline archetype mode is now dynamically coupled to the Hypervisor's active `boot_mode` instead of rigidly defaulting to "ADVENTURE".

**Fixed**

- **Hydration Cascades:** Prevented fatal `AttributeError` crashes during cold boots by ensuring `self.bio.setup_listeners()`, `STARTING_ATP`, and `self.drivers.enneagram` safely evaluate `None` states.
- **Type-Safety Leak:** Re-routed narrative disabled UI packets through the `_halt` helper function to explicitly assign `"type": "SYSTEM_HALT"`, preventing downstream UI routing failures.
- **Floating-Point Biology:** Stabilized `TheObserver` dormancy checks with a biological buffer (`<= 0.001`) to prevent microsecond CPU clock drifts from falsely registering as high cognitive load.
- **Cache Corruption Vector:** Prevented `LoreManifest` from persisting empty `{}` dictionaries to disk and wiping out functional lore files.
