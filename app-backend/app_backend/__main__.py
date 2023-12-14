from typer import Typer
import uvicorn
import structlog

from app_backend.restapi import api

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="ISO"),
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
)

app = Typer()

logger = structlog.get_logger(__name__)


@app.command()
def serve(host: str = "127.0.0.1", port: int = 8000):
    logger.info(event='start_serve', host=host, port=port)
    uvicorn.run(api, host=host, port=port)


if __name__ == '__main__':
    app()
