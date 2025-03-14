# URL Base Extractor

A simple Python script that extracts base URLs from a list of URLs and removes duplicates.

## Description

This script reads a list of URLs from `urls.txt`, extracts the base URL (protocol and domain) from each URL, removes duplicates, and saves the unique base URLs to `base_urls.txt`.

## Usage

1. Create a file named `urls.txt` containing one URL per line
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will create `base_urls.txt` containing unique base URLs

## Example

Input (`urls.txt`):
```
https://example.com/page1
https://example.com/page2
http://example.com/page3
https://another-site.com/page1
```

Output (`base_urls.txt`):
```
http://example.com
https://another-site.com
https://example.com
```

## Requirements

- Python 3.x

## Notes

- The script preserves the protocol (http/https) in the base URLs
- URLs are sorted alphabetically in the output file
- The script will print the number of unique base URLs processed 