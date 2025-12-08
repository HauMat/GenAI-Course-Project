import tkinter as tk
from tkinter import scrolledtext
from google import genai


def response_dispaly(response): #Window function
  reply_window = tk.Tk()
  reply_window.title("Gemini's long answer")
  reply_window.geometry("600x400")
  #Selectable text in window
  text_area = scrolledtext.ScrolledText(reply_window, wrap=tk.WORD, font=("Arial", 12))
  text_area.pack(expand=True, fill='both')
  #Window loop with response as text
  text_area.insert(tk.END, response)
  text_area.configure(state='disabled')
  reply_window.mainloop()

def read_code(file_name):#Add text from file to prompt
  try:
    with open(file_name, "r", encoding="utf-8") as file:
      return file.read()
  except Exception as e:
    print(f"Error: {e}")
    return None

def use_gemini(prompt):
  client = genai.Client()
  response = client.models.generate_content(
          model="gemini-2.5-flash", contents=prompt
      )
  return response.text


def main():
  query = input("Ask Gemini: ")
  file_path = input("Code/txt file for prompt: ")
  file_content = read_code(file_path) 
  if file_content:
    query += file_content

  q1 = use_gemini(query)
  simplify = f''' 
    This comes from a Python file designed to assist the user to learn while doing coding related work.
    Your task is to simplify the previous answer to the query: '{query}'.
    Make it a few sentences and only show as few important lines of relevant code as possible to move further.
    The previous response will stay readable to the user for review.
    Take that into consideration while simplifying.
    Previous response:\n\n{q1}'''
  q2 = use_gemini(simplify)
  print(q2)

  response_dispaly(q1)



if __name__ == "__main__":

  main()
