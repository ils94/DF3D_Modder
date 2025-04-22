import UnityPy
import os


def replace_audio(asset_file_path, audio_folder, progress=None, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    env = UnityPy.load(asset_file_path)

    audio_clips = [obj for obj in env.objects if obj.type.name == "AudioClip"]
    total = len(audio_clips)
    count = 0

    if progress:
        progress["maximum"] = total
        progress["value"] = 0

    for obj in audio_clips:
        try:
            name = obj.peek_name() or f"clip_{obj.path_id}"
            audio_path = os.path.join(audio_folder, f"{name}.ogg")

            if os.path.exists(audio_path):
                with open(audio_path, "rb") as f:
                    new_audio_data = f.read()
                obj.set_raw_data(new_audio_data)

        except Exception as e:
            print(f"Failed to replace audio ID {obj.path_id}: {e}")
        finally:
            count += 1
            if progress:
                progress["value"] = count
                progress.update()

    output_file_path = os.path.join(output_dir, os.path.basename(asset_file_path))
    env.save(output_file_path)
    os.startfile(output_dir)
