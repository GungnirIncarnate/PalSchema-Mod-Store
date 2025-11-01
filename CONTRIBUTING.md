# 🎮 Contributing to PalSchema Mod Store# 🎮 Contributing Mods to PalSchema Mod Store# 🎮 Contributing Mods to PalSchema Mod Store



Thank you for your interest in contributing to the PalSchema Mod Store! This guide will help you submit your mods to the community.



## 🚀 Submission MethodsThere are several ways to contribute your mod to the PalSchema Mod Store, depending on your technical comfort level:There are several ways to contribute your mod to the PalSchema Mod Store, depending on your technical comfort level:



### Method 1: Issue Template (Recommended)



**Perfect for:** Most users, especially those unfamiliar with Git## 🚀 **Method 1: Issue Submission (Recommended for most users)**## � **Method 1: Issue Submission (Recommended for most users)**



1. **[Click here to submit a new mod](../../issues/new?assignees=GungnirIncarnate&labels=mod-submission%2Cpending-review&template=mod-submission.yml&title=%5BMOD+SUBMISSION%5D+)**

2. Fill out the form with your mod details

3. Upload your mod ZIP and icon to a file hosting service (GitHub Releases, Google Drive, etc.)**Perfect for:** Non-technical users, quick submissions**Perfect for:** Non-technical users, quick submissions

4. Paste the download URLs in the form

5. Submit the issue and wait for review



**Processing Time:** 2-5 business days1. **Go to**: [Submit New Mod](../../issues/new?assignees=GungnirIncarnate&labels=mod-submission%2Cpending-review&template=mod-submission.yml&title=%5BMOD+SUBMISSION%5D+)1. **Go to**: [Submit New Mod](../../issues/new?assignees=GungnirIncarnate&labels=mod-submission%2Cpending-review&template=mod-submission.yml&title=%5BMOD+SUBMISSION%5D+)



**Approval Process:**2. **Fill out the form** with your mod details2. **Fill out the form** with your mod details

- Maintainers review your submission

- Comment `/approve-mod` to approve or `/reject-mod [reason]` to reject3. **Upload your files** to a file hosting service (GitHub releases, Google Drive, etc.)3. **Upload your files** to a file hosting service (GitHub releases, Google Drive, etc.)

- Approved mods are automatically added to the store

- Issue is automatically closed after processing4. **Submit the issue** - our team will handle the rest!4. **Submit the issue** - our team will handle the rest!



### Method 2: Pull Request



**Perfect for:** Developers comfortable with Git**⏱️ Processing Time:** 2-5 business days**⏱️ Processing Time:** 2-5 business days



1. Fork this repository

2. Create a new folder: `mods/YourModName/`

3. Add your files:---#### mod-info.json (Required)

   ```

   mods/YourModName/```json

   ├── mod-info.json              # Mod metadata (required)

   ├── YourModName-v1.0.0.zip     # Your mod files (required)## 🔧 **Method 2: Pull Request (For developers)**{

   └── icon.png                   # Mod icon (optional, recommended)

   ```  "ModName": "Your Mod Display Name",

4. Create a pull request with a clear description

5. Wait for maintainer review and approval**Perfect for:** Developers comfortable with Git  "Version": "1.0.0",



---  "Description": "A detailed description of what your mod does and how it enhances the game experience.",



## 📋 Mod Requirements1. **Fork** this repository  "Author": "Your Name or Username",



### Required Files2. **Create** a new folder in `mods/YourModName/`  "Tags": ["gameplay", "enhancement", "ui"],



#### 1. mod-info.json3. **Add** your files:  "MinGameVersion": "0.3.0",

Contains your mod's metadata:

   ```  "Homepage": "https://your-mod-page.com",

```json

{   mods/YourModName/  "SourceCode": "https://github.com/yourname/yourmod"

  "UUID": "auto-generated-on-approval",

  "ModName": "Your Mod Display Name",   ├── mod-info.json     # Mod metadata}

  "Version": "1.0.0",

  "Description": "A detailed description of what your mod does",   ├── YourModName-v1.0.0.zip  # Your mod files```

  "Author": "Your Name",

  "RequiredVersion": "steam",   └── icon.png          # Mod icon (optional)

  "Tags": ["gameplay", "enhancement"],

  "MinGameVersion": "0.3.0",   ```#### Mod Zip File (Required)

  "Homepage": "https://your-mod-page.com"

}4. **Create** a pull request- Name format: `YourModName-vX.Y.Z.zip`

```

