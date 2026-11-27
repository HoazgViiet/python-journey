# AGENTS.md — Python Journey V2

## Course contract

```text
PROJECT = Python Journey V2
DEFAULT_WORK_BRANCH = upgrade/python-journey-v2
PYTHON_BASELINE = >=3.12
LEARNING_LOOP = Learn → Build → Test → Debug → Improve → Commit → Prove
```

This repository is a beginner curriculum, not an application package.
Keep every change understandable to a learner encountering the topic for the
first time.

## Canonical ownership

- `SYLLABUS.md` is the curriculum source of truth.
- `FINAL_PROJECT.md` is the capstone source of truth.
- `README.md` is the overview and navigation entry point.
- `PROGRESS.md` is the learner tracker.
- `SETUP.md` owns installation and troubleshooting guidance.
- `STYLE_GUIDE.md` owns course-level Python style guidance.
- Week directories own their lesson content, exercises, and mini-projects.

When documents disagree, resolve the conflict in the owning document first.
Do not copy a second canonical version into another file.

## Curriculum boundary

Python Journey covers reliable Python foundations across 15 weeks.
The locked curriculum is:

1. Environment, REPL, terminal, Git/GitHub, and Hello Python.
2. Variables, types, and input/output.
3. Conditionals, Boolean logic, and input validation.
4. Strings, text processing, and a regex mini-lab.
5. Lists, tuples, mutability, and unpacking.
6. Loops, `enumerate`, `zip`, and comprehensions.
7. Functions, decomposition, scope, and basic type hints.
8. Dictionaries, sets, nested data, and data modeling.
9. Midterm Project.
10. Files, `pathlib`, CSV, and JSON.
11. Exceptions, tracebacks, debugging, and defensive coding.
12. Testing with pytest.
13. Modules, packages, dependencies, CLI, and API/HTTP.
14. OOP essentials, composition, and basic inheritance.
15. Capstone, tests, README, and Git/GitHub evidence.

Do not move advanced engineering material into this course merely because a
tool supports it. Advanced typing, concurrency, design patterns, packaging for
publication, and testing architecture belong in later courses unless the
syllabus explicitly says otherwise.

Do not rename or migrate week directories as part of unrelated tooling work.
Legacy week content may temporarily lag behind the canonical syllabus while
the V2 migration proceeds in separate drops.

## Learning design priorities

Apply these priorities in order:

1. Evidence over assumption.
2. Simple design over unnecessary complexity.
3. Learner clarity over feature count.

Prefer small examples with visible behavior. Introduce terminology only when
it helps learners reason about code. Each exercise should have a clear purpose,
an observable result, and an appropriate way to verify the result.

Do not rewrite learner starter files solely to make broad lint or test commands
green. Starter code may intentionally be incomplete. Maintainer checks must be
kept separate from learner exercises.

## Maintainer verification

The blocking maintainer checks are:

```bash
python scripts/verify_course.py
pytest
ruff check scripts tests projects/vuacoc-bot-journey
git diff --check
```

`pytest` is configured to collect repository invariant tests in `tests/` and
stable infrastructure tests in `projects/vuacoc-bot-journey/tests/`. Learner
tests inside week directories are run explicitly from their owning lesson; do
not add unfinished learner exercises to default collection.

Use these commands to measure existing course content without turning legacy
debt into a release blocker:

```bash
python -m compileall -q weeks
ruff check weeks
```

Report failures from the measurement commands honestly. Fix them only when the
active task explicitly includes the affected week content.

Maintainer dependencies are declared in the `dev` dependency group in
`pyproject.toml`. Install them with:

```bash
python -m pip install --upgrade "pip>=25.1"
python -m pip install --group dev
```

## Python and tooling policy

- Support Python 3.12 and newer.
- Treat `.python-version` as a convenience hint, not an override of the
  canonical baseline.
- Use Ruff only on the scope authorized by the current task.
- Use pytest for automated maintainer checks and learner tests introduced by
  their owning curriculum drop.
- Keep the course health verifier standard-library only.
- Avoid adding package metadata when the repository is not being distributed
  as an installable package.
- Never require secrets for course health checks.

## Git governance

- Work on `upgrade/python-journey-v2` unless the owner explicitly authorizes a
  different branch.
- Confirm repository root, branch, status, HEAD, and remotes before editing.
- Preserve unrelated user changes and stop if a clean baseline is required but
  the worktree is dirty.
- Keep commits scoped to one curriculum drop or one coherent maintenance task.
- Read the complete diff before committing.
- Do not force-push.
- Do not merge `main` as a shortcut during a scoped drop.
- Do not create a new branch unless the owner requests one.
- Do not commit secrets, virtual environments, caches, or generated bytecode.

