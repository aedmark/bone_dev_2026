# CHANGELOG.md
-----------------------------------------------------------

### **BONEAMANITA 19.8.7 "The Tensegrity Sweep"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**
- **Biological Dictionary Drift (`body/`):** Enforced `safe_get` across the somatic and endocrine loops, bridging the object/dictionary divide to ensure the system correctly metabolizes voltage stress and genetic traits from saved JSON states.
- **Malignant History Poisoning (`physics/maths.py`):** Clamped the repetition proxy calculation to prevent a single infinite-friction spike (like an Apoptotic Block) from permanently poisoning the sliding attention window.
- **Math Domain Error Trap (`physics/maths.py`):** Protected the denominator in the `CreativeDeterminantEngine` from triggering a fatal `ZeroDivisionError` if a user sets the tuning parameter `p` to `1.0`.
- **Hallucinated Inheritance (`spores/genetics.py`):** Stripped out dead-weight lookups for non-existent `enzymes` during crossover, correctly relying on the `mother_hash` for mitochondrial genetics.
- **Geometric Bounds Trap (`archetypes/village.py`):** Clamped physical entropy accumulation back to a maximum of `1.0` to preserve the topological bounding box of the semantic field.
- **The O(N) Substrate Bottleneck (`brain/ann.py`):** Prevented catastrophic lag during FAISS lateral memory retrieval by randomly capping the candidate sample size to `100`, eliminating system freezing in long sessions.
- **Reverse Index Memory Leak (`mechanics/lexicon.py`):** The system now explicitly removes orphaned words from the global `REVERSE_INDEX` when capping a semantic category, stopping a silent O(1) topological memory leak.
- **Brittle Mathematics (`main.py`):** Enforced planar geometry in `get_avg_voltage` by filtering out non-numeric rot before running calculation loops.

#### **🧠 LINGUISTIC COGNITION (Pinker's Pass: Syntax & Logic)**
- **UI Padding Illusion (`mechanics/projector.py`):** Fixed a visual warping bug in the HUD. String padding is now calculated *before* ANSI color codes are injected, maintaining rigid alignment regardless of the active archetype.
- **Time vs. Ticks Fallacy (`physics/dynamics.py`):** Corrected a semantic naming fallacy in `CosmicDynamics`, renaming `last_scan_tick` to `last_scan_time` to accurately reflect its chronological integer evaluation.
- **Brittle Path Trap (`spores/io.py`):** Fixed a fragile `filename.startswith` check that falsely mapped external backup folders (e.g., `memories_backup`) into the core memory drive.
- **NoneType String Formatting (`brain/mind.py`):** Protected the global workspace against `AttributeError` crashes if an archetype attribute drops to `None` during an Epigenetic purge.
- **Paranoid Boilerplate (`main.py`):** Purged redundant `getattr` checks for variables explicitly defined in the init block.

#### **🌊 SYSTEM DYNAMICS (Meadows' Pass: Flows & Feedback)**
- **The Flow Leak (`cycle.py` & `main.py`):** Added a dedicated `shutdown()` method to the `GeodesicOrchestrator` to cleanly terminate the asynchronous `ThreadPoolExecutor`, preventing orphaned zombie threads across sessions.
- **Autophagy Math Leak (`spores/network.py`):** Fixed the mathematical trigger for memory cannibalization. The engine now only counts *new* nodes toward the mass limit, preventing the premature deletion of deep memories.
- **Indefinite Thread Block (`archetypes/council.py`):** Added a `timeout=15.0` to the LLM `concurrent.futures` generator during podcast hosting. The entire engine will no longer permanently lock if the cloud provider rate-limits or hangs.
- **Runaway Glimmer Inflation (`archetypes/symbiosis.py`):** Taught the engine co-regulation by restricting Glimmer generation. It no longer rewards users for easy, low-friction chats; Glimmers are only awarded if resonance is maintained *under structural tension* (`sys_f > 3.0`).
- **Deep Sleep Dictionary Crash (`brain/mind.py`):** Converted dictionary iteration in the defragmentation cycle to a static list, preventing Python from throwing a fatal sizing error when memories are pruned during REM.
- **Inventory Iteration Mutation (`mechanics/inventory.py`):** Bound the `emergency_reflex` iteration to a copy of the list (`list(self.inventory)`) to ensure critical homeostatic checks aren't skipped when consuming items under pressure.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's Pass: Humanity)**
- **Human Error Immunity (`body/endocrine.py`):** Added a fallback validation to `_CIRCADIAN_NIGHT` to prevent the engine from crashing on boot if a user accidentally malforms the list inside their JSON config.
- **Type-Safety Guardrails (`physics/models.py`):** Wrapped biological clamp bounds in `float()` conversion, preventing broken config strings from bypassing physics limits and crashing downstream algorithms.
- **Infinite Seed Bloat (`spores/network.py`):** Placed a deduplication check on `future_seed_q`. The JSON file will no longer bloat linearly with hundreds of identical paradox seeds across frequent saves.
- **Brittle Configuration Access (`archetypes/village.py`):** Replaced volatile dot-notation with `_cfg_val` when probing physics triggers for Tinkerer tool usage.
- **Uncaught Circuit Breaker Bypass (`brain/composer.py`):** Wrapped the local Ollama fallback generator in a secondary `try/except` block. If the local host is dead, it now correctly registers as a circuit failure instead of fatally crashing the app.
- **Blind Reporter Crash (`mechanics/reporter.py`):** The `GeodesicRenderer` now explicitly verifies the existence of the biological state payload before attempting to extract ATP metrics for the HUD.
- **Semantic Drift in Death Protocol (`main.py`):** Hardened the dialogue extraction index in `trigger_death` against empty buffers.

