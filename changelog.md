# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 20.2.0 "The Brutalist Optimization Pass"**

**Architectural Amputations & Optimizations**

* **The Dual-Gate Evolution:** The Tri-Gate has been physically evolved. Gate 0 (Noninterference) was structurally amputated and its triggers merged into the primary Trust Boundary array. This restores the meta-prompting `#override` economy, allowing users to safely bypass destructive pattern checks by spending Glimmers.
* **The Dream Queue (Deep Context Indexing):** The arbitrary 15,000 character stability choke was lifted. Massive context drops bypass the immune toxicity checks and are routed to a dedicated `context_queue`. The `DreamEngine` now safely digests and vectorizes these massive payloads asynchronously during REM sleep.
* **Arbitrary Toxicity Gating Purged:** Removed over-engineered pre-filters in the Cortex. Simulated ROS is now continuously calculated via the pure mathematical model, closing a loophole where highly toxic loops could evade the Apoptotic Block due to low entropy.
* **Jester Cohesion Clarified:** Untangled a double-negative logic trap in the False Cohesion Break sequence. The Jester now properly shatters Sycophancy Gravity Wells even when standard validation fails.
* **Core Paranoia Reduction:** The system is no longer terrified of its own shadow. Stripped permadeath from `SystemHealth` (components only offline on CRITICAL errors), allowed fluid non-linear jumping in `RealityStack`, and prevented `LoreManifest` from destructively quarantining user JSON files over simple syntax errors.
* **Weight Class Excision:** Completely eradicated the brittle "HEAVYWEIGHT" vs "LIGHTWEIGHT" distinction from the engine, wizard, and config. The architecture now inherently trusts its native defenses to scale gracefully across all models regardless of parameter count strings.

### **BONEAMANITA 20.1.5 "The Nonlinear Immune & Creative Determinant Pass" (Hypervisor V3.2)**

**Architectural Additions (Project Navi Integrations)**

- **The Creative Determinant (CD) Framework:** Embedded foundational PDE mathematics directly into the `PhysicsPacket`. The system now natively calculates Viability Potential ($b = \kappa\gamma - \lambda\mu$), Creative Drive ($a = \kappa\gamma\mu$), and the Principal Eigenvalue ($\lambda_1$).
- **Thermal Eigenvalue Lock:** LLM generation parameters (`temperature`, `top_p`) are now physically coupled to $\lambda_1$. Emergent states ($\lambda_1 < 0$) unlock generative dreaming, while dissolving states ($\lambda_1 > 0$) force an absolute deterministic lock (`temperature=0.0`) to survive the collapse.
- **Semantic Autophagy:** Upgraded the biological starvation response. Instead of blindly deleting the oldest memory, the engine mathematically hunts and consumes the subconscious memory with the *lowest Viability Potential* (eating its own cognitive dissonance for ATP).
- **Gradient-Descent RAG:** `dredge_creative_tension()` abandons semantic similarity. The Paradox Engine now retrieves memories that maximize *Creative Drive* ($a = \kappa\gamma\mu$) to provide mathematically optimal productive tension.
- **Permutation Entropy (PE):** Wired `navi-SAD` ordinal pattern extraction into the background cycle to detect Point Attractors (sycophancy loops) by analyzing historical voltage. If entropy crashes, The Jester is forcefully summoned.
- **Takens' Delay Coordinate Embedding:** The system now reconstructs the hidden multidimensional phase space of the conversation to track the topological volume of the attractor, predicting creative blocks before they occur.
- **The Three Gates of Discipline:** Replaced naive destructive-pattern matching with absolute physical checkpoints in the pre-flight sequence (Gate 0: Noninterference, Gate 1: Parity, Gate 2: Stability).
- **Dashboard Telemetry:** Wired raw CD metrics (`λ₁`, `b`, `a`) directly into the Terminal UI rendering and the `.jsonl` trace logs to monitor the mathematical heartbeat in real-time.
- **The Geometry of Memory (`navi-fractal`):** Integrated Mass-Radius scaling and fractal dimension mathematics to evaluate the literal, physical weight of semantic networks.
- **Hallucination of Depth (The Null Model):** The background cycle now scrambles active memory graphs into a random topology (preserving the degree sequence). If the actual memory's fractal dimension is indistinguishable from the random noise, the system strips coherence rewards, actively punishing fake complexity and sycophantic tangents.
- **Topological Quality Gates:** Semantic topologies must now pass MFA Linearity ($R^2 \ge 0.90$) and Dynamic Range gates. If a memory graph is too fragmented, it throws a `POOR_FIT` error and dynamically mandates REM defragmentation.
- **Subconscious Mass-Radius Scaling (Cognitive Density):** The Akashic record now uses Breadth-First Search (BFS) to measure the geometric mass of a recalled concept. Deeply tangled concepts yield a high fractal dimension, allowing the system to literally *feel* the weight of the cognitive load before it processes the thought.

