import UnityPy
import os

# Path to the Unity .assets or .bundle file
asset_file_path = "sharedassets0.assets"
output_dir = "extracted_audio"
os.makedirs(output_dir, exist_ok=True)

# Load the Unity asset file
env = UnityPy.load(asset_file_path)

# Iterate through all objects in the file
for obj in env.objects:
    if obj.type.name == "AudioClip":
        try:
            name = obj.peek_name() or f"clip_{obj.path_id}"
            # Use ".ogg" as the extension for extracted audio files
            safe_name = f"{name}.ogg"
            output_path = os.path.join(output_dir, safe_name)

            # Get raw data from the AudioClip
            raw_data = obj.get_raw_data()
            if not raw_data:
                raise ValueError("No raw data available")

            # Save the raw data as an Ogg file
            with open(output_path, "wb") as f:
                f.write(raw_data)

            print(f"Audio saved: {output_path}")

        except Exception as e:
            print(f"❌ Failed to extract object ID {obj.path_id}: {e}")
