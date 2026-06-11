import os

total_urls = 4145
parts = 10

chunk_size = (total_urls + parts - 1) // parts

python_path = r"c:\Python Training\.venv\Scripts\python.exe"
script_path = r"c:\Python Training\only\only_all_product.py"
# script_path = r"c:\Python Training\only\all_image_dowload.py"

for i in range(parts):

    start = i * chunk_size
    end = min(start + chunk_size, total_urls)

    cmd = (
        f'start cmd /k ""{python_path}" "{script_path}" {start} {end}"'
    )

    os.system(cmd)

    print(f"Started: {start} -> {end}")
