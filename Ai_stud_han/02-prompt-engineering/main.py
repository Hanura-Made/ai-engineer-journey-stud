from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
topic = input("Masukkan topik: ")
task = input("Masukkan task: ")

prompt_v1= f"""
{task} tentang topik "{topic}" .
"""
prompt_v2= f"""
Kamu adalah seorang ahli dalam bidang {topic}. 
Tugasmu adalah {task} tentang topik "{topic}" .
"""

prompt_v3= f"""
Kamu adalah seorang ahli dalam bidang {topic}.
Saya adalah fresh graduate yang sedang belajar AI Engineering.
Tugasmu adalah {task} tentang topik "{topic}" . 
"""

prompt_v4= f""" 
Kamu adalah seorang ahli dalam bidang {topic}.
Saya adalah fresh graduate yang sedang belajar AI Engineering.
Tugasmu adalah {task} tentang topik "{topic}" . 
Constraints:
- Gunakan bahasa Indonesia yang mudah dipahami.
- Gunakan contoh analogi yang relevan dengan topik "{topic}".
- Gunakan format penulisan yang jelas dan terstruktur kurang dari 150 kata.
"""

prompt_v5 = f"""
Kamu adalah AI Engineering mentor.

Saya adalah fresh graduate yang sedang belajar AI Engineering.

{task} tentang topik "{topic}".

Constraints:
- Gunakan bahasa Indonesia.
- Gunakan bahasa yang mudah dipahami.
- Maksimal 150 kata.
- Berikan satu contoh sederhana.

Output Format:

Definisi:
...

Cara Kerja:
...

Contoh:
...
"""

print("""
Pilih Prompt Version:

1. V1 - Basic
2. V2 - Role
3. V3 - Context
4. V4 - Constraints
5. V5 - Output Format
""")

choice = input("Masukkan pilihan (1-5): ").strip()

choices = {
    "1": prompt_v1,
    "2": prompt_v2,
    "3": prompt_v3,
    "4": prompt_v4,
    "5": prompt_v5
}

if choice not in choices:
    print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")
else:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=choices[choice]
    )

    print("\n===HASIL===\n")
    print(interaction.output_text)