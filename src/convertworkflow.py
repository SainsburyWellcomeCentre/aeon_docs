import os
import sphinx
from pathlib import Path
from docutils import nodes

from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.osutil import ensuredir, copyfile

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

from sphinx.transforms.post_transforms.images import BaseImageConverter

logger = logging.getLogger(__name__)


class WorkflowImageConverter(BaseImageConverter):
    """An image converter to resolve workflow image references.
    
    The converter will handle any image reference targeting a .bonsai
    workflow file and look for the corresponding .svg file.

    If the builder output is html it will also copy the source file
    into the _workflows folder so it can be fetched by copy button scripts.
    """
    default_priority = 300

    def match(self, node: nodes.image) -> bool:
        _, ext = os.path.splitext(node['uri'])
        return '://' not in node['uri'] and ext == '.bonsai'
    
    def handle(self, node: nodes.image) -> None:
        try:
            srcpath = Path(node['uri'])
            abs_srcpath = self.app.srcdir / srcpath
            abs_imgpath = abs_srcpath.with_suffix('.svg')
            if not abs_imgpath.exists():
                logger.warning(__('Could not find workflow image: %s [%s]'), node['uri'], abs_imgpath)
                return

            # copy workflow image to _images folder
            destpath = os.path.join(self.imagedir, abs_imgpath.name)
            ensuredir(self.imagedir)
            copyfile(abs_imgpath, destpath)

            # resolve image cross-references
            if '*' in node['candidates']:
                node['candidates']['*'] = destpath
            node['uri'] = destpath
            self.env.original_image_uri[destpath] = srcpath
            self.env.images.add_file(self.env.docname, destpath)

            # copy workflow file to _workflows folder when output is html
            if self.app.builder.format == 'html':
                abs_workflowdir = self.app.builder.outdir / '_workflows'
                abs_workflowpath = abs_workflowdir / abs_srcpath.name
                ensuredir(abs_workflowdir)
                copyfile(abs_srcpath, abs_workflowpath)
        except Exception as exc:
            logger.warning(__('Could not fetch workflow image: %s [%s]'), node['uri'], exc)

def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_post_transform(WorkflowImageConverter)
    return {
        'version': sphinx.__display_version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }