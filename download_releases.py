#!/usr/bin/env python3
"""
Download all Smash Remix xdelta patches from GitHub releases.
Fetches release info and downloads .xdelta files to docs/remix/patches/
Also saves release notes to a JSON file for the patcher page.
"""

import json
import requests
import zipfile
import tempfile
from pathlib import Path

# GitHub API endpoints
RELEASES_API = f"https://api.github.com/repos/JSsixtyfour/smashremix/releases"

# Output directories
PATCHES_DIR = Path(__file__).parent / "docs" / "remix" / "patches" / "releases"
PATCHES_DIR.mkdir(parents=True, exist_ok=True)

# Releases
RELEASES_MANIFEST_FILE = Path(__file__).parent / "docs" / \
    "remix" / "patches" / "releases.json"


def fetch_releases():
    """Fetch all releases from GitHub API."""
    releases = []
    page = 1
    while True:
        print(f"  Fetching page {page}...")
        response = requests.get(
            RELEASES_API,
            params={
                "page": page,
                "per_page": 100
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"No more releases on page {page}")
            break
        print(f"Got {len(data)} releases on page {page}")
        releases.extend(data)
        page += 1
    return releases


def process_zip_assets(release):
    """
    Download zip asset(s) for a release and extract all .xdelta files.

    Returns a tuple (found_any_patches, notes_text_if_any, list_of_filenames).
    The function looks for any asset whose name ends with .zip (assuming release
    archives) and iterates their contents, extracting patches and patch notes.
    """
    tag = release["tag_name"]
    found_any = False
    notes_text = None
    filenames = []

    for asset in release.get("assets", []):
        name = asset.get("name", "")
        if not name.lower().endswith(".zip"):
            continue

        print(f"Downloading archive asset {name}...")
        try:
            response = requests.get(
                asset["browser_download_url"],
                timeout=10
            )
            response.raise_for_status()
        except Exception as e:
            print(f"Error downloading archive {name}: {e}")
            continue

        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = Path(tmpdir) / name
            with open(zip_path, "wb") as f:
                f.write(response.content)

            with zipfile.ZipFile(zip_path, "r") as zf:
                for member in zf.namelist():
                    lower = member.lower()

                    if lower.endswith(".xdelta"):
                        content = zf.read(member)
                        filename = Path(member).name
                        output_file = PATCHES_DIR / filename
                        with open(output_file, "wb") as f:
                            f.write(content)
                        print(f"Extracted xdelta: {filename}")
                        found_any = True
                        filenames.append(filename)
                    if "notes" in lower and lower.endswith(".txt"):
                        try:
                            notes_bytes = zf.read(member)
                            notes_text = notes_bytes.decode(
                                "utf-8",
                                errors="ignore"
                            )
                            print(f"Found patch notes file: {member}")
                        except Exception as e:
                            print(f"Failed to read notes {member}: {e}")
    if not found_any:
        print(f"No .xdelta files found in any zip assets for {tag}")

    return found_any, notes_text, filenames


def save_release_notes(releases):
    """Save release notes to a JSON file. Combines GitHub body with any notes found in ZIP."""
    notes = {}
    for release in releases:
        tag = release["tag_name"]
        body = release.get("body", "") or ""
        # if we discovered notes inside the zip or assets, append them
        zip_text = release.get("zip_notes")
        asset_text = release.get("asset_notes")
        if asset_text:
            body = (body + "\n\n" + asset_text).strip()
        if zip_text:
            body = (body + "\n\n" + zip_text).strip()

        notes[tag] = {
            "name": release.get("name", tag),
            "body": body,
            "html_url": release.get("html_url"),
        }

    with open(RELEASES_MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved release notes to {RELEASES_MANIFEST_FILE}")


def main():
    print("Fetching releases...")
    releases = fetch_releases()
    print(f"\nFound {len(releases)} releases.\n")

    releases_manifest = []

    for i, release in enumerate(releases, 1):
        tag = release["tag_name"]
        print(f"[{i}/{len(releases)}] Processing {tag}...")
        try:
            found, notes, files = process_zip_assets(release)

            if found:
                entry = {
                    "name": release.get("name", tag),
                    "version": tag,
                    "original_url": release.get("html_url"),
                    "files": {},
                    "patch_notes": notes or release.get("body", "")
                }

                for fname in files:
                    lower = fname.lower()
                    if "pal60" in lower or ("pal" in lower and "60" in lower):
                        entry["files"]["pal"] = fname
                    else:
                        entry["files"]["ntsc"] = fname

                releases_manifest.append(entry)
        except Exception as e:
            print(f"Error processing {tag}: {e}")

    # Save release manifest
    with open(RELEASES_MANIFEST_FILE, "w", encoding="utf-8") as mff:
        json.dump(releases_manifest, mff, indent=2)
    print(f"Wrote manifest to {RELEASES_MANIFEST_FILE}")


if __name__ == "__main__":
    main()
