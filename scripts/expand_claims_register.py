# Script to add CLAIM-INTERPRETATION-RISK and the two new claims (HC-ZBORIV-1649-001 and HC-HADIACH-SEJM-001)

with open("/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md", "r", encoding="utf-8") as f:
    content = f.read()

# Let us check how CLAIM-INTERPRETATION-RISK should look like.
# Each claim will have:
# - CLAIM-INTERPRETATION-RISK: LOW / MEDIUM / HIGH / VERY HIGH
# - WHY-CLAIM-RISK: <short explanation>

# First, let's prepare the updated text for the existing 10 claims and append the 2 new ones.
