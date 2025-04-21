# 🎧 Dead Frontier 3D Modder

This project includes two Python scripts that simplify the extraction and replacement of audio clips in the Unity-based game **Dead Frontier 3D**. Whether you're backing up game sounds or replacing them with custom audio, these tools make the process fast and straightforward.

## 📁 Features

-   ✅ Extract all `.ogg audio files` assets from a Unity `.assets` file (e.g., `sharedassets0.assets`)
-   ✅ Replace existing audio clips with custom `.ogg` files based on matching names
-   ✅ Fully automated, no manual importing required
    

## 🛠️ Requirements

-   Python 3.7+
    
-   [UnityPy](https://pypi.org/project/UnityPy/) (`pip install UnityPy`)
    

## 📜 Scripts

### `DF3D_Audio_Extractor.py`

Extracts all `AudioClip` objects from `sharedassets0.assets` file and saves them as `.ogg` files.

```bash
python DF3D_Audio_Extractor.py
```

-   Input: `assets_to_extract/sharedassets0.assets`
    
-   Output: `extracted_audios/audioname.ogg`

### `DF3D_Audio_Replacer.py`

Replaces the audio clips in `sharedassets0.assets` with files from the `extracted_audios` folder. Only `.ogg` files are supported and must have matching names.

```bash
python DF3D_Audio_Replacer.py
```

-   Input: `original_assets/sharedassets0.assets`, `extracted_audios/`
    
-   Output: `output/sharedassets0.assets`
    

## ⚠️ Notes

You must create both the `assets_to_extract` and `original_assets` folders for the scripts to work properly.  
Place the **original** `sharedassets0.assets` file in the `original_assets` folder, and the **modded** `sharedassets0.assets` file in the `assets_to_extract` folder.
-   File names must **exactly match** the original clip names for replacement to work.
-   Always back up your original game files before modding.
- `.wav` files are not supposed to be in the game assets. If there are any in there, it's because they were compiled into the game's final binary by mistake.
