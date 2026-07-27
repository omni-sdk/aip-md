import os
import glob

root = r'D:\dev\github.com\atp'
count = 0
for filepath in glob.glob(os.path.join(root, '**', '*.md'), recursive=True):
    if '.git' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('ATP', 'AITP')
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Updated: {filepath}')
print(f'Total files updated: {count}')