- Contains all mod files (`.json`, `.jsonc`, `.pak`, configs, etc.)

**Field Descriptions:**

- `UUID` - Auto-generated unique identifier (don't add manually)### mod-info.json Format:

- `ModName` - Display name shown in mod managers *(required)*

- `Version` - Semantic version in X.Y.Z format *(required)*```json#### Icon File (Recommended)

- `Description` - What your mod does *(required)*

- `Author` - Your name or username *(required)*{- Filename: `icon.png`, `icon.jpg`, or `icon.jpeg`

- `RequiredVersion` - `"steam"`, `"gamepass"`, or `"both"` *(required)*

- `Tags` - Category tags for discovery *(required)*  "ModName": "Your Mod Name",- Size: 256x256 pixels recommended

- `MinGameVersion` - Minimum Palworld version (default: "0.3.0")

- `Homepage` - Mod's webpage or documentation *(optional)*  "Version": "1.0.0",- Clear, recognizable representation of your mod



#### 2. Mod ZIP File  "Description": "What your mod does...",

- **Naming:** `YourModName-vX.Y.Z.zip` (e.g., `AwesomeMod-v1.0.0.zip`)

- **Contents:** All mod files (`.pak`, `.json`, `.jsonc`, configs, etc.)  "Author": "YourUsername",### 4. Field Descriptions

- **Structure:** Should match PalSchema mod structure requirements

  "Tags": ["ui", "enhancement"],

#### 3. Icon File (Optional but Recommended)

- **Filename:** `icon.png`, `icon.jpg`, or `icon.jpeg`  "MinGameVersion": "0.3.0",| Field | Required | Type | Description |

- **Size:** 256x256 pixels recommended

- **Format:** PNG or JPEG  "Homepage": "https://your-mod-page.com",|-------|----------|------|-------------|

- **Content:** Clear, recognizable representation of your mod

  "SourceCode": "https://github.com/you/your-mod"| `ModName` | ✅ | String | Display name shown in mod managers |

---

}| `Version` | ✅ | String | Semantic version (X.Y.Z format) |

## ✅ Quality Guidelines

```| `Description` | ✅ | String | Detailed mod description (max 500 chars) |

### Mod Quality

- ✅ Thoroughly tested in-game| `Author` | ⭕ | String | Creator name or username |

- ✅ No game-breaking bugs

- ✅ Compatible with latest Palworld version---| `Tags` | ⭕ | Array | Categorization tags |

- ✅ Clear functionality and purpose

| `MinGameVersion` | ⭕ | String | Minimum Palworld version |

### Content Standards

- ✅ Original work or properly credited## 📧 **Method 3: Direct Contact**| `Homepage` | ⭕ | String | Mod's main page URL |

- ✅ No malicious code or suspicious files

- ✅ Family-friendly content| `SourceCode` | ⭕ | String | Source code repository URL |

- ✅ Respects Palworld's EULA and ToS

**Perfect for:** Special cases, large mods, partnerships

### Documentation

- ✅ Clear, descriptive mod name### 5. Quality Guidelines

- ✅ Detailed description of functionality

- ✅ Proper categorization with tags- **Discord**: Join our community server

- ✅ Version follows semantic versioning (X.Y.Z)

- **Email**: Contact the maintainers#### Mod Quality

### ❌ Not Allowed

- Malicious code or viruses- **GitHub Discussions**: Start a conversation- ✅ Thoroughly tested in-game

- Copyrighted content without permission

- NSFW or inappropriate content- ✅ No game-breaking bugs

- Mods that violate game ToS

---- ✅ Clear installation instructions

---

- ✅ Compatible with latest Palworld version

## 🏷️ Available Tags

## 📋 **Mod Requirements**

Use these standardized tags to help users find your mod:

#### Content Standards

**Gameplay:**

- `gameplay` - Core game mechanics changes✅ **Must Have:**- ✅ Original work or properly credited

- `balance` - Game balance adjustments

- `difficulty` - Difficulty modifications- Compatible with PalSchema- ✅ No malicious code or suspicious files

- `progression` - Progression system changes

- Working mod files (tested)- ✅ Family-friendly content

**Content:**

- `pals` - New or modified Pals- Clear description- ✅ Respects game's EULA

- `items` - New items or equipment

- `buildings` - New structures or building options- Version information

- `world` - World generation or environment

- Safe code (no malware)#### Documentation

**Interface:**

- `ui` - User interface improvements- ✅ Clear, descriptive mod name

- `hud` - HUD modifications

- `menu` - Menu system changes✅ **Should Have:**- ✅ Detailed description of functionality



**Quality of Life:**- Mod icon (128x128 PNG recommended)- ✅ Proper categorization with tags

- `quality-of-life` - General QoL improvements

- `automation` - Automation features- Installation instructions- ✅ Version follows semantic versioning

- `convenience` - Convenience features

- `optimization` - Performance improvements- Source code link (if applicable)



**Other:**- Homepage or documentation### 6. Common Tags

- `enhancement` - General enhancements

- `visual` - Visual/graphical changes

- `statistics` - Stats and information displays

- `utility` - Utility tools and helpers❌ **Not Allowed:**Use these standardized tags to help users find your mod:



---- Malicious code



## 🔄 Updating Your Mod- Copyrighted content**Gameplay:**



### Via Issue Template:- NSFW content- `gameplay` - Core game mechanics changes

1. Create a new issue with "[MOD UPDATE]" in the title

2. Reference your original mod name- Mods that break game ToS- `balance` - Game balance adjustments

3. Provide new version information and download URL

- `difficulty` - Difficulty modifications

### Via Pull Request:

1. Update the version in `mod-info.json`---- `progression` - Progression system changes

2. Add the new ZIP file with updated version number

3. Update description if functionality changed

4. Submit pull request

## 🔄 **Update Process****Content:**

---

- `pals` - New or modified Pals

## 🤝 Getting Help

### For Issue Submissions:- `items` - New items or equipment

**Questions about submission?**

- 📖 Check existing [GitHub Issues](../../issues)1. Create a new issue with "[MOD UPDATE]" prefix- `buildings` - New structures or building options

- 💬 Join our Discord community

- 📧 Contact maintainers directly2. Reference your original mod- `world` - World generation or environment changes



**Problems with your submission?**3. Provide new version information

- Comment on your issue for updates

- Check validation logs in GitHub Actions**Interface:**

- Review error messages in automated comments

### For Pull Requests:- `ui` - User interface improvements

---

1. Update your mod-info.json version- `hud` - HUD modifications

## 🛠️ Development Contributions

2. Add new zip file with version number- `menu` - Menu system changes

Want to contribute to the mod store infrastructure?

3. Submit pull request

### Repository Structure

- `scripts/` - Python automation scripts**Quality of Life:**

- `.github/workflows/` - GitHub Actions automation

- `mods/` - Mod directories (mostly excluded from local sync)---- `quality-of-life` - General QoL improvements



### Useful Scripts- `automation` - Automation features

```bash

# Validate mod structure## 🤝 **Getting Help**- `convenience` - Convenience features

python scripts/validate-mod.py

- `optimization` - Performance improvements

# Generate manifest

python scripts/generate-manifest.py**Questions?** 

```

- 💬 Join our Discord community### 7. Submission Process

### Testing Locally

Fork the repository and test changes locally before submitting PRs.- 📖 Check existing GitHub issues



---- 🔍 Read the PalSchema documentation1. **Create Pull Request**



## 📜 Code of Conduct   - Fork the repository



- Be respectful to all contributors**Problems with submission?**   - Add your mod files

- Provide constructive feedback

- Help newcomers learn the process- Comment on your issue for updates   - Create a descriptive PR title: "Add [ModName] v[Version]"

- Follow GitHub's Community Guidelines

- Check validation logs in GitHub Actions   - Include mod description and changelog in PR description

---

- Contact maintainers directly

Thank you for contributing to the PalSchema modding community! 🎉

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