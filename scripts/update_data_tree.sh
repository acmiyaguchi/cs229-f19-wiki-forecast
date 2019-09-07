#!/bin/bash

# make a document with the structure of the data folder for documentation purposes

set -e

cd $(dirname $0)/..

cat > data-tree.md << END
# \`data\` folder structure

$(echo '```bash')
$(tree -h data)
$(echo '```')
END

head data-tree.md

