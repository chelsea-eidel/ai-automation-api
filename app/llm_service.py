import json
import re
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL


class LLMService:

    def __init__(self) -> None:
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set.")

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL


    def _parse_json(self, output: str) -> dict:
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", output.strip(), flags=re.MULTILINE)
        return json.loads(cleaned.strip())

    def summarize_text(self, text: str) -> str:
        prompt = f"""
Summarize the following text clearly and concisely.

Text:
{text}
""".strip()

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text.strip()


    def extract_tasks(self, text: str) -> dict:
        prompt = f"""
You are a structured data extraction system.

Extract actionable tasks from the text below.

Return ONLY valid JSON.

Output format:
{{
  "tasks": [
    {{
      "title": "string",
      "due_date": "string or null",
      "priority": "low | medium | high | null"
    }}
  ]
}}

Text:
{text}
""".strip()

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return self._parse_json(response.output_text)


    def extract_structured(self, text: str, schema_description: str) -> dict:
        prompt = f"""
Convert the following text into structured JSON.

Target schema:
{schema_description}

Return ONLY JSON.

Text:
{text}
""".strip()

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return self._parse_json(response.output_text)