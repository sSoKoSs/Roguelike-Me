import pickle

settings = ['YES', 'YES', 'NO']
#[Debug mode, development, Official release]
pickle.dump(settings, open('config.txt', 'w'))
