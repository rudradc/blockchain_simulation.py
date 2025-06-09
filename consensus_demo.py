import random

# -------------------------------
# Create Mock Validators
# -------------------------------

# PoW validators with random computational power
pow_validators = {
    "MinerA": random.randint(1, 100),
    "MinerB": random.randint(1, 100),
    "MinerC": random.randint(1, 100)
}

# PoS validators with random stake amounts
pos_validators = {
    "StakerA": random.randint(1, 100),
    "StakerB": random.randint(1, 100),
    "StakerC": random.randint(1, 100)
}

# DPoS delegates with random vote counts
dpos_votes = {
    "DelegateA": random.randint(1, 10),
    "DelegateB": random.randint(1, 10),
    "DelegateC": random.randint(1, 10)
}

# -------------------------------
# PoW Consensus Simulation
# -------------------------------
# Highest computational power wins
pow_winner = max(pow_validators, key=pow_validators.get)
print(f"[PoW] Mining Competition: {pow_validators}")
print(f"Selected Miner: {pow_winner} with Power = {pow_validators[pow_winner]}")
print("Explanation: In PoW, the miner with the highest computational power solves the block.\n")

# -------------------------------
# PoS Consensus Simulation
# -------------------------------
# Highest staked amount wins
pos_winner = max(pos_validators, key=pos_validators.get)
print(f"[PoS]  Stake Holders: {pos_validators}")
print(f" Selected Staker: {pos_winner} with Stake = {pos_validators[pos_winner]}")
print(" Explanation: In PoS, the validator with the largest stake is chosen to create the next block.\n")

# -------------------------------
# DPoS Consensus Simulation
# -------------------------------
# Most voted delegate is selected
dpos_winner = max(dpos_votes, key=dpos_votes.get)
print(f"[DPoS] ️ Vote Results: {dpos_votes}")
print(f" Selected Delegate: {dpos_winner} with Votes = {dpos_votes[dpos_winner]}")
print(" Explanation: In DPoS, token holders vote for delegates. The one with most votes gets to validate the block.\n")

# -------------------------------
# Summary: Print All Mocked Values
# -------------------------------
print(" Summary of Consensus Inputs:")
print("• PoW (Power):", pow_validators)
print("• PoS (Stake):", pos_validators)
print("• DPoS (Votes):", dpos_votes)
