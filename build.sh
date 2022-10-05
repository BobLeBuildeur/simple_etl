#!/bin/bash

docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