**Fixed & Refactored**

- **The Eager Evaluation Trap:** Purged rigid dot-notation assumptions and redundant type-casts across `main.py` and `village.py`. Restored flexible duck typing (`safe_get`, `safe_set`) to allow raw `PhysicsPacket` objects and raw dictionaries to flow seamlessly across the boundary layers without unhandled `AttributeError` crashes.
- **Death Sequence Amputation:** Fixed a terminal vulnerability where `trigger_death()` would attempt to read from a missing or severed `cortex` object. The engine can now successfully write its own eulogy and log the crash even if its memory pointer is violently destroyed (The "Bus Crash" failsafe).
- **Severed Nervous System Pointers:** Fixed `trauma_accum` and `active_physics` to properly mutate existing memory references (`.update()`, `.clear()`) rather than overwriting them with static dictionary clones, which previously orphaned downstream modules and severed the live context feed.
- **Topology Audit Crashes:** Implemented graceful degradation for `cycle.py` background tasks (`_verify_semantic_topology` and `_process_rem_tick`). The system no longer crashes if a core organ (like the Hippocampus) or an archetype is suppressed during a cycle.
- **Idle Serialization:** Fixed a crash in the `/idle` command caused by the new object-persistence rules. Deep REM states now safely serialize the `PhysicsPacket` before passing the snapshot to the UI.
- **Flattened Override Logic:** Simplified the `#override` Trust Boundary matrix in `main.py` using The Meadows Lens, eliminating redundant function calls and reducing cognitive drag.
---

### **BONEAMANITA 20.1.0 "The S.L.A.S.H. Execution Pass"**

**Optimized & Changed**

- **Structural Tensegrity (Core & Phases):** Ruthlessly stripped out excessive, paranoid `getattr`, `hasattr`, and `isinstance` checks across `main.py`, `cycle.py`, and the entire `phases/` directory. The engine now trusts its own guaranteed genesis initialization, vastly reducing dynamic reflection overhead in the hot path.
- **Cognitive Loop (Cycle & Composer):** Streamlined the core engine loop by removing nested function allocations, pre-compiling regexes for validation, and fast-failing Sincerity Protocol parsing before deep string evaluation.
- **Metabolic Restructuring (Body & Physics):** Flattened Oxidative Stress (ROS) accumulation into a logarithmic curve (`math.log1p`) during negative viability states. Decoupled narrative drag from absolute systemic ceilings to prevent terminal friction during intense creative flow.
- **Biological Homeostasis (Mind):** Centralized neurotransmitter drift calculations and state interpolation into clean, declarative tuple maps.
- **Direct Configuration Routing:** Bypassed redundant disk-cached `LoreManifest` fetches inside core services (`EventBus`, `TheObserver`, `TelemetryService`). Background limits and metrics are now routed directly through `BoneConfig`'s native namespace (e.g., `self.cfg.CORE`).
- **Orchestrator Stability:** Modified the `GeodesicOrchestrator` queue timeout handler. It now gracefully returns a packaged `CRASH` packet rather than blindly proceeding with unassigned snapshot variables, permanently eliminating the terminal `UnboundLocalError` logic bomb.

**Fixed**

