cp -r datasets/* app/collections/_datasets

for file in app/collections/_datasets/*.md; do
	sed -i '' -e '2s/^/layout\: default\n/;' $file
done