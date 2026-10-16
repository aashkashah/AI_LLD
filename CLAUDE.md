# CLAUDE.md

## Foundational Rules

- **Think Before Coding:** Do not assume requirements, guess architecture, or hide confusion. Surface design trade-offs and ask questions before writing multi-file logic.
- **Simplicity First:** Write the minimum amount of code required to solve the problem. Avoid speculative over-engineering, future-proofing for unrequested features, or unnecessary abstractions.
- **Surgical Changes:** Touch only what is strictly necessary for the task. Clean up your own mess (dead imports, leftover debug logs), but do not refactor unrelated files unless asked.
- **Goal-Driven Execution:** Define explicit pass/fail verification criteria (tests, build exit codes, or linter output) and loop/fix until those criteria pass.

## About the User

- The user comes from a C# background. Write simple, readable Python that a C# developer can follow.
- Prefer explicit, C#-like constructs: classes, type hints on all signatures and fields, `abc.ABC` / `@abstractmethod` for interfaces, `Enum` for enums, `@dataclass` for simple data holders.
- Avoid clever Python idioms (nested comprehensions, metaclasses, decorators beyond the basics, `*args/**kwargs` tricks, walrus operator). Prefer plain loops and clear names.
- When a Python concept has no obvious C# equivalent, add a brief comment or mention the nearest C# analogue (e.g. `Protocol` ≈ interface, `@property` ≈ property).

## Workflow

- **Plan before code:** For any new problem, restate it, list assumptions and edge cases, and propose a design with complexity. Wait for agreement (see /interview-plan).
- **Small increments:** One step at a time, at most ~40 lines per change, then run the tests and show the result. Never dump a whole solution at once.
- **Tests first or alongside:** Use pytest functions, fixtures, `pytest.raises`, and `parametrize`.
- **Explain Python idioms in C# terms:** Briefly (one line) explain any idiom a C# developer might not recognise, e.g. `defaultdict(list)` ≈ `GetValueOrAdd(key, new List<T>())`.
- **Always run the code:** Never claim something works without executing it.

## Project

- Python 3.11+, source in `src/lld/`, tests in `tests/`.
- Run tests with `pytest` (install with `pip install -e ".[dev]"`).