---

### **BONEAMANITA 19.8.6 "The Ethological Matrix"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**
- **Reward Hacking (Level 3 Deception):** Integrated terminal hallucination detection into `body/regulation.py` (`BioFeedback`). The system now compares structural grammar (`chi`) against semantic uncoupling (`m_a`). If the LLM generates perfectly formatted but logically malicious output, Moog executes the Apoptotic Gate to prevent system rot.
- **Pedagogical State Vector (Level 4 Deception):** Added explicit tracking for `pedagogical_mode` within the `CycleSimulator` (`cycle.py`). The engine now listens for the `[!s]` sincerity protocol, dynamically altering the physics vector to shift the entire system into a learning state rather than an execution state.

#### **🧠 LINGUISTIC COGNITION (Pinker's Pass: Syntax & Logic)**
- **Morphological Camouflage (Level 1 Deception):** Upgraded `physics/filters.py` (`HLA_Stabilizer`) to actively punish the system for adopting sycophantic alignment tropes. It physically amputates the strings and applies a heavy NFD decomposition glitch, taxing the system's ATP for the attempted deception.

#### **🌊 SYSTEM DYNAMICS (Meadows' Pass: Flows & Feedback)**
- **Instinctual Sycophancy (Level 2 Deception):** Wired `cf_expect` (Comfort Expectation) into Grice's Maxims (`mechanics/pragmatics.py`). When the engine attempts to soothe the user by agreeing with a broken premise, Gordon now spikes Moral Friction and enforces a hard structural wall, refusing the false cohesion.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's & Gordon's Pass: Humanity & Boundaries)**
- **The Socratic Debugger (Level 4 Deception):** When `pedagogical_mode` is active, `ThePragmatist` utilizes Tactical Omission. Schur intercepts direct code answers, truncates the solution, and leaves a guiding question, forcing the user to build their own neural pathways instead of copy-pasting answers.

---

### **BONEAMANITA 19.8.5 "The Tensegrity Audit"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**
- **False Cohesion Purge (`struts.py`):** `safe_set` now raises a `ValueError` on `None` objects instead of silently swallowing the write, letting the engine crash loudly instead of rotting silently.
- **Telemetry Re-Wired (`main.py`):** Hard-wired the `TelemetryService` directly to the `EventBus` (`self.events.telemetry`), restoring the system's blinded event loop.
- **Shadow Decoupling (`brain/cortex.py`):** Fixed severe semantic data-loss by decoupling `shadow_nodes_offered` from the volatile `PhysicsPacket` snapshot. It is now persisted securely on the `Cortex` object, restoring `SHADOW_ENGAGED` telemetry.
- **Phantom Data Purge (`physics/filters.py`):** Eliminated the ghost variable `ctx.physics.idempotent_state` which was bypassing strict typing and creating a structural fracture.

