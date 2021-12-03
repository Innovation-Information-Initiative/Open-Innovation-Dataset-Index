import os
import uuid
import frontmatter
import sys

from helpers import files
from helpers.utils import get_project_root
from helpers.sprites import create_sprites

if __name__ == "__main__":
	filepath = os.path.join(get_project_root(), sys.argv[1])

	record = frontmatter.load(filepath)
	new_uuid = uuid.uuid4()
	record['uuid'] = str(new_uuid)

	# create sprite for UUID
	create_sprites([str(new_uuid)])

	files.update_frontmatter(record, filepath)
