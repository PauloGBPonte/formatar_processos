import pandas as pd

df = pd.read_excel("RECORTE_ESTADO_TO.xlsx")
df.head()

df.info()

df["N º DO PROCESSO"] = df["N º DO PROCESSO"].astype(str)


print(len(df["N º DO PROCESSO"][0]))

def inserir_zeros(texto):
  faltam = 20 - len(texto)

  if len(texto) >= 20:
    return texto
  else:
    zeros = "0" * faltam
  return zeros + texto


df["N º DO PROCESSO"] = df["N º DO PROCESSO"].apply(inserir_zeros)


def formatar_processos(processo):
  return (
    processo[:7] + "-" +
    processo[7:9] + "." +
    processo[9:13] + "." +
    processo[13:14] + "." +
    processo[14:16] + "." +
    processo[16:20]
  )

df["N º DO PROCESSO"] = df["N º DO PROCESSO"].apply(formatar_processos)

df = df.set_index("GCPJ")

df.to_excel("RECORTE_ESTADO_TO CORRIGIDO.xlsx")

