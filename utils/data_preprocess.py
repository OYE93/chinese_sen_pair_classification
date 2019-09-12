"""
for data transform
author: EnOUYANG
email: enouyang@tongji.edu.cn
"""

from bs4 import BeautifulSoup


def RQE_parser(file_path, out_file_path):
    """
    transform xml files to tsv format
    :return:
    """
    out_file = open(out_file_path, "w")
    out_file.write("\t".join(["pid", "sen_a", "sen_b", "label"]) + "\n")
    file_content = open(file_path, "r", encoding="utf8")
    soup = BeautifulSoup(file_content, "html.parser")
    for pair in soup.find_all("pair"):
        pid = pair["pid"]
        label = pair["value"]
        sen_a = pair.chq.string.strip()
        sen_b = pair.faq.string.strip()
        out_file.write("\t".join([pid, sen_a, sen_b, label]) + "\n")


def main():
    train_file_path = "../data/MEDIQA_RQE_raw/MEDIQA2019-Task2-RQE-TrainingSet-AMIA2016.xml"
    dev_file_path = "../data/MEDIQA_RQE_raw/MEDIQA2019-Task2-RQE-ValidationSet-AMIA2016.xml"
    test_file_path = "../data/MEDIQA_RQE_raw/MEDIQA2019-Task2-RQE-TestSet-wLabels.xml"

    train_out_path = "../data/MEDIQA_RQE/train.tsv"
    dev_out_path = "../data/MEDIQA_RQE/dev.tsv"
    test_out_path = "../data/MEDIQA_RQE/test.tsv"

    RQE_parser(train_file_path, train_out_path)
    RQE_parser(dev_file_path, dev_out_path)
    RQE_parser(test_file_path, test_out_path)


if __name__ == "__main__":
    main()