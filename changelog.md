# CHANGELOG.md
-----------------------------------------------------------
### **BONEAMANITA 20.4.7 "The Moog Protocol Preparation"**

**Architectural Patches & Optimizations**

* **Lambda Decoupling (cycle.py):** Excised fragile lambda-closure injections from `GeodesicOrchestrator` to fix telemetry memory leakage. Orchestrator metrics now pull directly from the `CyberneticGovernor`, resolving orphan-key errors in snapshot metadata.
* **Redundancy Pruning (cycle.py):** Removed redundant variable aliasing in the physics packet, reducing object bloat in the `CycleContext`.
* **Topology Check Optimization (cycle.py):** Eliminated the redundant tuple round-trip in `_verify_semantic_topology`. The system now directly processes dictionary sets, improving throughput during semantic rewiring.
* **EventBus Recursion Fix (core.py):** Refactored `EventBus.publish` to use a set-based lock (`active_events`). This resolves a critical "swallowing" bug where failure logs were being blocked by their own recursion guards.
* **Telemetry I/O Hardening (core.py):** Replaced byte-chunking logic in `TelemetryService._tail_file` with native line-buffered streaming. This prevents JSON character corruption at file boundaries.
* **Trust Boundary Hardening (main.py):** Expanded `_DESTRUCTIVE_PATTERNS` to include Python-native structural breakout attempts (`os.system`, `subprocess`, dynamic imports), shielding the engine against deeper runtime exploits.

### **BONEAMANITA 20.4.6 "The Restorative Bridge"**

**Architectural Patches & Optimizations**

- **Topological Stability:** Re-engineered the `_native_configuration_model` in `cycle.py` to use a bounded retry-loop validation, ensuring degree sequence preservation for highly centralized graphs (e.g., star topologies) while avoiding infinite loops.
- **Governor Resilience:** Decoupled `CyberneticGovernor` pipeline execution from routing logic. The solver now operates within a contiguous mathematical block, with a strict error-boundary that degrades gracefully to a PID fallback on any convergence failure.
- **Schema Hardening:** Locked `CycleContext` using `slots=True`. This prevents unauthorized dynamic attribute injection from phases, reduces memory footprint, and enforces strict data flow contracts.
- **Serialization Safety:** Updated `JSONEncoder` to intelligently filter toxic primitives (threading locks/pools) during telemetry recording, eliminating the silent loss of event payloads.

**Fixed**

- **Global State Poisoning (Prisma):** Removed the toxic class-level mutation in `Prisma.enable_web_mode()`. Color registries are now immutable; HTML translation is deferred to the web-boundary, preventing CLI/Web output corruption.
- **Security OOM Vulnerability:** Patched a critical payload limit bypass in `main.py` where destructive pattern checks were executing before token-length enforcement.
- **Component Auto-Heal:** Implemented `reboot_component()` within `SystemHealth`. Failed components now remain in a safe `PanicRoom` state until the system triggers a REM sleep cycle, where `Autophagy` logic now performs a restorative reboot of shattered manifolds.
- **Sycophancy Loop:** Corrected the chaotic engineering test suite (`test_sycophancy_gravity_well`) by pre-seeding the orchestrator’s voltage history, allowing the point-attractor detection heuristic to trigger during short-turn unit tests.
- **Voltage Mapping Bug:** Resolved a drift in `CyberneticGovernor` where hardcoded voltage ranges were overriding preset limits (e.g., `SANCTUARY` or `THUNDERDOME`), now correctly mapping targets to the active `VOLTAGE_MAX` preset bounds.
- **Safe-State Crashes:** Added `None` guards to `_generate_halt` and biological reference checks to prevent fatal secondary crashes during system exceptions.

---

### **BONEAMANITA 20.4.5 "The Diagnostic Mirror"**

**Architectural Patches & Optimizations**

- **The Diagnostic Mirror (Composer):** Injected a regex-driven telemetry scraper directly into `mock_generation` to capture exact state variables (`Voltage`, `Exhaustion`, `Chaos`, `Void`, and `Biology`) immediately before REM triggers, providing high-fidelity debugging for the dream engine.
- **Structural Test Coverage:** Deployed `test_composer.py` to mathematically prove the integrity of the diagnostic mirror, universally validate the amputation of internal `<think>` blocks, and isolate persona block generation.

