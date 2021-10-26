.PHONY: build test run web web2

build:
		docker build --tag music-scales .

test: | build
		docker run music-scales /bin/bash -c "pytest -vv; mypy music_scales; pylint music_scales"

run: | build
		docker run -v ${PWD}/images:/images music-scales /bin/bash -c "python -m music_scales --demo"

web: | build
		docker run -v ${PWD}/web-images:/images music-scales /bin/bash -c "python -m music_scales --web"

web2: | build
		docker run -v ${PWD}/web-images:/images music-scales /bin/bash -c "python web/generate_site.py"
