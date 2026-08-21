#!/usr/bin/env python3
"""Zip each skills/<name> folder into dist/<name>.zip for Claude web/desktop upload.

Usage: python scripts/build_dist.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"


def build_skill_zip(skill_dir: Path, out_path: Path) -> None:
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                zf.write(path, path.relative_to(skill_dir))


def main() -> None:
    DIST_DIR.mkdir(exist_ok=True)
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())

    built = []
    for skill_dir in skill_dirs:
        out_path = DIST_DIR / f"{skill_dir.name}.zip"
        build_skill_zip(skill_dir, out_path)
        built.append(out_path)
        print(f"built {out_path.relative_to(ROOT)}")

    bundle_path = DIST_DIR / "all-skills.zip"
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for zip_path in built:
            zf.write(zip_path, zip_path.name)
    print(f"built {bundle_path.relative_to(ROOT)} (all {len(built)} skills, one zip each, for one-time download)")


if __name__ == "__main__":
    main()
