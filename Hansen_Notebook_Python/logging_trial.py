import logging
import mylib

def main():
	logging.basicConfig(filename='myapp.log', level = logging.INFO)
	logging.info('Started')
	mylib.do_something()
	logging.info('Finished')

# if you want to change the printed message format

logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)

# the output will 






if __name__ == '__main__':
	main()

