import re

text = "The events are scheduled on 12/05/2023, 01-01-2024, and 30.06.2022."

print(re.findall(r"\d{2}[-/.]\d{2}[-/.]\d{4}", text))