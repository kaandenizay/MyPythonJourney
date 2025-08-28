computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

print(computer_parts)

print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])

computer_parts[3] = "trackball"
print(computer_parts[3:])
print(computer_parts)

computer_parts[3:] = ["trackball"]
print(computer_parts)

computer_parts[3:] = "trackball"
print(computer_parts)