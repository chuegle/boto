#!/bin/bash

find bin/ boto/ tests/ docs/ -type f -exec sed -i ._bak 's/from boto/from boto2/' {} \;
find bin/ boto/ tests/ docs/ -type f -exec sed -i ._bak 's/import boto/import boto2/' {} \;
find bin/ boto/ tests/ docs/ -type f -exec sed -i ._bak 's/boto\./boto2./' {} \;

find . -iname '*._bak' -delete

mv boto/ boto2
git rm -r boto
git add boto2

