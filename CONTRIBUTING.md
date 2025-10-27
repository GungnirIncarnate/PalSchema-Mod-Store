# 🎮 Contributing Mods to PalSchema Mod Store# 🎮 Contributing Mods to PalSchema Mod Store



There are several ways to contribute your mod to the PalSchema Mod Store, depending on your technical comfort level:There are several ways to contribute your mod to the PalSchema Mod Store, depending on your technical comfort level:



## 🚀 **Method 1: Issue Submission (Recommended for most users)**## � **Method 1: Issue Submission (Recommended for most users)**



**Perfect for:** Non-technical users, quick submissions**Perfect for:** Non-technical users, quick submissions



1. **Go to**: [Submit New Mod](../../issues/new?assignees=GungnirIncarnate&labels=mod-submission%2Cpending-review&template=mod-submission.yml&title=%5BMOD+SUBMISSION%5D+)1. **Go to**: [Submit New Mod](../../issues/new?assignees=GungnirIncarnate&labels=mod-submission%2Cpending-review&template=mod-submission.yml&title=%5BMOD+SUBMISSION%5D+)

2. **Fill out the form** with your mod details2. **Fill out the form** with your mod details

3. **Upload your files** to a file hosting service (GitHub releases, Google Drive, etc.)3. **Upload your files** to a file hosting service (GitHub releases, Google Drive, etc.)

4. **Submit the issue** - our team will handle the rest!4. **Submit the issue** - our team will handle the rest!



**⏱️ Processing Time:** 2-5 business days**⏱️ Processing Time:** 2-5 business days



---#### mod-info.json (Required)

```json

## 🔧 **Method 2: Pull Request (For developers)**{

  "ModName": "Your Mod Display Name",

**Perfect for:** Developers comfortable with Git  "Version": "1.0.0",

  "Description": "A detailed description of what your mod does and how it enhances the game experience.",

1. **Fork** this repository  "Author": "Your Name or Username",

2. **Create** a new folder in `mods/YourModName/`  "Tags": ["gameplay", "enhancement", "ui"],

3. **Add** your files:  "MinGameVersion": "0.3.0",

   ```  "Homepage": "https://your-mod-page.com",

   mods/YourModName/  "SourceCode": "https://github.com/yourname/yourmod"

   ├── mod-info.json     # Mod metadata}

   ├── YourModName-v1.0.0.zip  # Your mod files```

   └── icon.png          # Mod icon (optional)

   ```#### Mod Zip File (Required)

4. **Create** a pull request- Name format: `YourModName-vX.Y.Z.zip`

- Contains all mod files (`.json`, `.jsonc`, `.pak`, configs, etc.)

### mod-info.json Format:

```json#### Icon File (Recommended)

{- Filename: `icon.png`, `icon.jpg`, or `icon.jpeg`

  "ModName": "Your Mod Name",- Size: 256x256 pixels recommended

  "Version": "1.0.0",- Clear, recognizable representation of your mod

  "Description": "What your mod does...",

  "Author": "YourUsername",### 4. Field Descriptions

  "Tags": ["ui", "enhancement"],

  "MinGameVersion": "0.3.0",| Field | Required | Type | Description |

  "Homepage": "https://your-mod-page.com",|-------|----------|------|-------------|

  "SourceCode": "https://github.com/you/your-mod"| `ModName` | ✅ | String | Display name shown in mod managers |

}| `Version` | ✅ | String | Semantic version (X.Y.Z format) |

```| `Description` | ✅ | String | Detailed mod description (max 500 chars) |

| `Author` | ⭕ | String | Creator name or username |

---| `Tags` | ⭕ | Array | Categorization tags |

| `MinGameVersion` | ⭕ | String | Minimum Palworld version |

## 📧 **Method 3: Direct Contact**| `Homepage` | ⭕ | String | Mod's main page URL |

| `SourceCode` | ⭕ | String | Source code repository URL |

**Perfect for:** Special cases, large mods, partnerships

### 5. Quality Guidelines

- **Discord**: Join our community server

- **Email**: Contact the maintainers#### Mod Quality

- **GitHub Discussions**: Start a conversation- ✅ Thoroughly tested in-game

- ✅ No game-breaking bugs

---- ✅ Clear installation instructions

- ✅ Compatible with latest Palworld version

## 📋 **Mod Requirements**

#### Content Standards

✅ **Must Have:**- ✅ Original work or properly credited

- Compatible with PalSchema- ✅ No malicious code or suspicious files

- Working mod files (tested)- ✅ Family-friendly content

- Clear description- ✅ Respects game's EULA

- Version information

- Safe code (no malware)#### Documentation

- ✅ Clear, descriptive mod name

✅ **Should Have:**- ✅ Detailed description of functionality

- Mod icon (128x128 PNG recommended)- ✅ Proper categorization with tags

- Installation instructions- ✅ Version follows semantic versioning

- Source code link (if applicable)

- Homepage or documentation### 6. Common Tags



❌ **Not Allowed:**Use these standardized tags to help users find your mod:

- Malicious code

- Copyrighted content**Gameplay:**

- NSFW content- `gameplay` - Core game mechanics changes

- Mods that break game ToS- `balance` - Game balance adjustments

- `difficulty` - Difficulty modifications

---- `progression` - Progression system changes



## 🔄 **Update Process****Content:**

- `pals` - New or modified Pals

### For Issue Submissions:- `items` - New items or equipment

1. Create a new issue with "[MOD UPDATE]" prefix- `buildings` - New structures or building options

2. Reference your original mod- `world` - World generation or environment changes

3. Provide new version information

**Interface:**

### For Pull Requests:- `ui` - User interface improvements

1. Update your mod-info.json version- `hud` - HUD modifications

2. Add new zip file with version number- `menu` - Menu system changes

3. Submit pull request

**Quality of Life:**

---- `quality-of-life` - General QoL improvements

- `automation` - Automation features

## 🤝 **Getting Help**- `convenience` - Convenience features

- `optimization` - Performance improvements

**Questions?** 

- 💬 Join our Discord community### 7. Submission Process

- 📖 Check existing GitHub issues

- 🔍 Read the PalSchema documentation1. **Create Pull Request**

   - Fork the repository

**Problems with submission?**   - Add your mod files

- Comment on your issue for updates   - Create a descriptive PR title: "Add [ModName] v[Version]"

- Check validation logs in GitHub Actions   - Include mod description and changelog in PR description

- Contact maintainers directly

2. **Automated Validation**

---   - GitHub Actions will automatically validate your mod

   - Check for proper file structure and metadata

## 📊 **Mod Store Stats**   - Ensure no errors in mod-info.json



Want to see how your mod is performing?3. **Review Process**

- **Downloads**: Check GitHub releases analytics   - Maintainers will review your mod for quality and safety

- **Usage**: Community feedback and ratings   - May request changes or improvements

- **Updates**: Automated manifest tracking   - Once approved, mod will be merged and added to manifest



Thank you for contributing to the PalSchema community! 🎉4. **Post-Merge**
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