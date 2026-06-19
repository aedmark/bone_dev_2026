# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 20.5.2 "The Paranoia Purge"**

**Security & Containment**
- **Strict Geometric Containment:** Patched a silent directory traversal vulnerability in `TheSubstrate.execute_writes` (`mechanics/tools.py`) by replacing `os.path.abspath` and `startswith()` string checks with strict `os.path.realpath` and `os.path.commonpath` evaluations.

**Performance & Architecture**
- **O(N) Amputations & Memory Optimizations:**
  - **Garbage Collection Relief:** Eradicated massive object instantiation inside the `_native_rewire` graph topology loop (`cycle.py`) and `ChemicalState.homeostasis` tick loop (`brain/mind.py`) by moving maps to class constants and bypassing eager dictionary `get()` defaults.
  - **Hash Traversal Rescue:** Converted `O(N)` list iterations to `O(1)` hash sets for vocabulary scanning in `drivers/syntax.py` and `drivers/liminal.py`.
  - **Native C-Level Execution:** Dropped redundant python-level `in` checks guarding `.replace()` calls in `brain/cortex.py`, letting the C-level string operations natively handle the workload.
- **The Vector Array Collapse:** Stabilized `goal_vec` matrix generation in the `GeodesicOrchestrator` (`cycle.py`) by rigidly mapping tag indices, neutralizing catastrophic mathematical misalignments if downstream modules inject rogue dictionary keys into the physics vector.
- **Config Pre-compilation:** Purged real-time `LoreManifest` JSON fetching from hot loops. Constant references (e.g., the Sincerity Map, Drag Maximums, Liminal Weights) are now strictly pre-compiled in `__init__` functions across the `phases/` and `drivers/` modules.
- **Type Paranoia Drift Remediation:** Systematically removed "paranoid" syntax logic. Stripped abstraction wrappers (`safe_get`/`safe_set`), redundant type-casting (e.g., `str()` on strings), and explicit string lowercasing where variables were mathematically guaranteed to be sanitized or strictly typed.
- **Graph Traversal Short-Circuits:** Restructured heavy boolean logic in `RandomRetrievalNavigator` into a short-circuited condition block, drastically reducing the operation weight during deep-library topological scans.
- **Object Bloat Removal:** Collapsed redundant intermediate dictionary generation in `TheAkashicRecord._get_dominant_force` down to a memory-efficient list comprehension.
- **Hardened Array Extraction:** Explicitly bound variable padding in `BoneArchitect.awaken` with `max(0, 5 - len(results))` to prevent Python's negative-multiplier quirk from swallowing silent array extraction index errors.

---

### **BONEAMANITA 20.5.1 "The Deep Tissue Massage"**

**Security & Immunity**
- **Cryptographic Upgrade:** Upgraded `HippocampalCache` hashing from computationally compromised MD5 to SHA-256 for robust neural cache hygiene (`brain/ann.py`).
- **Atomic State Swaps:** Patched `soul/oroboros.py` to use Python's secure `tempfile` library for writing legacy states, eliminating hardcoded `.tmp` path race conditions and symlink vulnerabilities.
- **Loud Failure Protocol:** Stripped silent `TypeError` catching from `PhysicsPacket.__setattr__` (`physics/models.py`). Toxic string injections into critical energy floats (like `voltage`) will now fail loudly to prevent corrupted state masking.

**Performance & Architecture**
- **The Big O Overhaul:** Drastically reduced computational overhead in `MemoryCore` (`spores/memory.py`):
  - Replaced massive list allocation and $O(N \log N)$ `min()` scans with $O(N)$ running minimums in `cannibalize()`.
  - Replaced $O(N \log N)$ `np.argsort` with $O(N)$ `np.argpartition` for lightning-fast Subconscious Dredging.
  - Amputated nested $O(N^2)$ iteration in `prune_synapses` in favor of C-level `set.intersection`.
  - Replaced boilerplate nested index loops with `itertools.combinations` in `illuminate()`.
- **I/O Apocalypse Averted:** Blocked two catastrophic disk-read bottlenecks:
  - Cached `LexiconService` in `machine/forge.py` to prevent reloading JSON from disk every time crafting is attempted.
  - Amputated `_load_index()` from `_prune_strata()` (`spores/memory.py`), slicing arrays directly in RAM instead of triggering a full disk re-parse and re-vectorization during deep memory pruning.
- **Paranoia Purge:** Removed redundant, CPU-wasting "paranoid programming" checks:
  - Optimized `safe_get` (`struts.py`) to bypass explicit `hasattr` loops, defaulting to native `dict.get` and `getattr` in $O(1)$ time.
  - Removed `hasattr` checks in `CycleContext.to_dict` (`core.py`), trusting `@dataclass(slots=True)` memory constraints.
  - Amputated pure-Python matrix math abstractions (`_identity`, `_mat_mul`, etc.) in `spores/spore_utils.py` to defer all linear algebra directly to NumPy.
