from ...ui import window
from ..logger import logger

def boot():
    logger.logging(__name__, 4, "Boot process launched")
    app = window.Window()
    logger.logging(__name__, 4, "Boot process finished")
    app.mainloop()
    