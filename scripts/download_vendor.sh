#!/usr/bin/env bash

vendor_dir='./app/static/vendor'

bootstrap_file='bootstrap-5.3.3-dist.zip'
bootstrap_url="https://github.com/twbs/bootstrap/releases/download/v5.3.3/${bootstrap_file}"

cd "${vendor_dir}"
wget "${bootstrap_url}"
unzip "${bootstrap_file}"
rm "${bootstrap_file}"