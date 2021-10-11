import io
import uuid
import frontmatter
import sys

if __name__ == "__main__":
	new_file = frontmatter.load(sys.argv[1])
	new_uuid = uuid.uuid4()
	new_file['uuid'] = str(new_uuid)

	# write out additions to metadata
	f = io.open(sys.argv[1], 'w', encoding='utf8')
	frontmatter.dump(new_file, f)
	f.close()

