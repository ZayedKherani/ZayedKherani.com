#!/usr/bin/env python3
"""Download external assets needed during the Cloudflare Pages build."""

from __future__ import annotations

import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class AssetSpec:
    """Describe a single asset that must be present in the build output."""

    filename: str
    subdir: str
    source_url: str


FILES_TO_FETCH: Sequence[AssetSpec] = (
    AssetSpec(
        "resume.pdf",
        "/",
        "https://shs.zayedkherani.com/resume.pdf"
    ),
    # AssetSpec(
    #     "cider-linux-x64.deb",
    #     "/objects/cider-linux/",
    #     "https://shs.zayedkherani.com/cider-linux-x64.deb",
    # ),
)


def workspace_root() -> Path:
    """Return the workspace root, overridable via WORKSPACE_ROOT env variable."""

    override = os.environ.get("WORKSPACE_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    # scripts/ directory lives one level beneath the repo root
    return Path(__file__).resolve().parent.parent


def normalize_subdir(subdir: str) -> Path:
    """Normalize the subdirectory path and guard against path traversal."""

    clean = Path(subdir.strip("/"))
    if any(part in {"..", ""} for part in clean.parts):
        raise ValueError(f"Refusing to use unsafe subdir: {subdir}")
    return clean


def ensure_directory(path: Path) -> None:
    """Create the directory for the supplied path if it does not exist."""

    path.mkdir(parents=True, exist_ok=True)


def download_asset(spec: AssetSpec, root: Path) -> Path:
    """Download a file defined by spec into the workspace root and return the path."""

    try:
        subdir = normalize_subdir(spec.subdir) if spec.subdir.strip("/") else Path()
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    target_dir = root / subdir
    target_path = target_dir / spec.filename
    ensure_directory(target_dir)

    request = Request(spec.source_url, headers={"User-Agent": "CloudflarePagesAssetFetcher/1.0"})
    try:
        with urlopen(request) as response, target_path.open("wb") as dest:  # nosec B310
            shutil.copyfileobj(response, dest)
    except HTTPError as err:
        raise SystemExit(f"Failed to download {spec.source_url}: HTTP {err.code}") from err
    except URLError as err:
        raise SystemExit(f"Failed to download {spec.source_url}: {err.reason}") from err

    return target_path


def download_assets(specs: Iterable[AssetSpec], root: Path | None = None) -> list[Path]:
    """Download each asset defined in specs."""

    base = root or workspace_root()
    downloaded: list[Path] = []
    for spec in specs:
        target = download_asset(spec, base)
        print(f"Downloaded {spec.source_url} -> {target.relative_to(base)}", flush=True)
        downloaded.append(target)
    return downloaded


def verify_assets(paths: Iterable[Path]) -> None:
    """Ensure each downloaded asset is present on disk."""

    missing = [path for path in paths if not path.exists()]
    if missing:
        details = ", ".join(str(path) for path in missing)
        raise SystemExit(f"Missing downloaded assets: {details}")


def delete_scripts_directory(script_file: Path) -> None:
    """Remove the scripts directory containing this build helper."""

    scripts_dir = script_file.parent
    if not scripts_dir.exists():
        return
    if scripts_dir.name != "scripts":
        raise SystemExit(f"Refusing to delete unexpected directory: {scripts_dir}")
    shutil.rmtree(scripts_dir)


def main() -> None:
    downloaded = download_assets(FILES_TO_FETCH)
    verify_assets(downloaded)
    delete_scripts_directory(Path(__file__).resolve())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Download interrupted by user")