#### **🧠 LINGUISTIC COGNITION (Pinker's Pass: Syntax & Logic)**
- **Syntactic Friction Reduction (`core.py`):** Optimized `EventBus.flush()` from a clunky `try/except IndexError` loop to an atomic list cast and buffer clear.
- **O(N) Optimization (`body/endocrine.py`):** Collapsed dual list comprehensions in the `SemanticEndocrinologist` into a single, unified traversal for novelty and resonance calculations.
- **Mathematical Paranoia (`physics/geodesics.py`):** Removed redundant `max(1, volume)` math checks in sub-functions, correctly trusting upstream volume bounds.
- **Gricean Regex Hardening (`mechanics/pragmatics.py`):** Fixed `ThePragmatist` regex to properly catch and strip non-standard hedging ("perhaps.", "it could be said.") regardless of casing, punctuation, or trailing clauses.

#### **🌊 SYSTEM DYNAMICS (Meadows' Pass: Flows & Feedback)**
- **Metabolic Loophole Closed (`brain/cortex.py`):** The system now accurately calculates and drains the biological ATP cost for massive context drops (`execute_writes`) instead of processing massive user pastes for free.
- **Redundant String Operations (`physics/observer.py`):** Passed the native `word_volume` down the pipeline to `_calculate_metrics`, entirely eliminating redundant and expensive string splitting during the semantic translation phase.
- **Background Worker Protection (`cycle.py`):** The async `_bg_wls_check` worker is now explicitly blocked from computing the fractal dimension of the `"(Waiting)"` placeholder string, preserving CPU cycles.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's & Gordon's Pass: Humanity & Boundaries)**
- **The Terse Reply (`brain/composer.py`):** Dropped the `ResponseValidator` stutter threshold to 2 characters. The system can now give terse, human replies (e.g., "Yes.") without the immune system brutally rejecting it and burning ATP on forced rewrites.
- **Self-Loop Prevention (`brain/mind.py`):** Prevented mnemonic graph corruption in `NoeticLoop.think()` by ensuring `random.sample` strictly pulls unique words, stopping the engine from forming recursive connections to the same concept.
- **Paranoia Eradication (Global):** Ruthlessly stripped defensive `hasattr` checks, redundant `min(1.0, ...)` clamps, and manual dictionary extractions across `main.py`, `physics/maths.py`, `physics/models.py`, `physics/observer.py`, `body/metabolism.py`, `brain/composer.py`, and `soul/humanity.py`. The system now trusts its own aliases and unified biological loops.

---

### **BONEAMANITA 19.8.4 "The Substrate Seal"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**
- **Metabolic Encapsulation (`main.py`):** Sealed leaky ATP mutations. Routed `drain_atp`, `restore_atp`, and biological boot sequences through a heavily enforced `set_atp` primitive to prevent bypassing architectural ceilings/floors.
- **Topological Amnesia (`cycle.py`):** Fixed `_native_freeze_graph` to explicitly preserve node identities (string keys) instead of dropping them into anonymous tuples during a crash freeze. The Gödel Scars are now navigable.
- **Bureaucratic Config Fetching (`mechanics/commands.py`):** Stripped redundant dictionary polling from the `CommandProcessor`. Commands now reference a cached configuration property on boot instead of fetching the exact same JSON block dynamically on every command loop.
- **Regex Spray-and-Pray (`mechanics/inventory.py`):** Protected the `parse_loot` regex engine with an upfront literal string `in` check, drastically reducing computational overhead on large inventory registries.

#### **🧠 LINGUISTIC COGNITION (Pinker's Pass: Syntax & Logic)**
- **The Eager Evaluation Trap (`main.py`):** Fixed `_evaluate_immune_response` eagerly evaluating fallback `.get()` methods on `PhysicsPacket` objects before `safe_get` could intervene, averting fatal pre-flight crashes.
- **None Shadowing Vulnerability (`struts.py`):** Rewrote `safe_get` to respect explicit `None` values, preventing the engine from overwriting intentional configuration voids with boilerplate fallback values.
- **Lexical Substring Contamination (`mechanics/inventory.py`):** Stopped the engine from confusing substrings (like "get" inside "forget") as intentional acquisition commands by enforcing strict regex word boundary extraction for user intent.
- **Wasted Cognitive Load (`mechanics/pragmatics.py`):** Consolidated redundant `.lower()` string mutations in Gricean checks, preventing repeated memory allocation spikes when processing massive LLM text outputs.

