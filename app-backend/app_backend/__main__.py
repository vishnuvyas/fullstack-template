from typer import Typer
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="ISO"),
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
)

app = Typer()

logger = structlog.get_logger(name=__name__)


@app.command()
def serve(host: str, port: int):
    logger.info(event='start_serve', host=host, port=port)


if __name__ == '__main__':
    app()
