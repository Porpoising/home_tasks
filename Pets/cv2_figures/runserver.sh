#/bin/sh
uvicorn src.figure_determinator:app --host 0.0.0.0 --port ${PORT}