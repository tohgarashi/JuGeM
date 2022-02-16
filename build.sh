#!/bin/bash

SOURCE=${JuGeM_SOURCE_FONTS_PATH:-"./sourceFonts"}
DIST="$(pwd)/dist"
mkdir -p "${DIST}"
log="${DIST}/log.txt"
touch "${log}"

mkdir -p "${SOURCE}"
cd "${SOURCE}"

if [ ! -e "JuliaMono-Regular.ttf" ]; then
  echo "Prepare JuliaMono Font" | tee -a "${log}"
  curl -LO "https://github.com/cormullion/juliamono/releases/download/v0.044/JuliaMono-ttf.tar.gz" | tee -a "${log}"
  unar JuliaMono-ttf.tar.gz 2>&1 | tee -a "${log}"
  for f in $(find ./JuliaMono-ttf/ -name "*.ttf"); do
    cp "${f}" ./ | tee -a "${log}"
  done
  rm -rf JuliaMono-ttf
  rm JuliaMono-ttf.tar.gz
fi

if [ ! -e "GenJyuuGothicL-Monospace-Regular.ttf" ]; then
  echo "Prepare GenJyuuGothicL Monospace Font" | tee -a "${log}"
  curl -LO "https://osdn.jp/downloads/users/8/8635/genjyuugothic-l-20150607.7z" | tee -a "${log}"
  unar genjyuugothic-l-20150607.7z | tee -a "${log}"
  for f in $(find ./genjyuugothic-l-20150607/ -name "*.ttf" | grep "Monospace"); do
    cp "${f}" ./ | tee -a "${log}"
  done
  rm -rf genjyuugothic-l-20150607
  rm genjyuugothic-l-20150607.7z
fi

cd ..

echo "Build" | tee -a "${log}"
fontforge -lang=py -script JuGeM.py 2>&1 | tee -a "${log}"