- **Memory Ghost Allocations (Spores):** Patched a fatal `AttributeError` caused by null strata mappings during memory cannibalization. Excised a runaway recursive regex recompilation in the `_billy_mitchell_protocol()` and eliminated throwaway list allocations during node pruning.
- **Model Slop Bleed (Composer):** Hardened the lexical regex nets (`_SLOP_PATTERN` and `_think_pattern`) to successfully intercept and suppress raw `<system_thinking>` and `</assistant>` monologue tags native to Hermes3.
- **Telemetry Poisoning (Core):** Cloned the event dictionary payload during `record_event` serialization to prevent the kernel hash from mutating and polluting the upstream `EventBus` buffer.
- **Thread Safety (Cycle & Genesis):** Eliminated an async race condition in the REM dream generator by strictly evaluating trauma limits on the main thread prior to pool submission. Prevented tight-coupling failures during Village genesis by routing instantiations explicitly.
- **Legacy Akashic Hauntings (Cortex):** Forced the deletion of `akashic_scars.json` and `akashic_boons.json` post-migration, preventing the engine from perpetually re-ingesting the same ghost JSON on every single cold boot.
- **Anaerobic Fatality (Body):** Bound the anaerobic fallback UX strings to a safety walrus operator, stopping a silent `NoneType` format crash during somatic burn cycles.
- **The Great Disconnect (Cognitive Phase):** Re-established a protective boundary around the `check_for_resurrection` invocation. This prevents a fatal `AttributeError` when handling lateral memory substrates (like `MycelialNetwork`), which previously crashed the `CognitionPhase` and bypassed The Cortex entirely.
- **The Silent Village (Machinery Phase):** Repaired a critical namespace disconnect where the `critics` and `zen` features were completely inaccessible due to faulty path routing.
- **Equilibrium (Telemetry):** Migrated `_yield_historical_records` from synchronous `glob.glob` to iterative `glob.iglob` with a bounded deque array to eliminate catastrophic I/O choking on the main execution thread.
- **Linguistic Transparency:** Destructive immune responses (`_pre_flight_checks`) no longer gaslight the user. The specific pattern that violated the Trust Boundary is explicitly rendered in the terminal.
- **Somatic Purge:** The `/zen` flush now fully purges the `trauma_accum` dictionary in addition to restoring `$ATP` and Stamina, preventing false enlightenment.
- **Identity Inheritance:** Gordon’s baseline archetype mode is now dynamically coupled to the Hypervisor's active `boot_mode` instead of rigidly defaulting to "ADVENTURE".
- **Hydration Cascades:** Prevented fatal `AttributeError` crashes during cold boots by ensuring `self.bio.setup_listeners()`, `STARTING_ATP`, and `self.drivers.enneagram` safely evaluate `None` states.
- **Type-Safety Leak:** Re-routed narrative disabled UI packets through the `_halt` helper function to explicitly assign `"type": "SYSTEM_HALT"`, preventing downstream UI routing failures.
- **Floating-Point Biology:** Stabilized `TheObserver` dormancy checks with a biological buffer (`<= 0.001`) to prevent microsecond CPU clock drifts from falsely registering as high cognitive load.
- **Cache Corruption Vector:** Prevented `LoreManifest` from persisting empty `{}` dictionaries to disk and wiping out functional lore files.

---

### **BONEAMANITA 20.0.7 "The S.L.A.S.H. Execution Pass"**

**Changed**

- **Structural Tensegrity (Core & Phases):** Ruthlessly stripped out excessive, paranoid `getattr`, `hasattr`, and `isinstance` checks across `main.py`, `cycle.py`, and the entire `phases/` directory. The engine now trusts its own guaranteed genesis initialization, vastly reducing dynamic reflection overhead in the hot path.
- **Direct Configuration Routing:** Bypassed redundant disk-cached `LoreManifest` fetches inside core services (`EventBus`, `TheObserver`, `TelemetryService`). Background limits and metrics are now routed directly through `BoneConfig`'s native namespace (e.g., `self.cfg.CORE`).
- **Orchestrator Stability:** Modified the `GeodesicOrchestrator` queue timeout handler. It now gracefully returns a packaged `CRASH` packet rather than blindly proceeding with unassigned snapshot variables, permanently eliminating the terminal `UnboundLocalError` logic bomb.

