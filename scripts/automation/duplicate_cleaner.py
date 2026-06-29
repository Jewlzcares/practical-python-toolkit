from pathlib import Path
import hashlib

# Nur sichere Medienformate
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi"}


def calculate_hash(file_path: Path) -> str:
    """
    Creates a SHA-256 hash for a file.
    Used to detect identical files.
    """
    hash_obj = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


def get_media_files(folder: Path):
    """
    Collects all images and videos in a folder (recursive).
    """
    for file in folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS | VIDEO_EXTENSIONS:
            yield file


def run_duplicate_cleaner(path: str, delete: bool = False):
    """
    Main tool function.
    Scans for duplicate images/videos and optionally deletes them.
    """

    folder = Path(path)

    if not folder.exists():
        print("❌ Folder not found.")
        return

    print(f"\n🔍 Scanning folder: {folder}\n")

    seen_hashes = {}
    duplicates = []

    # 1. Scan files
    for file in get_media_files(folder):
        file_hash = calculate_hash(file)

        if file_hash in seen_hashes:
            duplicates.append((file, seen_hashes[file_hash]))
        else:
            seen_hashes[file_hash] = file

    # 2. No duplicates
    if not duplicates:
        print("✅ No duplicates found.")
        return

    # 3. Show results
    print(f"⚠️ Found {len(duplicates)} duplicates:\n")

    for dup, original in duplicates:
        print(f"DUPLICATE: {dup}")
        print(f"ORIGINAL : {original}\n")

    # 4. Safety: Dry Run default
    if not delete:
        print("🧪 DRY RUN MODE ACTIVE")
        print("No files were deleted.")
        print("Use --delete to enable removal.")
        return

    # 5. Confirmation before deletion
    confirm = input("Type 'YES' to delete duplicates: ")

    if confirm == "YES":
        for dup, _ in duplicates:
            try:
                dup.unlink()
                print(f"🗑 Deleted: {dup}")
            except Exception as e:
                print(f"❌ Error deleting {dup}: {e}")
    else:
        print("Aborted.")
