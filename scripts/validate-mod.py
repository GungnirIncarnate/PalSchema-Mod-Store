#!/usr/bin/env python3
"""
Palworld Mod Store - Mod Validator

This script validates mod structure and metadata to ensure quality standards.
"""

import json
import os
import zipfile
from pathlib import Path
import sys
import re

class ModValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def error(self, message):
        """Add an error message."""
        self.errors.append(f"❌ ERROR: {message}")
        print(f"❌ ERROR: {message}")
    
    def warning(self, message):
        """Add a warning message."""
        self.warnings.append(f"⚠️  WARNING: {message}")
        print(f"⚠️  WARNING: {message}")
    
    def info(self, message):
        """Add an info message."""
        print(f"ℹ️  {message}")
    
    def validate_mod_info(self, mod_dir, mod_info):
        """Validate mod-info.json content."""
        self.info(f"Validating mod info for {mod_dir.name}")
        
        # Required fields
        required_fields = {
            "ModName": str,
            "Version": (str, int, float),
            "Description": str
        }
        
        for field, field_type in required_fields.items():
            if field not in mod_info:
                self.error(f"Missing required field '{field}' in {mod_dir.name}/mod-info.json")
            elif not isinstance(mod_info[field], field_type):
                self.error(f"Field '{field}' must be of type {field_type.__name__} in {mod_dir.name}")
        
        # Validate specific fields
        if "ModName" in mod_info:
            if len(mod_info["ModName"].strip()) == 0:
                self.error(f"ModName cannot be empty in {mod_dir.name}")
            elif len(mod_info["ModName"]) > 50:
                self.warning(f"ModName is quite long ({len(mod_info['ModName'])} chars) in {mod_dir.name}")
        
        if "Description" in mod_info:
            if len(mod_info["Description"].strip()) == 0:
                self.error(f"Description cannot be empty in {mod_dir.name}")
            elif len(mod_info["Description"]) > 500:
                self.warning(f"Description is very long ({len(mod_info['Description'])} chars) in {mod_dir.name}")
        
        if "Version" in mod_info:
            version_str = str(mod_info["Version"])
            if not re.match(r'^\d+\.\d+\.\d+$', version_str):
                self.warning(f"Version '{version_str}' doesn't follow semantic versioning (X.Y.Z) in {mod_dir.name}")
        
        # Optional field validation
        if "Tags" in mod_info:
            if not isinstance(mod_info["Tags"], list):
                self.error(f"Tags must be an array in {mod_dir.name}")
            elif len(mod_info["Tags"]) > 10:
                self.warning(f"Too many tags ({len(mod_info['Tags'])}) in {mod_dir.name}, consider reducing")
        
        if "Author" in mod_info and len(mod_info["Author"].strip()) == 0:
            self.warning(f"Author field is empty in {mod_dir.name}")
        
        return len(self.errors) == 0
    
    def validate_mod_structure(self, mod_dir):
        """Validate mod directory structure."""
        self.info(f"Validating directory structure for {mod_dir.name}")
        
        # Check for mod-info file
        info_files = ["mod-info.json", "mod-info.jsonc"]
        info_file_found = any((mod_dir / info_file).exists() for info_file in info_files)
        
        if not info_file_found:
            self.error(f"No mod-info.json or mod-info.jsonc found in {mod_dir.name}")
            return False
        
        # Check for zip files
        zip_files = list(mod_dir.glob("*.zip"))
        if not zip_files:
            self.error(f"No zip files found in {mod_dir.name}")
            return False
        
        if len(zip_files) > 1:
            self.warning(f"Multiple zip files found in {mod_dir.name}, only the latest will be used")
        
        # Validate zip file naming
        for zip_file in zip_files:
            if not self.validate_zip_name(zip_file, mod_dir.name):
                self.warning(f"Zip file name '{zip_file.name}' doesn't follow recommended pattern '{mod_dir.name}-vX.Y.Z.zip'")
        
        # Check for icon
        icon_files = ["icon.png", "icon.jpg", "icon.jpeg"]
        icon_found = any((mod_dir / icon_file).exists() for icon_file in icon_files)
        
        if not icon_found:
            self.warning(f"No icon file found in {mod_dir.name}, consider adding icon.png")
        
        return True
    
    def validate_zip_name(self, zip_path, mod_name):
        """Validate zip file naming convention."""
        expected_pattern = f"{mod_name}-v*.zip"
        return zip_path.name.startswith(f"{mod_name}-v")
    
    def validate_zip_contents(self, zip_path):
        """Validate zip file contents."""
        self.info(f"Validating zip contents: {zip_path.name}")
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                # Test zip integrity
                zip_file.testzip()
                
                file_list = zip_file.namelist()
                
                # Check for common mod files
                has_pak_files = any(f.endswith('.pak') for f in file_list)
                has_lua_files = any(f.endswith('.lua') for f in file_list)
                
                if not has_pak_files and not has_lua_files:
                    self.warning(f"No .pak or .lua files found in {zip_path.name}, is this a valid mod?")
                
                # Check for suspicious files
                suspicious_extensions = ['.exe', '.dll', '.bat', '.cmd', '.ps1']
                suspicious_files = [f for f in file_list if any(f.lower().endswith(ext) for ext in suspicious_extensions)]
                
                if suspicious_files:
                    self.warning(f"Potentially suspicious files in {zip_path.name}: {suspicious_files}")
                
                return True
                
        except zipfile.BadZipFile:
            self.error(f"Corrupt zip file: {zip_path.name}")
            return False
        except Exception as e:
            self.error(f"Error reading zip file {zip_path.name}: {e}")
            return False
    
    def load_mod_info(self, mod_dir):
        """Load and parse mod-info.json."""
        info_files = ["mod-info.json", "mod-info.jsonc"]
        
        for info_file in info_files:
            info_path = mod_dir / info_file
            if info_path.exists():
                try:
                    with open(info_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Basic JSONC support
                        lines = content.split('\n')
                        cleaned_lines = []
                        for line in lines:
                            if '//' in line:
                                line = line[:line.index('//')]
                            cleaned_lines.append(line)
                        cleaned_content = '\n'.join(cleaned_lines)
                        return json.loads(cleaned_content)
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    self.error(f"Failed to parse {info_path}: {e}")
                    continue
        
        return None
    
    def validate_mod(self, mod_dir):
        """Validate a single mod directory."""
        print(f"\n🔍 Validating mod: {mod_dir.name}")
        
        # Reset error/warning counts for this mod
        initial_errors = len(self.errors)
        initial_warnings = len(self.warnings)
        
        # Validate directory structure
        if not self.validate_mod_structure(mod_dir):
            return False
        
        # Load and validate mod info
        mod_info = self.load_mod_info(mod_dir)
        if mod_info is None:
            return False
        
        if not self.validate_mod_info(mod_dir, mod_info):
            return False
        
        # Validate zip files
        zip_files = list(mod_dir.glob("*.zip"))
        for zip_file in zip_files:
            if not self.validate_zip_contents(zip_file):
                return False
        
        # Summary for this mod
        mod_errors = len(self.errors) - initial_errors
        mod_warnings = len(self.warnings) - initial_warnings
        
        if mod_errors == 0:
            print(f"✅ {mod_dir.name} validation passed")
            if mod_warnings > 0:
                print(f"   ({mod_warnings} warnings)")
        else:
            print(f"❌ {mod_dir.name} validation failed ({mod_errors} errors, {mod_warnings} warnings)")
        
        return mod_errors == 0

def validate_all_mods():
    """Validate all mods in the repository."""
    print("🔍 Starting mod validation...")
    
    validator = ModValidator()
    mods_dir = Path("mods")
    
    if not mods_dir.exists():
        validator.error("Mods directory not found!")
        return False
    
    mod_dirs = [d for d in mods_dir.iterdir() if d.is_dir()]
    
    if not mod_dirs:
        validator.warning("No mod directories found")
        return True
    
    valid_mods = 0
    total_mods = len(mod_dirs)
    
    for mod_dir in mod_dirs:
        if validator.validate_mod(mod_dir):
            valid_mods += 1
    
    # Final summary
    print(f"\n📊 Validation Summary:")
    print(f"   Total mods: {total_mods}")
    print(f"   Valid mods: {valid_mods}")
    print(f"   Failed mods: {total_mods - valid_mods}")
    print(f"   Total errors: {len(validator.errors)}")
    print(f"   Total warnings: {len(validator.warnings)}")
    
    if valid_mods == total_mods:
        print("🎉 All mods passed validation!")
        return True
    else:
        print("❌ Some mods failed validation")
        return False

if __name__ == "__main__":
    success = validate_all_mods()
    sys.exit(0 if success else 1)