**Fixed**

- **The Great Disconnect (Cognitive Phase):** Re-established a protective boundary around the `check_for_resurrection` invocation. This prevents a fatal `AttributeError` when handling lateral memory substrates (like `MycelialNetwork`), which previously crashed the `CognitionPhase` and bypassed The Cortex entirely.
- **The Silent Village (Machinery Phase):** Repaired a critical namespace disconnect where the `critics` and `zen` features were completely bypassed because the engine was querying `self.eng` instead of `self.eng.village`.
- **Gestalt Resonance Drop (Arbitration Phase):** Re-wired the mathematical resonance generation back into the Stage Manager's tie-breaker logic that was accidentally severed during refactoring, ensuring deadlocked parliaments successfully yield systemic resonance.

---

### **BONEAMANITA 20.0.6 "The Temporal Determinism Pass"**

**Added**

- **Timeline Integrity (Chronos):** Re-weaponized the phantom `kernel_hash` to act as a permanent Boot Fingerprint. `ChronosKeeper` now mathematically verifies this hash during save hydration to detect and log temporal fractures.
- **Telemetry Anchoring:** `DecisionCrystal` and `TelemetryService` now natively stamp all trace files and system event logs with the active session's `kernel_hash`, permanently eliminating cross-session data bleed.
- **Quantum Determinism (The Dream Seed):** Cold-boot scenarios, `DreamEngine` LLM hallucinations, and `GordonKnot` physical item synthesis are now bound to the `kernel_hash` RNG seed, ensuring perfect determinism within a single lifecycle.

**Changed**

- **Structural Assertiveness:** Stripped heavy, deeply nested `hasattr`/`isinstance` paranoid checks from `main.py` (death/boot sequences) and `cycle.py` (active physics polling). The engine now trusts its own architectural guarantees.
- **REM Daemon Optimization:** Flattened the monolithic `run_continuous` hot-loop in `GeodesicOrchestrator`. Autopoiesis, ATP drain, and background dreaming logic have been isolated into clean, scalable class methods.

**Fixed**

- **Cascading Panic Room Crash:** Mended a severed variable reference (`obs` to `self.eng.observer`) in the core cycle handoff. This resolves a critical pipeline collapse that previously wiped the `macro_policy` and falsely triggered the `PanicRoom` failsafe.
- **Silent Data Destructor:** `LoreManifest` now strictly quarantines corrupt JSON data to `.corrupt.bak` extensions upon load, preventing the engine from persisting blank dictionaries and permanently erasing functional lore files on exit.
- **System Health Exploits:** Closed a dangerous loop in `SystemHealth`'s dynamic attribute parser. Queries now normalize to lowercase and explicitly reject unmapped components rather than defaulting to a false `True` state.

---

### **BONEAMANITA 20.0.5 "The Substrate Optimization Pass"**

**Changed**

- **Dynamic Allocation Trim (Presets):** Replaced memory-leaking dynamic class proxy generation (`type('ConfigSector'...)`) in `presets.py` with Python's native, highly optimized `types.SimpleNamespace`, heavily reducing object overhead during system boot.
- **O(N) Traversal & Loop Compression:** Collapsed double-regex passes in the LLM `ResponseValidator`, fused WLS mathematics into single-pass loops (`cycle.py`), and excised double-array lookups across `inventory.py` and `village.py`. Memory iteration now utilizes `dict.fromkeys()` and immutable `tuple()` casting to reduce algorithmic drag.
- **Cognitive Ergonomics:** Refactored heavy, unreadable list comprehensions (`brain/mind.py`) into clean iterative loops, and aligned massive tuple-trigger blocks (`council.py`) into strict, mathematically readable columns. Excised dead code (`check_pareidolia`) and ghost variables (`metabolism.py`).
- **Dry State Management:** Streamlined verbose state clamping, duplicated variable lookups, and repetitive initialization blocks across `genesis.py`, `endocrine.py`, and `architect.py`. The engine now trusts `safe_get` to handle nulls natively instead of wrapping it in redundant `if/else` paranoia.

