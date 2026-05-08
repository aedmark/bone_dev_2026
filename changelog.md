# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 19.9.2 "The S.L.A.S.H. Audit & Synergetic Tensegrity"**

**Added**

- **Biological Pulse Wire-In:** The theoretical math of the `CreativeDeterminantEngine` is now physically wired into the `QuantumObserver` and `TheCortex`. Every generated thought now calculates its exact Viability and mathematically deducts `$ATP` and adds `ROS` before the generation completes, finalizing Nelson Spence's equation in the physical layer.
- **Legacy Epigenetic Migration:** Added a backward-compatibility loader to `TheAkashicRecord` to automatically ingest legacy `akashic_scars.json` and `akashic_boons.json` flat-files and natively migrate them into the unified `LoreManifest` system.

**Changed**

- **Epigenetic Unification (Memory):** Eradicated the redundant flat-file saving mechanism for Scars and Boons in `TheAkashicRecord`. Epigenetic mutations are now routed directly through `LoreManifest.save("SYSTEM_PROMPTS")`, completely sealing the prompt generation truth-state and dropping disk I/O.
- **O(1) Interaction Lookups:** Replaced the highly expensive O(N) dynamic Regex compilation loop inside `GordonKnot.enforce_object_action_coupling` with a clean O(1) set-intersection check, drastically reducing cognitive drag when the user inputs physical verbs.
- **Lazy Memory Parsing:** The `SemanticEndocrinologist` no longer converts the `cortical_stack` into a set on every single heartbeat. Set conversion is now lazily evaluated only when an unmapped, dense word is discovered, eliminating massive passive CPU drag during long sessions.
- **Syntactic Checkpoint Purge:** Streamlined `_pre_flight_checks` inside the Checkpoint Council to use a single-pass string scan instead of an overlapping `any()` loop.

**Fixed**

- **The Blinded Immune Failsafe:** Repaired a critical typo in `BioFeedback.check_vital_signs` where Level 3 Apoptosis was querying `malignancy_factor` instead of the actual `m_a` attribute, ensuring the system can now successfully trigger Mausoleum Clamps during reward hacking loops.
- **The Epistemological UI Leak:** The `/truth` command now actually works. `TruthRenderer` was correctly overriding `render_truth`, but failing to intercept the `render_frame` master pipeline.
- **Terminal Reality Breaches:** By dropping the silent `False` return in the `RealityStack` and replacing it with a hard `ValueError`, the engine now crashes loudly on topological layer skips. The `/layer push` command was updated to properly catch and render these reality violations.
- **The Panic UI Wipe:** Emergency `MAUSOLEUM_CLAMP` events inside the `SomaticLoop` no longer wipe the UI data. The endocrine state is now successfully preserved and passed to the `_package_result` early return.
- **Silent Data Eaters:** Deleted the paranoid `safe_dict` wrapper in `core.py`. Un-serializable custom objects will now properly throw a `TypeError` in the `BoneJSONEncoder` telemetry background thread instead of silently destroying the data and writing empty brackets.
- **Chronological Boot Rot:** Fixed a critical timeline flaw in `main.py` where `TheCortex` was being spun up before `host_stats` was initialized, essentially lobotomizing hardware latency tracking on boot.
- **Thermodynamic Alias Breach:** Added alias variables (`V`, `F`) to the `__setattr__` safety clamps in `PhysicsPacket` to prevent downstream modules from injecting negative energy or narrative drag values.
- **O(n) String Redundancy:** `HLA_Stabilizer` now pre-lowers its corporate antigen patterns upon initialization instead of calling `.lower()` repeatedly during every rejection scan.

---

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
