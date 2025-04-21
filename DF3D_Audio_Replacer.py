import UnityPy
import os

# Path to the Unity .assets or .bundle file
asset_file_path = "sharedassets0.assets"  # Path to your .assets file
audio_folder = "audio_folder"  # Path to your folder with the audio files
output_dir = "output"  # Directory where the modified file will be saved
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

# Load the Unity asset file
env = UnityPy.load(asset_file_path)

# Iterate through all objects in the file
for obj in env.objects:
    if obj.type.name == "AudioClip":
        try:
            # Get the name of the AudioClip
            name = obj.peek_name() or f"clip_{obj.path_id}"
            safe_name = f"{name}.ogg".replace("/", "_").replace("\\", "_")
            audio_path = os.path.join(audio_folder, safe_name)

            # Check if a matching audio file exists in the folder
            if os.path.exists(audio_path):
                # Read the new audio file data
                with open(audio_path, "rb") as f:
                    new_audio_data = f.read()

                # Replace the raw data of the AudioClip
                # The 'obj.set_raw_data()' method can be used to replace the raw data of the AudioClip object
                obj.set_raw_data(new_audio_data)

                print(f"Audio replaced: {name}")
            else:
                print(f"File not found to replace: {name}")
        except Exception as e:
            print(f"Failed to replace audio ID {obj.path_id}: {e}")

# Save the modified asset file
output_file_path = os.path.join(output_dir)
env.save(output_file_path)

print(f"Modified asset file saved as '{output_file_path}'")
