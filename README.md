# Palworld Mod Store

A centralized repository for distributing Palworld mods with automated manifest generation and validation.

## 🚀 Features

- **Automated Manifest Generation**: GitHub Actions automatically update the mod catalog
- **Mod Validation**: Ensures all mods meet quality standards
- **Easy Distribution**: Direct download links for mod manager integration
- **Version Control**: Track mod updates and changes
- **Metadata Rich**: Comprehensive mod information including descriptions, authors, and compatibility

## 📁 Repository Structure

```
palworld-mod-store/
├── .github/
│   └── workflows/          # GitHub Actions for automation
├── mods/                   # Individual mod directories
│   └── ModName/
│       ├── mod-info.json   # Mod metadata
│       ├── icon.png        # Mod icon (64x64 recommended)
│       └── ModName-vX.Y.Z.zip  # Mod files
├── scripts/                # Automation scripts
├── manifest.json           # Auto-generated mod catalog
└── README.md              # This file
```

## 📦 Adding a New Mod

1. Create a new directory in `mods/` with your mod name
2. Add your mod files in a zip format: `ModName-vX.Y.Z.zip`
3. Create a `mod-info.json` file with the required metadata
4. Optionally add an `icon.png` file (64x64 pixels recommended)
5. Submit a Pull Request

### Mod Metadata Format (`mod-info.json`)

```json
{
  "ModName": "Your Mod Name",
  "Version": "1.0.0",
  "Description": "A detailed description of what your mod does",
  "Author": "Your Name",
  "Tags": ["gameplay", "enhancement", "ui"],
  "MinGameVersion": "0.3.0",
  "Homepage": "https://your-mod-homepage.com",
  "SourceCode": "https://github.com/yourname/yourmod"
}
```

## 🔄 Automated Workflows

- **Manifest Update**: Automatically regenerates `manifest.json` when mods are added/updated
- **Mod Validation**: Verifies mod structure and metadata on pull requests
- **Release Creation**: Optionally creates GitHub releases for mod versions

## 🛠 For Mod Manager Developers

The `manifest.json` file contains all available mods and can be queried at:
```
https://raw.githubusercontent.com/GungnirIncarnate/palworld-mod-store/main/manifest.json
```

Each mod entry includes:
- Download URLs for mod files
- Icon URLs
- Metadata (name, version, description, etc.)
- File checksums for integrity verification

## 📝 Contributing

1. Fork this repository
2. Add your mod following the structure above
3. Ensure your mod passes validation
4. Submit a Pull Request with a clear description

## 📄 License

This repository structure is MIT licensed. Individual mods retain their own licenses as specified by their authors.