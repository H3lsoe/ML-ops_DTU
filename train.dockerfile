FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*



COPY pyproject.toml pyproject.toml
COPY src/ src/
COPY data/ data/

ENV PYTHONPATH=/src
ENTRYPOINT ["uv", "run", "python", "-m", "ml_ops_dtu.train"]

ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv uv sync

