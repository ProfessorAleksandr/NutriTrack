from .commands import router as commands_router
from .text import router as text_router
from .callbacks import router as callbacks_router

__all__ = ["commands_router","text_router","callbacks_router"]