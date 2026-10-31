files = ['pygen_icon.png', 'Oppenheimer(2024).mkv', 'ideas.TxT', 'codes.txt', 'avatar.PNG']
fileset = {file.lower() for file in files if file.lower().endswith('.png')}
sort_fileset = sorted(fileset)
print(*sort_fileset)
