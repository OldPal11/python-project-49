install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl

make lint:
	uv run ruff check brain_games