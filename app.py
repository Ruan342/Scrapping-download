from seleniumbase import SB
import time

i = 1
def save_log(text):
    with open('execution_log.txt', 'a') as file:  
        file.write(text + '\n')
with SB() as sb:
    sb.open("url de acesso ao site")
    time.sleep(5)
    sb.type("#username", "usuario")
    sb.type("#password", "senha")
    sb.click('button:contains("Conectar")')
    time.sleep(5)
    sb.click('a:contains("Relatórios")')
    sb.click("#relatorioGravacao")
    sb.type("#txtDataI", "inserção de data")
    sb.click("#btnSearch")
    time.sleep(3)
    #checando log para ultima pagina registrada
    def load_last_page():
        try:
            with open('execution_log.txt', 'r') as file:
                lines = file.readlines()
                for line in reversed(lines):
                    if "Ultima pagina realizada" in line:
                        page_number = int(line.split(":")[-1].strip())
                        return page_number
            return None  
        except FileNotFoundError:
            return None  
    last_page = load_last_page()
    if last_page:
        print(last_page)
    else:
        print("Nenhuma página registrada encontrada.")
    #continuando do ultimo log registrado
    while i < 1680:
        current_text = sb.get_text("/html/body/div[3]/div/div/div/div[3]/div/div/div/div[1]/ul/li[5]/a")
        if current_text == str(last_page):
            print(f'Continuando a partir do ultimo LOG registrado: {last_page}')
            break
        else:
            sb.click("/html/body/div[3]/div/div/div/div[3]/div/div/div/div[1]/ul/li[5]/a")
            time.sleep(1)
            i += 1
    #paginas entre 4 e 1680
    while i <= 1680:
        try:
            sb.click("/html/body/div[3]/div/div/div/div[3]/div/div/div/div[1]/ul/li[5]/a")
        except Exception as e:
            print('erro , tentando novamente')
            time.sleep(10)
        time.sleep(3)
        try:
            sb.execute_script("document.querySelector('ins.iCheck-helper').click();")
        except Exception as e:
            print('erro , tentando novamente')
            time.sleep(10)
        try:
            sb.click("#btnDownloadSelected")
        except Exception as e:
            print('erro , tentando novamente')
            time.sleep(10)
        text = sb.get_text("/html/body/div[3]/div/div/div/div[3]/div/div/div/div[1]/ul/li[5]/a")
    
        # Salvar o texto no arquivo de log
        save_log(f"Ultima pagina realizada: {text}")
        time.sleep(20)  
        i += 1

