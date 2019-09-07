#!/bin/bash
set -eou pipefail
set -x

cd data
mkdir -p processed

for name in raw/*.gz; do
	out="bzipped/${name%.gz}.bz2"
	zcat < $name | bzip2 > $out
done
