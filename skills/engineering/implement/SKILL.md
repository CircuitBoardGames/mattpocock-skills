---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once the full suite passes, use /open-code-review-delegate to review the work before committing it:

- Preview in workspace mode, which sees uncommitted work. If you committed along the way, commit the rest and review the range from where the work started instead.
- Pass the spec or tickets as the review's background.
- OCR's rules cover correctness, security, performance, maintainability and test coverage. They do not read the repo's documented coding standards (`CODING_STANDARDS.md`, `CONTRIBUTING.md`) and they do not check the diff against the spec, so check both yourself: requirements that are missing or partial, behaviour nobody asked for, and requirements implemented wrongly.
- Fix every critical and high finding, then rerun the tests the fixes touch.

Commit your work to the current branch.
