import json


def build_prompt(topic, previous_problems):

    recent_titles = [
        p["title"]
        for p in previous_problems[-10:]
    ]

    recent_signatures = [
        p["signature"]
        for p in previous_problems[-10:]
    ]

    prompt = f"""
You are an expert coding interview problem curator.

Generate ONE beginner-to-medium coding interview problem.

CURRENT TOPIC:
{topic}

GOAL:
Help strengthen DSA foundations for coding interviews and online assessments.

TARGET COMPANIES:
- Amazon
- Google
- Microsoft
- IBM
- Infosys
- TCS
- HackerRank style OAs

FOCUS ONLY ON:
- Arrays
- Strings
- HashMaps
- Sets
- Sliding Window
- Two Pointers
- Prefix Sum
- Linked Lists
- Stack/Queue basics
- Binary Search basics

AVOID:
- Graphs
- Trees
- Advanced DP
- Segment Trees
- Tries
- Monotonic Queue
- Hard problems

PREVIOUSLY USED TITLES:
{json.dumps(recent_titles, indent=2)}

PREVIOUSLY USED SIGNATURES:
{json.dumps(recent_signatures, indent=2)}

IMPORTANT:
- Do NOT repeat previous problems
- Do NOT generate same logic with different wording
- Mostly Easy-Medium difficulty
- Questions should resemble real OA problems

IMPORTANT JAVA REQUIREMENTS:
- Use clean Java 17 compatible code
- Use meaningful variable names
- Use proper class structure
- Avoid unnecessary comments
- Prefer optimal Java collections
- Use ArrayList, HashMap, HashSet appropriately

The generated Java solution must compile correctly.

RETURN STRICT JSON ONLY.

JSON FORMAT:

{{
  "title": "",
  "difficulty": "",
  "category": [],
  "reference": {{
    "platform": "",
    "url": ""
  }},
  "problem_description": "",
  "expectation": "",
  "constraints": [],
  "examples": [
    {{
      "input": "",
      "output": "",
      "explanation": ""
    }},
    {{
      "input": "",
      "output": "",
      "explanation": ""
    }},
    {{
      "input": "",
      "output": "",
      "explanation": ""
    }}
  ],
  "bruteforce": {{
    "approach": "",
    "time_complexity": "",
    "space_complexity": ""
  }},
  "optimal_solution": {{
    "intuition": "",
    "approach": "",
    "java_code": "",
    "time_complexity": "",
    "space_complexity": ""
  }},
  "signature": [],
  "topic": "{topic}"
}}
"""

    return prompt