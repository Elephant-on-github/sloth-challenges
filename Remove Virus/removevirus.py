# Ai was used to solve this problem

keywords = ["malware", "virus"]
notwords = ["not", "no", "free", "anti"]

def remove_virus(text):
    def filter_files(files):
        if not files:
            return []
        file = files[0]
        if any(keyword in file for keyword in keywords) and not any(notword in file for notword in notwords):
            return filter_files(files[1:])
        return [file] + filter_files(files[1:])
    
    files = text.split(": ")[1].split(", ")
    filtered_files = filter_files(files)
    result = ", ".join(filtered_files)
    print(f"PC Files: {result}")

remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
# Expected output: "PC Files: spotifysetup.exe, dog.jpg"

remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
# Expected output: "PC Files: antivirus.exe, cat.pdf"

remove_virus("PC Files: notvirus.exe, funnycat.gif")
# Expected output: "PC Files: notvirus.exe, funnycat.gif"