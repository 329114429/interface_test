import Bobo

@bobo.query('/')
def hello(person):
    return 'hello %s' % (person)

if __name__ == '__main__':
    bobo -f testbobo.py
    