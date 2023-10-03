from playwright.sync_api import sync_playwright
import time
from PyPDF2 import PdfReader

def automacao_web_DOUSs():
    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        pagina.goto("https://www.diariomunicipal.com.br/amm-mg/")
        #pagina.screenshot(path="teste.png")

        pagina.locator('//*[@id="formCalendario"]/fieldset/div/div[2]/table/tbody/tr[5]/td[4]/a').click()

        #pagina.locator('//*[@id="btDownloadSimples2"]').click()

            # Start waiting for the download
        with pagina.expect_download() as download_info:
            # Perform the action that initiates download
            pagina.click('//*[@id="btDownloadSimples2"]')
        download = download_info.value

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(download.suggested_filename)

        #catch_pdf(download.suggested_filename)

    time.sleep(1000)


#pdf = str('publicado_96007_2023-09-26_2b094e14c97153e332a4be1408b108cc.pdf')

def catch_pdf():
        
    #Abrindo aqruivo pdf em modo leitura e lendo em binario
    reader = PdfReader(open('publicado_96007_2023-09-26_2b094e14c97153e332a4be1408b108cc.pdf', 'rb'))
    #Mostrando número de páginas do arquivo
    print(len(reader.pages))
    #Armazenando uma pagina na variavel page
    page = reader.pages[50]
    #Extraindo o texto da pagina
    text = page.extract_text()

    try:
        print(text)
    except Exception as e:
        print("Erro ao ler o arquivo pdf erro {}".format(e))

    
    with open('DOUMG.txt', 'w') as f:
            f.write(text)
            f.close()
    
#automacao_web_DOUSs()
catch_pdf()

