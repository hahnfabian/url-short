import json
import os

def main():
    html = '<html><head><meta http-equiv="refresh" content="0;url={url}" /></head></html>'

    with open('links.json') as f:
        links = json.load(f)
    
    if not os.path.exists('dist') and not os.path.isdir('dist'):
        os.mkdir('dist')

    for link in links:
        html_document = html.format(url=link['url'])

        linkname = link['name']
        file_path = f'dist/{linkname}.html'

        with open(file_path, 'w') as f:
            f.write(html_document)


if __name__ == "__main__":
    main()