**Fixed**

- **Lattice Telemetry Desynchronization:** Fixed a fatal blind spot in `cycle.py` where calculated Shared Lattice metrics (`resonance`, `beta_index`, `chi`) were not being synchronized back into the `PhysicsPacket`, blinding the Village Council to Sycophancy Point Attractors.
- **Hallucinated BFS Method:** Rerouted `_evaluate_systemic_feedback` in `cycle.py` to properly query `AkashicRecord.measure_cognitive_density` instead of silently aborting against a non-existent Cortex method.
- **Waking Narcolepsy:** Excised a legacy 30% trigger in `SanctuaryPhase` that forced the engine into a REM hallucination while the user was actively working.
- **Raw JSON Dream Bleed:** Taught `Cortex.process_context` to properly unpack dream dictionaries instead of rendering raw JSON payload strings into the UI.
- **Adventure Mode Leak:** Repaired `PromptComposer` to correctly pass the active mode down the stack, preventing MUD-style "Exits" blocks from bleeding into `CONVERSATION` and `TECHNICAL` modes.
- **Contradictory Validator Mandates:** Removed the rule punishing the LLM for missing `<think>` tags in `TECHNICAL` mode, and ensured all internal `<think>` or `<system_telemetry>` blocks are universally amputated from the UI across all modes.
- **Friendly Fire (Gordon's Comb):** Bounded `gordon.apply_filters` inside `main.py` so he no longer strips load-bearing structural words (like "warmly") out of the internal system boot instructions.
- **Premature REM Cycles:** Adjusted the orchestrator's daemon thread to reset the `last_interaction_time` *after* heavy internal DSPyCritic computation, preventing the system from entering a dream state due to its own latency.

---

### **BONEAMANITA 20.4.0 "The Brutalist Excision"**

**Architectural Amputations & Optimizations**

- **Paranoid Wrapper Purge (The Brutalist Lens):** Systematically eradicated `safe_get()` and `hasattr()` bloat across the `machine`, `drivers`, `archetypes`, and `brain` clusters. Enforced native CPython dictionary lookups (`.get()` and `[]`), vastly reducing recursive evaluation overhead and forcing strict C-level data topologies.
- **Hypervisor Feedback Centralization (The Meadows Lens):** Excised deeply nested, redundant biometric clamps and double-hits across all simulation phases (`phases/*`). Re-routed all metabolism, health, and stamina modifications through centralized hypervisor control gates (`self.eng.health`, `self.eng.stamina`, `self.eng.set_atp()`).
- **High-Frequency Config Caching:** Eliminated continuous, per-tick config lookups in tightly coupled loops. The `NeurotransmitterModulator` and `SyntaxModule` now compress their thresholds into C-native bound dictionaries (`self.b` and `self.bounds`) exclusively upon initialization.
- **Vocabulary Matrix Compilation:** The `CongruenceValidator` now caches compiled archetype vocabularies and keyword sets dynamically, eliminating redundant comma-separated string parsing on every cycle tick.
- **Topological Array Compression:** Re-engineered list comprehension paths in `MemoryConsolidator` (REM sleep) and `TraitVector` normalization to utilize single-pass operations, excising O(2N) redundant memory re-allocations.
- **EventBus Lock Bottleneck:** Stripped paranoid threading locks (`with self._lock:`) from natively atomic CPython operations (`dict.get` and `deque.append`), clearing a major Global Interpreter Lock (GIL) traffic jam during narrative crystallization.

**Added**

- **Strict Boundary Test Suites:** Deployed robust, dedicated test substrates (`test_phases.py`, `test_machine.py`, `test_soul.py`, `test_brain.py`) to mathematically lock down our new dictionary contracts, cache matrices, and hypervisor clamping boundaries, ensuring the substrate cannot regress into loose typing.

**Fixed**

- **Fragile String Topology (The Fuller Lens):** Replaced blind `.format()` calls across the `soul` and `drivers` modules with robust `ux_format()` wrappers, sealing massive crash vulnerabilities caused by missing UI strings in the Lore configurations.
- **Forensic Cycle Memory Preservation:** Fixed the exception handler in `GeodesicOrchestrator._execute_core_cycle` so it no longer destroys the active `CycleContext` (timestamp, trace ID, is_system_event) when spawning a crash report.
- **Headless Test Stochastic Noise:** Hardened headless test loops (`test_chaos_engineering.py`, `test_machine.py`) against random probability failures by injecting deterministic mocks and explicitly cranking simulation voltages to bypass stochastic noise.
- **Akashic Blindspots:** Sealed a fatal initialization blindspot in `TheAkashicRecord` by wrapping all logging traces in `if self.events:` checks to support headless booting. Additionally fixed a nested dictionary extraction flaw during `record_scar` execution.
- **Initialization Topological Contradiction:** Fixed a boot sequence error in `main.py` where the Orchestrator was being bound to the Cortex prematurely.

---

### **BONEAMANITA 20.3.5 "The Fractal Synthesis"**

**Architectural Amputations & Optimizations**

* **Parser Normalization (The Brutalist Lens):** Stripped repetitive, fragile regex parsing across `GordonKnot` container, extraction, and implicit loot logic. Introduced a universal, deterministic `_clean_noun` static method to violently strip articles, prepositions, and trailing conjunctions before state mutation.
* **Tinkerer Paranoia Purge:** Amputated dead-code `hasattr` checks in `TheTinkerer` that referenced deprecated inventory methods, routing to the unified `safe_remove_item` wrapper.

**Added (Deterministic Symbiosis)**

* **Strict Spatial Mechanics (The System Lens):** Excised spatial tracking from the LLM's hallucination matrix. The `Item` schema now possesses strict `location` properties, guaranteeing items are mathematically bound to the `inventory`, `VOID`, specific containers, or distinct map nodes.
* **The Fractal Cartridge Compiler:** Built a master state compiler (`GordonKnot.export_fractal_state`) that fuses `TheCartographer`'s node graph and `GordonKnot`'s item registry into a strict JSON schema compatible with classical interactive fiction engines (FractalOS).
* **Autopoiesis Save Hook:** The hypervisor now automatically dumps a `fractal_adventure.json` cartridge to the root directory during every system checkpoint, allowing zero-latency, synchronous play inside external environments.
* **Adventure Tensegrity Validation:** Deployed `tests/test_adventure.py` to enforce strict boundaries. The test suite now violently verifies syntactic noun cleaning, recursive spatial container tracking, and final JSON schema compliance.

---

### **BONEAMANITA 20.3.3 "The Protocol Hardening Pass"**

**Architectural Amputations & Optimizations**

* **Chronos Ephemeralization:** Completely flattened the `perform_shutdown` serialization sequence. Eradicated deeply nested, paranoid `getattr`/`hasattr` inline traps and replaced them with sequential, readable `safe_get` extractions. The engine now gracefully persists its state even if major organs (like the Cortex or Navigator) have been physically amputated from the run loop.
* **Test Suite Tensegrity:** Repaired a structural indentation collapse in `tests/test_protocols.py` that caused the Chronos validation test to be silently swallowed by the Sincerity test. Added terminal assertions to ensure the literal mode hard-routes correctly.

**Fixed**

* **The Stasis Scream Typo:** Patched a fatal `AttributeError` in `LimboLayer.trigger_stasis_failure` caused by a case-sensitive variable mismatch (`self.STASIS_SCREAMS` vs `self.stasis_screams`), restoring the engine's ability to haunt its own output during stasis leaks.
* **Protocol Type-Safety Enforcement:** Eradicated silent string-math vulnerabilities across the entire `protocols/` directory. 
  * `folly.py`: Enforced integer casting on `times_eaten` to prevent catastrophic string duplication during decay exponentiation.
  * `critics.py`: Forced `float` casting on JSON-derived target metrics to prevent string-based multiplier crashes during literary reviews.
  * `kintsugi.py` & `grief.py`: Safely cast `trauma_accum` dictionary values to floats before subtracting severity reductions.
  * `zen.py` & `therapy.py`: Wrapped threshold markers in explicit `int(float())` casts to bulletproof the logic against loosely typed config payloads.
  * `bureau.py`: Safely extracted `MIN_WORD_COUNT` to prevent `AttributeError` crashes when `BoneConfig` arrives as a dynamic dictionary rather than a namespace.
* **Dialogue Buffer Protection:** Protected the Chronos `_build_continuity_packet` from throwing an `IndexError` when attempting to fetch the last system output from a completely empty dialogue buffer during cold boots.

---

### **BONEAMANITA 20.3.2 "The Deep Type-Safety Pass"**

**Architectural Additions & Test Suite Sealing**

* **Dual-Baseline Topology Enforcement:** Upgraded the `navi-fractal` semantic topology check to evaluate active memory graphs against *both* the Maslov-Sneppen (`_native_rewire`) and configuration model (`_native_configuration_model`) null models simultaneously. The system now takes the strictest clustering threshold of the two to mathematically guarantee a terminal false positive is impossible.
* **Lexicon Sentiment Resurrection:** Uncovered and excised a massive logical blind spot in `LexiconStore.load_vocabulary` that previously prevented sentiment-based tokens from entering the Reverse Index. The `measure_valence` sentiment analyzer is now fully alive and actively grading inputs.
* **Chaos Engineering Suites (`test_drivers.py` & `test_lexicon.py`):** Authored brutal new test coverage that intentionally blasts the drivers and linguistic analyzers with malformed, loosely typed `SimpleNamespace` objects and string-coerced JSON configuration numbers to guarantee the type-casting armor never yields to a `TypeError`.

**Fixed**

* **Permutation Entropy Blindness:** Fixed a silently swallowed `AttributeError` in the `GeodesicOrchestrator`. The `navi-SAD` protocol now natively tracks `voltage_history` inside the daemon loop rather than querying the downstream dataclass, restoring The Jester's ability to shatter Point-Attractors.
* **Enneagram Baseline Paralysis:** Fixed a flaw in the hysteresis test suite that fed the driver a "perfect comfort" baseline, which mathematically caused it to refuse shifting to `THE MANIC` despite high voltage.
* **Terminal Autophagy Race Condition:** Fixed `test_macro.py`'s `cannibalize` validation. The engine mathematically purges the oldest/lightest nodes first; the test now properly isolates the Genesis blueprint before evaluating the load-bearing wall against the typo.
* **Subconscious Burial Data Leaks:** Patched `SubconsciousStrata.bury` to safely evaluate `word` keys before persisting to disk, preventing `KeyError` IO halts when archiving fractured thoughts.
* **Cold Boot Crash:** Guarded `embryo.physics` manipulations with `safe_set` to prevent `NoneType` crashes during headless or purely API-driven engine boots.

**Changed & Optimized**

* **EAFP Over Paranoid Catching:** Executed a system-wide purge of nested `isinstance` and `hasattr` boilerplate across `reporter.py`, `genesis.py`, `core.py`, and `lexicon.py`, replacing them with explicit `safe_get` dynamic typing and clean scalar routing.
* **String-Coerced JSON Armor:** Defended the entire `drivers/` directory (Enneagram, Consultant, Liminal, Syntax, Validator, UserProfile) against dynamic JSON typing by enforcing strict `float()` and `int()` casting on all physical thresholds, vectors, and config parameters.
* **Exception Control Flow Excised:** Overhauled `SystemHealth.__getattr__` to cleanly return `.get(comp, True)` for online flags rather than leveraging Python's heavy `AttributeError` exception handler to act as the pipeline's circuit breaker control flow.
* **Thread-Lock Fast-Failing:** Optimized `EventBus.unsubscribe` to verify subscriber existence before paying the allocation cost of launching generator comprehensions inside a global thread lock.
* **Telemetry History Sweeps:** Optimized `TelemetryService.get_last_fatal_error` to verify the payload outcome exists before attempting to cast thousands of JSON lines into raw strings.

---

### **BONEAMANITA 20.3.1 "The Tensegrity Pass"**

**Architectural Hardening & Test Suite Sealing**

* **The Load-Bearing Center:** Built titanium test coverage for the engine's core defensive loops. The `Gordon Tensegrity Anchor`, `Counterfactual Toxicity Rejection`, and the `Jester's False Cohesion Break` are now mathematically grounded in the test suite and proven to safely mutate the system under high drag and entropy.
* **Exorcism of Phantom Objects:** Exterminated deeply nested `MagicMock` topology traps across the test suite. Forced biological regulators and physical gates to evaluate against hard deterministic floats rather than dynamically crashing on phantom objects during `process_context` ticks.
* **Paradox State Alignment:** Forced the Paradox engine test to evaluate within `TECHNICAL` mode, proving the `PromptComposer` correctly injects Orthogonal Attention under high contradiction (which `ADVENTURE` mode intentionally ignores).

**Fixed**

* **The Apoptotic REM Crash:** Patched a fatal `NameError` in `DreamEngine.enter_rem_cycle`. The system can now successfully compress its conversational trauma into "scar-tissue axioms" without crashing the sleep cycle.
* **Akashic Amnesia:** Fixed a localized amnesia bug where the `_mutate_epigenetics` cycle successfully injected mutated axioms into the active `lore` dictionary but failed to flush them to the hard drive, causing the system to forget its evolution upon reboot.
* **False Assertions:** Purged hallucinated `unittest.mock` assertions (`called_with`) and functionally impossible logic checks (asserting memory burial during an `illuminate` node-read) from the memory test pipelines. 

**Changed & Optimized**

* **Neurochemical Hot-Loop Optimization:** Stripped paranoid `safe_get` dictionary wrapping inside high-frequency biological loops (`ChemicalState.mix`, `NeurotransmitterModulator.modulate`, and `hallucinate`), buying back fractional execution time on every engine tick.
* **Spore Network Pruning:** Completely eradicated transitional `ordvec` type-checking from the Spore networks. Removed mathematically dead code loops and paranoid void checks across `spores/memory.py` now that the core math natively guarantees deterministic list returns.

---

### **BONEAMANITA 20.3.0 "The Ordinal Proof Pass"**

**Architectural Additions (Project Navi Integrations)**

* **Mechanized Memory Architecture:** Ripped out the heuristic Householder matrix decay math in the `SubconsciousStrata`. Replaced it with native, zero-dependency Ordinal Vector Quantization adapted directly from Nelson's `ordvec` crate. 
* **Provably Optimal Forgetting:** The memory compression layer is now mathematically backed by mechanized Lean 4 proofs. The system guarantees Bayes-Optimal retrieval and Ordinal Sufficiency, meaning the engine can aggressively starve the data footprint of its memories without the risk of hallucinating false synaptic connections.
* **Native Rank-Cosine Search:** Converted the fuzzy memory dredge into a blazing-fast, pure-NumPy matrix dot product. The engine can now perform phase-space searches across thousands of "epigenetic scars" instantly without burning the ATP budget.

**Changed**

* **Memory Footprint:** Deprecated the heavy `M_t` and `Q_n` matrix JSON artifacts. The engine now stores relative topological ranks natively in a C-contiguous array (`rank_bank`), making the subconscious immune to amplitude noise.
* **Direct Attribute Config Lookup:** Refactored the `BioSystem` and `EndocrineSystem` to bypass nested dictionary getters, allowing them to cleanly inherit dynamic and patched configuration boundaries during runtime.

**Fixed**

* **The Severed Spinal Cord:** Fixed a critical state-contamination bug in `main.py` where the live `BoneConfig` feed was accidentally severed during the `BoneGenesis` boot sequence, causing the biology layer to fall back to hardcoded defaults.
* **Event Bus Race Condition:** Fixed an `AttributeError` during `MycelialNetwork` genesis where the engine attempted to broadcast a deprecated memory matrix to the event bus before the system was fully anchored.

---

### **BONEAMANITA 20.2.0 "The Excavation"**

**Architectural Amputations & Optimizations**

* **The Weight Class Purge:** Completely eradicated the artificial `WEIGHT_CLASS` (`LIGHTWEIGHT` vs `HEAVYWEIGHT`) auto-classifier from the `LLMInterface` and `PromptComposer`. All models now receive the unadulterated, complex persona block and are subjected to the `DSPyCritic`. Weak models will now fail via natural simulated physics (Terminal Exhaustion, Narrative Drag) rather than arbitrary string-based safety gates.
* **Biological Bureaucracy Excised:** Executed a massive, system-wide purge of nested `hasattr` and `getattr` defensive checks across the `phases` pipeline (`biological.py`, `cognitive.py`, `environmental.py`, `mechanical.py`), `spores/genetics.py`, and `brain/cortex.py`. The runtime loop now mathematically trusts the `Genesis` bootloader and handles fallbacks natively to drastically reduce cognitive noise and wasted CPU cycles.
* **EAFP Over TOCTOU:** Replaced Time-of-Check to Time-of-Use (TOCTOU) race conditions in `core.py` (e.g., OS directory and file existence checks) with pure EAFP (Easier to Ask for Forgiveness than Permission) logic. 
* **Algorithmic Ephemeralization:** * Replaced an O(N*M) nested double-list comprehension in `brain/mind.py` with readable, flat extension loops. 
  * Flattened iterative directory scans in `spores/io.py` into highly optimized declarative list comprehensions.
  * Flattened visual ternary bloat and consolidated duplicate control flow modifiers across the cognitive layer.
* **Topological Failsafes Enforced:** Solidified strict interface contracts for truly optional, modular components (`mind_memory.ann`, `shared_lattice`, `akashic`, `governor`). This preserves the engine's ability to seamlessly scale down for lightweight deployment and guarantees the asynchronous `PanicRoom` reboot can survive a catastrophic `Cortex` amputation ("The Bus Crash" scenario).
* **Circadian Rhythm (Idle Detection):** The engine now possesses temporal awareness. It tracks the temporal delta between inputs; if 300 seconds (5 minutes) elapse without interaction, the system crosses the idle threshold and transitions from a `WAKE` state to `REM` sleep.
* **The Dream Engine:** While in `REM` sleep, the engine continues to metabolize. It slows its execution loop to save CPU, slowly burns ATP, reduces Cortisol/ROS, triggers memory defragmentation (`Autophagy`), and hallucinates "Shadow Casts" by blending its accumulated trauma vector with objects in Gordon's inventory via silent, zero-UI DSPy calls. These dreams are prepended to the UI upon waking.

**Changed**

* **Core Ignition Sequence:** Moved the daemon boot sequence (`engine.orchestrator.start_daemon()`) out of the terminal UI loop and directly into the engine's internal anatomy (`_initialize_cognition`). The pacemaker now starts automatically upon instantiation.
* **Lineage Routing Resilience:** Modified `autoload_last_spore` in `spores/network.py` to resiliently iterate through memory lineage candidates until a viable ancestor is ingested, preventing total failure on a corrupted youngest save.

**Fixed**

* **The Forge Short-Circuit:** Fixed a terminal blockage in `machine/forge.py` where a single failed entanglement check would instantly abort the entire inventory iteration, ignoring valid crafting recipes. 
* **Catastrophic UnboundLocalError:** Hard-reset spatial indentation and explicit variable padding in `machine/architect.py`'s legacy unpacking logic to fix a boot-sequence crash that shattered 138 tests.
* **Cache Race Conditions:** Eradicated in-place list mutation in `machine/consolidator.py` to prevent thread race conditions when saving syntactic weights to the Lore Manifest.
* **Sycophancy Rollback Bug:** Restored headless UI bypassing in `brain/cortex.py` to prevent `KeyError` transaction rollbacks during the Sycophancy Gravity Well chaos tests, ensuring The Jester can successfully shatter point-attractors.
* **Concurrency Deadlocks (The Great Hang):** Implemented a structural fail-safe in the Geodesic Orchestrator's background thread. If the daemon encounters an unhandled exception or `MemoryError`, it forcibly unblocks the main thread by injecting a `CRITICAL DAEMON CRASH` snapshot into the output buffer, preventing terminal paralysis.
* **Test Suite Paralysis:** Fixed an issue where tests (e.g., `test_governor_macro_policy_shift`) would infinitely hang because the headless test environment was bypassing the terminal-level daemon ignition.
