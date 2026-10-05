"""The org fork's gate: what the hub vendors from this fork must parse, and no merge may leave
conflict markers behind. Added after #5 landed four SKILL.md files with markers in them: the repo
had no CI, so nothing could refuse it."""
import re, subprocess, sys
bad = []
# A marker line is the 7-char run plus a space or end of line; a bare `=======` is left alone,
# since Markdown uses it as a setext heading underline.
hits = subprocess.run(["git", "grep", "-nE", r"^(<<<<<<<|>>>>>>>)( |$)"], capture_output=True, text=True)
if hits.returncode > 1:
    sys.exit("gate: git grep failed: " + hits.stderr)
bad += [f"{l}: conflict marker" for l in hits.stdout.splitlines()]
files = subprocess.run(["git", "ls-files", "skills/**/SKILL.md"], capture_output=True, text=True, check=True).stdout.split()
if not files:
    sys.exit("gate: no SKILL.md files found -- the check would measure nothing")
for f in files:
    m = re.match(r"---\n(.*?)\n---\n", open(f, encoding="utf-8").read(), re.S)
    if not m:
        bad.append(f"{f}: no frontmatter"); continue
    keys = {l.split(":", 1)[0].strip() for l in m.group(1).splitlines() if ":" in l}
    bad += [f"{f}: frontmatter has no {k}" for k in ("name", "description") if k not in keys]
print(f"gate: checked {len(files)} skills and every tracked file for conflict markers")
if bad:
    print("\n".join(bad)); sys.exit(1)
