import os
import json

# Folder where allure results are generated
RESULTS_DIR = "allure-results"

# Automatically creates environment.properties file for Allure
def generate_environment_file():
    env_path = os.path.join(RESULTS_DIR, "environment.properties")
    with open(env_path, "w") as f:
        f.write("Browser=Chrome\n")
        f.write("Environment=Staging\n")
        f.write("Tester=QA Automation\n")
    print(f"✔ environment.properties generated at: {env_path}")

# Optional: Print summary of test results from allure JSON files
def summarize_results():
    passed, failed, skipped = 0, 0, 0
    for file in os.listdir(RESULTS_DIR):
        if file.endswith("-result.json"):
            with open(os.path.join(RESULTS_DIR, file), "r", encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status")
                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                elif status == "skipped":
                    skipped += 1
    print(f"✔ Summary - Passed: {passed}, Failed: {failed}, Skipped: {skipped}")

if __name__ == "__main__":
    generate_environment_file()
    summarize_results()