- **Reflection Bottleneck:** Cached `dataclasses.fields(cls)` in `PhysicsPacket._safe_init` (`physics/models.py`), eliminating dynamic class reflection overhead during high-volume packet instantiation.

**Bug Fixes**
- **The Infinite Recursion Trap:** Patched the Mitchell Protocol (`spores/memory.py`) to track object `id()` hashes, preventing fatal `RecursionError` crashes when encountering circular references.
- **Combinatorial Scope Crash:** Fixed a critical indentation bug in `MemoryCore.illuminate` where `itertools` pairing was accidentally scoped inside the memory-scoring loop, triggering `UnboundLocalError` on zero-resonance inputs and severing the phase pipeline.
- **Event Redundancy:** Consolidated `Q_MATRIX_UPDATED` broadcasts into a centralized `_sync_q_matrix()` method in `spores/network.py` to uphold DRY principles and prevent desyncs.


### **BONEAMANITA 20.5.0 "The S.L.A.S.H. Audit"**

**Security & Immunity**

- **The Lexical Firewall Hardening:** Expanded `_DESTRUCTIVE_PATTERNS` in `main.py` to intercept raw `eval()`, `exec()`, and native system imports (`pty`, `sys`), physically blocking adversarial python injection prior to cognitive load.
- **API Key Redaction:** Overhauled `core.py`'s `JSONEncoder` to actively scrub dictionaries for terms like "api_key", "secret", "token", and "password". Toxic payload data is now cleanly replaced with `[REDACTED]` before being flushed to telemetry logs.

**Refactoring & Optimization**

- **The Syntactic Purge:** Upgraded `safe_get` in `struts.py` to support array-based key fallbacks, allowing the system to amputate deeply nested, paranoid `getattr()` chains throughout the cognitive cycle.
- **$O(1)$ Graph Traversal:** Ripped out the $O(N)$ `list.pop(0)` operation inside the `cycle.py` background WLS thread and replaced it with a `collections.deque` topological BFS queue, preventing the thread from choking as the spatial memory radius expands.
- **EAFP Logic Shifts:** Replaced paranoid, multi-tier object inspection in `_verify_semantic_topology` and `purge_context` with clean, pythonic 'Easier to Ask for Forgiveness than Permission' `try-except` boundary blocks.

**Fixed**

- **The Reality Fracture (`NameError`):** Fixed a load-bearing amputation in `cycle.py` where the Cybernetic Governor's native variable demands (`res_delta`, `u_exhaustion`) were accidentally severed from the local namespace, instantly shunting the system into Safe Mode.
- **The Override Currency Bug:** Re-routed the Architect's `#override` gate in `main.py` to target the correct endocrine pathway (`self.bio.endo.glimmers`), allowing the user to properly spend their currency to assert agency. Introduced mathematical proofs in the test suite to validate both successful expenditures and bankrupt rejections.
- **The Moog Memory Erasure:** Fixed an architectural flaw in `brain/cortex.py` where the system prematurely popped the `dialogue_buffer` upon detecting un-actionable toxicity. High-drag prompts are now properly quarantined in the worry ledger without accidentally deleting the previous, healthy conversational turn.
- **The Anaerobic Chaos Leak:** Plugged a massive accounting error in `body/metabolism.py`. Heavy structural payloads (`chi` > 0.8, `psi` > 0.8) were dodging their biological tax because the `ANAEROBIC_THRESHOLD` bypass fired before the waste was calculated. Chaos waste is now dynamically calculated and actively poisons the `ros_buildup` even when the system burns HP instead of ATP.
- **Silent Asynchronous Failures:** Re-bound the `mem` local variable inside the background topology WLS thread so the engine can properly execute apoptosis (terminal shutdown) when it detects structural rot, rather than the shutdown command crashing silently.

---

### **BONEAMANITA 20.4.9 "The Jester's Gambit"**

**Feature Additions**

* **The Void (`/hallucinate`):** Integrated a native hallucination command into the `CommandProcessor`. It levies a strict 25 ATP tax to mathematically bypass the thermal locks, physically spiking phase-space tension ($\mu \approx 0.9$) and creative drive ($\kappa \ge 0.5$). It injects a hardcoded cognitive mandate directly into the `dialogue_buffer` to summon The Jester and force a lateral paradigm shift.
* **Topological Reality Validation:** Ripped out the performative abstraction (mock linear data) in `_bg_wls_check` inside `cycle.py`. Wired in a true Breadth-First Search (BFS) algorithm to calculate the actual Mass-Radius scaling and fractal geometry of the `hippocampus` memory graph. 

**Refactoring & Optimization**

