from inPainting-nps import *

def main():
    filenames = ["test_im1.bmp","test_im2.bmp"]
    for file in filenames:
        for windowSize in [5,9,11]:
            start = time.time()
            #Run the Algorithm with the parameters
            textureSynthesis("img/"+file, windowSize)
            end = time.time()
            #Calculate and log the running times
            logging.info("\t"+file+"-"+str(windowSize)+"\t:-  "+str(end-start)+" secs")




if __name__ == '__main__':
    main()
