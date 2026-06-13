import argparse
from processor import process_label

def main():
    parser = argparse.ArgumentParser(description="AI Alcohol Label Verification")
    parser.add_argument("--input-folder", required=True, help="Path to label images")
    args = parser.parse_args()

    print(f"Scanning folder: {args.input_folder}")
    # Logic to iterate through files will go here
    result = process_label(args.input_folder)
    print(result)

if __name__ == "__main__":
    main()