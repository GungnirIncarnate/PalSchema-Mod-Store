# Contributing to Palworld Mod Store

Thank you for your interest in contributing to the Palworld Mod Store! This guide will help you submit mods and contribute to the repository.

## 📦 Submitting a New Mod

### 1. Prepare Your Mod

Ensure your mod is properly packaged and tested:
- Create a zip file containing all mod files
- Test the mod in-game to ensure it works
- Prepare a 64x64 pixel icon (PNG format recommended)

### 2. Create Mod Directory

1. Fork this repository
2. Create a new directory in `mods/` with your mod name (e.g., `mods/YourModName/`)
3. Use a descriptive name without spaces (use PascalCase or kebab-case)

### 3. Add Required Files

#### mod-info.json (Required)
```json
{
  "ModName": "Your Mod Display Name",
  "Version": "1.0.0",
  "Description": "A detailed description of what your mod does and how it enhances the game experience.",
  "Author": "Your Name or Username",
  "Tags": ["gameplay", "enhancement", "ui"],
  "RequiresPalSchema": true,
  "MinGameVersion": "0.3.0",
  "Homepage": "https://your-mod-page.com",
  "SourceCode": "https://github.com/yourname/yourmod"
}
```

#### Mod Zip File (Required)
- Name format: `YourModName-vX.Y.Z.zip`
- Contains all mod files (`.pak`, `.lua`, configs, etc.)
- Should not exceed 100MB

#### Icon File (Recommended)
- Filename: `icon.png`, `icon.jpg`, or `icon.jpeg`
- Size: 64x64 pixels recommended
- Clear, recognizable representation of your mod

### 4. Field Descriptions

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `ModName` | ✅ | String | Display name shown in mod managers |
| `Version` | ✅ | String | Semantic version (X.Y.Z format) |
| `Description` | ✅ | String | Detailed mod description (max 500 chars) |
| `Author` | ⭕ | String | Creator name or username |
| `Tags` | ⭕ | Array | Categorization tags |
| `RequiresPalSchema` | ⭕ | Boolean | Whether mod needs PalSchema (default: true) |
| `MinGameVersion` | ⭕ | String | Minimum Palworld version |
| `Homepage` | ⭕ | String | Mod's main page URL |
| `SourceCode` | ⭕ | String | Source code repository URL |

### 5. Quality Guidelines

#### Mod Quality
- ✅ Thoroughly tested in-game
- ✅ No game-breaking bugs
- ✅ Clear installation instructions
- ✅ Compatible with latest Palworld version

#### Content Standards
- ✅ Original work or properly credited
- ✅ No malicious code or suspicious files
- ✅ Family-friendly content
- ✅ Respects game's EULA

#### Documentation
- ✅ Clear, descriptive mod name
- ✅ Detailed description of functionality
- ✅ Proper categorization with tags
- ✅ Version follows semantic versioning

### 6. Common Tags

Use these standardized tags to help users find your mod:

**Gameplay:**
- `gameplay` - Core game mechanics changes
- `balance` - Game balance adjustments
- `difficulty` - Difficulty modifications
- `progression` - Progression system changes

**Content:**
- `pals` - New or modified Pals
- `items` - New items or equipment
- `buildings` - New structures or building options
- `world` - World generation or environment changes

**Interface:**
- `ui` - User interface improvements
- `hud` - HUD modifications
- `menu` - Menu system changes

**Quality of Life:**
- `quality-of-life` - General QoL improvements
- `automation` - Automation features
- `convenience` - Convenience features
- `optimization` - Performance improvements

### 7. Submission Process

1. **Create Pull Request**
   - Fork the repository
   - Add your mod files
   - Create a descriptive PR title: "Add [ModName] v[Version]"
   - Include mod description and changelog in PR description

2. **Automated Validation**
   - GitHub Actions will automatically validate your mod
   - Check for proper file structure and metadata
   - Ensure no errors in mod-info.json

3. **Review Process**
   - Maintainers will review your mod for quality and safety
   - May request changes or improvements
   - Once approved, mod will be merged and added to manifest

4. **Post-Merge**
   - Manifest.json is automatically updated
   - Your mod becomes available in mod managers
   - Download URLs and metadata are generated

### 8. Updating Your Mod

To update an existing mod:

1. Update the zip file with new version number
2. Update `Version` field in mod-info.json
3. Update `Description` if functionality changed
4. Submit a new Pull Request with changes

### 9. Support and Questions

- 📖 Check existing issues for common questions
- 🐛 Report bugs in the Issues section
- 💬 Join discussions in the Discussions tab
- 📧 Contact maintainers for urgent matters

### 10. Code of Conduct

- Be respectful to all contributors
- Provide constructive feedback
- Help newcomers learn the process
- Follow GitHub's Community Guidelines

## 🛠 Development Contributions

### Repository Structure
- `scripts/` - Python automation scripts
- `.github/workflows/` - GitHub Actions workflows
- `mods/` - Individual mod directories

### Scripts
- `generate-manifest.py` - Creates manifest.json from mod data
- `validate-mod.py` - Validates mod structure and metadata

### Testing Locally
```bash
# Validate all mods
python scripts/validate-mod.py

# Generate manifest
python scripts/generate-manifest.py
```

Thank you for contributing to the Palworld modding community! 🎮