# 🎧 Dead Frontier 3D Audio Modding Tools

This project includes two Python scripts that simplify the extraction and replacement of audio clips in the Unity-based game **Dead Frontier 3D**. Whether you're backing up game sounds or replacing them with custom audio, these tools make the process fast and straightforward.

## 📁 Features

- ✅ Extract all `AudioClip` assets from a Unity `.assets` file (e.g., `sharedassets0.assets`)
- ✅ Replace existing audio clips with custom `.ogg` files based on matching names
- ✅ Fully automated, no manual importing required

## 🛠️ Requirements

- Python 3.7+
- [UnityPy](https://pypi.org/project/UnityPy/) (`pip install UnityPy`)

## 📜 Scripts

### `DF3D_Audio_Extractor.py`

Extracts all `AudioClip` objects from the specified Unity `.assets` file and saves them as `.ogg` files.

```bash
python DF3D_Audio_Extractor.py
```

- Input: `sharedassets0.assets`
- Output: `extracted_audio/clip_name.ogg`

### `DF3D_Audio_Replacer.py`

Replaces the audio clips in `sharedassets0.assets` with files from the `extracted_audio` folder. File names must match the original clip names.

```bash
python DF3D_Audio_Replacer.py
```

- Input: `sharedassets0.assets`, `extracted_audio/`
- Output: `output/sharedassets0.assets`

## ⚠️ Notes

- Make sure replacement audio clips are valid `.ogg` files.
- File names must exactly match the original extracted names.
- Always back up your original game files before modding.

These scripts are not limited to audio.
They can be tweaked to extract textures, models, etc... Then use the replacer to insert everything (with some adjustments needed too and as long as the modified file name matches what is inside the sharedassets0.assets).
