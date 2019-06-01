from subprocess import call

file_names_dict = {
    "read1": "example_data_R1_001.fastq",
    "read2": "example_data_R2_001.fastq",
    "amp": "example_data.amplicons.txt",
    "inserts": "example_data.inserts.fa",
    # "maf": "0.05",
}


def build_cmd():
    cmd_str = ""
    for k, v in file_names_dict.items():
        cmd_str += " --{} <{}>".format(k, v)
    return cmd_str


def run_files():
    import pdb; pdb.set_trace()
    call([
        "python",
        "aiHunter.py",
        build_cmd()
    ])


if __name__ == '__main__':
    run_files()
