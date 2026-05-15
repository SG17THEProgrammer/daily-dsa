import json
import os
import time
import requests

from groq import Groq
from slugify import slugify

from prompt_builder import build_prompt
from memory_manager import (
    load_problems,
    save_problems,
    load_topic_progress,
    save_topic_progress
)
from similarity_checker import is_similar_problem
from save_problem import save_problem


# =========================================================
# CONFIG
# =========================================================

MODEL_NAME = "llama-3.3-70b-versatile"

MAX_RETRIES = 5

TEMPERATURE = 0.7


# -------------------------
# TELEGRAM CONFIG
# -------------------------

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")



# =========================================================
# INIT GROQ CLIENT
# =========================================================

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found")

client = Groq(
    api_key=GROQ_API_KEY
)


# =========================================================
# SELECT TOPIC
# =========================================================

def get_current_topic(progress_data):
    """
    Choose the least-practiced topic.
    """

    topic_counts = progress_data["topic_counts"]

    sorted_topics = sorted(
        topic_counts.items(),
        key=lambda item: item[1]
    )

    return sorted_topics[0][0]


# =========================================================
# CALL LLM
# =========================================================

def call_llm(prompt):

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert coding interview problem curator. "
                    "Always return STRICT VALID JSON ONLY."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=TEMPERATURE,
        response_format={"type": "json_object"}
    )

    content = completion.choices[0].message.content

    return json.loads(content)


# =========================================================
# VALIDATE GENERATED JSON
# =========================================================

def validate_problem(problem):

    required_fields = [
        "title",
        "difficulty",
        "category",
        "reference",
        "problem_description",
        "expectation",
        "constraints",
        "examples",
        "bruteforce",
        "optimal_solution",
        "signature",
        "topic"
    ]

    for field in required_fields:

        if field not in problem:
            print(f"Missing field: {field}")
            return False

    # category must be list
    if not isinstance(problem["category"], list):
        return False

    # constraints must be list
    if not isinstance(problem["constraints"], list):
        return False

    # examples must be list
    if not isinstance(problem["examples"], list):
        return False

    # need minimum 3 examples
    if len(problem["examples"]) < 3:
        print("Need at least 3 examples")
        return False

    # signature must be list
    if not isinstance(problem["signature"], list):
        return False

    # optimal solution validation
    optimal_solution = problem["optimal_solution"]

    optimal_fields = [
        "intuition",
        "approach",
        "java_code",
        "time_complexity",
        "space_complexity"
    ]

    for field in optimal_fields:

        if field not in optimal_solution:
            print(f"Missing optimal_solution field: {field}")
            return False

    return True


# =========================================================
# UPDATE MEMORY
# =========================================================

def update_memory(
    problem,
    previous_problems,
    progress_data
):
    """
    Store compact metadata only.
    """

    current_day = progress_data["current_day"]

    memory_entry = {
        "day": current_day,
        "title": problem["title"],
        "topic": problem["topic"],
        "difficulty": problem["difficulty"],
        "signature": problem["signature"]
    }

    previous_problems.append(memory_entry)

    save_problems(previous_problems)

    # update topic counts
    topic = problem["topic"]

    if topic in progress_data["topic_counts"]:
        progress_data["topic_counts"][topic] += 1

    # increment day
    progress_data["current_day"] += 1

    save_topic_progress(progress_data)


# =========================================================
# TELEGRAM MESSAGE
# =========================================================