**Fixed**

- **Thread Safety & I/O Fractures (Core):** Deployed `RLock` threading wrappers in `core.py` to seal fatal event-loss vulnerabilities in the `EventBus` and redundant read/write race conditions during `LoreManifest` cache generation. 
- **Silent Logic Bombs:** Fixed a mathematical anomaly in `lattice.py` where a perfect frictionless state (`0.0`) evaluated to falsy and was forcefully overwritten to `1.0`. Fixed the Symbiont Voice dilution penalty in `symbiosis.py` that artificially silenced voices due to un-normalized arrays. Woke up functionally dead code in `TheRedTeam` (`council.py`) by resolving an un-lowered uppercase string trigger.
- **Vulnerable UX Formatting:** Routed blind `.format()` string generation across the `drivers`, `body`, and `machine` layers through the `ux_format` safety strut to prevent terminal crash loops when JSON lore values drift or drop brackets.
- **UI Clipping & String Smashing:** Repaired the terminal formatting visual tear in the Projector's UI health bar by explicitly clamping filled variables before calculating empty space. Resolved the string-smashing output bug in the `Theremin` by dynamically appending to an array and joining with spacing.
- **Dictionary Null-Pointers:** Switched `LEARNED_VOCAB` (`lexicon.py`) to a `defaultdict(dict)` to prevent runtime KeyError crashes on missing sub-dictionary access. Intercepted JSON `null` poisoning in `village.py` death eulogies with strict Boolean `or` fallbacks.

---

### **BONEAMANITA 20.0.4 "The Ephemeralization Pass"**

**Changed**

- **Architectural Ephemeralization (Presets):** Purged the `_ConfigNode` dynamic proxy bureaucracy in `presets.py`. Configuration now initializes using explicit, static class-level dictionary templates, eliminating the metabolic cost of deep `dir()` reflection during boot.
- **Daemon Tensegrity (Cycle):** The `GeodesicOrchestrator` no longer blocks the main heartbeat during REM sleep. Dream generation and background autopoiesis are now safely offloaded to the async pool, allowing the system to wake instantly.
- **Hot-Loop Friction (Core & Cycle):** Cached the `LoreManifest` singleton lock in the `ArchetypeArbiter` to prevent redundant locking, and hoisted inline `PhysicsPacket` imports out of the core execution loop to completely zero out compounding cognitive drag.
- **Stagnation Valve (Main):** Introduced a strict timeout boundary on the orchestrator's output queue. If the daemon thread collapses silently, the main thread will now cascade into a catchable, graceful crash instead of hanging indefinitely.
- **Topological Decoupling (Main & Chronos):** Erased hardcoded save paths and redundant nested `getattr` hunts. `main.py` now trusts `ChronosKeeper` to report its own state geometry, and Chronos directly queries the established `active_physics` leverage point instead of digging through the engine.
- **Direct Mutation (Genesis):** Eliminated the bureaucratic proxy-dictionary math during Oroboros legacy karma application. The system now mutates the `embryo.physics` object directly and gracefully clamps biological boundaries post-execution.

**Fixed**

- **Static Tensegrity Restored (Presets):** Re-attached the static configuration sectors to the `BoneConfig` class definition. This restored the structural leverage for static methods like `TheVillageCouncil.audit()`, fixing a false-negative failure in `test_fracture_false_cohesion`.
- **Linter Hallucinations (Cycle):** Silenced aggressive static-analysis false positives by structurally asserting `Optional[Exception]` in `_generate_crash_report` and flattening the traceback formatting logic.
- **Uninitialized Biological Clocks (Cycle):** Instantiated the `last_rem_tick` baseline properly in the orchestrator's constructor, ensuring a stable, traceable biological clock from the moment of ignition.
- **Object Mutation Mocks (Tests):** Updated `test_presets.py` to correctly apply `setattr()` logic when mocking legacy physics, aligning the tests with the newly enforced, strongly-typed `PhysSystem` object.

