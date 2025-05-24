from brent_get_csv import fetch_csv_file
from brent_get_excel import fetch_excel_file
from brent_get_json import fetch_json_file
from brent_get_text import fetch_txt_file


OUTPUT_PATH = 'C:\\Repos\\datafun-03-analytics\\data'

csv_url = 'https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv'
excel_url = 'https://go.microsoft.com/fwlink/?LinkID=521962'
json_url = 'https://www.filesampleshub.com/download/code/json/sample2.json'
txt_url = 'https://sample-files.com/downloads/documents/txt/data.txt'


def main():

    fetch_csv_file(OUTPUT_PATH, "industry_names.csv", csv_url)

    fetch_excel_file(OUTPUT_PATH, "sample_financial_data.xlsx", excel_url)

    fetch_json_file(OUTPUT_PATH, "random_info.json", json_url)

    fetch_txt_file(OUTPUT_PATH, "identification_info", txt_url)

















if __name__ == "__main__":
    main()