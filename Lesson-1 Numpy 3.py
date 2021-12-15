a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)

print(a_centered_sp / (a_centered.shape[0] - 1))