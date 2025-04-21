import UnityPy
import os

# Path to the Unity .assets or .bundle file
asset_file_path = "assets_to_extract/sharedassets0.assets"
output_dir = "extracted_audios"
os.makedirs(output_dir, exist_ok=True)

# Load the Unity asset file
env = UnityPy.load(asset_file_path)


def detect_audio_format(data: bytes) -> tuple[str | None, bytes]:
    header = data[:64]
    if b'OggS' in header:
        return "ogg", data
    return None, data


# Iterate through all objects in the file
for obj in env.objects:
    if obj.type.name == "AudioClip":
        try:
            name = obj.peek_name() or f"clip_{obj.path_id}"

            # Get raw data from the AudioClip
            raw_data = obj.get_raw_data()
            if not raw_data:
                raise ValueError("No raw data available")

            # Detect file extension
            ext, clean_data = detect_audio_format(raw_data)

            # Skip non-OGG audio
            if ext is None:
                print(f"Skipping non-OGG audio: {name}")
                continue

            safe_name = f"{name}.{ext}"
            output_path = os.path.join(output_dir, safe_name)

            # Save the raw data
            with open(output_path, "wb") as f:
                f.write(clean_data)

            print(f"Audio saved: {output_path}")

        except Exception as e:
            print(f"Failed to extract object ID {obj.path_id}: {e}")
