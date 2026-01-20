# curl is a command line utility
# run
# python /home/anshul/Documents/CodeWithHarry/Day\ 85:\ Creating\ command\ line\ utility.py https://tinyjpg.com/images/social/website.jpg -o image2.jpg
# or
# python /home/anshul/Documents/CodeWithHarry/Day\ 85:\ Creating\ command\ line\ utility.py https://tinyjpg.com/images/social/website.jpg
# from terminal

import argparse
import requests

# Source - https://stackoverflow.com/a/16696317
# Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-20, License - CC BY-SA 4.0


def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split("/")[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()
parser.add_argument("url", help="Url of the file to download")
parser.add_argument("-o", "--output", help="Output file name", default=None)

args = parser.parse_args()

print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)
