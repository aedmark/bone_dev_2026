# CHANGELOG.md
-----------------------------------------------------------

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

