import csv
from pprint import pprint

from jsonlines import jsonlines

from src.settings import GLOSSSEQ2POLISH_FILEPATH


def main():
    with jsonlines.open(GLOSSSEQ2POLISH_FILEPATH) as reader, open(
        "./autotrain_train.csv", "w"
    ) as f:
        out_writer = csv.writer(f)
        out_writer.writerow(["gloss_concatenated_text", "polish_text"])

        for record in reader:
            gloss_concatenated_text = " ".join(
                [g["text"] for g in record["gloss_sequence"]]
            )
            polish_text = record["polish_annotation"]["text"]
            out_writer.writerow(
                [
                    gloss_concatenated_text,
                    polish_text,
                ]
            )


if __name__ == "__main__":
    main()
