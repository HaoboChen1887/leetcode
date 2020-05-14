import sys
import os
import re
import click

@click.command()
@click.argument('ctg', nargs=1, required=False)
@click.argument('prob', nargs=1, required=False)
@click.option('--chmod', is_flag=True, help='chmod +rw for all files')
def main(ctg, prob, chmod):
    if chmod:
        change_mode()
    else:
        try:
            generate_file(ctg, prob)
        except:
            click.echo('not enouch arguments')
            sys.exit(1)

def change_mode():
    for root, dirs, files in os.walk("."):
        for f_name in files:
            if re.search(r'^\d+\.py|^\d+\.txt', f_name):
                click.echo('chmod +rw ' + f_name)
                os.chmod(os.path.join(root, f_name), 0o666)

def generate_file(ctg, prob):
    click.echo('generating ' + os.path.join('.', ctg, prob))
    path = os.path.join('./', ctg, prob)
    os.makedirs(path, exist_ok=True)
    prob_num = re.search(r'^\d+', prob).group(0)
    code_file = os.path.join(path, prob_num + '.py')
    test_file = os.path.join(path, prob_num + '.txt')
    with open(code_file, 'w+') as _:
        pass
    with open(test_file, 'w+') as _:
        pass

if __name__ == "__main__":
    main()
