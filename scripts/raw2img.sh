#!/usr/bin/env bash

# > bfconvert -version
# Version: 6.13.0
# Build date: 2 May 2023
# VCS revision: afaff5ef177c51d99e673cad6031d31637b431eb

basedir="${1}"
if [ ! -d "${basedir}" ]; then
    echo "Not a directory: ${basedir}"
    exit 1
fi

for rawfile in "${basedir}"/raw/*.vsi; do
    filename=$(basename "$rawfile")
    bfconvert -bigtiff -compression LZW -overwrite "${rawfile}" "${basedir}/img/${filename%.vsi}.tiff"
done
