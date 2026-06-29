import argparse
from scripts.automation.duplicate_cleaner import run_duplicate_cleaner


def main():
    parser = argparse.ArgumentParser(description="Python Automation Toolkit")

    parser.add_argument("--tool", required=True)
    parser.add_argument("--path", required=True)
    parser.add_argument("--delete", action="store_true")

    args = parser.parse_args()

    if args.tool == "duplicate_cleaner":
        run_duplicate_cleaner(args.path, args.delete)
    else:
        print(f"Unknown tool: {args.tool}")


if __name__ == "__main__":
    main()