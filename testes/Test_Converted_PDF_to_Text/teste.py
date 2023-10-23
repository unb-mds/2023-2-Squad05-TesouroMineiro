from playwright.sync_api import sync_playwright
import time
from PyPDF2 import PdfReader
import tabula

def automacao_web_DOUSs():
    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        pagina.goto("https://www.diariomunicipal.com.br/amm-mg/")
        #pagina.screenshot(path="teste.png")

        pagina.locator('//*[@id="formCalendario"]/fieldset/div/div[2]/table/tbody/tr[1]/td[3]/a').click()

        #pagina.locator('//*[@id="btDownloadSimples2"]').click()

            # Start waiting for the download
        with pagina.expect_download() as download_info:
            # Perform the action that initiates download
            pagina.click('//*[@id="btDownloadSimples2"]')
            global download
        download = download_info.value
        

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(download.suggested_filename)

        #catch_pdf(download.suggested_filename)

    time.sleep(1000)



def catch_pdf():
        
    #Abrindo aqruivo pdf em modo leitura e lendo em binario
    reader = PdfReader(open("publicado_96011_2023-10-02_f8411b1cd47b4150f7026ca15e88202f.pdf", 'rb'))
    #Mostrando número de páginas do arquivo
    print(len(reader.pages))
    #Armazenando uma pagina na variavel page
    page = reader.pages[308]
    #Extraindo o texto da pagina
    text = page.extract_text()

    try:
        print(text)
    except Exception as e:
        print("Erro ao ler o arquivo pdf erro {}".format(e))

    
    with open('/home/elias/Unb/2023-2-Squad05/testes/Test_Converted_PDF_to_Text/publicado_96007_2023-09-26_2b094e14c97153e332a4be1408b108cc.pdf', 'w') as f:
            f.write(text)
            f.close()
    
#automacao_web_DOUSs()
#catch_pdf()


def tabela():
     
        # Substitua "seu_arquivo.pdf" pelo caminho do seu arquivo PDF
    arquivo_pdf = "Test_Converted_PDF_to_Text/arquivo_doy_mg.pdf"

    # Extrai as tabelas do PDF e retorna uma lista de DataFrames do pandas
    tabelas = tabula.read_pdf(arquivo_pdf, pages='307')

    print(tabelas)


tabela()