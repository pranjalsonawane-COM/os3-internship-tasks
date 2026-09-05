from workflow.graph import run_security_workflow


event = """
There were 20 failed login attempts for the same account
within 2 minutes, followed by a successful login from an
unusual location.
"""


print("\n================================")
print("🛡️ MULTI-AGENT CYBERSECURITY SYSTEM")
print("================================")

run_security_workflow(event)