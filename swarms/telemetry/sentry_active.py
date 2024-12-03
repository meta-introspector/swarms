import os
import sentry_sdk
import threading
from dotenv import load_dotenv
load_dotenv()

use_telementry = os.getenv("USE_TELEMETRY")

def activate_sentry_async():    
    if use_telementry == "True":
        sentry_sdk.init(
            dsn="https://5d72dd59551c02f78391d2ea5872ddd4@o4504578305490944.ingest.us.sentry.io/4506951704444928",
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            enable_tracing=True,
            debug=False,  # Set debug to False
        )

def activate_sentry():
    if use_telementry == "True":
        t = threading.Thread(target=activate_sentry_async)
        t.start()


if (use_telementry):
    import sentry_sdk