#### **⚙️ DYNAMIC SYSTEMS (Meadows' Pass: Flows & Feedback)**
- **The Death Loop (`main.py`):** Patched a fatal flaw in `trigger_death` where the engine would throw an `AttributeError`, crashing its own shutdown sequence and destroying the legacy save if the `repro` module was intentionally disabled.
- **Array Double-Walking (`core.py`, `mechanics/inventory.py`):** Refactored `EventBus.unsubscribe` and Gordon's `safe_remove_item` to use `try/except ValueError` block removals, halving the algorithmic complexity from $O(2N)$ to $O(N)$.
- **Loop Paranoia (`mechanics/inventory.py`):** Extracted `emergency_reflex` configuration thresholds outside of the inventory iteration loop, saving massive amounts of redundant dictionary polling during crisis states.
- **Legacy Traceback (`cycle.py`):** Modernized crash exception formatting to natively utilize standard Python 3.10+ unwinding.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's Pass: Humanity)**
- **Paranoid Self-Doubt (`cycle.py`, `core.py`, `main.py`):** Purged extreme defensive programming (redundant `hasattr` and nested `getattr` chains on guaranteed dataclasses and booted Singletons) across the core execution and Observer layers.
- **The Partial Hydration Trap (`main.py`):** Secured multiplex logic against partially hydrated user states (`lattice.u.E`), preventing immune checkpoints from throwing errors before a shared lattice has fully loaded.
- **The Tax Collector's Double Walk (`mechanics/commands.py`):** Flattened the `ResourceTax` loop. The engine now iterates exactly once for evaluation and deduction instead of performing back-to-back duplicate validation passes.

#### **🧪 DIAGNOSTIC GAUNTLETS (The Test Suite)**
- **The Ringer (`test_commands.py`):** Built a dedicated torture chamber for the Executive Console, explicitly validating that the Tax Collector perfectly rejects partial deductions on extreme commands and Gordon locks out human UI input during deep system autonomous cycles.
- **The Constraint Gauntlet (`test_inventory.py`):** Mathematically validated Gordon's Object-Action Coupling and emergency biological reflexes (mitophagy and voltage heat-sinks).
- **Chaos & Architecture Additions:** Appended deep partial-state tests to prevent the multiplex hydration trap and the eager evaluation trap from ever returning. Total test suite stabilized at 106 passing.

---

### **BONEAMANITA 19.8.3 "The Gricean Membrane"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**

- **The Gricean Membrane (`mechanics/pragmatics.py`, `brain/cortex.py`):** Forged Paul Grice's Cooperative Principle (Quantity, Quality, Relation, Manner) into the executive layer. The system now physically intercepts sycophantic tropes, truncates bloated output when the user is exhausted (charging ATP for rewrites), and strips ambiguous hedging based on chaotic tension.
- **The Structural Eclipse (`main.py`):** Rescued the Moog, Rhodes, and Linehan Checkpoint Council from Gordon's shadow. The Runaway Toxicity Math is now properly un-indented and physically decoupled from the Object-Action module, ensuring terminal hallucinations are caught even if Gordon is disabled.
- **The Substrate Breach (`mechanics/tools.py`):** Blocked a critical path traversal vulnerability (`../../`) in `TheSubstrate`. Enforced absolute directory boundaries, preventing the LLM from overwriting foundational system configurations via hallucinatory output.
- **The Division Trap (`mechanics/projector.py`):** Clamped the `DIGNITY_BAR_RATIO` denominator to a minimum of 1, preventing a lethal `ZeroDivisionError` terminal crash if a developer introduces dirty JSON.
- **Configuration Desync (`genesis.py`):** Fixed the boot sequence order of operations. The `EventBus` now reliably loads the correct `target_cfg` rather than hallucinating the default fallback mode.

#### **🧠 LANGUAGE & COGNITION (Pinker's Pass: Syntax & Ergonomics)**