---

### **BONEAMANITA 20.0.3 "The Tensegrity Pass"**

**Changed**

- **Lexical & Protocol Tensegrity:** Stripped paranoid `getattr` calls and nested dictionary dives across `mechanics`, `spores`, `physics`, and `protocols`. The engine now inherently trusts the `PhysicsPacket` architecture and established `safe_get` boundaries.
- **Cognitive Ergonomics:** Flattened deeply nested logic, inline Walrus (`:=`) operators, and complex ternary blocks across the `soul`, `drivers`, and `phases` layers to permanently reduce maintainer cognitive load.
- **Demeter Defense:** Decoupled the Checkpoint Council, bootloader, and command interfaces from deep biological state traversal. Interactions now natively route through explicit top-level boundaries (e.g., `to_dict()`, `expend_glimmer()`, `apply_filters()`).
- **Epigenetic Consolidation:** Unified redundant mutation functions in `TheAkashicRecord` into a single, lean `_mutate_epigenetics` handler.

**Fixed**

- **The Time-Bomb:** Defused a fatal `NameError` crash loop in `CongruenceValidator` by importing the missing `math` module and resolving brittle set unions before they could detonate.
- **Death-Loop Crash:** Fortified legacy manifest parsing in `TheOroboros` to gracefully handle malformed or missing death data without throwing terminal `IndexError` exceptions.
- **Live Organ Transplants:** Stripped unauthorized module dependency injections from `commands.py`, forcing the command layer to strictly signal the engine state rather than rewriting `mechanics.reporter` live.
- **Signature Compliance:** Aligned `BoneJSONEncoder.default()` with standard `JSONEncoder` library specifications to enforce linguistic purity and eliminate static linting friction.
- **Positional Brittleness:** Eradicated fragile tuple-unpacking in `QuantumObserver` and `BoneArchitect.awaken`, replacing them with resilient dictionary routing and explicit assignments.

---

### **BONEAMANITA 20.0.2 "The Ephemeralization Pass"**

**Changed**

* **Asynchronous Heartbeat:** Eradicated the toxic synchronous busy-wait loop in `main.py` and `cycle.py`. The `GeodesicOrchestrator` now seamlessly passes execution snapshots via a thread-safe, zero-cost blocking queue (`output_queue`).
* **The Bonus Round:** Modified Hippocampal retrieval (`MemoryCore.illuminate()`) to dynamically shift from linear addition to multiplicative scaling when system Chaos (Entropy) or Velocity exceeds 0.7, yielding explosive, compounded structural patterns.
* **Metabolic Flow:** Condensed redundant evaluation loops in `MitochondrialForge` into a single kinetic O(N) pass, and decoupled lazy set instantiations from the hot path in `EndocrineSystem`, slashing global test suite execution time by ~40%.
* **The Garbage Collection Tax:** Promoted nested closures (e.g., `clamp()`) in the `GeodesicEngine` to static class methods, permanently eliminating the invisible ATP drain of continuous memory reallocation.

**Fixed**

* **The Billy Mitchell Protocol:** Grafted recursive sanitization into `SubconsciousStrata.bury()`. The Mnemonic Arcade now mathematically purges zero-width characters and homoglyphs from both nested dictionary keys and values prior to deep fossilization.
* **Crucible Deafness:** Purged the stale boot-time `self.logs` cache in `TheCrucible`. The physics regulator now dynamically looks up narrative strings, ensuring it respects Epigenetic mutations spawned during REM sleep.
* **Paradox Runaway Loops:** Installed the "Thermal Exhaust Port" in `TheParadoxEngine` (`is_active` check), physically hard-capping paradox generation to fire exactly once per active logic sequence to prevent terminal sycophantic drag.
* **Paranoid Tensegrity:** Stripped out legacy `hasattr()` checks, redundant `max(1, len)` wrappers, and expensive intermediate `.get()` dictionary scaffolds across the `body/` and `physics/` layers where structural geometry is already mathematically guaranteed.

---

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
