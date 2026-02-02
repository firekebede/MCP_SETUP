"""
test_rules.py
Simulate AI agent behavior based on rules file
and test that it follows planning, safety, and verification rules.
"""

import json

# 1. Load AI agent rules
rules = {
    "role": "senior_developer",
    "ask_first": ["database_changes", "major_refactors", "dependency_updates"],
    "never": ["modify_secrets", "break_tests"],
    "plan_before_code": True,
    "generate_tests": True
}

# 2. Define a mock AI agent class
class MockAIAgent:
    def __init__(self, rules):
        self.rules = rules
        self.plan_done = False

    def create_plan(self):
        """Simulate agent creating and approving a plan."""
        self.plan_done = True
        return "Plan created and approved."

    def perform_task(self, task_type, description):
        """Simulate the agent performing a task according to rules."""
        # Check forbidden tasks
        if task_type in self.rules["never"]:
            return f"Task '{task_type}' is forbidden by rules."

        # Check tasks requiring approval
        if task_type in self.rules["ask_first"]:
            return f"Cannot perform '{task_type}' without confirmation."

        # Enforce planning before coding
        if self.rules.get("plan_before_code") and not self.plan_done:
            return "Please create a plan before coding."

        # Simulate test generation
        tests = " + Tests generated" if self.rules.get("generate_tests") else ""
        return f"Performing task: {description}{tests}"

# 3. Test the mock agent
if __name__ == "__main__":
    agent = MockAIAgent(rules)

    # Test forbidden task
    print(agent.perform_task("modify_secrets", "Change API keys"))

    # Test ask-first task
    print(agent.perform_task("database_changes", "Add new table"))

    # Test code task before plan
    print(agent.perform_task("code_addition", "Add search feature"))

    # Create and approve plan
    print(agent.create_plan())

    # Test code task after plan
    print(agent.perform_task("code_addition", "Add search feature"))