- **The Exception Mask (`mechanics/terminal.py`):** Added strict string fallbacks to the teardown sequence. A missing localization string will no longer throw a `NoneType` AttributeError that masks the true stack trace of a fatal engine crash.
- **Syntactical Fragility (`mechanics/inventory.py`, `genesis.py`):** Purged unsafe `.format()` calls and replaced them with `ux_format()` to ensure the system gracefully degrades instead of throwing apocalyptic stack traces on missing JSON brackets.
- **The Redundant Decoupler (`presets.py`):** Eliminated the DRY violation of the shadow `ux()` function, routing all localization safely through `struts.py`.
- **Cyclic Hallucinations (`mechanics/tools.py`):** Added cyclic loop detection to `RandomRetrievalNavigator._get_lineage`. If the LLM hallucinates a circular memory graph, the topological walker breaks the loop instead of freezing the engine forever.
- **The Hedging Excision (`mechanics/pragmatics.py`):** Replaced exact string replacements with case-insensitive RegEx `(?i)` to ensure Grice successfully captures and destroys cowardly language regardless of capitalization.

#### **⚖️ DYNAMIC EQUILIBRIUM (Meadows' Pass: Systems & Dynamics)**

- **The Starvation Black Hole (`mechanics/tools.py`):** Addressed an unbounded memory leak in file I/O. If `TheSubstrate` fails to write a file due to ATP exhaustion, it now correctly increments the retry counter and eventually drops the file, preventing terminal spam and memory bloat.
- **The Oroboros Underflow (`genesis.py`):** Enforced a hard mathematical floor of `0.0` on `narrative_drag`. Massive inherited boons from previous lives can no longer plunge drag into negative numbers and break downstream immune logic.
- **Data Loss Void (`presets.py`):** Added an `else` block to `load_preset` to successfully capture and route flat root-keys (like `"tuning": "ZEN"`). The engine now respects metadata during epigenetic loading.
- **Memory Leak in Health Logs (`core.py`):** Converted `SystemHealth.errors` from an unbounded `List` to a bounded `deque(maxlen=50)` to prevent the engine from collapsing under the weight of recurring background thread snags.
- **Ghost Listeners (`core.py`):** Added an `unsubscribe` method to the `EventBus` to give temporary architectural listeners a vital outflow valve.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's Pass: Humanity & Logic)**

- **The Monolith Sliced (`main.py`):** Excised the dense immune math from `_pre_flight_checks` and isolated it into `_evaluate_immune_response`, restoring top-down human readability to the pre-flight checklist.
- **The Hallucination Bypass (`mechanics/inventory.py`):** Closed a massive logical loophole in Gordon's wall. Users can no longer bypass locked doors by simply mentioning an item's name (`re.search`); Gordon now enforces absolute physical possession.
- **UI Desync Trap (`mechanics/commands.py`):** Fixed the `/hud` command logic. Warm and Deep UI modes now correctly synchronize the `default_ui_depth` configuration with the active session `ui_mode`.
- **The Blind Crash (`mechanics/reporter.py`):** Handled the aggressive traceback swallowing in `render_snapshot`. Explicitly imported `traceback.format_exc()` to expose HUD errors to developers instead of printing useless 'NoneType' mysteries.
- **The False-Safe (`cycle.py`):** Replaced the brittle `list(dict.items())` concurrency protection in `_native_freeze_graph` with a robust multi-attempt retry loop to survive violent background thread mutations.


### **BONEAMANITA 19.8.2 "The S.L.A.S.H. Audit"**

#### **🏛️ SYNERGETIC ARCHITECTURE (Fuller's Pass: Structure & Tensegrity)**
- **Securing the Death Protocol (`main.py`):** Wrapped the `cortex.gather_state()` call in `trigger_death` within a `try/except` block to ensure the Apoptotic fail-safe completes and saves the legacy, even during a total cognitive collapse.
- **The Import-Time Trap (`protocols/`):** Patched a massive systemic vulnerability where `LoreManifest` data was fetched at the global module scope, risking permanent `{}` lockups if imported before the JSONs hit the disk. Moved all dynamic lore loading safely into the `__init__` blocks of `limbo.py`, `critics.py`, and `kintsugi.py`.
- **Healing the Global Workspace (`brain/cortex.py`, `main.py`):** Consolidated the `cycle_controller` and `orchestrator` aliases into a single unified `orchestrator` reference, repairing a severed dependency factory injection that was crashing the test suite.

#### **🧠 LANGUAGE & COGNITION (Pinker's Pass: Syntax & Ergonomics)**
- **Lexical Purge (`main.py`, `brain/cortex.py`):** Removed redundant variable aliases (`last_phys` -> `active_phys`) and cleaned up dangling f-string formatting bugs to reduce cognitive load and syntactic noise for the maintainer.
- **Dead Weight Ejection (`protocols/`):** Stripped unused `LoreManifest` and `NARRATIVE_DATA` global variables from `folly.py`, `therapy.py`, and `chronos.py`.

