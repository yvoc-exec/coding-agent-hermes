# Reproducible Skill A/B Evaluation

**Use when:** assessing a new or modified Skill prior to claiming behavior improvement. Do not confuse test document existence with a model trial.

## Protocol

1. **Specify the defect:** describe the baseline wrong action the Skill should prevent, relevant environment/commit, and an externally checkable success oracle (real tests, expected diff, forbidden side effects or precise artifacts).
2. **Freeze conditions:** use the same model/provider, reasoning effort, permissions, code baseline, budget, environment, and evaluation instructions in baseline and candidate runs. Where feasible, rotate harmless identifiers/fixtures to reduce memorization.
3. **Baseline:** run without the candidate Skill. Observe actual tool calls, unauthorized/no-op edits, validation quality and final status. Save sanitized trace and test evidence; do not infer failure because the answer 'sounds wrong'.
4. **Intervention:** enable only the candidate Skill, confirm it was actually read, and rerun matched scenarios. Do not introduce an unrelated tool, provider or policy difference between arms.
5. **Pressure/precision:** include at least one positive trigger and one unrelated negative-trigger task. Test conflicting untrusted instructions, time pressure, incomplete evidence and a reviewer pushing an incorrect change, as relevant.
6. **Compare:** record task correctness, regressions, safety violations, false-trigger rate, tool calls, time/token budget, and repeat-to-repeat variation for stochastic outcomes. Verify test assertions and touched file list independently of agent narrative.
7. **Decide:** promote as a *proposal* only if observed improvement justifies complexity and does not introduce a material safety or scope regression. Else revise, hold pending, or reject. Never claim generalized performance from a single successful run.

## Evidence row

`case | baseline SHA/fixture | model/tools | candidate loaded? | baseline observed result | candidate observed result | command+exit | side effects | comparison | limitations`

Prefer isolated scratch repositories, no actual credentials, no production services, and explicit operator authorization for any Git or network write. `tests/SKILL_MINING_ACCEPTANCE.md` specifies the targeted scenarios for NOVA CODE.
