This project uses **MkDocs** with the Material theme and relies on Jinja server-side templating. Use `uv` to manage dependencies and run the local server:

```bash
# install dependencies via uv's pip frontend
uv pip install -r requirements.txt

# run development server
uv run mkdocs serve --livereload
```

Open `http://127.0.0.1:8000/` in your browser; changes to `docs/` rebuild automatically.

The `mkdocs.yml` configuration contains theme and plugin settings (Material, macros, git-committers, etc.).