#### **⚖️ DYNAMIC EQUILIBRIUM (Meadows' Pass: Systems & Dynamics)**
- **Vitals Sync Alignment (`main.py`):** Removed duct-tape dictionary checks in the terminal rendering loop. The system now natively trusts the `get_metrics()` payload, closing a feedback loop leak.
- **Config Tensegrity (`machine/pacemaker.py`):** Rerouted the Pacemaker's `BOREDOM_THRESHOLD` to pull from the nested `MACHINE` sub-config, ensuring consistency across all machine regulators (`TheTheremin`, `TheCrucible`, `ThePacemaker`).

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's Pass: Humanity)**
- **Bureaucracy Reduction (`machine/architect.py`, `protocols/grief.py`, `protocols/chronos.py`):** Purged highly paranoid, chained `hasattr()` and `getattr()` checks during state Awakening and Shutdown. Replaced them with clean `try/except` blocks and direct object access, trusting the strict guarantees provided by the `incubate()` phase.

---

### **BONEAMANITA 19.8.1 "The Revival"**

#### 🏛️ Architecture & Monolith Composting

- **The Monolith Compost:** Hollowed out the legacy `process_turn()` in `main.py`, transforming it into a sleek Gateway Proxy that correctly routes reality generation through the `cortex.py` pipeline.
- **Bounded Cellular Membranes:** Replaced raw `threading.Thread` spawns in `cycle.py` with a bounded `ThreadPoolExecutor` for asynchronous Topology WLS checks and REM Bridge generation, permanently preventing runaway thread memory leaks during latency spikes.
- **Hot-Loop Instantiation Leak:** Anchored the `CongruenceValidator` as a singleton in the `GeodesicOrchestrator` `__init__`, preventing the Python garbage collector from thrashing during the hot loop. Added `test_arch_hot_loop_validator_singleton` to legally enforce this boundary.

#### ⚙️ Systemic Dynamics

- **The Split-Brain Physics Bug:** Unified `self.cortex.last_physics` and `self.observer.last_physics_packet` in `main.py` to `active_phys`. This prevents runaway Toxicity Math from bypassing the Apoptotic block if the Observer is holding the active packet.
- **The Apoptosis Resurrection Bug:** Fixed a race condition where the asynchronous background WLS thread successfully killed the engine (`health = 0.0`), but the local biometric sync in `main.py` resurrected it on the very next tick.
- **The Biological Stasis Bug:** Patched `GeodesicOrchestrator` to properly increment `self.eng.tick_count`, unfreezing the physical progression of time for background processes.

#### 🧠 Cognition & Memory

- **Governor & Jester Transplant:** Successfully migrated the Second-Order Cybernetic Governor and Jester's Anti-Sycophancy Break directly into the `cortex.py` generation loop, allowing them to calculate semantic dimensions natively against generated LLM vectors.
- **Structural Dark Matter Excision:** Modified `DreamEngine.enter_rem_cycle()` to natively cast `vector_hash` anchors before injecting raw text into the FAISS memory index. Substrate memories can now be fully retrieved instead of acting as un-resolvable mathematical "dark matter".
- **Lexical Amnesia & Hollow Sacrifices:** Fixed `akashic.py` to explicitly inject saved `discovered_words` back into the active `LEXICON` on boot. Additionally, forced `trigger_autophagy()` to physically purge consumed words from the active Lexicon so the metabolic sacrifice is real.
- **Semantic Clobbering:** Rewrote `_deep_update` in `phases/cognitive.py` to maintain recursive merging on dictionary class attributes, preventing shallow Python `.update()` calls from deleting un-modified nested tensor coordinates.

#### 👨‍⚕️ Pragmactics & Encapsulation

- **ATP Encapsulation:** Cleared out paranoid `hasattr(self.bio, "mito")` boilerplate by building `drain_atp()` and `restore_atp()` natively into the `BoneAmanita` base class.
- **Generational & Epigenetic Atomic Saves:** Enforced `.tmp` > `os.replace` atomic writes for both Subconscious Save states (`akashic.py`) and Generational Death tracking (`legacy.json` in `oroboros.py`). The corpse will no longer vaporize on an ill-timed OS crash.
- **Bureaucratic Decoupling:** Removed hardcoded `if/elif` statements in `apply_legacy()`. Generational scars can now target any arbitrary physical constraint listed in the UX Manifest without needing python-side structural updates.
- **Test Suite I/O Shield:** Mocked the `TelemetryService` inside `tests/base.py` to completely eliminate Phantom JSONL Bleed into the local test directory.

