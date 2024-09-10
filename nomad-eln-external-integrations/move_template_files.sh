#!/bin/sh

if ! command -v rsync &> /dev/null; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh nomad-eln-external-integrations/ .
  rm -rfv nomad-eln-external-integrations
fi
