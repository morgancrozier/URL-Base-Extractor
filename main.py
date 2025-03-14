# Read URLs from file
with open('urls.txt', 'r') as file:
    urls = [line.strip() for line in file]

# Extract base URLs and remove duplicates
base_urls = sorted(set(url.split('/', 3)[0] + '//' + url.split('/', 3)[2] for url in urls))

# Save to a new file
with open('base_urls.txt', 'w') as file:
    for url in base_urls:
        file.write(url + '\n')

print(f"Processed {len(base_urls)} unique base URLs.")