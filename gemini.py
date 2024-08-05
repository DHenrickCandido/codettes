import pandas as pd
import vertexai
from vertexai.generative_models import GenerativeModel
import datetime
project_id = "gemini-project-analyzer"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

def read_txt_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def summarize_csv(file_path):
    df = pd.read_csv(file_path)

    csv_content = ""
    for index, row in df.iterrows():
        csv_content += " ".join(map(str, row.values)) + "\n"
    response = model.generate_content(
        f"Por favor utilize apenas o que tem no conteudo e separe em seçoes proximos eventos de tecnologia, palestras e cursos com: \n{csv_content}, devolver apenas as informaçoes seccionadas sem comentarios adicionais. Leve em consideraçao que o dia de hoje é {datetime.datetime.today()} e nao faz sentido pegar os eventos de antes dessa data (devolver em html sem esquecer dos links)"
    )

    return response.text

def example_merge(summary):
    example_file_path = "exemplo-newsletter.html"
    with open(example_file_path, "r", encoding="utf-8") as file:
        example = file.read()
    response = model.generate_content(
        f"Por favor formate o seguinte texto dividido em seçoes {summary} no modelo do seguinte exemplo {example}, se nao houver links e informacoes de uma certa seçao do exemplo, pode deixar sem essa seçao, tenha em mente que é um modelo de newsletter, entregue sem comentarios adicionais. (devolver em html sem esquecer dos links, os emojis, o cabeçalho e coisas do tipo, no caso a newsletter é a codettes entao nao perca a identidade)"
    )
    return response.text

def main():
    file_path = "search_results.csv"

    summary = summarize_csv(file_path)

    md_file_path = "conteudo-em-secoes.html"
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)

    newsletter_ready = "newsletter-ready.html"

    newsletter = example_merge(summary)

    with open(newsletter_ready, 'w', encoding="utf-8") as file:
        file.write(newsletter)


if __name__ == "__main__":
    main()