import os
import json
from slugify import slugify
import re

def to_java_class_name(title):
    """
    Convert title into valid Java class name.

    Example:
    'subarray with given sum'
    -> SubarrayWithGivenSum
    """

    words = re.findall(r'[a-zA-Z0-9]+', title)

    return ''.join(word.capitalize() for word in words)

def save_problem(problem_data, day_number):

    title_slug = slugify(problem_data["title"])

    folder_name = f"Day{day_number}_{title_slug}"

    folder_path = os.path.join("practice", folder_name)

    os.makedirs(folder_path, exist_ok=True)

    # README
    readme_path = os.path.join(folder_path, "README.md")

    with open(readme_path, "w", encoding="utf-8") as f:

        f.write(f"# {problem_data['title']}\n\n")

        f.write(f"## Difficulty\n{problem_data['difficulty']}\n\n")

        f.write(f"## Category\n{', '.join(problem_data['category'])}\n\n")

        ref = problem_data.get("reference", {})

        if ref.get("platform"):
            f.write(f"## Reference\n")
            f.write(f"Platform: {ref.get('platform')}\n\n")
            f.write(f"Link: {ref.get('url')}\n\n")

        f.write("## Problem Description\n")
        f.write(problem_data["problem_description"] + "\n\n")

        f.write("## Expectation\n")
        f.write(problem_data["expectation"] + "\n\n")

        f.write("## Constraints\n")

        for c in problem_data["constraints"]:
            f.write(f"- {c}\n")

        f.write("\n")

        f.write("## Examples\n\n")

        for i, ex in enumerate(problem_data["examples"], start=1):
            f.write(f"### Example {i}\n")
            f.write(f"Input: {ex['input']}\n\n")
            f.write(f"Output: {ex['output']}\n\n")
            f.write(f"Explanation: {ex['explanation']}\n\n")

        bf = problem_data["bruteforce"]

        f.write("## Brute Force Approach\n")
        f.write(bf["approach"] + "\n\n")

        f.write(f"Time Complexity: {bf['time_complexity']}\n\n")
        f.write(f"Space Complexity: {bf['space_complexity']}\n\n")

        optimal = problem_data["optimal_solution"]

        f.write("## Optimal Solution Intuition\n")
        f.write(optimal["intuition"] + "\n\n")

        f.write("## Optimal Approach\n")
        f.write(optimal["approach"] + "\n\n")


        class_name = to_java_class_name(problem_data["title"])

        imports = (
    "import java.util.*;\n"
)

        wrapped_java_code = (
        f"{imports}\n"
        f"public class {class_name} {{\n\n"
        f"{optimal['java_code']}\n"
        f"}}"
        )

        f.write("## Java Solution\n")
        f.write("```java\n")
        f.write(wrapped_java_code)
        f.write("\n```\n\n")

        # f.write("## C++ Solution\n")
        # f.write("```cpp\n")
        # f.write(optimal["cpp_code"])
        # f.write("\n```\n\n")

        f.write(f"Time Complexity: {optimal['time_complexity']}\n\n")
        f.write(f"Space Complexity: {optimal['space_complexity']}\n")

    # Save JAVA Solution
    py_path = os.path.join(folder_path, "Solution.java")

    with open(py_path, "w", encoding="utf-8") as f:
        f.write(problem_data["optimal_solution"]["java_code"])

    # Save metadata
    metadata = {
        "title": problem_data["title"],
        "topic": problem_data["topic"],
        "difficulty": problem_data["difficulty"],
        "signature": problem_data["signature"]
    }

    metadata_path = os.path.join(folder_path, "metadata.json")

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)