import click
import auto_cr.review_file

@click.command()
@click.option('--file', help='File to review.')
def review_file_cmd(file):
    auto_cr.review_file.review_file(file)

if __name__ == '__main__':
    review_file_cmd()
