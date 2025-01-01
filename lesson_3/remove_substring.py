advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.removesuffix('house training your pet dinosaur.'))

# LS solution
print(advice.split('house')[0])