# S.A.A.M. – Serviço de Assistência com Aprendizagem de Máquina

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader
import os
from dotenv import load_dotenv
import traceback

# ======== API KEY ========
load_dotenv()  # Carrega variáveis de ambiente

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY não definida no .env")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# ======== INICIALIZAÇÃO =========
try:
    chat = ChatGroq(model='llama3-70b-8192')
    print("SARA inicializada com sucesso!")
except Exception:
    print("Erro ao inicializar a IA:")
    traceback.print_exc()
    exit()

# ======== FUNÇÕES DE CARREGAMENTO =========
def carrega_sites():
    url = input('Digite a URL do site: ')
    return WebBaseLoader(url).load()

def carrega_pdf():
    caminho = input('Digite o caminho do PDF: ')
    return PyPDFLoader(caminho).load()

def carrega_video():
    link = input('Digite o link do video: ')
    return YoutubeLoader.from_youtube_url(link, language=['pt']).load()

# ======== GERAR RESPOSTA COM CONTEXTO =========
def responde_com_contexto(lista_docs, pergunta):
    texto = ''.join(doc.page_content for doc in lista_docs)
    template = ChatPromptTemplate.from_messages([
        ('system', 'Você é um assistente amigável, que responde com base nestas informações: {documento_informado}'),
        ('user', '{input}')
    ])
    chain = template | chat
    return chain.invoke({'documento_informado': texto, 'input': pergunta}).content

# ======== CHATPAD TRADICIONAL =========
def resposta_do_bot(lista_mensagens):
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content='Você é um assistente amigável chamado Asimo')
    ] + lista_mensagens)
    chain = template | chat
    return chain.invoke({}).content

# ======== MENU PRINCIPAL =========
print('Bem-vindo ao ChatBot da S.A.R.A.! (Digite x para sair a qualquer momento.)\n')

menu_texto = ''' Selecione a opção desejada:
1 - Conversa com a SARA
2 - Pesquisa na Web
3 - Leitor de Vídeos do YouTube
4 - Leitor de PDFs
'''

mensagens = []

while True:
    selecao = input(menu_texto)
    if selecao == '1':
        mensagens.append(SystemMessage(content="Você é a SARA, um assistente profissional que vai diretamente ao ponto, que é fofa, muito educada, muito inteligente, e me chama de Amor todas as vezes."))
        try:
            while True:
                pergunta = input('Usuário: ')
                if pergunta.strip().lower() in ['x', 'exit']:
                    break
                mensagens.append(HumanMessage(content=pergunta))
                resposta = resposta_do_bot(mensagens)
                mensagens.append(AIMessage(content=resposta))
                print(f'Assistente: {resposta}')
        except KeyboardInterrupt:
            print("\nInterrupção detectada. Encerrando o chat.")
        except Exception:
            print("Erro inesperado:")
            traceback.print_exc()
        break

    elif selecao == '2':
        documentos = carrega_sites()
        mensagens.append(SystemMessage(content='Você é um assistente amigável e informativo. Use o conteúdo do site carregado para responder.'))
        while True:
            pergunta = input("Usuário (Web): ")
            if pergunta.strip().lower() in ['x', 'exit']:
                break
            resposta = responde_com_contexto(documentos, pergunta)
            print(f'Resposta: {resposta}')
        break

    elif selecao == '3':
        documentos = carrega_video()
        mensagens.append(SystemMessage(content='Você é um assistente amigável e informativo. Use o conteúdo do vídeo carregado para responder.'))
        while True:
            pergunta = input("Usuário (YouTube): ")
            if pergunta.strip().lower() in ['x', 'exit']:
                break
            resposta = responde_com_contexto(documentos, pergunta)
            print(f'Resposta: {resposta}')
        break

    elif selecao == '4':
        documentos = carrega_pdf()
        mensagens.append(SystemMessage(content='Você é um assistente amigável e informativo. Use o conteúdo do PDF carregado para responder.'))
        while True:
            pergunta = input("Usuário (PDF): ")
            if pergunta.strip().lower() in ['x', 'exit']:
                break
            resposta = responde_com_contexto(documentos, pergunta)
            print(f'Resposta: {resposta}')
        break

    else:
        print('Opção inválida. Digite um dos valores acima.')

print('\nMuito obrigado por utilizar a SARA. Até logo, Amor!')