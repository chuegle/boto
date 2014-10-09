#!/bin/bash

if ! [[ -e boto1 ]]; then
 git mv boto boto1
fi

find bin/ boto1/ docs/ setup.py -type f -exec sed -i ._bak 's/from boto\./from boto1./g' {} \;
find bin/ boto1/ docs/ setup.py -type f -exec sed -i ._bak 's/from boto /from boto1 /g' {} \;
find bin/ boto1/ docs/ setup.py -type f -exec sed -i ._bak 's/import boto$/import boto1/g' {} \;
find bin/ boto1/ docs/ setup.py -type f -exec sed -i ._bak 's/import boto\./import boto1./g' {} \;
find bin/ boto1/ docs/ setup.py -type f -exec sed -i ._bak 's/boto\./boto1./g' {} \;
find setup.py -type f -exec sed -i ._bak "s/'boto'/'boto1'/g" {} \;
find setup.py -type f -exec sed -i ._bak 's/"boto"/"boto1"/g' {} \;

find . -iname '*._bak' -delete

git add boto1 bin docs setup.py
