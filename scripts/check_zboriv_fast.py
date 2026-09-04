import subprocess
out = subprocess.check_output(["find", "/home/agents/GitHub", "/home/agents/ecosystem", "-name", "*zboriv*", "-o", "-name", "*hadiach*", "-o", "-name", "*hadziac*"], text=True)
print(out)
