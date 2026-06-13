seconds = 3661
hours = seconds // 3600
rest = seconds % 3600
min = rest // 60
sec = rest % 60
print(hours, "час", min, "минута", sec, "секунда")
