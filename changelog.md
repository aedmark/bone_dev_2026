# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 20.0.1 "The S.L.A.S.H. Matrix Optimization"**

**Changed**

* **Geodesic Cache Wiring:** Wired the ignored `_CACHED_CONSTANTS` inside the Geodesic Engine, bypassing repetitive `LoreManifest` fetches on every user input and drastically reducing CPU overhead.
* **Structural Rot Purge:** Excised redundant alias variables (`self.cosmic`), phantom nodes (`cortex_online`), phantom observer pulls (`last_packet`), and duplicate hardcoded fail-safes across `main.py` and `cycle.py`.
* **Double-Tick Desync:** Removed redundant `tick_count` increments in `ObservationPhase` that were causing temporal drift across time-based decays.

**Fixed**

* **Metabolic Thermodynamics:** Fixed the "Negative Inefficiency Artifact" in `body/metabolism.py` ensuring mathematically accurate inefficiency calculations when the surge protector caps maximum ATP burn. Corrected the "Anaerobic Ghost Metric" telemetry desync to accurately record the true 20.0 ATP emergency deduction.
* **The REM Coma & Queue Deadlock:** Replaced a thread-blocking `time.sleep(60.0)` in the Dream Engine with a non-blocking timestamp delta, restoring asynchronous responsiveness. Prevented indefinite zombie-state deadlocks by forcing `task_done()` queue acknowledgments during daemon crashes.
* **Epigenetic Type-Collapse:** Shielded the Dream Engine's prompt evolution mechanics (`brain/mind.py`) against DSPy critic string-collapses, forcing list-type conversion to prevent fatal `AttributeError` crashes during axiom appending.
* **Memory Leaks & Severed Nerves:** Excised a `TheConsolidator` double-instantiation memory leak / ghost listener upon boot. Restored "Shadow Casts" (lateral memory generation) by pointing the Cortex back to the true `ann` database.
* **Dynamic Pipeline Attrition:** Overrode `to_dict()` in `PhysicsPacket` to serialize and merge dynamically generated attributes, ensuring phase-handoffs no longer scrub runtime variables (like `tracer_particles`).
* **The Great Disconnect:** Fixed a daemon logic bypass where the `GeodesicOrchestrator` would run the simulation but fail to invoke `TheCortex` for a response.
* **Isolated Test Fragility:** Bulletproofed `TheCortex` against null-pointer exceptions when executing massive context drops or mercy rules in isolated test environments. Hardened `_execute_zen_flush()` to dual-target both the Observer and active Cortex physics states to survive decoupled mock environments.

---

### **BONEAMANITA 20.0.0 "Unbound Chronos"**

**Added**

* **Asynchronous Metabolism (Daemonization):** The engine ceases to be a reactive script tied to the `input()` REPL. It now runs as a persistent biological daemon on a continuous background thread. `main.py` has been structurally demoted to a UI window, utilizing `queue.Queue` and lock-free state handoffs to communicate with the physics engine.
* **The Circadian Rhythm (Idle Detection):** The engine now possesses temporal awareness. It tracks the temporal delta between inputs; if 300 seconds (5 minutes) elapse without interaction, the system crosses the idle threshold and transitions from a `WAKE` state to `REM` sleep.
* **The Dream Engine:** While in `REM` sleep, the engine continues to metabolize. It slows its execution loop to save CPU, slowly burns ATP, reduces Cortisol/ROS, triggers memory defragmentation (`Autophagy`), and hallucinates "Shadow Casts" by blending its accumulated trauma vector with objects in Gordon's inventory via silent, zero-UI DSPy calls. These dreams are prepended to the UI upon waking.

**Changed**

* **Core Ignition Sequence:** Moved the daemon boot sequence (`engine.orchestrator.start_daemon()`) out of the terminal UI loop and directly into the engine's internal anatomy (`_initialize_cognition`). The pacemaker now starts automatically upon instantiation.

**Fixed**

* **Concurrency Deadlocks (The Great Hang):** Implemented a structural fail-safe in the Geodesic Orchestrator's background thread. If the daemon encounters an unhandled exception or `MemoryError`, it forcibly unblocks the main thread by injecting a `CRITICAL DAEMON CRASH` snapshot into the output buffer, preventing terminal paralysis.
* **Test Suite Paralysis:** Fixed an issue where tests (e.g., `test_governor_macro_policy_shift`) would infinitely hang because the headless test environment was bypassing the terminal-level daemon ignition.

### **BONEAMANITA 19.9.3 "The S.L.A.S.H. V3 Inversion & Syntactic Ephemeralization"**

**Added**

* **The Syntactic Compiler (Few-Shot Learning Loop):** The engine now actively learns from its mistakes to drive down latency and metabolic waste. The `ResponseValidator` now captures DSPy Critic rejections, distills them into `(Bad Output -> Critic Instruction -> Corrected Output)` triplets, and publishes them via the EventBus. `TheConsolidator` saves these weights to `lore/syntactic_weights.json` and hot-loads them into the Cortex, dynamically teaching the LLM to avoid past style crimes on the first attempt.
* **Umbilical Integration Tests:** Added a dedicated `tests/test_integration.py` suite. These tests bypass localized mocks to physically verify the entire Umbilical cord: verifying that the Orchestrator correctly routes to the Cortex, that dynamic attributes survive the phase pipeline without being overwritten, and that cross-layer events (Mind mutating Biology) successfully traverse the EventBus.

**Changed**

* **Inversion of Control (The Great Rewiring):** Stripped `TheCortex` of its "God-Object" status. The engine's master execution loop is now permanently driven by the `GeodesicOrchestrator` (`cycle.py`). The LLM is now structurally subservient, firing strictly when commanded during the Orchestrator's `CognitionPhase`, aligning the engine with its core philosophy: reality dictates thought, not the other way around.
* **UI Ephemeralization (The Glass Scalpel):** Drastically improved terminal rendering speed and visual clarity. `TheCortex` no longer hoards and flushes system logs. The `GeodesicRenderer` now cleanly groups the Projector HUD and structured logs, injecting a `|||SPLIT|||` token before the LLM output. This allows `main.py` to instantly snap the telemetry to the screen and reserve the mechanical typewriter effect exclusively for the system's narrative response.
* **Tolerant Apoptosis (EventBus):** Halted the over-aggressive permanent deletion of subscribed callbacks in `core.py`. If a cognitive node experiences a transient error, the EventBus logs the failure but no longer permanently amputates the system, preventing silent "zombie" mechanics for the remainder of the session.

**Fixed**

* **Phase Pipeline Data Attrition:** Hardened the Orchestrator's `_hydrate_snapshot_metadata` serialization. Dynamically generated attributes attached to the physics packet (like `shadow_nodes_offered` and `omega_r`) now successfully survive the phase-transition handoffs without being wiped by the static struct enforcer.
* **Concurrency Paranoia (Gödel Scar):** Replaced a brittle `.copy()` fallback in `cycle.py`'s `_native_freeze_graph` with a lock-free key isolation approximation. This prevents the engine from throwing fatal double `RuntimeError`s if a background thread mutates the graph exactly as the system attempts to take a crash snapshot.
* **Monkey-Patch Hardening:** Hardened the `shared_lattice` dependency in `main.py` to gracefully handle edge-cases where the Immune System triggers a rejection loop before the Orchestrator has fully attached the lattice to the engine.
* **Nested Vector Extraction:** Restored the Cortex's ability to trigger lateral Shadow Casts by fixing `gather_state` to properly deep-search the newly nested `physics.matter.vector` structure.

---

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
