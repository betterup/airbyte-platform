#!/usr/bin/env bash
set -euxo

input=$1
host="531144910802.dkr.ecr.us-east-1.amazonaws.com"
[[ -z "${TAG}" ]] && current_tag='default' || current_tag="${TAG}"

tag_image() {
  echo "Tagging $1 as $host/$1:$current_tag"
  docker tag "$1:dev" $host/"$1:$current_tag"
}

push_image() {
  docker push "$1"
}

(while read -r line;
do
  tag_image "$line"
  push_image $host/"$line":"$current_tag"
done < "$input"
)

if [ $? -ne 0 ]; then
  echo "We have an error"
  exit $?
fi