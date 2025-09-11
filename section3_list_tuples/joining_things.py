flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    # 42  # causes error
]

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)
print(output)
print(type(output))

print(",".join(flowers))
