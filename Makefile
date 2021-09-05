.PHONY: build test

build:
		docker build --tag music-scales .

test: | build
		docker run music-scales /bin/bash -c "pytest -vv; mypy music_scales; pylint music_scales"
