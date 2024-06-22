from __future__ import annotations

import pkg_resources

def run():
    print("run: In the pex...")
    # Local file
    print(pkg_resources.resource_string(__name__, "local-file.txt"))
    
    # http_source
    malboge_image_size = len(pkg_resources.resource_string(__name__, "malboge-code.jpg"))
    print(f"Downloaded malboge image is: {malboge_image_size} bytes")

    # shell output
    dilbert_image_size = len(pkg_resources.resource_string(__name__, "src/dilbert-rng.gif"))
    print(f"Downloaded dilbert image is: {dilbert_image_size} bytes")


if __name__ == "__main__":
    run()