* **Reality Stack Tensegrity:** Cleaned a structural dependency leak in `core.py`. Decoupled grammar rules from the mutable `RealityStack` object and centralized them into the static `RealityLayer` class as the absolute source of truth. Altered the test harness to respect the decoupled architecture.
* **Command Migration & Interrupts:** Stripped the hardcoded `/zen` and `/flush` commands out of `main.py`'s primary `process_turn` loop, routing them gracefully through `CommandProcessor` under the unified `_cmd_rest` protocol.
* **Data Amputation:** Purged dead-weight state tracking (`village_data`, `joy_history`, `mutations: {}`) from the `save_state` serialization payload, optimizing memory output and disk I/O.
* **Asynchronous Latency:** Offloaded the synchronous `actual_adj` dictionary comprehension in the `_verify_semantic_topology` check to the async worker pool, preventing main thread blocking and subsequent `queue.Empty` crashes.

**Fixed**

* **The Null Exception Minefield:** Executed a global syntactic purge across `commands.py`, replacing reckless `ux().format()` chained calls with the safe `ux_format()` utility. This prevents fatal `AttributeError` engine crashes if a string is ever missing from `ux_strings.json`.
* **Dictionary vs. Object Fallback:** Resolved a silent assignment failure where `safe_set` failed to mutate the `MockPhys` class object because it was originally designed for the `active_physics` dictionary. Explicitly separated the live state update from the base engine update.
* **Telemetry Crash Trap:** Hardened the `/report` and `/diag` commands with safe `getattr` boundary checks to prevent the engine from fatally crashing if the telemetry module boots offline.
* **The Apoptotic Test Trigger:** Restored the `do this forever` trap to `main.py`'s execution loop explicitly as a load-bearing pillar for the Apoptotic Crash test harness.

---

### **BONEAMANITA 20.4.8 "The Moog Protocol"**

**Feature Additions**

* **The Moog Protocol (cortex.py & cycle.py):** Integrated a cognitive quarantine system (`worry_ledger`) into `TheCortex`. The engine now intercepts high-drag, high-chaos loops before they trigger an Apoptotic Crash, physically amputating the text from the `dialogue_buffer`.
* **Headless Worry Processing (cycle.py):** Wired the `worry_ledger` into the `GeodesicOrchestrator`'s asynchronous background daemon (`_process_rem_tick`). Worries are processed during REM sleep without blocking the main user thread.
* **Metabolic Yield & Dark Matter:** Implemented a binary actionability filter for quarantined worries. Actionable items are converted directly into strict Council Mandates. Uncontrollable/existential concerns are permanently stripped of narrative weight, stamped into the Akashic Record as "Dark Matter", and yield a massive ROS purge and a Glimmer.

**Test Suite & Architecture Hardening**

* **Python 3.12 Sequence Fortification:** Grounded unconfigured `MagicMock` injections in the `test_architecture.py` suite. Fixed strict sequence validation errors (`random.sample()`) and tuple-unpacking crashes (`ValueError: not enough values to unpack`) across the `Composer`, `Gatekeeper`, and `Inventory` mocks.
* **Gordon Anchor Restoration:** Fixed a physical leak in `_evaluate_toxicity` where the `SYSTEM_HALT` return statement was accidentally bypassed, restoring Gordon's ability to cleanly lock the architecture under high narrative friction.
* **Typing Convergence:** Resolved cascading `TypeError` collapses in the test runner by explicitly hydrating the engine mocks with concrete floats and integers for mathematical limits (`tick_count`, `m_a`, `latency`, `calculate_coupling`). All 211 tests now run green.

---

### **BONEAMANITA 20.4.7 "The Moog Protocol Preparation"**

**Architectural Patches & Optimizations**

* **Lambda Decoupling (cycle.py):** Excised fragile lambda-closure injections from `GeodesicOrchestrator` to fix telemetry memory leakage. Orchestrator metrics now pull directly from the `CyberneticGovernor`, resolving orphan-key errors in snapshot metadata.
* **Redundancy Pruning (cycle.py):** Removed redundant variable aliasing in the physics packet, reducing object bloat in the `CycleContext`.
* **Topology Check Optimization (cycle.py):** Eliminated the redundant tuple round-trip in `_verify_semantic_topology`. The system now directly processes dictionary sets, improving throughput during semantic rewiring.
* **EventBus Recursion Fix (core.py):** Refactored `EventBus.publish` to use a set-based lock (`active_events`). This resolves a critical "swallowing" bug where failure logs were being blocked by their own recursion guards.
* **Telemetry I/O Hardening (core.py):** Replaced byte-chunking logic in `TelemetryService._tail_file` with native line-buffered streaming. This prevents JSON character corruption at file boundaries.
* **Trust Boundary Hardening (main.py):** Expanded `_DESTRUCTIVE_PATTERNS` to include Python-native structural breakout attempts (`os.system`, `subprocess`, dynamic imports), shielding the engine against deeper runtime exploits.

---

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

