cp -r datasets/* app/collections/_datasets

for file in app/collections/_datasets/*.md; do
	sed -i '2s/^/layout\: default\n/;' $file
done

cp -r tools/* app/collections/_tools

for file in app/collections/_tools/*.md; do
	sed -i '2s/^/layout\: default\n/;' $file
done