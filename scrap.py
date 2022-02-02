import requests
import pandas as pd

# Coleta uma tabela com as letras do alfabeto e seus símbolos em código morse, NATO, etc.

url = "http://www.sckans.edu/~sireland/radio/code.html"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(url, headers=header)
response.raise_for_status()
data = response.text

df_text_code = pd.read_html(data)[0]
df_num_punc_code = pd.read_html(data)[1]


df_text_code.to_csv("data/text_code.csv", index=False)
df_num_punc_code.to_csv("data/numbers_punc_code.csv", index=False)


# text_code.csv contém o alfabeto com a codificação em morse e em nato de cada letra
# numbers_punc_code.csv contém o código morse de números e pontuações
df_text = pd.read_csv("data/text_code.csv", index_col="Letter")
df_np = pd.read_csv("data/numbers_punc_code.csv")


# Cria dois DFs, um com o número e o outro com a pontuação como index, e, como coluna, o código morse
df_num = pd.DataFrame(df_np.set_index("Number")["Code"]).rename({"Code": "Morse"}, axis=1)
df_punc = pd.DataFrame(df_np.set_index("Punctuation")["Code.1"]).rename({"Code.1": "Morse"}, axis=1)


# Concatena o DF do alfabeto com o dos números e com o das pontuações, mesclando na coluna "Morse"
df = pd.concat([df_text, df_num, df_punc])


# Divide o DF anterior em dois: em código morse, e o outro com o alfabeto fonético
df_morse = pd.DataFrame(df["Morse"].dropna())
df_phonetic = pd.DataFrame(df.drop(["Morse"], axis=1)[:26])


# Substitui o nome das pontuações pelos seus respectivos símbolos
df_morse.rename(index={"Period": ".", "Comma": ",", "Colon": ":", "Question Mark": "?", "Apostrophe": "'",
                       "Hyphen": "-", "Fraction Bar": "/", "Parentheses": ("("), "Quotation Marks": '"'},
                inplace=True)

# Insere o fechamento de parêntesis e o espaço
df_morse.loc[")"] = "-*--*-"
df_morse.loc[" "] = "/"


# Converte o index para str
df_morse.index = df_morse.index.astype(str)

# Salva os dois DFs prontos para uso
df_morse.to_csv("data/morse.csv")
df_phonetic.to_csv("data/phonetic_alphabet.csv")
