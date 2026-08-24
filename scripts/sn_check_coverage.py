#!/usr/bin/env python3
"""
Cross-check every text spec in an sn_content_0N module against
bilara-data itself: does the spec's key range cover every non-empty,
non-structural segment in its source, and does every referenced key
actually exist?

This catches two mistakes plain ast.parse and sn_verify.py cannot:
  * a range that stops short of the discourse's real content (e.g.
    ending at 3.19 when the actual closing "No, sir." lives at 3.21)
  * a range that names a sub-key index bilara-data never created

Usage:
    python3 scripts/sn_check_coverage.py sn_content_03
    python3 scripts/sn_check_coverage.py sn_content_03 sn-24.   # slug prefix filter
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sn_build  # noqa: E402


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    module_name = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else ""

    mod = importlib.import_module(module_name)
    errors = []
    checked = 0

    for page in mod.PAGES:
        if prefix and not page["slug"].startswith(prefix):
            continue
        checked += 1
        src = sn_build.load_source(page["source"])
        covered = set()
        try:
            for item in page["text"]:
                if item[0] != "p":
                    continue
                covered.update(sn_build.segments(src, item[2]))
        except KeyError as e:
            errors.append("%s: segments() error: %s" % (page["slug"], e))
            continue

        uid = page["source"].split("/")[-1]
        required = set(
            k for k in src
            if k.startswith(uid + ":") and src[k] != ""
            and not sn_build.is_structural(k, src[k])
        )
        missing = required - covered
        if missing:
            errors.append("%s: MISSING from text spec: %s" % (page["slug"], sorted(missing)))
        # Note: covered - required is NOT reported as an error. A range
        # spec legitimately spans empty placeholder keys (peyyāla
        # elision markers with no text of their own) that sit between
        # real content keys within the same span.

    if errors:
        print("FOUND %d issues across %d pages checked:" % (len(errors), checked))
        for e in errors:
            print(" -", e)
        sys.exit(1)
    else:
        print("%s%s: %d pages checked, full coverage, no errors." % (
            module_name, " (%s*)" % prefix if prefix else "", checked))


if __name__ == "__main__":
    main()
