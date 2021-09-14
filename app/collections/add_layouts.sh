for file in _datasets/*.md; do
	sed -i '' -e '2s/^/layout\: default\n/;' $file
done