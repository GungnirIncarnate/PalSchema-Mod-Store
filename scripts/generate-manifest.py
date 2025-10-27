#!/usr/bin/env python3
"""
Palworld Mod Store - Manifest Generator

This script automatically generates the manifest.json file by scanning
the mods directory and collecting metadata from each mod.
"""

import json
import os
import hashlib
import zipfile
from datetime import datetime
from pathlib import Path
import sys

def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_file_size(file_path):
    """Get file size in bytes."""
    return os.path.getsize(file_path)

def load_mod_info(mod_dir):
    """Load mod-info.json from a mod directory."""
    info_files = ["mod-info.json", "mod-info.jsonc"]
    
    for info_file in info_files:
        info_path = mod_dir / info_file
        if info_path.exists():
            try:
                with open(info_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Basic JSONC support - remove comments
                    lines = content.split('\n')
                    cleaned_lines = []
                    for line in lines:
                        # Remove line comments
                        if '//' in line:
                            line = line[:line.index('//')]
                        cleaned_lines.append(line)
                    cleaned_content = '\n'.join(cleaned_lines)
                    return json.loads(cleaned_content)
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                print(f"Warning: Failed to parse {info_path}: {e}")
                continue
    
    return None

def find_mod_zip(mod_dir, mod_name):
    """Find the mod zip file in the directory."""
    zip_files = list(mod_dir.glob(f"{mod_name}-v*.zip"))
    if not zip_files:
        # Try without version prefix
        zip_files = list(mod_dir.glob("*.zip"))
    
    if zip_files:
        # Return the most recent zip file
        return max(zip_files, key=lambda p: p.stat().st_mtime)
    
    return None

def generate_manifest():
    """Generate the manifest.json file."""
    print("🔄 Generating manifest.json...")
    
    # Repository information
    repo_info = {
        "owner": os.environ.get("GITHUB_REPOSITORY_OWNER", "GungnirIncarnate"),
        "repo": os.environ.get("GITHUB_REPOSITORY", "GungnirIncarnate/PalSchema-Mod-Store").split("/")[-1]
    }
    
    base_url = f"https://github.com/{repo_info['owner']}/{repo_info['repo']}"
    raw_url = f"https://raw.githubusercontent.com/{repo_info['owner']}/{repo_info['repo']}/main"
    
    manifest = {
        "version": "1.0",
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "repository": {
            "url": base_url,
            "raw_url": raw_url
        },
        "mods": []
    }
    
    mods_dir = Path("mods")
    if not mods_dir.exists():
        print("❌ Mods directory not found!")
        return False
    
    processed_mods = 0
    
    # Scan each mod directory
    for mod_dir in mods_dir.iterdir():
        if not mod_dir.is_dir():
            continue
            
        print(f"📦 Processing mod: {mod_dir.name}")
        
        # Load mod metadata
        mod_info = load_mod_info(mod_dir)
        if not mod_info:
            print(f"⚠️  No valid mod-info.json found for {mod_dir.name}")
            continue
        
        # Required fields
        required_fields = ["ModName", "Version", "Description"]
        missing_fields = [field for field in required_fields if field not in mod_info]
        if missing_fields:
            print(f"⚠️  Missing required fields in {mod_dir.name}: {missing_fields}")
            continue
        
        # Find mod zip file
        mod_zip = find_mod_zip(mod_dir, mod_dir.name)
        if not mod_zip:
            print(f"⚠️  No zip file found for {mod_dir.name}")
            continue
        
        # Generate mod entry
        mod_entry = {
            "id": mod_dir.name.lower().replace(" ", "-"),
            "name": mod_info["ModName"],
            "version": str(mod_info["Version"]),
            "description": mod_info["Description"],
            "author": mod_info.get("Author", "Unknown"),
            "folder_name": mod_dir.name,
            "download_url": f"{raw_url}/mods/{mod_dir.name}/{mod_zip.name}",
            "file_size": get_file_size(mod_zip),
            "checksum": f"sha256:{calculate_file_hash(mod_zip)}",
            "min_game_version": mod_info.get("MinGameVersion", "0.1.0"),
            "tags": mod_info.get("Tags", []),
            "last_updated": datetime.fromtimestamp(mod_zip.stat().st_mtime).isoformat() + "Z"
        }
        
        # Add icon URL if icon exists
        icon_files = ["icon.png", "icon.jpg", "icon.jpeg"]
        for icon_file in icon_files:
            icon_path = mod_dir / icon_file
            if icon_path.exists():
                mod_entry["icon_url"] = f"{raw_url}/mods/{mod_dir.name}/{icon_file}"
                break
        
        # Add optional fields
        if "Homepage" in mod_info:
            mod_entry["homepage"] = mod_info["Homepage"]
        if "SourceCode" in mod_info:
            mod_entry["source_code"] = mod_info["SourceCode"]
        
        manifest["mods"].append(mod_entry)
        processed_mods += 1
        print(f"✅ Added {mod_info['ModName']} v{mod_info['Version']}")
    
    # Write manifest file
    manifest_path = Path("manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"🎉 Manifest generated successfully!")
    print(f"📊 Total mods: {processed_mods}")
    print(f"📝 Manifest saved to: {manifest_path}")
    
    return True

if __name__ == "__main__":
    success = generate_manifest()
    sys.exit(0 if success else 1)