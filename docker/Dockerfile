FROM python:3.12-slim as builder

ENV WORKSPACE=/workspace
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR $WORKSPACE

COPY . .

RUN pip3 install uv
RUN uv sync


FROM python:3.12-slim

ENV PYTHONBUFFERED=1
ENV WORKSPACE=/workspace

WORKDIR $WORKSPACE

COPY --from=builder $WORKSPACE/.venv/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder $WORKSPACE/src .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