def send_telegram_message(problem, current_day):

    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing")
        return

    examples_text = ""

    for index, example in enumerate(problem["examples"], start=1):

        examples_text += (
            f"\nExample {index}:\n"
            f"Input: {example['input']}\n"
            f"Output: {example['output']}\n"
        )
    
    problem_slug = slugify(problem["title"])

    github_link = (
    f"https://github.com/SG17THEProgrammer/daily-dsa/"
    f"tree/main/practice/Day{current_day}_{problem_slug}"
)

    message = f"""
🔥 DAILY DSA PROBLEM 🔥

📅 Day: {current_day}

📌 Title:
{problem['title']}

📊 Difficulty:
{problem['difficulty']}

🧠 Topic:
{problem['topic']}

🏷️ Categories:
{', '.join(problem['category'])}

📝 Problem:
{problem['problem_description']}

🎯 Expectation:
{problem['expectation']}

📌 Constraints:
{chr(10).join(['- ' + c for c in problem['constraints']])}

🧪 Examples:
{examples_text}

⏱️ Optimal Complexity:
Time: {problem['optimal_solution']['time_complexity']}
Space: {problem['optimal_solution']['space_complexity']}

💡 Solve first yourself before reading solution.

📂 Full solution available in GitHub repository.
{github_link}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        data=payload
    )

    if response.status_code == 200:
        print("Telegram message sent!")
    else:
        print("Telegram failed")
        print(response.text)


# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("DAILY DSA AUTOMATION")
    print("=" * 60)

    # -----------------------------------------------------
    # LOAD MEMORY
    # -----------------------------------------------------

    print("\nLoading memory...")

    previous_problems = load_problems()

    progress_data = load_topic_progress()

    current_day = progress_data["current_day"]

    print(f"Current Day: {current_day}")

    # -----------------------------------------------------
    # SELECT TOPIC
    # -----------------------------------------------------

    topic = get_current_topic(progress_data)

    print(f"Selected Topic: {topic}")

    # -----------------------------------------------------
    # BUILD PROMPT
    # -----------------------------------------------------

    prompt = build_prompt(
        topic=topic,
        previous_problems=previous_problems
    )

    final_problem = None

    # -----------------------------------------------------
    # GENERATION LOOP
    # -----------------------------------------------------

    for attempt in range(1, MAX_RETRIES + 1):

        print(f"\nAttempt {attempt}/{MAX_RETRIES}")

        try:

            generated_problem = call_llm(prompt)

            print("LLM response received")

            # ---------------------------------------------
            # VALIDATION
            # ---------------------------------------------

            if not validate_problem(generated_problem):
                print("Validation failed")
                continue

            print("Validation passed")

            # ---------------------------------------------
            # DUPLICATE CHECK
            # ---------------------------------------------

            duplicate = is_similar_problem(
                generated_problem,
                previous_problems
            )

            if duplicate:
                print("Duplicate-like problem detected")
                continue

            print("Unique problem generated")

            final_problem = generated_problem

            break

        except json.JSONDecodeError:
            print("Invalid JSON returned")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(2)

    # -----------------------------------------------------
    # FAILURE CASE
    # -----------------------------------------------------

    if final_problem is None:
        raise Exception(
            "Failed to generate unique valid problem"
        )

    # -----------------------------------------------------
    # SAVE FILES
    # -----------------------------------------------------

    print("\nSaving files...")

    save_problem(
        problem_data=final_problem,
        day_number=current_day
    )

    print("Files saved successfully")

    # -----------------------------------------------------
    # UPDATE MEMORY
    # -----------------------------------------------------

    print("Updating memory...")

    update_memory(
        problem=final_problem,
        previous_problems=previous_problems,
        progress_data=progress_data
    )

    print("Memory updated")


    # -----------------------------------------------------
    # SEND TELEGRAM MESSAGE
    # -----------------------------------------------------

    print("Sending Telegram message...")

    send_telegram_message(
        problem=final_problem,
        current_day=current_day
    )

    # # -----------------------------------------------------
    # # SUCCESS
    # # -----------------------------------------------------

    # print("\n" + "=" * 60)
    # print("AUTOMATION COMPLETED")
    # print("=" * 60)

    # print(f"Problem: {final_problem['title']}")
    # print(f"Difficulty: {final_problem['difficulty']}")
    # print(f"Topic: {final_problem['topic']}")


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()