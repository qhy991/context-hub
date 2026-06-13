#!/usr/bin/env python3
"""
Build registry.json and search-index.json from DOC.md files.

This script scans all DOC.md files under content/ and generates:
- dist/registry.json: Full documentation registry with metadata
- dist/search-index.json: Simplified search index

Usage:
    python3 scripts/build_registry.py [--content-dir content] [--output-dir dist]
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return None


def get_file_size(filepath):
    """Get file size in bytes."""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return 0


def parse_doc_file(filepath, content_dir):
    """
    Parse a DOC.md file and extract metadata.

    Args:
        filepath: Path to the DOC.md file
        content_dir: Base content directory for relative path calculation

    Returns:
        dict with parsed metadata or None if invalid
    """
    try:
        with open(filepath) as f:
            content = f.read()

        frontmatter = extract_frontmatter(content)
        if not frontmatter:
            print(f"  ⚠️  No valid frontmatter: {filepath.relative_to(content_dir)}")
            return None

        # Validate required fields
        name = frontmatter.get("name")
        description = frontmatter.get("description")
        metadata = frontmatter.get("metadata", {})

        if not name or not description:
            print(f"  ⚠️  Missing name or description: {filepath.relative_to(content_dir)}")
            return None

        languages = metadata.get("languages")
        versions = metadata.get("versions")

        if not languages or not versions:
            print(f"  ⚠️  Missing languages or versions: {filepath.relative_to(content_dir)}")
            return None

        # Calculate relative path from content_dir
        rel_path = filepath.relative_to(content_dir)
        doc_path = str(rel_path.parent)  # Path without the filename

        # Get file metadata
        file_size = get_file_size(filepath)
        updated_on = metadata.get("updated-on", datetime.now().strftime("%Y-%m-%d"))

        # Parse tags
        tags_str = metadata.get("tags", "")
        tags = [tag.strip() for tag in tags_str.split(",")] if isinstance(tags_str, str) else tags_str

        # Parse versions
        if isinstance(versions, str):
            versions_list = [v.strip() for v in versions.split(",")]
        elif isinstance(versions, list):
            versions_list = versions
        else:
            versions_list = [str(versions)]

        # Build version objects
        version_objects = []
        for ver in versions_list:
            version_objects.append({
                "version": ver,
                "path": doc_path,
                "files": ["DOC.md"],
                "size": file_size,
                "lastUpdated": updated_on
            })

        # Determine source
        source = metadata.get("source", "unknown")

        # Build ID (category/name)
        # Extract from path like "ascendc/docs/ascendc-softmax/DOC.md"
        path_parts = rel_path.parts
        if len(path_parts) >= 2:
            category = path_parts[0]
            id_suffix = name
        else:
            category = "unknown"
            id_suffix = name

        doc_id = f"{category}/{id_suffix}"

        return {
            "id": doc_id,
            "name": name,
            "description": description,
            "source": source,
            "tags": tags,
            "languages": [{
                "language": languages,
                "versions": version_objects,
                "recommendedVersion": versions_list[0] if versions_list else "latest"
            }],
            "path": doc_path,
            "fileSize": file_size,
            "lastUpdated": updated_on
        }

    except Exception as e:
        print(f"  ⚠️  Error parsing {filepath}: {e}")
        return None


def build_registry(docs_data, generated_time):
    """
    Build registry.json from parsed docs data.

    Args:
        docs_data: List of parsed doc dictionaries
        generated_time: ISO timestamp for generation time

    Returns:
        registry dictionary
    """
    registry = {
        "version": "1.0.0",
        "generated": generated_time,
        "count": len(docs_data),
        "docs": []
    }

    for doc in sorted(docs_data, key=lambda x: x["id"]):
        # Build simplified entry for registry
        registry_entry = {
            "id": doc["id"],
            "name": doc["name"],
            "description": doc["description"],
            "source": doc["source"],
            "tags": doc["tags"],
            "languages": doc["languages"]
        }
        registry["docs"].append(registry_entry)

    return registry


def build_search_index(docs_data):
    """
    Build search-index.json from parsed docs data.

    Args:
        docs_data: List of parsed doc dictionaries

    Returns:
        search index dictionary
    """
    search_index = {
        "version": "1.0.0",
        "documents": []
    }

    for doc in sorted(docs_data, key=lambda x: x["id"]):
        # Tokenize fields for search
        search_doc = {
            "id": doc["id"],
            "name": doc["name"],
            "description": doc["description"].lower(),
            "tags": [tag.lower() for tag in doc["tags"]],
            "tokens": []
        }

        # Build search tokens from name, description, and tags
        name_tokens = doc["name"].replace("-", " ").replace("_", " ").split()
        desc_tokens = doc["description"].lower().split()
        tag_tokens = [tag.lower() for tag in doc["tags"]]

        all_tokens = list(set(name_tokens + desc_tokens + tag_tokens))
        search_doc["tokens"] = all_tokens

        search_index["documents"].append(search_doc)

    return search_index


def main():
    parser = argparse.ArgumentParser(
        description="Build registry.json and search-index.json from DOC.md files"
    )
    parser.add_argument(
        "--content-dir",
        type=str,
        default="content",
        help="Content directory containing DOC.md files"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="dist",
        help="Output directory for registry files"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Only validate without writing output files"
    )

    args = parser.parse_args()

    # Setup paths
    root_dir = Path(__file__).resolve().parent.parent
    content_dir = root_dir / args.content_dir
    output_dir = root_dir / args.output_dir

    if not content_dir.exists():
        print(f"Error: Content directory not found: {content_dir}")
        sys.exit(1)

    # Find all DOC.md files
    print(f"Scanning {content_dir} for DOC.md files...")
    doc_files = list(content_dir.rglob("DOC.md"))

    if not doc_files:
        print("No DOC.md files found")
        sys.exit(1)

    print(f"Found {len(doc_files)} DOC.md files")

    # Parse all DOC.md files
    docs_data = []
    for filepath in doc_files:
        doc_data = parse_doc_file(filepath, content_dir)
        if doc_data:
            docs_data.append(doc_data)

    print(f"Successfully parsed {len(docs_data)} docs")

    if not docs_data:
        print("No valid docs found")
        sys.exit(1)

    # Generate timestamp
    generated_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # Build registry
    print("Building registry.json...")
    registry = build_registry(docs_data, generated_time)

    # Build search index
    print("Building search-index.json...")
    search_index = build_search_index(docs_data)

    if args.validate:
        print("\n=== VALIDATION RESULTS ===")
        print(f"Total docs: {len(docs_data)}")
        print(f"Registry entries: {len(registry['docs'])}")
        print(f"Search index entries: {len(search_index['documents'])}")
        print("\n✓ Validation passed")
        return

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write registry.json
    registry_file = output_dir / "registry.json"
    with open(registry_file, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"  Written: {registry_file}")

    # Write search-index.json
    search_file = output_dir / "search-index.json"
    with open(search_file, "w") as f:
        json.dump(search_index, f, indent=2)
    print(f"  Written: {search_file}")

    print(f"\n✓ Successfully generated registry files")
    print(f"  Registry: {len(registry['docs'])} entries")
    print(f"  Search index: {len(search_index['documents'])} entries")
    print(f"  Output directory: {output_dir}")


if __name__ == "__main__":
    main()
