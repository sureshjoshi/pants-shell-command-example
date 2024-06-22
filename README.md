# pants-shell-command-example

This repo is an example of different ways to access local files (or remote files, technically).

Easiest being a fully local resource, another that downloads a resource (via `http_source`), and a last that runs a shell command to call a script to read from `manifest.txt`, and then downloads the specified image.

All of these are wrapped into `resource` targets and passed into the pex. In `main.py`, we use `pkg_resources` to open and read the file contents.

```bash
% pants run src:bin

run: In the pex...
b'Hello, world!\n'
Downloaded malboge image is: 155928 bytes
Downloaded dilbert image is: 79601 bytes
```