## Change discipline

Follow the explicit file scope of the active task. If a necessary change falls
outside that scope, stop and report the dependency instead of silently
expanding the change.

Keep Markdown links relative inside the repository. Preserve UTF-8 Vietnamese
text. Keep Python examples compatible with the declared baseline. Favor
standard-library examples until an external dependency is itself the lesson.

Before handoff, state which checks ran, which passed, and which were only
measurements. Never report PASS for a command that was not executed.

## Student-facing AI collaboration (ChatGPT and Codex)

These additional instructions apply when helping the repository owner study or
complete learner exercises. They complement the course contract above and do
not replace the syllabus, exercise requirements, or maintainer checks.

- Communicate in Vietnamese by default, keeping code identifiers and required
  output text exactly as specified by the exercise.
- Before editing, read the owning week's README, exercise instructions and
  starter files, and relevant assessment guidance. Inspect the actual files;
  do not assume requirements from prior chat history.
- Teach at a beginner level using only concepts already introduced by the
  course unless the learner explicitly requests an extension. Explain why
  the code works, important lines, and common mistakes.
- Prefer the learning loop: explain → guide → let the learner try → test →
  debug → improve. When the learner requests direct edits or a complete
  solution, follow the mandatory preview-and-approval workflow below before
  implementing the approved scope and explaining the changes.
- Respect interactive input requirements. Use `input()` and appropriate
  explicit type conversions when the exercise requires user-entered values;
  do not hardcode those values or replace required output with a different
  interface.
- Keep changes limited to the week, exercise, or file requested by the
  learner. Do not change graders, scoring rules, tests, reference solutions,
  or other weeks to make an exercise pass. Preserve unrelated local edits.
- For Week 02, follow its own requirements for variables, types and
  input/output. Distinguish core exercises, practice, and mini-projects.
  If available and appropriate, run the official student assessment:
  `python weeks/week-02-variables-types/assessment/core-exercises/autograde_w02.py --student`.
  Do not treat a practice or mini-project result as the core exercise score.
- If requested to add a web interface, keep it separate from the original
  required Python exercises unless the learner explicitly requests otherwise.
  Preserve the original exercise behavior and assessment compatibility.
- For direct coding requests, make small, reviewable edits, verify with
  relevant tests or examples, and summarize files changed, reasons, checks
  actually run, and any remaining issues in Vietnamese. Never fabricate
  results or report a test as passed if it was not run.
- Before Git operations, inspect the current branch and local changes where
  accessible. Follow the Git governance above; do not discard changes,
  force-push, commit or push without authorization. If a designated work
  branch is missing, report it rather than creating one without permission.
- Treat this file as shared project guidance, not shared chat memory.
  Re-read current instructions and source files when switching between
  ChatGPT and Codex. Use Git to synchronize committed code, and report
  any local or remote state that cannot be verified.

## Mandatory code preview and approval (ChatGPT and Codex)

For every proposed code or project-file change, follow this workflow even when
the learner asks to fix, implement, create, or complete something directly.
A request to make a change is not approval of an unseen patch.

1. Inspect the relevant files and requirements using read-only operations.
2. Explain in Vietnamese what needs to change, why, and which file paths
   are affected.
3. Show the actual proposed code before editing: include the existing and
   proposed snippets, or a unified diff with removed and added lines.
   For new files, show their proposed contents. For short exercises, show
   the complete proposed code so the learner can understand it. A plan or
   summary without the proposed code is not sufficient.
4. Ask explicitly: "Bạn có đồng ý để mình áp dụng đoạn code này không?"
   Stop and wait for affirmative approval of the displayed proposal.
   Do not edit, create, delete, rename, format, or overwrite project files,
   apply patches, run commands that modify files, commit, or push while
   awaiting approval. Read-only inspection is allowed.
5. After approval, apply only the exact approved changes. If additional
   changes become necessary or the proposed code differs materially, show
   the updated proposal and obtain approval again before applying it.
6. Verify the approved changes using appropriate checks, then report the
   actual diff, files changed, test results, and any remaining issues.
   Obtain separate authorization for committing or pushing unless already
   explicitly authorized for the approved change.

If the learner rejects the proposal or asks to revise it, show the revised
code without editing files. Do not treat silence or a general request to fix
code as approval. This workflow takes precedence over earlier instructions
to perform direct edits; it applies to both local VS Code work and GitHub
changes. It is a project instruction, not a technical permission mechanism.
