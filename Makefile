.PHONY: build install uninstall publish

# the library name
name = thunder-subtitle
# may change to pip3 or python3 -m pip, etc.
pip = pip

install: clean build
	$(pip) install --force-reinstall ./dist/*.whl

build:
	python setup.py sdist
	python setup.py bdist_wheel --python-tag py3

publish: clean build install
	twine upload dist/* && git push --follow-tags

uninstall:
	$(pip) uninstall $(name)

clean:
	rm -fr build dist *.egg-info
