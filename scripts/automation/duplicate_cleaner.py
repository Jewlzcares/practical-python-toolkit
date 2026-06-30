# We import Path from pathlib to work with files and folders in a clean,
# cross-platform way (Windows, Linux, macOS).
from pathlib import Path

from utils.logger import ConsoleLogger

# hashlib provides cryptographic hash functions (we use SHA-256)
# to create unique fingerprints of file contents.
import hashlib

# ----------------------------
# CONFIGURATION SECTION
# ----------------------------

# We define which file extensions are considered valid images.
# A "set" {} is used because it allows fast lookup and prevents duplicates.
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

# We define which file extensions are considered valid videos.
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi"}

logger = ConsoleLogger()

# Colors for output messages
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ----------------------------
# FUNCTION: calculate_hash
# ----------------------------

def calculate_hash(file_path: Path) -> str:
    """
    Creates a SHA-256 hash for a file.

    A hash is a fixed-length string generated from file content.
    Even a tiny change in the file will produce a completely different hash.

    This is used to detect duplicate files based on content.
    """

    # We create a SHA-256 hash object.
    # SHA-256 produces a 64-character hexadecimal string.
    hash_obj = hashlib.sha256()

    # We open the file in binary mode ("rb"):
    # - "r" = read
    # - "b" = binary (important for images/videos)
    with file_path.open("rb") as file:

        # We read the file in chunks instead of loading it all at once.
        # Why? Large files could consume too much memory.
        #
        # The walrus operator (:=) assigns and checks at the same time:
        # - file.read(8192) reads 8192 bytes (8 KB per chunk)
        # - loop stops when chunk is empty (end of file)
        while chunk := file.read(8192):

            # We update the hash with each chunk of the file.
            hash_obj.update(chunk)

    # We return the final hash as a hexadecimal string.
    return hash_obj.hexdigest()


# ----------------------------
# FUNCTION: get_media_files
# ----------------------------

from pathlib import Path

def get_media_files(folder: Path):
    """
    Collects all image and video files in a folder recursively.

    This function walks through the entire directory tree,
    including all subfolders, and yields media files one by one.
    """

    # rglob("*") performs a recursive search through all files and folders
    # "*" means: match everything (files + directories)
    for file in folder.rglob("*"):

        # 1. Safety check:
        # Skip anything that is not a file (e.g. directories)
        if not file.is_file():
            continue  # ignore folders and continue looping

        # 2. Extract file extension
        # .lower() ensures consistency (e.g. .JPG == .jpg)
        suffix = file.suffix.lower()

        # 3. Check if the file is an image
        if suffix in IMAGE_EXTENSIONS:
            print(f"{PURPLE}[Image]{RESET} {file}")  # debug output for images
            yield file  # yield file immediately (memory efficient generator)

        # 4. Otherwise check if the file is a video
        elif suffix in VIDEO_EXTENSIONS:
            print(f"{CYAN}[Video]{RESET} {file}")  # debug output for videos
            yield file  # yield file immediately

# ----------------------------
# FUNCTION: run_duplicate_cleaner
# ----------------------------

def run_duplicate_cleaner(path: str, delete: bool = False):
    """
    Main function of the tool.

    Purpose:
    - Scan a folder for duplicate images/videos
    - Compare files using SHA-256 hashes
    - Optionally delete duplicates (if delete=True)
    """

    # Convert string path into a Path object for easier file handling.
    folder = Path(path)

    # Check if the folder exists before continuing.
    if not folder.exists():
        logger.error(f"Folder: {folder} does not exist.")
        return

    print(f"\n{GREEN}[Scanning folder]{RESET} {folder}\n")

    # Dictionary to store hashes we have already seen.
    # Structure:
    # {file_hash: original_file_path}
    seen_hashes = {}

    # List to store duplicates as tuples:
    # (duplicate_file, original_file)
    duplicates = []

    # ----------------------------
    # 1. SCANNING FILES
    # ----------------------------

    for file in get_media_files(folder):

        # Calculate unique fingerprint of file content
        file_hash = calculate_hash(file)
        print(f"{GREEN}[Calculated hash]{RESET} {file_hash}")

        # If we have already seen this hash:
        if file_hash in seen_hashes:

            # Then this file is a duplicate
            duplicates.append((file, seen_hashes[file_hash]))
            print(f"{YELLOW}[Evaluation]{RESET} > This is a duplicate. Added to duplicates.\n")

        else:
            # Otherwise, store it as the original
            seen_hashes[file_hash] = file
            print(f"{GREEN}[Evaluation]{RESET} > This is an original. Added to seen_hashes.\n")

    # ----------------------------
    # 2. NO DUPLICATES FOUND
    # ----------------------------

    if not duplicates:
        logger.info(f"> No duplicate files found.")
        return

    # ----------------------------
    # 3. SHOW RESULTS
    # ----------------------------

    print(f"{BLUE}> Found {len(duplicates)} duplicates:{RESET}\n")

    for dup, original in duplicates:
        print(f"{RED}[Duplicate]{RESET} {dup}")
        print(f"{GREEN}[Original ]{RESET} {original}\n")

    # ----------------------------
    # 4. SAFETY FEATURE: DRY RUN
    # ----------------------------

    # If delete=False, we DO NOT delete anything.
    # This is a safety mechanism to prevent accidental data loss.
    if not delete:
        print(f"{YELLOW}[DRY RUN MODE] ACTIVE{RESET}")
        print("> No files were deleted.")
        print("> Use --delete to enable removal.")
        return

    # ----------------------------
    # 5. USER CONFIRMATION BEFORE DELETION
    # ----------------------------

    # We ask the user to type YES explicitly.
    # This prevents accidental deletion of important files.
    logger.warn("> This operation will permanently delete duplicate files. This action cannot be undone.")
    confirm = input(f"{YELLOW}[WARNING] > Type 'YES' if you want to continue: {RESET}")

    if confirm == "YES":

        # Loop through all duplicate files
        for dup, _ in duplicates:
            try:
                # unlink() deletes the file from the filesystem
                dup.unlink()
                print("")
                print(f"{GREEN}[Deleted]{RESET} {dup}")

            except Exception as e:
                # If something goes wrong (permissions, file in use, etc.)
                print(f"{RED}[Error deleting]{RESET} {dup}: {e}")

    else:
        # Any input other than "YES" cancels the operation
        logger.info("Process aborted.")