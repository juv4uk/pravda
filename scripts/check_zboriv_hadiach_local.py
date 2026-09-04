import os

# Check if there are other files in the ecosystem or pravda
for root, dirs, files in os.walk("/home/agents"):
    for f in files:
        if any(w in f.lower() for w in ["zboriv", "hadziac", "hadiach", "zborow"]):
            full_path = os.path.join(root, f)
            print(full_path, os.path.getsize(full_path))