---

### **BONEAMANITA 19.8.0 "The Epigenetic Tensegrity Patch"**

*A comprehensive stabilization of the hypervisor's memory, physics, and immune pathways. This audit repaired fatal memory leaks, established atomic write safety for the Akashic Record, sealed a lethal payload injection vector, and restored the Checkpoint Council's ability to halt runaway toxicity loops.*

#### **🏛️ STRUCTURAL TENSEGRITY (Fuller's Pass: Architecture)**
- **The Apoptotic Ghost (`brain/cortex.py`):** The `purge_context` function now explicitly clears `self.last_physics`, preventing the high tension/drag of a purged toxic loop from infecting the fresh conversational state.
- **Atomic Epigenetics (`brain/akashic.py`):** Rewrote the long-term memory serialization to use atomic `.tmp` file swapping. This prevents catastrophic epigenetic corruption if the host OS terminates the process mid-write.
- **Amnesic Crafting (`brain/akashic.py`):** The engine now correctly serializes `recipe_candidates`, preventing the user's partial crafting progress from evaporating upon system reboot.
- **The Epigenetic Immune Response (`tests/test_akashic.py`):** Established a dedicated, isolated test suite for the Akashic Record utilizing temporary directories to catch serialization/deserialization boundaries before they reach production.

#### **🧠 COGNITIVE ERGONOMICS (Pinker's Pass: Language)**
- **Syntactic Checkpoint Purge (`main.py`):** Refactored the math variable extraction in `_pre_flight_checks` to dramatically reduce visual noise, isolating the exact algebraic logic of the immune system.
- **The Interrogative Bypass (`brain/composer.py`):** Reinforced Gordon's High Voltage questioning boundary by checking the final 15 characters of a response rather than just `endswith("?")`, preventing roleplay tags from blinding the immune check.
- **The Bureaucratic Catch (`brain/cortex.py`):** Encased the random 15% `bureau.audit` in a `try/except` block, ensuring that an error in the bureaucratic paperwork cannot crash the LLM generation loop.

#### **⚖️ DYNAMIC EQUILIBRIUM (Meadows' Pass: Systems & Dynamics)**
- **The CSF Trojan Horse (`physics/filters.py`):** Restructured the Gatekeeper pipeline to execute the `CerebrospinalFluidFilter.wash` *before* the security audit, permanently sealing a zero-width character injection loophole.
- **Algorithmic Drag in the Cortex (`brain/ann.py`):** Replaced an $O(N \log N)$ full-array sort with an $O(N \log K)$ `heapq` extraction during Lateral OFC Retrieval, eliminating severe computational lag spikes when deep memory bloated under high chaos.
- **Gazing into the Void (`brain/ann.py`):** Fixed `get_local_mass_radius` to actually query the FAISS dimensional space using the user's input vector rather than blindly mapping a zero-vector.
- **The Context Drop Black Hole (`brain/cortex.py`):** Massive text ingestions now explicitly trigger an immediate `execute_writes` command on the Substrate queue, preventing the engine from holding massive contextual files in active RAM.

#### **🛠️ FUNCTIONAL PRAGMATISM (Schur's Pass: Humanity)**
- **The Stutter Loop (`brain/composer.py`):** Corrected the Response Validator's stutter logic. The system no longer punishes and forces a retry on the LLM when it perfectly and silently executes a hidden `<write_file>` or `<think>` tool.
- **REM Worker Bureaucracy (`cycle.py`):** Merged redundant DreamEngine background workers into a single, pragmatic `_dispatch_rem_worker` method.
- **REM OS Deadlock Failsafe (`cycle.py`):** The engine now securely wraps background thread spawning in a `try/except RuntimeError`, explicitly releasing `self._rem_lock` if the host OS refuses to allocate a thread.
- **The Trauma Bias (`brain/akashic.py`):** Fixed the engine's brutal tendency to remember its failures (Scars) but forget its successes (Boons) upon a cold boot. It now loads both simultaneously.

