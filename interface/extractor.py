import UnityPy
import os


def extract_audio(asset_file_path, output_dir, progress=None):
    env = UnityPy.load(asset_file_path)

    def detect_audio_format(data: bytes) -> tuple[str | None, bytes]:
        header = data[:64]
        if b'OggS' in header:
            return "ogg", data
        return None, data

    audio_clips = [obj for obj in env.objects if obj.type.name == "AudioClip"]
    total = len(audio_clips)
    count = 0

    if progress:
        progress["maximum"] = total
        progress["value"] = 0

    for obj in audio_clips:
        try:
            name = obj.peek_name() or f"clip_{obj.path_id}"
            raw_data = obj.get_raw_data()
            if not raw_data:
                continue

            ext, clean_data = detect_audio_format(raw_data)
            if ext is None:
                continue

            safe_name = f"{name}.{ext}"
            output_path = os.path.join(output_dir, safe_name)

            with open(output_path, "wb") as f:
                f.write(clean_data)

        except Exception as e:
            print(f"Failed to extract object ID {obj.path_id}: {e}")
        finally:
            count += 1
            if progress:
                progress["value"] = count
                progress.update()
