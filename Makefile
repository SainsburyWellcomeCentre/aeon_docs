# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src
BUILDDIR      = docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(SOURCEDIR)/reference/api.rst:
	@echo "Generating API documentation..."
	@python make_mecha_doctree.py
	@python make_acquisition_doctree.py

copy-examples:
	@echo "Copying example notebooks to 'src'..."
	@python copy_examples_to_src.py

clean:
	@echo "Removing auto-generated files under 'docs' and 'src'..."
	@rm -rf $(BUILDDIR)
	@rm -rf $(SOURCEDIR)/reference/api/
	@rm -rf $(SOURCEDIR)/xml/

.PHONY: help Makefile copy-examples

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option. $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile $(SOURCEDIR)/reference/api.rst copy-examples
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)