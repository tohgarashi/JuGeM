#!/bin/bash

SOURCE=${JuGeM_SOURCE_FONTS_PATH:-"./sourceFonts"}
DIST="$(pwd)/dist"
mkdir -p "${DIST}"
log="${DIST}/log.txt"
touch "${log}"
error_log="${DIST}/error_log.txt"
touch "${error_log}"

mkdir -p "${SOURCE}"
cd "${SOURCE}"

if [ ! -e "JuliaMono-Regular.ttf" ]; then
  echo "Prepare JuliaMono Font" | tee -a "${log}"
  curl -LO "https://github.com/cormullion/juliamono/releases/download/v0.045/JuliaMono-ttf.tar.gz" | tee -a "${log}"
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

if [ ! -e "${DIST}/noemoji/JuGeM-Regular.ttf" ]; then
  echo "Build" | tee -a "${log}"
  fontforge -lang=py -script JuGeM.py 2>>"${error_log}" | tee -a "${log}"
fi

cd "${DIST}/noemoji"

if [ ! -e "${DIST}/noemoji/before/JuGeM-Regular.ttf" ]; then
  echo "modify xAvgCharWidth" | tee -a "${log}"
  for file in JuGeM*.ttf; do
    ttx -t OS/2 "$file" 2>&1 | tee -a "${log}"
    xmlstarlet ed --inplace -u "/ttFont/OS_2/xAvgCharWidth/@value" -v 1199 "${file%%.ttf}.ttx"
    mv "$file" "./before/${file}" | tee -a "${log}"
    ttx -m "./before/${file}" "${file%%.ttf}.ttx" 2>&1 | tee -a "${log}"
  done
fi