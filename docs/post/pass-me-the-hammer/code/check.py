"""Run each case file and verify it produces the expected output."""
import subprocess
import sys

CASES = [
    {
        "file": "1_muscle_memory.py",
        "exit_code": 1,
        "stderr_contains": "KeyError: 'hammer'",
    },
    {
        "file": "2_empty_hands.py",
        "exit_code": 1,
        "stderr_contains": "TypeError: C needs a Hammer, got None",
    },
    {
        "file": "3_send_a_note.py",
        "exit_code": 1,
        "stderr_contains": "TypeError: C needs a Hammer, got \"I don't have a hammer :)\"",
    },
    {
        "file": "4_idempotency.py",
        "exit_code": 1,
        "stdout": "(done, no crash)\n",
        "stderr_contains": "IndexError: list index out of range",
    },
    {
        "file": "5_cya.py",
        "exit_code": 0,
        "stdout": "C: working with a Hammer\n",
    },
    {
        "file": "6_helpful_unhelpful.py",
        "exit_code": 1,
        "stderr_contains": "HammerNotFound: Could not find hammer in any drawers.",
    },
    {
        "file": "7_indiscrete.py",
        "exit_code": 0,
        "stdout": "Could not find Hammer: 'hammer'\n",
    },
    {
        "file": "8_union_member.py",
        "exit_code": 0,
        "stdout": "ERROR:__main__:Could not find Hammer: 'hammer'\n",
    },
    {
        "file": "9_arson.py",
        "exit_code": 1,
        "stdout": "",
        "stderr": "",
    },
]

passed = 0
failed = 0

for case in CASES:
    result = subprocess.run(
        [sys.executable, case["file"]],
        capture_output=True,
        text=True,
    )

    errors = []

    if result.returncode != case["exit_code"]:
        errors.append(f"exit code: got {result.returncode}, want {case['exit_code']}")

    if "stdout" in case and result.stdout != case["stdout"]:
        errors.append(f"stdout: got {result.stdout!r}, want {case['stdout']!r}")

    if "stderr" in case and result.stderr != case["stderr"]:
        errors.append(f"stderr: got {result.stderr!r}, want {case['stderr']!r}")

    if "stderr_contains" in case and case["stderr_contains"] not in result.stderr:
        errors.append(f"stderr missing: {case['stderr_contains']!r}")

    if errors:
        print(f"FAIL  {case['file']}")
        for e in errors:
            print(f"      {e}")
        failed += 1
    else:
        print(f"PASS  {case['file']}")
        passed += 1

print(f"\n{passed} passed, {failed} failed")
if failed:
    sys.exit(1)
