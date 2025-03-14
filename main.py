from urllib.parse import urlparse

# Read URLs from file
with open('urls.txt', 'r') as file:
    urls = [line.strip() for line in file]

# Track skipped URLs
skipped_urls = []
valid_urls = []

# Process URLs
for url in urls:
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        valid_urls.append(f"{parsed.scheme}://{parsed.netloc}")
    else:
        skipped_urls.append(url)

# Remove duplicates and sort
base_urls = sorted(set(valid_urls))

# Save to a new file
with open('base_urls.txt', 'w') as file:
    for url in base_urls:
        file.write(url + '\n')

print(f"Processed {len(base_urls)} unique base URLs.")
if skipped_urls:
    print("\nSkipped URLs (invalid format):")
    for url in skipped_urls:
        print(f"- {url}")
    print(f"\nTotal skipped: {len(skipped_urls)}")