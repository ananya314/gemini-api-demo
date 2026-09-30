# Simple call to a gemini model

# the logging and time imports are only for performance logs
import logging
import time

# the imports below are required to run the gemini models
from dotenv import load_dotenv
from google import genai

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("demo")

load_dotenv()  # loads .env values into the environment
model = "gemini-3.5-flash-lite"
client = genai.Client()  # finds GEMINI_API_KEY automatically

logger.info("Client created, sending request to %s", model)

start = time.perf_counter()
response = client.interactions.create(
    model=model,
    input="This is a demo, say hi!",
)
end = time.perf_counter()

print("model response:")
print("-" * 20)
print(response.output_text)
print("-" * 20)

logger.info("Response received in %.2fs", (end - start))

logger.info("Response exited with status %s", response.status)
