from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

while True:
    x=input("masukan dan tekan enter untuk mengirim pertanyaan: ")

    if x.lower() == "exit":
        print("Terima kasih telah menggunakan layanan ini. Sampai jumpa!")
        break
    
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input= x
    )
    print(interaction.output_text)